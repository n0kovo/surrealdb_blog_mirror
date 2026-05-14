---
title: "From medical doctor to rust developer - interview with our new Senior Clinical Research Fellow"
slug: "from-medical-doctor-to-rust-developer--interview-with-our-new-senior-clinical-research-fellow"
date: "2024-03-08T00:00:00.000Z"
categories:
  - "community"
read_time: "10 min read"
summary: "Read about her journey and why she is using SurrealDB for her current research."
source: "https://surrealdb.com/blog/from-medical-doctor-to-rust-developer--interview-with-our-new-senior-clinical-research-fellow"
cover: "../../assets/9d18a2147fa505fa.jpg"
---

# From medical doctor to rust developer - interview with our new Senior Clinical Research Fellow

![From medical doctor to rust developer - interview with our new Senior Clinical Research Fellow](../../assets/9d18a2147fa505fa.jpg)

The following is a conversation between Lizzie Holmes and Dr Caroline Morton, where you will learn of her journey from a medical doctor to a Rust developer and why she is using SurrealDB for her current research.

## Who is Dr Caroline Morton

Dr Caroline Morton is a Senior Clinical Research Fellow at Queen Mary University of London, where she builds reproducible data pipelines for a large genomic project called Genes and Health. Caroline previously trained as a GP and epidemiologist in London, and worked on the COVID-19 data platform OpenSAFELY at the University of Oxford. She is starting a PhD in Medical Statistics at the London School of Hygiene and Tropical Medicine exploring ways of creating realistic synthetic data. She likes to use Rust and Python to solve difficult problems in the medical space, and runs a medical education simulation platform called Clinical Metrics with [Maxwell Flitton (our Senior Software Engineer).](/features)

## Let's dive into the interview

### What is your story? How did you get here?

Good question! Let me start with where "here" is. I spend most of my time writing software that helps other epidemiologists or health researchers write better studies.

I define that to be studies that are more reproducible, good quality and easy to understand.

Most research these days involves writing statistical code and I strongly believe that we can take advantage of what has already been done in the software industry and make research better by adopting these concepts and practices.

Things like code review, unit testing, and good documentation are second nature to programmers but aren't universally done in research. I want to change that.

So going back to your question, I got into coding through a series of coincidences and good fortune. I did medical school and then thought a part-time Masters in Epidemiology might be cool as I was interested in research. I fell in love with programming there - writing statistical code to figure stuff out. We were using Stata at the time.

At the same time, I was working part-time as an education fellow at Imperial College. I had a great boss, Professor Sue Smith, and was given a lot of freedom to do qualitative research into the best educational interventions in medical school. Sue introduced me to a guy called Dr Matt Williams, an oncologist, who wanted to set up a weekend course teaching Python coding to medical students. So, whilst setting that up, I started to pick up Python by taking a lot of online courses and trying stuff out. I got obsessed with it, trying to figure it out.

I went on and did GP training eventually, but always worked part-time as I always had another job either running a course with Matt on teaching Python or working as a software engineer. Max and I were friends by then and used to meet up and do coding projects together - first in Python, and then later Rust.

### How did you meet Max?

A coincidence really! Max was speaking at a conference that was hosted in my office and I just happened to be walking past. It was an introduction to programming, and I just thought, “he seems like a guy I should know”. I went to his talk and the rest is history!

### In terms of your path into Rust, how did you start that?

