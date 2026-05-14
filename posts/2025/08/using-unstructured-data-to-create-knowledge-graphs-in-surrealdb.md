---
title: "Using unstructured data to create knowledge graphs in SurrealDB"
slug: "using-unstructured-data-to-create-knowledge-graphs-in-surrealdb"
date: "2025-08-22T00:00:00.000Z"
categories:
  - "featured"
  - "tutorials"
  - "ai"
read_time: "8 min read"
summary: "There are many ways to give structure to unstructured data so that it can be used systematically in a database."
source: "https://surrealdb.com/blog/using-unstructured-data-to-create-knowledge-graphs-in-surrealdb"
cover: "../../assets/2bfd4dfcd3a73da9.jpg"
---

# Using unstructured data to create knowledge graphs in SurrealDB

![Using unstructured data to create knowledge graphs in SurrealDB](../../assets/2bfd4dfcd3a73da9.jpg)

This post is the first of a small series that will look at how to give structure to unstructured data so that it can be used in all the ways that SurrealDB excels: graph queries, vector search, data visualisations, and more. The examples below use both SurrealQL and Rust, but move one step at a time so that they can be redone in another language (most likely Python) by the reader.

## What unstructured data is

Unstructured data is any set of information that happens to be in an unpredictable format. The languages we use are all examples of unstructured data. Take the following made-up employee for example:

> "My name is Tyler Banks, and I’ve been working as a software engineer for the past four years. Currently, I’m part of the developer relations team, where I focus on creating tools and documentation to help developers integrate our APIs more easily. Our team is led by Brian Thompson."

Note that the data is structured enough for us, because humans are good at dealing with the variety that natural languages have. A person who is proficient in English will come away knowing a few facts about this Tyler Banks, and if asked to create some records to represent the data in SurrealDB, would write something like this. This ability to conceptualise data in a structured manner is what our minds excel at.

```surrealql
LET $manager = CREATE ONLY employee CONTENT {
    name: "Brian Thompson"
};

LET $employee = CREATE ONLY employee CONTENT {
  name: "Tyler Banks",
  gender: "M",
  career_length: 4y,
  reports_to: (SELECT VALUE id FROM ONLY employee WHERE name = "Brian Thompson" LIMIT 1),
  team: "Developer relations",
  role: "Software engineer"
};

RELATE $employee->reports_to->$manager;
```

Now that the data is structured, it can be queried.

```surrealql
SELECT *, 
  ->reports_to->employee AS manager
FROM employee;

-- Output
[
	{
		career_length: 4y,
		gender: 'M',
		id: employee:7qls9c8fttzeg1f0d5w2,
		manager: [
			employee:g4n8736dzfagf3hcjldf
		],
		name: 'Tyler Banks',
		reports_to: employee:g4n8736dzfagf3hcjldf,
		role: 'Software engineer',
		team: 'Developer relations'
	},
	{
		id: employee:g4n8736dzfagf3hcjldf,
		manager: [],
		name: 'Brian Thompson'
	}
]
```

Traditionally, computers have been largely ineffective at working with the original data written in a human language. Fortunately, in recent years we have access to a large variety of large language models (LLMs) that allow the original text to be turned into structured data that doesn't need manual human intervention.

## Choosing and experimenting with a natural language processing model

There are many models and programming languages available to work with unstructured natural language data. In this post we'll look at one in the [`rust_bert`](https://docs.rs/rust-bert/latest/rust_bert/index.html) crate for the Rust programming language, which itself is a port of the original [Transformers library](https://github.com/huggingface/transformers) made by [Hugging Face](https://huggingface.co/), still the most memorable website name out there.

To start, we'll lengthen the average employee introduction and add four more coworkers for Tyler Banks.

