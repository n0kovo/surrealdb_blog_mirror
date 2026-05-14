---
title: "Using SurrealDB to Expose Organised Influence Campaigns"
slug: "using-surrealdb-to-expose-organised-influence-campaigns"
date: "2025-10-10T00:00:00.000Z"
categories:
  - "featured"
  - "tutorials"
read_time: "10 min read"
summary: "SurrealDB's built-in capabilities comprising graph queries, geolocational data and recursive queries make it the perfect fit to identify malevolent entities involved in organised influence campaigns."
source: "https://surrealdb.com/blog/using-surrealdb-to-expose-organised-influence-campaigns"
cover: "../../assets/03b66a5fade071ff.jpg"
---

# Using SurrealDB to Expose Organised Influence Campaigns

![Using SurrealDB to Expose Organised Influence Campaigns](../../assets/03b66a5fade071ff.jpg)

Mass-produced information to sway the opinions of the public has been with us at least since the advent of the printing press. But the advent of bot farms and AI-produced content has introduced a new variable in which it can be hard to know whether online comments have been written by paid actors or autonomous bots delivering a single overarching message to influence the opinion or even upcoming elections of a country.

To keep the subject of this post from pertaining to a certain country time and possibly going out of date, let's choose the fictional country of Klezskavania that forms the subject of [this fantastic 1999 album](https://music.apple.com/us/album/in-klezskavania-original-score/1001829899) from a band in Calgary called the Plaid Tongued Devils. Klezskavania is one of those places that you've never heard of and where everything that can go wrong, does. One of the lyrics from the album goes as follows:

```syntax
In Klezskavania, evil is everywhere
In Klezskavania, skeletons walk
In Klezskavania, bad guys always win...
```

But quite a lot of time has passed since 1999! We can imagine that Klezskavania has since overthrown its corrupt leadership and has also had an election or two. Things are starting to improve. But on the horizon is a new threat: it looks like a larger country has an interest in keeping Klezskavania subjugated and is using bot farms on Klezskavania's largest social network that pretend to be average citizens. They are stirring up unrest where there was none before. How can its citizens pinpoint bot-related activity while allowing human users to continue to write without restrictions as they have the right to?

Fortunately, SurrealDB has this sort of functionality built in, three of which will be introduced in this post. The first method we will look at involves using event-driven architecture to react to events the moment they happen.

## Use an event to check if likes are happening too soon

A comment that receives a ton of likes within the first few minutes is clearly suspicious. Here is how we can use the schema itself to keep an eye on this behaviour.

This schema has two regular tables: `user` and `comment`. A user can write a comment or like a comment.

```surrealql
DEFINE TABLE user;
DEFINE TABLE comment;
DEFINE TABLE likes TYPE RELATION IN user OUT comment;
DEFINE TABLE wrote TYPE RELATION IN user OUT comment;
```

We can test this out a bit by creating some users and comments...

```surrealql
CREATE user:one, user:two;
LET $comment = CREATE ONLY comment SET content = "Nice blog!";
RELATE user:one->wrote->$comment;
RELATE user:two->likes->$comment;
```

...followed by a graph query to see who wrote and liked what.

```surrealql
SELECT 
    id, 
    ->likes->comment.{id, content} AS likes,
    ->wrote->comment.{id, content} AS wrote
FROM user;
```

Output:

```surrealql
[
	{
		id: user:one,
		likes: [],
		wrote: [
			{
				content: 'Nice blog!',
				id: comment:7q84slpq1lwf0ioun3kp
			}
		]
	},
	{
		id: user:two,
		likes: [
			{
				content: 'Nice blog!',
				id: comment:7q84slpq1lwf0ioun3kp
			}
		],
		wrote: []
	}
]
```

The above definitions also give us a nice schema too.

So far so good. Now we want to add the intelligent behaviour mentioned above so that the database can automatically detect suspiciously active likes the moment in which they are stored. To start, we'll add `written_at` fields to keep track of when a comment was written or liked, as well as a `state` on the likes table in which a suspicious like can be set as invalid.

This `state` field can be a simple bool, but it can also be a [`literal`](/docs/surrealql/datamodel/literals) as shown below in which an optional `context` field can be added. Using a literal makes for more interesting output so let's go with that.