Max and I were writing the medical education simulation software that our company makes ([Clinical Metrics](https://clinicalmetrics.co.uk)). It was all written in Python and that seemed great, but when you actually had real users who all logged in at the same time, we had a lot of performance issues so we had to look at a more performant language.

Max was already getting into Rust by then, eventually writing the book [Rust Web Programming](https://www.packtpub.com/product/rust-web-programming/9781800560819) so it was natural to move in that direction and it solved the performance problems we were having.

### Let's now dive into your PhD - what is it about, and why is it important?

My PhD explores the ways that you can make synthetic data for electronic health record research. Electronic health record research is research that is based on data which are captured during routine care, like a visit to your GP.

I'm really a big believer that we should be open about what we're doing in terms of research. We are writing code but when it comes to results, we are often writing papers that say this is a description of the study, and the results.

You don't actually get to see the statistical code that actually did the research. That's a shame in my view because I want to see how the research was actually done at the level of the code.

Therefore I think we need to move to a model where people release their code alongside their study, but the biggest criticism that people have of this model is that the code is not very useful if you can't release the data alongside it, and we can't release the data, right?

I mean it could be your GP record - who would want that to be released publicly?

Therefore, I want to create synthetic data that is good quality. Similar in structure to the real data but completely made up. The code can be run against this synthetic data and be released with the study, but there are no privacy concerns.

I am just at the beginning, but there's lots of stuff I'm really looking forward to. There is an opportunity to create massively complicated synthetic datasets in a way that has been difficult to do in the past because the compute power needed. Rust makes it a lot easier to imagine these possibilities.

![Caroline Morton - dummy data](../../assets/7ca8794b6f315a84.jpg)

### How long would it take to create that?

I don't know, but I don't think it would take very long in Rust. As an example, I've done an experiment where I created 10 patients and all their records in less than a second. That's a simple example, but I think it can scale up well.

### When did you first hear about SurrealDB and how does SurrealDB fit into your research?

I first heard about SurrealDB when my good friend and business partner Max joined.

I thought it sounded like an interesting concept and I got really interested in using SurrealDB to solve some of the problems I saw.

Firstly, pretty much all the reference data that is needed to create synthetic data is arranged in a graph or a tree structure. I need a way to traverse that tree and send off queries, which eventually come back to form the synthetic data. It is difficult to do that in a traditional database, especially at scale. That's one aspect where I think SurrealDB is going to be huge.

The second is live querying. I want to be able to do complicated queries on the data without having to pull the data out of the database.

Finally, you have the potential to run models directly using SurrealML, without moving data back and forth between the database and model.

I am not sure what models I am going to use right now but just having it as a possibility is huge.

### What's the first step in getting started with this?

The first step is to try and load all of the potential diagnoses for the entire UK reference set, what we call the data dictionary, into SurrealDB. I'm gonna try this next week. We'll see how it goes.

### The whole dictionary?

Yeah, we're talking about hundreds and thousands of what are called SNOMED codes. They are codes that represent events like a diagnosis of a cough or a blood test result.

When you see a GP, they are picking diagnoses from the data dictionary and that is what gets coded into a patient record.

### In terms of the outcomes, what is your dream product at the end of this?

I really want to produce a tool that you as an epidemiologist use as part of your normal workflow.

Right now we write down a graph called a [Directed Acyclical Graph (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) at the start of a study, and it says things like how is this variable, smoking, related to another variable such as a particular type of cancer.

We then build up what we know or speculate about how variables might be related to each other. My idea is that since we have to write a DAG anyway, we can consume this into a program and set some parameters like size of population, and the program will produce the realistic synthetic dataset for you to use and download.

What is key here is the relationships between the variables are maintained in this data. That is essential and will allow us to use this synthetic data for solving all sorts of problems.

I am particularly thinking about sharing data with code, as mentioned before, but I can see it would also be helpful for training the next generation of researchers, testing models, testing healthcare software and lots of things really.

### What are a couple of ways that we can encourage more women to enter the ecosystem of writing code?

This may be incorrect in terms of the actual numbers, but my experience is that there are actually quite a lot of women who are in data science. It doesn't feel like there is a huge gender disparity.

It does feel like there are a lot less women who are writing software, even though both groups are essentially writing code.

I think what we need to do is really encourage people to come across from data science into software.

I think that can feel very intimidating, but there are a ton of resources and free or very cheap courses out there that make it easier.

It also depends on how you learn best. I personally prefer devising a project and then learning about a design pattern, a package or an approach through that project. That is basically how I learned to code.

Asking for help is also important. The online forums like GitHub issues or Stack Overflow can feel scary, especially if you have seen or even experienced being told off for not asking questions clearly.

Finding a group of people who are at the same level as you or a bit further along can be so helpful.

Initiatives like [Women Who Code](https://womenwhocode.com/) or [One Health](https://www.onehealthtech.com) Tech can make a big difference by growing a community.

## Announcing the launch of our new series: Women in Rust.

As you've heard from Caroline, community and proactive action can make a big difference! That’s why we’re thrilled to be launching our new series Women in Rust, where women can come together to explore, learn, and share our passion for Rust programming language!

You can sign up here: [https://www.meetup.com/women-in-rust/](https://www.meetup.com/women-in-rust/)

Our first hybrid event will be hosted at our London HQ and available to rewatch. This will be on Thursday 4 April, details via Meetup, we hope to see you there!

This International Womens’ Day we are also launching our new Discord channel on our SurrealDB server, [women-of-surrealdb](https://discord.com/channels/902568124350599239/1215623756303831092) a place for women within our SurrealDB community to come together, ask questions and connect, and also share ideas and inspiration from the wider tech ecosystem.