```rust
const STATEMENTS: [&str; 5] = [
    "My name is Tyler Banks, and I’ve been working as a software engineer for the past four years. Currently, I’m part of the developer relations team, where I focus on creating tools and documentation to help developers integrate our APIs more easily. Our team is led by Brian Thompson, who oversees both the developer relations and technical support groups. In total, there are two of us on the team: myself and a technical writer. We collaborate closely with the product and engineering teams to ensure our resources are up-to-date and aligned with the latest features.",
    "Hi, I’m Carlos Mendez. I’ve been with the company for six years now, currently serving as a senior data scientist in the AI research team. My work primarily involves developing machine learning models to improve our product recommendations and user experience. I report to Elena Rodriguez, who leads the AI and data science divisions. Our team consists of three scientists, including myself, one specializing in natural language processing and another in predictive analytics. We also work closely with the engineering team to deploy our models into production and monitor their performance in real-world scenarios.",
    "I’m Sophia Lin, a data scientist in the AI research team. I focus on computer vision and collaborate with Carlos and our third team member, who specializes in reinforcement learning. Elena Rodriguez manages our team, and we often work together on cross-functional projects with the product and engineering teams. Our goal is to build scalable AI solutions that enhance user engagement and satisfaction.",
    "I’m Daniel Johnson, the technical writer on the developer relations team. Our team's manager is Brian Thompson, and we ensure that our guides and tutorials are accessible to both new and experienced developers. I work alongside Tyler Banks to create clear and comprehensive documentation for our APIs and developer tools. We also gather feedback from the community to continuously improve our resources.",
    "I’m Emma Wu, the third data scientist in the AI research team. My focus is on reinforcement learning, and I work closely with Carlos and Sophia to develop and refine our models. Elena Rodriguez is our manager, and she helps us align our research with the company’s broader product goals. We regularly present our findings to the engineering team to ensure smooth integration of our models into the product.",
];
```

Now let's look at [the available models](https://docs.rs/rust-bert/latest/rust_bert/pipelines/index.html) for us to choose from. These span a wide range of uses, many of which we don't need such as the language translation model or dialogue model, used respectively to translate into other languages and for chatbots. Some of the models useful for our situation are:

- Question answering model: this model allows us to get answers to a question in

the context of a piece of text. This is the only model we will use in this post.

- Summarisation model: this model summarises a piece of text in a shorter form.

It could be useful for metadata, though probably not necessary with statements this short.

- Zero-shot classification model: this model matches up a number of short pieces

of text (even single words) against a passage of text. For example, "SurrealDB is a multi-model database developed by SurrealDB the company in London" when matched against ["software", "vacation", "heavy metal music"] would show a high score for "software" and a low score for the rest. We will try to get to this model in a later post.

- Sentiment analysis: this model is useful to see if a comment is positive,

negative, or neutral. The statements above are all pretty neutral so we won't need to use it.

- Named entity recognition model: this model is used to find persons, locations,

organisations, and miscellaneous from a text. This model technically does work for us, but is more useful for larger and more complex pieces of content.

The external crates for the code are as follows.

```yaml
anyhow = "1.0.99"
rust-bert = "0.23.0"
serde = "1.0.219"
surrealdb = { version = "2.3.7", features = ["kv-mem"] }
tokio = "1.47.1"
```

The models hold `*mut` pointers to the actual model written in C, so Rust will complain if we try to put them into a `static`. They also can't be [created inside async code](https://github.com/guillaume-be/rust-bert/blob/6db859ef097edfdda338004b4d60deebf6a3ab66/src/lib.rs#L700) because they end up dropping the async runtime if run inside one. We'll get to that part later in the post.

The models can be created with a single line of code:

```rust
QuestionAnsweringModel::new(Default::default()).unwrap();
```