```surrealql
DEFINE FIELD written_at ON likes READONLY VALUE time::now();
DEFINE FIELD written_at ON comment READONLY VALUE time::now();
-- state will always have the `valid` field, while `context` is optional
DEFINE FIELD state ON likes TYPE { valid: bool, context: string | NONE } DEFAULT { valid: true };
```

While we are at it, let's also define an index on `likes` so that only one like can happen between a user and a comment. This is often done on the app level, but thanks to this `DEFINE INDEX` statement we can achieve the same behaviour on the database level instead.

```surrealql
DEFINE INDEX only_one_like ON TABLE likes FIELDS in, out UNIQUE;

// With the index set, you can do this once...
RELATE user:one->likes->comment:one;
// But not a second time
// Output: 'Database index `only_one_like` already contains [user:one, comment:one], with record `likes:knq69ljjbakokvc955p3`'
RELATE user:one->likes->comment:one;
```

Since a `likes` is valid by default, we will need some logic to determine when a like should be invalid. A [`DEFINE EVENT`](/docs/surrealql/statements/define/event) statement will do the trick. This will keep track of any new `likes` records via the `WHEN $event = "CREATE"` clause. When a new `likes` shows up, it will compare the `written_at` field to the `written_at` field of the comment. If the like happens within a short time it will be set to invalid, as well as if a like comes in within a somewhat longer time by a user with low credibility.

To test this ourselves though we'll set the elapsed time to 3 seconds and 10 seconds. In real life this would certainly be somewhat longer (maybe something like 30 seconds and 5 minutes).

```surrealql
DEFINE EVENT comment_too_soon ON likes WHEN $event = "CREATE" THEN {
    // Time elapsed since the original comment, which is located at the `out` field
    LET $elapsed = time::now() - $after.out.written_at;
    
    // Invalidate anything liked within 3 seconds
    IF $elapsed < 3s {
        UPDATE $after SET state = { valid: false, context: "Liked within 3 seconds" }
    // If within two minutes, check credibility of user
    // Set to not valid if user is not very credible
    } ELSE IF $elapsed < 10s {
        IF $after.in.credibility < 0.4 {
            UPDATE $after SET state = { valid: false, context: "Liked within 10 seconds by user with less than 0.4 credibility"}
        }
    }
};
```

Now let's test this behaviour out by creating two normal users, a bot farm user that leaves comments specifically designed to lower the morale of everyday Klezskavanians, and a sketchy user that is hired by the bot farm to go around clicking like on these comments as soon as they are issued. In between these likes are two calls to [`sleep()`](/docs/surrealql/functions/database/sleep) to simulate the passage of time in the real world.

```surrealql
CREATE user:normal1, user:normal2, user:bot_farm;
CREATE user:sketchy SET credibility = 0.3;

RELATE user:normal1->wrote->(CREATE ONLY comment:one SET content = "Interesting!");
RELATE user:normal1->wrote->(CREATE ONLY comment:two SET content = "Food for thought for sure.");
RELATE user:bot_farm->wrote->(CREATE ONLY comment:three SET content = "I don't support this bad thing that is happening but here in Klezskavania we have to think about ourselves first and...");
RELATE user:bot_farm->wrote->(CREATE ONLY comment:four SET content = "I think it's a good idea but Klezskavanians come first, so we should stay out of it");
RELATE user:bot_farm->wrote->(CREATE ONLY comment:five SET content = "Prices are too high here in Klezskavania, things were so good back in the day!");

RELATE user:sketchy->likes->comment:three;
sleep(3s);
RELATE user:sketchy->likes->comment:four;
sleep(7s);
RELATE user:sketchy->likes->comment:five;
```

We can use this query to see the likes for each comment regardless of validity. This allows us to eyeball the likes to make sure that our event is working as intended.

```surrealql
SELECT 
    *, 
    <-likes.* AS likes
FROM comment;
```

Here is one example from a like that was done within 10 seconds but by the sketchy user, so it was marked as invalid.

```surrealql
{
	content: "I think it's a good idea but Klezskavanians come first, so we should stay out of it",
	id: comment:four,
	likes: [
		{
			id: likes:0oisekbicmsh38ssblez,
			in: user:sketchy,
			out: comment:four,
			state: {
				context: 'Liked within 10 seconds by user with less than 0.4 credibility',
				valid: false
			},
			written_at: d'2025-10-01T02:40:54.872Z'
		}
	],
	written_at: d'2025-10-01T02:40:51.861Z'
}
```

