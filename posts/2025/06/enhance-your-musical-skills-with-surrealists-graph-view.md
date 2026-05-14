---
title: "Enhance your musical skills with Surrealist's Graph View"
slug: "enhance-your-musical-skills-with-surrealists-graph-view"
date: "2025-06-03T00:00:00.000Z"
categories:
  - "tutorials"
  - "featured"
read_time: "10 min read"
summary: "Did you know that Surrealist's Graph Visualisation tool can even make you into a better musician? Let's find out how."
source: "https://surrealdb.com/blog/enhance-your-musical-skills-with-surrealists-graph-view"
cover: "../../assets/d8fc8ce7af09603c.jpg"
---

# Enhance your musical skills with Surrealist's Graph View

![Enhance your musical skills with Surrealist's Graph View](../../assets/d8fc8ce7af09603c.jpg)

A few months ago we released [Surrealist's](/surrealist) graph view, a fantastic way to visualise your data. [The blog post](/blog/visualising-your-data-with-surrealists-graph-view) introducing the feature shows you how to use Surrealist to visualise train stations, cities and countries, company org charts, the complex web of international agreements in Europe, and even random art.

But did you know that you can also use Surrealist to let you know which chord to play next when practicing piano or guitar? (Or baritone ukelele, in my case...)

It's all thanks to something called the circle of fifths that I found out about recently and am just beginning to explore. So if you are a professional musician, apologies in advance if I butcher any terminology in this post.

This circle is a mysterious tool that has a lot of power. One thing it allows you to do is to see at a glance which chords "belong" with each other, making it possible to always move from the current chord you are playing into another one that is guaranteed to sound good!

## Making a circle of notes

Before we build this circle, let's start with something more basic by visualising all the possible notes. Notes go from A to G, and all of them except B and E can be sharp, making twelve notes in total. Notes can also be called flat, meaning that the note just below B can be called either A sharp or B flat, but we'll just show them in their sharp form for simplicity. That gives us the following possible notes.

```surrealql
["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"];
```

We can use each of these strings as the `id` for twelve `note` records.

```surrealql
FOR $note IN ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"] {
    CREATE note SET id = $note;
};
```

A simple `SELECT VALUE id FROM note` statement shows them all. Looking good so far!

```surrealql
[
	note:A,
	note:⟨A#⟩,
	note:B,
	note:C,
	note:⟨C#⟩,
	note:D,
	note:⟨D#⟩,
	note:E,
	note:F,
	note:⟨F#⟩,
	note:G,
	note:⟨G#⟩
]
```

Now let's connect them to each other. We want to create a circle, so each note should be connected to the next, and the last note should be connected to the first. SurrealQL has a lot of fancy array operators that let us do this using just a little bit of code. We'll do the following:

- Grab each `note` record by using `SELECT * FROM note`, which returns an array.
- Call the [`.append()`](/docs/surrealql/functions/database/array#arrayappend)

method on this array to add `note:A` once more on the end so that `G#` (the last note) can connect to it.

- Then call the

[`.windows(2)`](/docs/surrealql/functions/database/array#arraywindows) method to create a sliding window of two items at a time (because we passed in a `2` for two items each). This will give us the pair `note:A, note:⟨A#⟩`, followed by `note:⟨A#⟩, note:B`, then `note:B, note:C`, and so on, all the way to the end.

Then we can use [`INSERT RELATION`](/docs/surrealql/statements/insert#insert-relation-tables) to link the first with the second.

```surrealql
FOR $pair IN (SELECT * FROM note).append(note:A).windows(2) {
    INSERT RELATION INTO connected_to {
        in: $pair[0].id,
        out: $pair[1].id
    };
};
```

As the notes are now joined in a circle, we can use Surrealist's graph view to see what this looks like. Click on the button to the left of "Run selection" and change the view from "Combined", which shows the regular output of a query, to "Graph". Then run this query:

```surrealql
SELECT id, ->connected_to->note FROM note;
```

You'll probably see a circle that looks like this:

Or maybe a figure eight:

That's because Surrealist generates these visualisations randomly. You can click on the "Reset graph" button to try again if you want to regenerate the output.

To make the output a bit prettier, let's add a single record called `the:centre` and connect it to each note.

```surrealql
CREATE the:centre;

FOR $note IN SELECT VALUE id FROM note {
    LET $id = $note.id;
    RELATE the:centre->to->$id;  
};
```

Let's give the graph visualisation another try, this time showing each note as it connects to the next, as well as each note as it is _connected to_ by that record in the centre.

```surrealql
SELECT id, ->connected_to->note, <-to<-the FROM note;
```

That's looking pretty nice!

## About the circle of fifths

With practice time over, we can now move on to the magic of the circle of fifths. This is also a circle of musical notes, but this time it's not each note followed by the next ne. Instead, it's each note followed by its perfect fifth.

A perfect fifth is called a fifth because it's the fifth note after the current one. Which means that...

- The perfect fifth of A is E, because E is four letters after A.
- The perfect fifth of E is B, because B is four letters after E. (E = 1, F = 2,

G = 3, A = 4, so B = 5)

Now, the precise definition of a perfect fifth isn't "four notes up" but "seven steps up". This is because the notes B and C, and E and F, don't have a step between them. So if you go with seven steps up then you'll be moving at the same distance each time.

Looking at this again:

- The perfect fifth of A is E because E is the note that is seven steps up (A,

A#, B, C, C#, D, D#, E)

- The perfect fifth of E is B because B is the note that is seven steps up (E,

F, F#, G, G#, A, A#, B)

- The perfect fifth of B is F# because F# is the note that is seven steps up (B,

C, C#, D, D#, E, F, F#)

If you keep moving seven steps at a time starting from A, you'll go from A to E, then E to B, then B to F#, and so on until you get back to A again.

If that's hard to visualise, no problem! We'll get Surrealist to do the visualisation for us.

## Making the circle of fifths inside Surrealist

Time to get started. First we'll create a database-wide parameter called `$NOTES` which is an array of each possible note.

```surrealql
DEFINE PARAM $NOTES VALUE ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"];
```

We can then use this parameter to define a function that will return the perfect fifth of any note. All we have to do is find the index of any note in the array, add seven, and return that. Here is how we will build the function:

- Use the [`.any()`](/docs/surrealql/functions/database/array#arrayany) method

on `$NOTES` to see if the input matches any of its items. If it doesn't then we'll use `THROW` to fail. We are going for simplicity here, so no flats like `B♭` will be accepted. Just the notes inside `$NOTES`.

- Use

[`.find_index()`](/docs/surrealql/functions/database/array#arrayfind_index) to get the index of the note. If the function receives a "B", that will be index 2.

- Adding 7 to the index might overflow the `$NOTES` array. We could use an

`IF ELSE` statement here, but the easiest way is to just use [`.concat()`](/docs/surrealql/functions/database/array#arrayconcat) to join `$NOTES` with itself to double its size. With a length of 24 characters, there is now no danger of overflow.

```surrealql
DEFINE FUNCTION fn::get_perfect_fifth($input: string) -> string {
    IF !$NOTES.any($input) {
        THROW "Note must be one of " + <string>$NOTES;
    };
    LET $index = $NOTES.find_index($input);
    $NOTES.concat($NOTES)[$index + 7]
};
```

Let's test this function out a bit.

```surrealql
fn::get_perfect_fifth("A"); -- Returns 'E'
fn::get_perfect_fifth("D#"); -- Returns 'A#'
fn::get_perfect_fifth("C"); -- Returns 'G'
```

That's all correct!

Now we can use `fn::get_perfect_fifth()` to recreate our `note` records, this time joining them to their perfect fifth. An [`UPSERT`](/docs/surrealql/statements/upsert) statement will work great here by creating a note if it doesn't exist, and returning an existing note otherwise.

```surrealql
FOR $note IN $NOTES {
    LET $perfect_fifth = fn::get_perfect_fifth($note);
    LET $first_note = UPSERT note SET id = $note;
    LET $second_note = UPSERT note SET id = $perfect_fifth;
    RELATE $second_note->fifth_of->$first_note;
};
```

Then we'll create that `the:centre` record to help Surrealist make the circle look as pretty as possible.

```surrealql
CREATE the:centre;

FOR $note IN SELECT VALUE id FROM note {
    LET $id = $note.id;
  RELATE the:centre->to->$id;  
};
```

With this done, we'll display the circle. Since we want to see all the connections to each note, we can use a simple query that uses the wildcard `?` operator. `->?->?` will return everything that a `note` connects to, and `<-?<-?` to return the opposite: everything that connects to a `note`.

```surrealql
SELECT id, ->?->?, <-?<-? FROM note;
```

The output looks exactly the same as before! Except that this time it's a circle of fifths. So when you hover the mouse over an individual note, you will now see its neighbouring fifth, instead of the note one step away from it.

Now we can start to get into the magic of the circle of fifths.

Take out your guitar or piano, and try playing the major chord for one of the notes here. For example, D major. On the circle of fifths, chords that sound nice together are close to each other. So if you hover your mouse over the D note, you can see that it is connected to both A and G. That means that you can play the D chord a bit, then move to A, and then from A you can go to E or back to D, and it will always sound pretty nice. Usually a chord one or two steps away will always sound nice, while a chord that is far away will sound jarring and wrong.

(It all depends on the type of music you want to play, of course)

Now what if you don't know which notes make up the chord of D major or any other major chord? No problem, because this is another bit of magic that the circle of fifths provides. If you want to play a D major chord, you do the following:

- Start with D on the circle.
- Move one step clockwise. That's A.
- Then move three more steps clockwise. That's F#.

And that's your major chord! It works every time. No matter where you are, the other two notes for a major chord will always be one step and then three more steps away.

And since it works every time, that means that we can use Surrealist to show us that too. Let's go through each note inside `$NOTES` and add its major chord by using `UPSERT`. The notes can then be joined by calling `fn::get_perfect_fifth` once for the second note, and four times for the third note.

```surrealql
FOR $note IN $NOTES {
    LET $chord = UPSERT ONLY chord SET id = $note;
    LET $base = SELECT VALUE id FROM ONLY note WHERE id.id() = $note LIMIT 1;
    LET $second = SELECT VALUE id FROM ONLY note WHERE id.id() = fn::get_perfect_fifth($note) LIMIT 1;
    LET $third = SELECT VALUE id FROM ONLY note WHERE id.id() = fn::get_perfect_fifth(fn::get_perfect_fifth(fn::get_perfect_fifth(fn::get_perfect_fifth($note)))) LIMIT 1;
    RELATE $chord->note->$base;
    RELATE $chord->note->$second;
    RELATE $chord->note->$third;
};
```

We can visualise the whole thing now using a query that shows all of the connections between `chord` and `note`.

```surrealql
SELECT id, ->?->?, <-?<-? FROM chord, note;
```

That gives us a more web-like network that looks like this.

Now get your guitar or piano out again, and we'll put it to use! Let's start with A, which looks like this.

Since we're at A, we'll play the A major chord a few times.

Now what if you forgot which notes make up the A major chord? No problem, just move the mouse over to the connected record `chord:A`. Now you can see which notes to play: it's A, C#, and E.

Now go back to A on the circle of fifths, where you can see that D and E match well with A. Let's move to E!

How do we play E major again? No problem, just mouseover `chord:E` and there are the notes: E, G# and B.

The circle of fifths has a mathematical precision that really appeals to developers. The awesome thing about each type of chord is that it always has the same shape, as you can see through a search on YouTube. This one I find sums up the shapes the best in the shortest time: [https://www.youtube.com/shorts/1gz-8BUQbaM](https://www.youtube.com/shorts/1gz-8BUQbaM)

And by the way, I can't believe that nobody ever mentioned this useful tool in Canada where I grew up during music class. But that's a subject for another day.

Now, our circle of fifths is a bit simple compared to the actual one, which includes a second circle on the inside with minor scales so that you can go from major to minor as well. The idea is that any chord next to or across from the current chord will sound good, and the farther away you go the riskier it gets.

If you are up for a challenge, try creating the full circle of fifths and see how close you can get it to the original one!