The [possible configuration](https://docs.rs/rust-bert/latest/rust_bert/pipelines/question_answering/struct.QuestionAnsweringConfig.html) pertains to bits like model type, device type, whether to strip accents, and various other things that don't apply here.

The first thing to do is to decide on the best question to give the model. Should we ask it "Who are you?", "Who is the person introduced?", "Who is this?", or something else?

This can be tested by trying them all to see the score returned by each. The first number inside the `.predict()` method is the number of results to return. The second number is the batch size (the number of questions to send in at a time), which isn't important for an example this small.

```rust
let model = QuestionAnsweringModel::new(Default::default()).unwrap();

let questions = [
    "Who are you?",
    "Who is the person introduced?",
    "What employee is this?",
    "Who is this?",
    "Give the name of the main character in the text",
]
.into_iter()
.map(|q| QaInput {
    question: q.to_string(),
    context: STATEMENTS[0].to_string(),
})
.collect::<Vec<QaInput>>();
println!("{:#?}", model.predict(&questions, 2, 5));
```

The reason why we chose two answers is because that will allow us to compare the model's most confident answer with its next most confident answer. Ideally, the first answer should have a very high confidence while the second one should be as low as possible.

The `score` field in the output below shows that the second question ("Who is the person introduced?") is the one with the highest score, with "Tyler Banks" as the person's name coming in at 0.99 while the second answer ("My name is Tyler Banks") for the person's name way behind at 0.003.

```syntax
[
    [
        Answer {
            score: 0.9899401068687439,
            start: 11,
            end: 22,
            answer: "Tyler Banks",
        },
        Answer {
            score: 0.005480845924466848,
            start: 11,
            end: 23,
            answer: "Tyler Banks,",
        },
    ],
    [
        Answer {
            score: 0.9908392429351807,
            start: 11,
            end: 22,
            answer: "Tyler Banks",
        },
        Answer {
            score: 0.0038600098341703415,
            start: 0,
            end: 22,
            answer: "My name is Tyler Banks",
        },
    ],
    [
        Answer {
            score: 0.9357039332389832,
            start: 11,
            end: 22,
            answer: "Tyler Banks",
        },
        Answer {
            score: 0.012884973548352718,
            start: 11,
            end: 68,
            answer: "Tyler Banks, and I’ve been working as a software engineer",
        },
    ],
    [
        Answer {
            score: 0.9888983964920044,
            start: 11,
            end: 22,
            answer: "Tyler Banks",
        },
        Answer {
            score: 0.005144201684743166,
            start: 11,
            end: 23,
            answer: "Tyler Banks,",
        },
    ],
    [
        Answer {
            score: 0.9618594646453857,
            start: 11,
            end: 22,
            answer: "Tyler Banks",
        },
        Answer {
            score: 0.025323452427983284,
            start: 0,
            end: 22,
            answer: "My name is Tyler Banks",
        },
    ],
]
```

Here are the scores for each question in a single chart.

| Question | Top answer score | Top answer |
|---|---|---|
| "Who are you?" | 0.9899 | "Tyler Banks" |
| **"Who is the person introduced?"** | **0.9908** | **"Tyler Banks"** |
| "What employee is this?" | 0.9357 | "Tyler Banks" |
| "Who is this?" | 0.9889 | "Tyler Banks" |
| "Give the name of the main character in the text" | 0.9619 | "Tyler Banks" |

We can also use the output of other questions to feed into the next questions. We can see this by comparing the output of the possible second question, which is the person's role. Since we can grab the output of the first question to feed into the second question, that will allow us to ask "What is the role of Tyler Banks?" instead of "What is the person's role?".

```rust
let questions = [
    "What is the role of Tyler Banks?",
    "What is the person's role?"
]
.into_iter()
.map(|q| QaInput {
    question: q.to_string(),
    context: STATEMENTS[0].to_string(),
})
.collect::<Vec<QaInput>>();
println!("{:#?}", model.predict(&questions, 2, 1));
```

While the output from "What is the person's role?" is still correct, asking the question with the name "Tyler Banks" gives the model a confidence of 0.847 in its first answer as opposed to 0.412.

```surrealql
[
    Answer {
        score: 0.8474743366241455,
        start: 51,
        end: 68,
        answer: "software engineer",
    },
    Answer {
        score: 0.11456232517957687,
        start: 49,
        end: 68,
        answer: "a software engineer",
    },
],
[
    [
        Answer {
            score: 0.4126545786857605,
            start: 51,
            end: 68,
            answer: "software engineer",
        },
        Answer {
            score: 0.0236787311732769,
            start: 49,
            end: 68,
            answer: "a software engineer",
        },
    ],
]
```

## Getting the rest of the needed data

Let's now see what happens when we ask some remaining questions about each employee. We want to know who the person's role is, manager, and team or department. The questions will be as follows:

- "Who is the person introduced?"
- "What is the role of {name}?"
- "In what context does {name} work?"
- "Who is the manager of {name}?"
- "What team does {name} work in?"

```rust
use rust_bert::pipelines::question_answering::{QaInput, QuestionAnsweringModel};

const STATEMENTS: [&str; 5] = [
    "My name is Tyler Banks, and I’ve been working as a software engineer for the past four years. Currently, I’m part of the developer relations team, where I focus on creating tools and documentation to help developers integrate our APIs more easily. Our team is led by Brian Thompson, who oversees both the developer relations and technical support groups. In total, there are two of us on the team: myself and a technical writer. We collaborate closely with the product and engineering teams to ensure our resources are up-to-date and aligned with the latest features.",
    "Hi, I’m Carlos Mendez. I’ve been with the company for six years now, currently serving as a senior data scientist in the AI research team. My work primarily involves developing machine learning models to improve our product recommendations and user experience. I report to Elena Rodriguez, who leads the AI and data science divisions. Our team consists of three scientists, including myself, one specializing in natural language processing and another in predictive analytics. We also work closely with the engineering team to deploy our models into production and monitor their performance in real-world scenarios.",
    "I’m Sophia Lin, a data scientist in the AI research team. I focus on computer vision and collaborate with Carlos and our third team member, who specializes in reinforcement learning. Elena Rodriguez manages our team, and we often work together on cross-functional projects with the product and engineering teams. Our goal is to build scalable AI solutions that enhance user engagement and satisfaction.",
    "I’m Daniel Johnson, the technical writer on the developer relations team. Our team's manager is Brian Thompson, and we ensure that our guides and tutorials are accessible to both new and experienced developers. I work alongside Tyler Banks to create clear and comprehensive documentation for our APIs and developer tools. We also gather feedback from the community to continuously improve our resources.",
    "I’m Emma Wu, the third data scientist in the AI research team. My focus is on reinforcement learning, and I work closely with Carlos and Sophia to develop and refine our models. Elena Rodriguez is our manager, and she helps us align our research with the company’s broader product goals. We regularly present our findings to the engineering team to ensure smooth integration of our models into the product.",
];

fn ask_question(question: &str, context: String, model: &QuestionAnsweringModel) -> String {
    print!("{question} ");

    let mut output = model
        .predict(
            &[QaInput {
                question: question.to_string(),
                context,
            }],
            1,
            1,
        )
        .remove(0);

    let answer = output.remove(0).answer;
    println!("{answer}");
    answer
}

fn main() {
    let model = QuestionAnsweringModel::new(Default::default()).unwrap();
    for person in STATEMENTS {
        let name = ask_question("Who is the person introduced?", person.to_string(), &model);
        ask_question(&format!("What is the role of {name}?"), person.to_string(), &model);
        ask_question(
            &format!("In what context does {name} work?"),
            person.to_string(), &model
        );
        ask_question(
            &format!("Who is the manager of {name}?"),
            person.to_string(), &model
        );
        ask_question(
            &format!("What team does {name} work in?"),
            person.to_string(), &model
        );
        println!();
    }
}
```

That gives us the following output. Thanks to the data being mostly predictable, a single pass through a single model is enough to give us the information we wanted.

```syntax
Who is the person introduced? Tyler Banks
What is the role of Tyler Banks? software engineer
In what context does Tyler Banks work? software engineer
Who is the manager of Tyler Banks? Brian Thompson
What team does Tyler Banks work in? developer relations team

Who is the person introduced? Carlos Mendez
What is the role of Carlos Mendez? senior data scientist
In what context does Carlos Mendez work? machine learning models to improve our product recommendations and user experience
Who is the manager of Carlos Mendez? Elena Rodriguez
What team does Carlos Mendez work in? AI research team

Who is the person introduced? Sophia Lin
What is the role of Sophia Lin? data scientist
In what context does Sophia Lin work? AI research team
Who is the manager of Sophia Lin? Elena Rodriguez
What team does Sophia Lin work in? AI research team

Who is the person introduced? Daniel Johnson
What is the role of Daniel Johnson? technical writer
In what context does Daniel Johnson work? developer relations
Who is the manager of Daniel Johnson? Brian Thompson
What team does Daniel Johnson work in? developer relations team

Who is the person introduced? Emma Wu
What is the role of Emma Wu? third data scientist
In what context does Emma Wu work? reinforcement learning
Who is the manager of Emma Wu? Elena Rodriguez
What team does Emma Wu work in? AI research team
```

## Saving the data in SurrealDB

Now it's time to add SurrealDB to the mix so that we can create records for employees and teams and link them together.

To start, we want a few `DEFINE` statements for the relation tables. These can be set as [`TYPE RELATION`](/docs/surrealql/statements/define/table#table-with-specialized-type-clause). This allows us to ensure that they can only be used as graph edges, as well as from one certain record to another.

```surrealql
DEFINE TABLE member_of  TYPE RELATION IN employee OUT team;
DEFINE TABLE reports_to TYPE RELATION IN employee OUT employee;
DEFINE TABLE works_at   TYPE RELATION IN employee OUT company;
```

But more importantly, we also want a lot of [`UNIQUE`](/docs/surrealql/statements/define/indexes#unique-index) indexes. This will let us use the `UPSERT` statement to create employees if they didn't exist yet, or retrieve the existing employee if the name is already present in the database. We also want unique indexes on the `in` and `out` fields of the relation tables so that an employee can't have more than one `works_at` or `reports_to` between it and a company or team.

```surrealql
DEFINE INDEX only_one_name      ON employee   FIELDS name UNIQUE;
DEFINE INDEX only_one_team_name ON team       FIELDS name UNIQUE;

DEFINE INDEX only_one_team      ON member_of  FIELDS in, out UNIQUE;
DEFINE INDEX only_one_manager   ON reports_to FIELDS in, out UNIQUE;
DEFINE INDEX only_one_company   ON works_at   FIELDS in, out UNIQUE;
```

After that, we will create the company. Let's call it `kicksey_winsey` in honour of a company of the same name from a [series of seven fantasy books](https://en.wikipedia.org/w/index.php?title=The_Death_Gate_Cycle&oldid=1293512653#Arianus,_the_world_of_air).

```rust
db.query("CREATE company:kicksey_winsey").await.unwrap();
```

Every time we come across the data for an employee, we can then do the following:

- `UPSERT` the employee and give it a `name`, `role`, and `context`.
- `UPSERT` the manager as well, for whom we will only know the `name`. We will

create a parameter called `$manager` that holds the `id` from the output of this statement.

- `UPSERT` the team, and return its `id` in the same way as above in a parameter

called `$team`.

- Finally, `RELATE` all of these parameters: the employee to the manager,

employee to the team, manager to the team, employee to the company, and manager to the company.

```rust
db.query(
"LET $employee = UPSERT ONLY employee SET 
name = $name,
role = $role,
context = $context;",
    )
    .bind(("name", name))
    .bind(("role", role))
    .bind(("context", context))
    .query("LET $manager = UPSERT ONLY employee SET name = $manager RETURN VALUE id;")
    .bind(("manager", manager))
    .query("LET $team = UPSERT ONLY team SET name = $team RETURN VALUE id;")
    .bind(("team", team))
    .query(
        "RELATE $employee->reports_to->$manager;
RELATE $employee->member_of->$team;
RELATE $manager->member_of->$team;
RELATE $employee->works_at->company:kicksey_winsey;
RELATE $manager->works_at->company:kicksey_winsey")
```

## The final code

Here is the code to run. The most entertaining way to run it is by using `surreal start --unauthenticated` to start a running SurrealDB instance, because then you can go into Surrealist and experiment with the records once they are added. Otherwise, you can change `connect("ws://localhost:8000")` to `connect("memory")` if you prefer to experiment with the records completely via the Rust SDK.

```rust
use rust_bert::pipelines::question_answering::{QaInput, QuestionAnsweringModel};
use surrealdb::engine::any::connect;
use tokio::runtime::Runtime;

const STATEMENTS: [&str; 5] = [
    "My name is Tyler Banks, and I’ve been working as a software engineer for the past four years. Currently, I’m part of the developer relations team, where I focus on creating tools and documentation to help developers integrate our APIs more easily. Our team is led by Brian Thompson, who oversees both the developer relations and technical support groups. In total, there are two of us on the team: myself and a technical writer. We collaborate closely with the product and engineering teams to ensure our resources are up-to-date and aligned with the latest features.",
    "Hi, I’m Carlos Mendez. I’ve been with the company for six years now, currently serving as a senior data scientist in the AI research team. My work primarily involves developing machine learning models to improve our product recommendations and user experience. I report to Elena Rodriguez, who leads the AI and data science divisions. Our team consists of three scientists, including myself, one specializing in natural language processing and another in predictive analytics. We also work closely with the engineering team to deploy our models into production and monitor their performance in real-world scenarios.",
    "I’m Sophia Lin, a data scientist in the AI research team. I focus on computer vision and collaborate with Carlos and our third team member, who specializes in reinforcement learning. Elena Rodriguez manages our team, and we often work together on cross-functional projects with the product and engineering teams. Our goal is to build scalable AI solutions that enhance user engagement and satisfaction.",
    "I’m Daniel Johnson, the technical writer on the developer relations team. Our team's manager is Brian Thompson, and we ensure that our guides and tutorials are accessible to both new and experienced developers. I work alongside Tyler Banks to create clear and comprehensive documentation for our APIs and developer tools. We also gather feedback from the community to continuously improve our resources.",
    "I’m Emma Wu, the third data scientist in the AI research team. My focus is on reinforcement learning, and I work closely with Carlos and Sophia to develop and refine our models. Elena Rodriguez is our manager, and she helps us align our research with the company’s broader product goals. We regularly present our findings to the engineering team to ensure smooth integration of our models into the product.",
];

fn ask_question(question: &str, context: String, model: &QuestionAnsweringModel) -> String {
    let mut output = model
        .predict(
            &[QaInput {
                question: question.to_string(),
                context,
            }],
            2,
            2,
        )
        .remove(0);

    output.sort_by(|a, b| b.score.total_cmp(&a.score));
    output.remove(0).answer
}

fn main() {
    let model = QuestionAnsweringModel::new(Default::default()).unwrap();

    let rt = Runtime::new().unwrap();

    rt.block_on(async {
        let db = connect("ws://localhost:8000").await.unwrap();
        db.use_ns("ns").use_db("db").await.unwrap();
        db.query(
     "DEFINE TABLE member_of  TYPE RELATION IN employee OUT team;
      DEFINE TABLE reports_to TYPE RELATION IN employee OUT employee;
      DEFINE TABLE works_at   TYPE RELATION IN employee OUT company;

      DEFINE INDEX only_one_name      ON employee   FIELDS name UNIQUE;
      DEFINE INDEX only_one_team_name ON team       FIELDS name UNIQUE;

      DEFINE INDEX only_one_team      ON member_of  FIELDS in, out UNIQUE;
      DEFINE INDEX only_one_manager   ON reports_to FIELDS in, out UNIQUE;
      DEFINE INDEX only_one_company   ON works_at   FIELDS in, out UNIQUE;"
        )
        .await
        .unwrap();

        db.query("CREATE company:kicksey_winsey").await.unwrap();

        for person in STATEMENTS {
            let name = ask_question("Who is the person introduced?", person.to_string(), &model);
            let role = ask_question(
                &format!("What is the role of {name}?"),
                person.to_string(),
                &model,
            );
            let context = ask_question(
                &format!("In what context does {name} work?"),
                person.to_string(),
                &model,
            );
            let manager = ask_question(
                &format!("Who is the manager of {name}?"),
                person.to_string(),
                &model,
            );
            let team = ask_question(
                &format!("What team does {name} work in?"),
                person.to_string(),
                &model,
            );

            db.query(
            "LET $employee = UPSERT ONLY employee SET 
            name = $name,
            role = $role,
            context = $context;
        ",
                )
                .bind(("name", name))
                .bind(("role", role))
                .bind(("context", context))
                .query("LET $manager = UPSERT ONLY employee SET name = $manager RETURN VALUE id;")
                .bind(("manager", manager))
                .query("LET $team = UPSERT ONLY team SET name = $team RETURN VALUE id;")
                .bind(("team", team))
                .query(
                    "RELATE $employee->reports_to->$manager;
           RELATE $employee->member_of->$team;
           RELATE $manager->member_of->$team;
           RELATE $employee->works_at->company:kicksey_winsey;
           RELATE $manager->works_at->company:kicksey_winsey",
                )
                .await
                .unwrap();
        }
    });
}
```

Now that the data is structured, you can use graph queries like the following in Surrealist to see not just structured output...

```surrealql
SELECT *, 
    ->works_at->company AS company,
    ->member_of->team AS team
FROM employee SPLIT company, team;

[
	{
		company: company:kicksey_winsey,
		id: employee:897k8b8knjc5580zdeap,
		name: 'Elena Rodriguez',
		team: team:oepx56g8z5ycl5ky9zcp
	},
	{
		company: company:kicksey_winsey,
		context: 'AI research team',
		id: employee:ctn4j70ai0o58n40039t,
		name: 'Sophia Lin',
		role: 'data scientist',
		team: team:oepx56g8z5ycl5ky9zcp
	},
	{
		company: company:kicksey_winsey,
		context: 'machine learning models to improve our product recommendations and user experience',
		id: employee:hp757y574s0jsmmpik78,
		name: 'Carlos Mendez',
		role: 'senior data scientist',
		team: team:oepx56g8z5ycl5ky9zcp
	},
	{
		company: company:kicksey_winsey,
		context: 'reinforcement learning',
		id: employee:i1x4n0n0mrgmyp1fyve8,
		name: 'Emma Wu',
		role: 'third data scientist',
		team: team:oepx56g8z5ycl5ky9zcp
	},
	{
		company: company:kicksey_winsey,
		context: 'software engineer',
		id: employee:npsl35ryp6zh3gcpxtwr,
		name: 'Tyler Banks',
		role: 'software engineer',
		team: team:0zafookbed9oawg6tf5z
	},
	{
		company: company:kicksey_winsey,
		id: employee:rq2da3godh2zyectk04o,
		name: 'Brian Thompson',
		team: team:0zafookbed9oawg6tf5z
	},
	{
		company: company:kicksey_winsey,
		context: 'developer relations',
		id: employee:s7l6rlo529jpc1ml7svp,
		name: 'Daniel Johnson',
		role: 'technical writer',
		team: team:0zafookbed9oawg6tf5z
	}
]
```

...but also a graphical view of the same data!

Curious about how graph visualisation in Surrealist works? Check out [this post](/blog/visualising-your-data-with-surrealists-graph-view) that goes into much greater detail on the subject.

This blog post has only scratched the surface of how to work with unstructured data, so we'll see you again soon in the next one!