And to pass on the number of valid likes to the app, just pass in a `[WHERE state.valid]` [filter](/docs/surrealql/datamodel/arrays#mapping-and-filtering-on-arrays).

```surrealql
SELECT 
  *,
  <-likes[WHERE state.valid]<-user AS liked_by
FROM comment;
```

Now only a single like by `user:sketchy` has been allowed to get through, while `comment:three` and `comment:four` don't show any likes, keeping their visibility low.

```surrealql
[
	{
		content: 'Prices are too high here in Klezskavania, things were so good back in the day!',
		id: comment:five,
		liked_by: [
			user:sketchy
		],
		written_at: d'2025-10-01T02:40:51.862Z'
	},
	{
		content: "I think it's a good idea but Klezskavanians come first, so we should stay out of it",
		id: comment:four,
		liked_by: [],
		written_at: d'2025-10-01T02:40:51.861Z'
	},
	{
		content: 'Interesting!',
		id: comment:one,
		liked_by: [],
		written_at: d'2025-10-01T02:40:51.857Z'
	},
	{
		content: "I don't support this bad thing that is happening but here in Klezskavania we have to think about ourselves first and...",
		id: comment:three,
		liked_by: [],
		written_at: d'2025-10-01T02:40:51.860Z'
	},
	{
		content: 'Food for thought for sure.',
		id: comment:two,
		liked_by: [],
		written_at: d'2025-10-01T02:40:51.859Z'
	}
]
```

## Detect whether too many comments are in too small an area

### By exact location

Sometimes the presence of a bot farm can be identified by the sudden influx of comments from a single location. SurrealDB has [`geometry`](/docs/surrealql/datamodel/geometries) types built in, which lets us benefit in a number of ways.

One is to simply group by location to see if any locations stand out as having a particularly large number of comments.

In the example below, we have `comment` records that have an ID composed of the time and location in which they were written. This format is used in [record ranges](/docs/surrealql/datamodel/ids#record-ranges), queries performed on just a slice of a table's records instead of the whole table.

Here are a few comments made using this ID format: three from random locations and three from a single location: a bot farm.

```surrealql
CREATE comment:[time::now(), (49.923, 49.923)] SET content = rand::string(20);
CREATE comment:[time::now(), (48.933, 45.994)] SET content = rand::string(20);
CREATE comment:[time::now(), (42.903, 47.920)] SET content = rand::string(20);

CREATE comment:[time::now(), (50.001, 50.001)] SET author = user:one, content = "Klezskavanians shouldn't have to...";
CREATE comment:[time::now(), (50.001, 50.001)] SET author = user:one, content = "Things were better in the old days when...";
CREATE comment:[time::now(), (50.001, 50.001)] SET author = user:one, content = "I no longer recognize Klezskavania, it's...";
```

To do a search for abnormalities over the past day, we can use the range `comment:[time::now() - 1d]..`, meaning any comments from a day ago.

```surrealql
// Get the comments for the last day grouped by location
SELECT * FROM (SELECT count(), id[1] AS location FROM comment:[time::now() - 1d].. GROUP BY location) ORDER BY count DESC;
```

The query shows that one location in particular has a suspiciously large number of comments!

```surrealql
[
	{
		count: 3,
		location: (50.001, 50.001)
	},
	{
		count: 1,
		location: (42.903, 47.92)
	},
	{
		count: 1,
		location: (48.933, 45.994)
	},
	{
		count: 1,
		location: (49.923, 49.923)
	}
]
```

### By exact distance

Functions like [`geo::distance()`](/docs/surrealql/functions/database/geo#geodistance) can also be used instead of exact longitude and latitudes. Here are two points that we can see thanks to this function are 1321 metres away from each other:

```surrealql
LET $point1 = (50.0, 50.0);
LET $point2 = (49.99, 49.99);
geo::distance($point1, $point2);
-- 1321.894787004681f
```

Let's test this out with the same comments as above, but now with the bot-created comments close to each other instead of being at the exact same location.

```surrealql
// Normal comments over a range of areas
CREATE comment:[time::now(), (49.923, 49.923)] SET content = rand::string(20);
CREATE comment:[time::now(), (48.933, 45.994)] SET content = rand::string(20);
CREATE comment:[time::now(), (42.903, 47.920)] SET content = rand::string(20);

// Suspicious comments created all in nearly the same location
CREATE comment:[time::now(), (50.001, 50.001)] SET author = user:one, content = "Klezskavanians shouldn't have to...";
CREATE comment:[time::now(), (50.000, 50.000)] SET author = user:one, content = "Things were better in the old days when...";
CREATE comment:[time::now(), (50.000, 50.001)] SET author = user:one, content = "I no longer recognize Klezskavania, it's...";
```

The `geo::distance()` function can be put into a query like the one below that uses a subquery to see which of the day's comments are written in places suspiciously close to each other. The query is a bit complex so here are the main points to pay attention to when reading it:

- `(SELECT * FROM comment:[time::now() - 1]..)[WHERE neighbours]` is the main

query, which gets all the comments over the past day as long as there is something in the `neighbours` field.

- The `neighbours` field will hold all the comments over the past day that are

within 1000 metres of this comment.

- The subclause to find the `neighbours` uses

`WHERE geo::distance(id[1], $parent.id[1]) < 1000 AND id != $parent.id`: any comment that has a distance of less than 1000 metres and doesn't have the same ID as the current comment.

- And finally `author, geo::distance(id[1], $parent.id[1]) AS distance, content`

inside the subquery so that the output is interesting and readable to us.

Here is the query!

```surrealql
(SELECT *, 
    SELECT 
      author,
        geo::distance(id[1], $parent.id[1]) AS distance,
        content
      FROM comment:[time::now() - 1d].. WHERE 
        geo::distance(id[1], $parent.id[1]) < 1000 AND id != $parent.id
    AS neighbours
FROM comment:[time::now() - 1d]..)[WHERE neighbours];
```

As the output shows, there are a few comments that are suspiciously written close to each other.

```surrealql
[
	{
		author: user:one,
		content: "Klezskavanians shouldn't have to...",
		id: comment:[
			d'2025-10-01T04:15:39.758Z',
			(50.001, 50.001)
		],
		neighbours: [
			{
				author: user:one,
				content: 'Things were better in the old days when...',
				distance: 132.18505769364782f
			},
			{
				author: user:one,
				content: "I no longer recognize Klezskavania, it's...",
				distance: 71.47333314265806f
			}
		]
	},
	{
		author: user:one,
		content: 'Things were better in the old days when...',
		id: comment:[
			d'2025-10-01T04:15:39.760Z',
			(50, 50)
		],
		neighbours: [
			{
				author: user:one,
				content: "Klezskavanians shouldn't have to...",
				distance: 132.18505769364782f
			},
			{
				author: user:one,
				content: "I no longer recognize Klezskavania, it's...",
				distance: 111.19508023327376f
			}
		]
	},
	{
		author: user:one,
		content: "I no longer recognize Klezskavania, it's...",
		id: comment:[
			d'2025-10-01T04:15:39.762Z',
			(50, 50.001)
		],
		neighbours: [
			{
				author: user:one,
				content: "Klezskavanians shouldn't have to...",
				distance: 71.47333314265806f
			},
			{
				author: user:one,
				content: 'Things were better in the old days when...',
				distance: 111.19508023327376f
			}
		]
	}
]
```

## Use recursive queries to see quality of a user's network

Bot farms aren't just composed of users pumping out comments and others liking them. Often they are more subtle, in which users a few steps away that seem innocuous like the posts of one user who likes the posts of another, eventually leading to the bot farm-created content.

But how can you go that far down a network to see what's going on? In SurrealDB it's easy: just use a [recursive graph query](/blog/data-analysis-using-graph-traversal-recursion-and-shortest-path).

Before we begin the recursive queries, let's take a look at the situation in this example network. We have some good users, as well as a user that has a pretty high `botness` score: a number between 0 and 100 that the system uses to determine if a user exhibits bot-like behaviour.

```surrealql
CREATE user:good SET botness = 0, friends = [user:good2];
CREATE user:good2 SET botness = 0, friends = [user:good];
CREATE user:bot1 SET botness = 90;
```

Via the `friends` field we can see who has befriended the bot, but we wouldn't want to silence users just for that - after all, the point of a bot is to trick others into thinking they are real people. Plus, the networks we mentioned use a lot of indirect routes to set up a network of bot content.

Here are three more users to show how this works. The first one has had a few strikes against it but still has a fairly low `botness` score, the next friend has a higher score of 40, and finally one with a score of 50 is direct friends with the bot.

```surrealql
CREATE user:suspicious SET botness = 20, friends = [user:suspicious2];
CREATE user:suspicious2 SET botness = 40, friends = [user:suspicious3];
CREATE user:suspicious3 SET botness = 50, friends = [user:bot1];
```

So instead of trying to determine one by one whether a user is indirectly part of the network or not, we can create an overall quality score to recalculate a user's botness. This is where recursive queries come in.

Here is a simple recursive query to get started. The `@.{3+collect}.friends` part means the following:

- `@.` Starting from this record
- `{3+collect}` Go down three levels, collecting all the record IDs as you go
- `.friends` by following the `friends` path.

```surrealql
// Eyeball if any bots are within three steps
SELECT 
  id, 
  @.{3+collect}.friends AS friends
FROM user;
```

Eyeballing the output is enough to see who has any connections, direct or indirect, to the bot.

```surrealql
[
	{
		friends: [],
		id: user:bot1
	},
	{
		friends: [
			user:good2,
			user:good
		],
		id: user:good
	},
	{
		friends: [
			user:good,
			user:good2
		],
		id: user:good2
	},
	{
		friends: [
			user:suspicious2,
			user:suspicious3,
			user:bot1
		],
		id: user:suspicious
	},
	{
		friends: [
			user:suspicious3,
			user:bot1
		],
		id: user:suspicious2
	},
	{
		friends: [],
		id: user:suspicious3
	}
]
```

The recursive syntax also just be used with a single number like `{2}` if you want the query to go down to an exact depth. The query below uses this with `@.{2}.friends` and `@.{3}.friends` to tell the database to go that many steps down the `friends` path and see what's there at that point.

```surrealql
SELECT 
    id, 
    friends,
    @.{2}.friends AS friends_2nd,
    @.{3}.friends AS friends_3rd
FROM user;
```

Here is one of the users in the output, who has a bot friend at the third level.

```surrealql
{
  friends: [
    user:suspicious2
  ],
  friends_2nd: [
    user:suspicious3
  ],
  friends_3rd: [
    user:bot1
  ],
  id: user:suspicious
}
```

We can use this pattern to determine a recalculation of a user's botness to now include quality of network. We will determine this by doing the following:

- Get the average botness of a user's direct friends, multiply this by 0.5
- Same for the second level, multiply this by 0.3
- Again for the third level, multiply this by 0.2
- Add them all together.

This allows some small consequences for a user's overall greater network, while still ensuring that a user's direct friends have the greatest effect.

The query looks like this:

```surrealql
SELECT *, 
    // User's own botness still matters the most
    botness,
    // But botness inside larger network of friends and their friends counts too
    (IF friends.botness { math::sum(friends.botness) } ELSE { 0 } * 0.5) +
    (IF (friends.botness).{2} { math::sum(friends.botness) } ELSE { 0 } * 0.3) +
    (IF (friends.botness).{3} { math::sum(friends.botness) } ELSE { 0 } * 0.2 ) AS greater_botness
FROM user;
```

As the output shows, `user:suspicious` (the one who pretends to be entirely trustworthy and not related to any bot farms) now has a `greater_botness` score of 40, twice that of the original `botness` score of 20. That allows us to see that this user might be working as a front for an influence network, attempting to use its relatively high trustworthiness to influence posts and comments that are indirectly tied to the influence network.

```surrealql
[
	{
		botness: 90,
		greater_botness: 0,
		id: user:bot1
	},
	{
		botness: 0,
		friends: [
			user:good2
		],
		greater_botness: 0,
		id: user:good
	},
	{
		botness: 0,
		friends: [
			user:good
		],
		greater_botness: 0,
		id: user:good2
	},
	{
		botness: 20,
		friends: [
			user:suspicious2
		],
		greater_botness: 40,
		id: user:suspicious
	},
	{
		botness: 40,
		friends: [
			user:suspicious3
		],
		greater_botness: 50,
		id: user:suspicious2
	},
	{
		botness: 50,
		friends: [
			user:bot1
		],
		greater_botness: 90,
		id: user:suspicious3
	}
]
```

This post has only touched on a few of the ways SurrealDB can be used to combat organised influence campaigns, so another will follow it in the near future. See you in the next one!
