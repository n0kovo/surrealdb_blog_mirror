---
title: "Enhancing Retrieval-Augmented Generation with SurrealDB"
slug: "enhancing-retrieval-augmented-generation-with-surrealdb"
date: "2025-01-31T00:00:00.000Z"
categories:
  - "tutorials"
  - "featured"
  - "ai"
read_time: "25 min read"
summary: "GraphRAG: Enhancing Retrieval-Augmented Generation with SurrealDB, Gemini and DeepSeek"
source: "https://surrealdb.com/blog/enhancing-retrieval-augmented-generation-with-surrealdb"
cover: "../../assets/0ac49324d93f27cf.jpg"
---

# Enhancing Retrieval-Augmented Generation with SurrealDB

![Enhancing Retrieval-Augmented Generation with SurrealDB](../../assets/0ac49324d93f27cf.jpg)

**GraphRAG: Enhancing Retrieval-Augmented Generation with SurrealDB, Gemini and DeepSeek**

Imagine a detective investigating a complex case. They have a mountain of evidence: witness statements, forensic reports, surveillance footage. But sifting through it all, trying to connect the dots and uncover hidden relationships, proves overwhelming. Traditional RAG systems are like this detective, diligently analysing individual pieces of information but often missing crucial connections that lie hidden within the data.

Now, imagine that same detective equipped with a powerful tool - a knowledge graph that visually maps out all the entities involved in the case and their intricate relationships. Suddenly, the detective can see the bigger picture, identify key connections, and even infer new information that was previously obscured. This is the power of GraphRAG: by combining the strengths of traditional RAG with the semantic richness of graph databases, we unlock a new level of understanding and insight.

In this blog post, we'll explore how GraphRAG enhances Retrieval-Augmented Generation by incorporating graph databases in SurrealDB alongside traditional vector search. We'll delve into the practical implementation, demonstrate tangible benefits through concrete examples and code, and compare the impact of different LLMs, from locally run open-source models like DeepSeek to massive hosted models like Gemini. Join us on this journey as we unlock the true potential of RAG with the power of graphs.

**LLM and Hosting Options**

Choosing the right LLM and hosting option can significantly impact your GraphRAG system's performance and capabilities. Here's a comparison of the three options explored in this post:

| Feature | Gemini 1.5 Flash | DeepSeek R1 (Local) | DeepSeek R1 (TogetherAI) |
|---|---|---|---|
| Model Size | ~32 billion parameters | 7 billion parameters | 671 billion parameters |
| Context Window | Massive | Large | Limited by api |
| Chunking Required | No | No | Yes |
| Hosting | Google Cloud | Local | TogetherAI Cloud |
| Speed | Extremely Fast | Moderate | Moderate |
| Control | Less | Full | Less |
| Cost | Pay-as-you-go | Dependent on infrastructure | Pay-as-you-go |
| Benefits | Powerful performance, handles complex queries, large context window | Local control, potentially lower latency, large context window | Access to full model, large context window |
| Limitations | Less control, cost may vary | Requires local infrastructure, potential maintenance | Token limits require chunking, less control, cost may vary |

As you can see, each option offers a unique set of advantages and disadvantages.

- **Gemini**, with its massive size and powerful performance, excels at handling complex queries and large documents directly. Its API also allows for uploading attachments, reducing the need for repetitive interactions.
- **DeepSeek R1 (Local)** offers greater control and potentially lower latency due to local hosting. Its large context window also eliminates the need for chunking.
- **DeepSeek R1 (TogetherAI)** provides access to the full model but necessitates chunking due to token limits. This option offers a balance between model power and accessibility.

**DeepSeek R1 (DeepSeek hosted)** the DeepSeek hosted version wasn’t tested due to cyber security concerns and an outage of registering API tokens at the time of this analysis.

Ultimately, the best choice depends on your specific needs and priorities. Consider factors such as the complexity of your queries, the size of your documents, your budget, and your desired level of control when making your decision.

### **Why Graphs Matter**

Traditional RAG systems rely on vector search to find relevant text chunks based on semantic similarity. However, this approach can miss crucial connections and contextual information not explicitly present in the retrieved text.

By using a knowledge graph, we can explicitly represent entities and their relationships as nodes and edges. This allows for a more nuanced understanding of the context surrounding a user's query.

### **Extending Semantic Search with Graphs**

Here's how graph databases improve RAG systems:

- **Context Enrichment:** Vector search within a graph database leverages both the semantic meaning of the text and the structural relationships between entities. This enriches the context for the language model.
- **Relationship Awareness:** Graph traversal reveals connections between concepts that might be missed by vector search alone. For example, if a user asks about "Sam Rivera's work," a graph-based system could identify related entities like "Dulce Base" or "Paranormal Military Squad."
- **Reasoning Capabilities:** The graph structure enables reasoning based on relationships, allowing the system to infer new information.
- **Improved Accuracy:** Combining semantic meaning with relationship information leads to more accurate and contextually relevant answers.
- **Dynamic and Flexible:** The graph structure adapts to data changes, ensuring robustness and allowing for the addition of new knowledge.

Adding graph capabilities to vector search enables a RAG system to move beyond simple keyword matching and reason about the user's query within a broader context.

### **The SurQL to retrieve the graph**

The get_related_entities function uses SurrealDB's vector search capabilities to find related entities based on text descriptions.

```surrealql
DEFINE FUNCTION OVERWRITE fn::get_related_entities($text: string) {

  LET $emb = fn::sentence_to_vector($text);
  
  RETURN SELECT id, description, ->RELATED_TO.{out, strength, description}
    FROM PERSON
    WHERE embedding <|5,COSINE|> $emb;
  
};
```

Here's a breakdown:

- `DEFINE FUNCTION OVERWRITE fn::get_related_entities($text: string) { ... };:` This defines a function named fn::get_related_entities that accepts a string argument $text. The OVERWRITE keyword ensures any existing function with the same name is replaced.
- `LET $emb = fn::sentence_to_vector($text);:` This calculates the vector embedding of the input string $text using the `fn::sentence_to_vector function` (a custom function likely using a pre-trained model like GloVe) and stores the result in the `$emb` variable.
- `RETURN SELECT id, description, ->RELATED_TO.{out, strength, description} ...:` This specifies the data to be returned, including the id, description, and related records (with out, strength, and description fields) linked through the `RELATED_TO` edge.
- `FROM PERSON:` This indicates the query should be executed against the `PERSON` table.
- `WHERE embedding <|5,COSINE|> $emb;:` This filters records in the `PERSON` table based on the semantic similarity of their embeddings to the input, using a k-nearest neighbours search (KNN) with cosine distance to find the 5 most similar records.

In essence, this function takes a text query, converts it into a vector embedding, and finds the 5 most semantically similar records in the `PERSON` table, returning their details and related records.

### **Enhancing Your RAG with Graph Capabilities**

The notebooks provides code examples demonstrating how to use these graph capabilities.

### **Retrieving Context from the Graph**

```python
get_the_graph_context_surql = "fn::get_related_entities('{0}')"

outcome = await db.query(
    get_the_graph_context_surql.format("Who is the main character?")
)
```

This snippet calls the `fn::get_related_entities` function to get context from the graph, executing it with the question "Who is the main character?" and transforming the result into a data structure used to provide context to the language model.

### **Generating a Response with a Knowledge Graph**

These functions create a message for the LLM by augmenting the input prompt with data from the database. Depending on the model we follow different methods for querying the LLM.

**Gemini:**

1)Upload the corpus document as an attachment

2)Query the database for the relevant graph data

3)Construct the prompt combining the graph and question

4)Send the prompt and reference to the API for processing

**DeepSeek R1 (Local):**

1)Query the database for the relevant graph data

2)Construct the prompt combining the corpus, graph and question

3)Send the prompt and reference to the API for processing

**DeepSeek R1 (TogetherAI):**

1)Query the database for the relevant graph data

3)Query the database for the relevant chunks from the corpus document

3)Construct the prompt combining the corpus chunks, graph and question

4)Send the prompt and reference to the API for processing

In all cases the function get_graph_RAG_response , while generate_graph_RAG_messages generates the semantically relevant knowledge graph using `fn::get_related_entities.` For the chunking operation we leverage the function `fn::get_related_chunks.` which is similar to the related entities function but just returns the semantically similar chunks without the need for a graph.

The standard RAG prompt makes reference to the source material and appends the input text as such:

> Goal - You are a researcher who is providing answers to a question for you client based on documents provided you. Answer the questions to the best of your ability given the documents.

> >

> \\ {question} \\

>

We extend that prompt to include the knowledge graph for comparison:

> Goal-

> >

> You are a researcher who is providing answers to a question for your client based on documents provided to you.

>

> You also have access to a knowledge graph based on the documents provided.

>

> Answer the questions to the best of your ability given the documents and knowledge graph.

> >

> \<knowledge graph>

>

> {knowledge_graph}

>

> \</knowledge graph>

>

> \<question>

>

> {question}

>

> \</question>

>

For the DeepSeek prompts we also incorporate a section to contain the document or chunks of the document in a section delimited by .

## Comparing Results

While both standard RAG and Graph RAG aim to answer questions based on a given text, their approaches and results differ significantly. Let's delve deeper into the specific examples from the notebook to highlight these differences:

**1. Enhanced Detail and Context:**

- **Question:** "Who is the main character and what motivates them?"
- **Observation:** Graph RAG consistently provides more detailed and contextually rich answers. For instance, in response to this question, Graph RAG not only identifies Alex Mercer as the main character but also provides a more nuanced understanding of his motivations. It gleans details like mentorship and survival from the knowledge graph, which are not explicitly mentioned in the text but are crucial to understanding his character. Standard RAG, on the other hand, primarily focuses on motivations explicitly stated in the text, resulting in a less comprehensive analysis.

**2. Inference and Relationship Awareness:**

- **Question:** "What places and people does Alex Mercer hold dearest?"
- **Observation:** Graph RAG demonstrates a superior ability to infer relationships and connections that are not explicitly stated in the text. In this case, standard RAG struggles to provide relevant information as the text doesn't explicitly mention personal attachments. However, Graph RAG leverages the knowledge graph to infer Alex's close relationships with Jordan Hayes and Sam Rivera based on the strength of their connections, showcasing its ability to understand implicit relationships.

**3. Consistent and Nuanced Table Generation:**

- **Question:** "Create a table of places that Alex communicates with..." and "Create a table of places that Alex visits..."
- **Observation:** Both standard RAG and Graph RAG can generate tables in response to complex queries. However, Graph RAG consistently incorporates specific data from the knowledge graph, such as bond strength scores and location importance, leading to more nuanced and informative tables. Standard RAG, while capable of generating tables, often relies on subjective assessments and may miss crucial details present in the knowledge graph.

**4. Subjectivity vs. Grounded Responses:**

- **Question:** "Based on Alex Mercer's strongest relationships and the places most important to the plot, choose a scene that is the most emotionally charged..."
- **Observation:** When faced with subjective questions, Graph RAG still manages to provide grounded responses by leveraging the knowledge graph. It identifies key relationships and locations based on their strength and relevance, leading to a more focused and relevant scene selection. Standard RAG, while capable of creative interpretation, may not be as consistent in identifying the most relevant aspects due to its reliance on textual analysis alone.

In summary, these examples illustrate how Graph RAG consistently outperforms standard RAG in terms of detail, context, inference, and nuanced understanding. By incorporating a knowledge graph, Graph RAG moves beyond simple text matching and delves into the intricate web of relationships and meanings, leading to more comprehensive and insightful responses.

## **Model-Specific Observations: A Tale of Two LLMs**

While both Gemini and DeepSeek showcased the advantages of graph-enhanced RAG, their outputs revealed some intriguing differences, highlighting the diverse capabilities of these language models.

**Quality of Response:**

Gemini consistently generated more comprehensive and nuanced responses, demonstrating a deeper understanding of the context and relationships within the knowledge graph. For instance, when asked about Alex Mercer's motivations, Gemini provided a detailed analysis, incorporating information from both the text and the knowledge graph to paint a complete picture of his character. DeepSeek's responses, while accurate, were sometimes overly simplistic and lacked the same level of depth.

**Example:**

- **Question:** "Who is the main character and what motivates them?"
- **Gemini:** (Provides a detailed analysis of Alex Mercer's motivations, including duty, determination, hunger for knowledge, mentorship, and survival, drawing evidence from both the text and the knowledge graph.)
- **DeepSeek:** (Provides a more basic response, focusing primarily on duty, determination, and a hunger for knowledge, with less emphasis on mentorship and survival.)

**Following Formatting Instructions:**

Gemini consistently followed the given formatting instructions, producing well-structured markdown tables and lists as requested. DeepSeek, on the other hand, struggled with this aspect, sometimes failing to generate proper markdown tables or deviating from the specified format. This suggests that Gemini has a better grasp of formatting conventions and can more reliably produce outputs that adhere to specific requirements.

**Example:**

- **Question:** "Create a table of places that Alex visits..."
- **Gemini:** (Generates a well-formatted markdown table with all the requested columns and information.)
- **DeepSeek:** (Attempts to generate a table but struggles with the markdown formatting, resulting in an inconsistent and less readable output.)

**Speed:**

Gemini exhibited significantly faster response times compared to both locally hosted DeepSeek and DeepSeek hosted on TogetherAI. This highlights Gemini's impressive processing power and efficiency, making it a strong choice for applications where speed is critical. While DeepSeek's local hosting offers potential advantages in terms of control and data privacy, it may come at the cost of slower response times.

**DeepSeek's "Think" Section:**

One unique aspect of DeepSeek's responses is the inclusion of a "think" section, which provides valuable insights into the model's reasoning process. This section reveals how DeepSeek utilises the knowledge graph to enhance its responses, offering a better understanding of the mechanisms at work. This transparency is invaluable for developers and researchers seeking to analyse and improve RAG systems.

**In summary, both Gemini and DeepSeek demonstrated the benefits of graph-enhanced RAG, but their outputs revealed distinct differences in terms of response quality, formatting capabilities, and speed. Gemini's power and efficiency make it a strong choice for complex tasks and large-scale applications, while DeepSeek's local hosting and "think" section offer advantages in terms of control, transparency, and potential for customisation.**

### **Analysing Sample Questions**

The notebook includes several sample questions to highlight the differences in responses between standard RAG and graph-enhanced RAG.

**1:** "Who is the main character and what motivates them?"

------ STANDARD RAG -------------------------

- **Main Character:** Agent Alex Mercer is arguably the main character, though the narrative is ensemble-focused, giving significant attention to the perspectives and motivations of other key players.
- **Motivations:**
- **Duty and Obedience:** Mercer is a highly trained agent, deeply committed to following protocols and completing his assigned mission. This is demonstrated by his initial compliance with Agent Cruz's directives, though this is gradually challenged throughout the story.
- **Discovery and Understanding:** Despite his inherent obedience, Mercer is driven by a powerful desire to understand the mysteries of Dulce Base and the alien communication. This intellectual curiosity clashes with his ingrained sense of duty, creating internal conflict that fuels his actions.
- **Protection of Humanity:** Mercer's concern for the safety and well-being of humanity is a significant motivator. His ultimate goal is to ensure that first contact with extraterrestrial intelligence is handled responsibly and doesn't lead to harm.
- **Teamwork and Collaboration:** As the story progresses, Mercer demonstrates a growing reliance on and trust in his team members. His leadership style shifts from strict adherence to protocol to collaborative problem-solving, emphasising the importance of combined human insight to navigate the unprecedented challenges they face.

While other characters like Dr. Jordan Hayes (driven by scientific curiosity) and Agent Taylor Cruz (motivated by ambition and control) also play pivotal roles, Mercer's character arc, spanning from strict compliance to a more nuanced understanding of the mission, positions him as the central figure through which the overarching narrative unfolds.

----- GRAPH RAG -------------------------

- **Main Character:** Agent Alex Mercer is the main character of the story. While the narrative features other important agents, Alex's perspective is central, and his actions and internal conflicts drive much of the plot.
- **Motivations:** Alex is motivated by several factors:
- **Duty and Responsibility:** As a high-ranking member of the Paranormal Military Squad, he feels a strong sense of duty to complete his mission and protect national security. This is evident in his compliance with Agent Cruz’s orders and his concern for the safety of his team.
- **Determination and Resolve:** Alex possesses unwavering determination and displays resilience in the face of the unknown. He demonstrates this through his consistent engagement with the mission even when uncertain and in the face of challenges.
- **A Hunger for Knowledge:** Alex shows significant curiosity and a desire for understanding beyond following orders. This is seen in his conversations with Dr. Hayes, where he acknowledges a sense of being pulled into "someone else's game" and seeks deeper truths beyond the official narrative. He is driven to discover and understand the mysteries of Dulce Base.
- **Mentorship:** Alex acts as a mentor to Sam Rivera, guiding and supporting their contributions. This suggests a desire to foster growth and share his expertise, indicating a sense of responsibility beyond his own mission.
- **Survival:** While duty and knowledge drive him, survival and the protection of his team are also strong motivating factors. This is implicit in his actions throughout the story as he continuously assesses risks and strives for the team's success.

**Analysis:** The graph RAG response provides a more definitive answer and includes additional motivations like mentorship and survival, gleaned from the knowledge graph.

**2:** "What places and people does Alex Mercer hold dearest? Format your response as a markdown list."

----- STANDARD RAG -------------------------

Based solely on the provided text, there is no explicit mention of places or people Alex Mercer holds dearest. The text focuses on his professional life and his participation in Operation: Dulce. While he shows camaraderie and respect for his team members (Jordan Hayes, Taylor Cruz, and Sam Rivera), there's no indication of these relationships extending beyond professional respect and shared mission objectives. The narrative doesn't offer details about his personal life or attachments outside of his work with Paranormal Military Squad.

----- GRAPH RAG -------------------------

Based on the provided text and knowledge graph, here's what we can infer about the places and people Alex Mercer holds dearest:

- **Places:** The knowledge graph strongly indicates Dulce Base as a significant location for Alex Mercer due to his involvement in Operation: Dulce. While the text doesn't explicitly state he holds it *dear*, its importance to his mission suggests a strong connection. Washington D.C. is also mentioned, representing his chain of command and source of orders. Whether he holds Washington dear is unclear, as the connection is purely professional.
- **People:** The knowledge graph highlights strong relationships with Jordan Hayes and Sam Rivera, indicating a close working relationship and mutual respect. The strength of these connections (9 and 7 respectively) suggests a level of camaraderie and trust exceeding mere professional obligation. Taylor Cruz is also mentioned, but with a lower strength rating (8), indicating a working relationship with less personal closeness. There is no information in the provided text to suggest he holds any of these individuals "dearest" in a personal, emotional sense, rather that these are people he works closely with, trusts, and respects professionally. The text suggests he respects Jordan's intellect highly.

**Analysis:** The standard RAG system fails to provide any relevant information, while the graph RAG system infers the answer based on the knowledge graph.

**3:** "Create a table of places that Alex communicates with: In the first column indicate the person. In the 2nd column list the frequency he has scenes with them. In the 3rd column list the places they had scenes together ordered by In the 4th column indicate the strength of the bond between the people In the 5th column score the total weight of the interactions across the output the response in a table format using markdown language."

----- STANDARD RAG -------------------------

## **Alex Mercer's Communication Network**

| **Person** | **Communication Frequency** | **Places of Communication (Ordered by Importance)** | **Bond Strength** | **Interaction Weight Score** |
|---|---|---|---|---|
| Jordan Hayes | Very High | 1. Dulce Base Command Center (multiple scenes, critical collaborations), 2. Dulce Base Corridors (shared concerns), 3. Elevator to Dulce (shared apprehension), 4. Dulce Base Lab (scientific collaboration) | Very Strong | 9 |
| Taylor Cruz | High | 1. Dulce Base Command Center (conflicts and uneasy alliances), 2. Briefing Room (initial instructions, later collaboration), 3. Equipment Bay (philosophical disagreement) | Strong but strained | 7 |
| Sam Rivera | High | 1. Dulce Base Command Center (collaborative work, shared excitement), 2. Sam's Office (advice and encouragement), 3. Dulce Base Corridors (shared mission) | Strong | 7 |

**Note:** The "Interaction Weight Score" is a subjective assessment based on the length and significance of their interactions throughout the provided text. A higher score indicates more frequent and/or more impactful interactions. The ordering of places within each person's row reflects the apparent importance of the setting to their relationship and the overall narrative.

----- GRAPH RAG -------------------------

Based on the provided text and knowledge graph, here's a table summarising Alex Mercer's communication and interactions, keeping in mind that the provided knowledge graph lacks information on the *frequency* of scenes and requires inference from the narrative. The "Strength of Bond" and "Total Interaction Weight" columns are estimations based on the narrative and the knowledge graph's strength scores. Precise quantification isn't possible without more structured data.

| **Person** | **Frequency of Scenes** | **Places of Interaction (ordered by importance)** | **Strength of Bond** | **Total Interaction Weight (estimated)** |
|---|---|---|---|---|
| Jordan Hayes | Very High | Dulce Base Command Center, Mainframe Room, Communications Hub, Underground Meeting Room | 9 | 90 |
| Sam Rivera | High | Dulce Base Command Center, Mainframe Room, Server Room, Underground Meeting Room | 8 | 72 |
| Taylor Cruz | High | Dulce Base Command Center, Mainframe Room, Underground Meeting Room, Briefing Room | 7 | 63 |

**Notes:**

- **Frequency:** This column is an approximation based on the narrative's emphasis on the interactions between characters. "Very High" indicates frequent, significant interactions throughout the story. "High" suggests numerous important interactions.
- **Places:** The order of places reflects the narrative's emphasis on the importance of each location within the context of their interactions. For instance, the Dulce Base Command Center is listed first because many major interactions occur there.
- **Strength of Bond:** This is a subjective assessment based on the descriptive language in the text and the strength scores from the knowledge graph. It reflects the level of trust, cooperation, and understanding between characters.
- **Total Interaction Weight:** This is a rough estimate, multiplying the "Frequency" (interpreted as a numerical value: Very High=10, High=8) by the "Strength of Bond". It attempts to quantify the overall significance of the interactions.

The knowledge graph is limited. A more comprehensive graph that includes scene frequency and interaction details would allow for a more precise and detailed response.

**Analysis:** Both responses provide tables, but the graph RAG system incorporates specific data from the knowledge graph (like bond strength scores) for a more nuanced response.

**4:** "Create a table of places that Alex visits: In the first column indicate the place name. In the 2nd column indicate the frequency he visits them. In the 3rd column list the people who were there with him by strength In the 4th column indicate the importance of the place. output the response in a table format using markdown language."

----- STANDARD RAG -------------------------

| **Place Name** | **Frequency** | **People Present (Bond Strength)** | **Importance** | **Location Description** | **Interaction Weight** |
|---|---|---|---|---|---|
| Briefing Room | 3 | Cruz (Antagonistic), Hayes (Understanding), Rivera (Respectful), | High (Mission planning, strategy)b | Sterile, large room with projectors; used for mission briefings. | 7 |
| Cramped Underground Room | 1 | Hayes, Cruz | High (Mission initiation, descent) | Small, dark room, leading to elevator to Dulce. | 3 |
| Elevator Shaft | 1 | Hayes, Cruz, Rivera | High (Journey to Dulce) | Metal shaft, descending into Dulce base. Dark and claustrophobic. | 3 |
| Dulce Base Corridors | 3 | Hayes (Strong), Cruz (Antagonistic), Rivera (Respectful) | High (Exploration, discoveries) | Long, dark corridors within Dulce base. Steel doors, eerie atmosphere. | 8 |
| Dulce Base Mainframe Room | 2 | Hayes (Strong), Cruz (Antagonistic), Rivera (Respectful) | High (Central hub, communication) | Large room containing mainframe and communications equipment. | 7 |
| Dulce Base Lab | 1 | Hayes (Strong) | Moderate (Alien tech analysis) | A laboratory within Dulce base; contains alien technology. | 2 |
| Dulce Base Server Room | 1 | Rivera (Mentor-Mentee), | Moderate (Data analysis) | Small room with numerous servers; used for data analysis. | 2 |
| Dulce Base Command Center | 6 | Hayes (Strong), Cruz (Antagonistic), Rivera (Respectful) | Highest (Alien communication, mission culmination) | Central hub of Dulce base, containing advanced communications equipment and consoles. | 15 |

**Note:** Bond strength is a subjective assessment based on the narrative. Interaction weight is an aggregate score reflecting the significance of interactions in each location across all chapters, with higher scores indicating greater importance and interaction. Frequency counts instances where Alex is explicitly present and actively participating.

----- GRAPH RAG -------------------------

Based on the provided text and knowledge graph, here's a table summarising the places Alex Mercer visits, along with associated details:

| **Place Name** | **Visit Frequency** | **People Present (by strength of bond)** | **Importance of Place** | **Location Description** | **Total Interaction Weight** |
|---|---|---|---|---|---|
| Dulce Base | Multiple | Jordan Hayes (9), Taylor Cruz (8), Sam Rivera (7) | Very High | Underground military base; mysterious, potentially dangerous. | 24 |
| Briefing Room | Multiple | Jordan Hayes, Taylor Cruz, Sam Rivera | High | Sterile room where missions are briefed. | 24 |
| Cramped Office | At least once | Sam Rivera | Medium | Small office where Sam works with servers; cramped workspace. | 7 |
| Deserted Corridor | At least once | Taylor Cruz | Low | A hallway inside Dulce Base. | 6 |
| Secluded Equipment Bay | At least once | Taylor Cruz, Jordan Hayes | Low | Equipment storage area inside Dulce Base. | 11 |
| Underground Meeting Room | At least once | Jordan Hayes, Taylor Cruz, Sam Rivera | Medium | Small underground room near elevator to Dulce Base. | 24 |
| Cramped Underground Meeting Room | At least once | Jordan Hayes, Taylor Cruz, Sam Rivera | Medium | Small underground room near elevator to Dulce Base. | 24 |
| Central Communications Hub | At least once | Jordan Hayes, Taylor Cruz, Sam Rivera | High | Main communications area within Dulce Base. | 24 |
| Central Hub | At least once | Jordan Hayes, Taylor Cruz, Sam Rivera | High | Main access point to deeper areas within Dulce Base. | 24 |
| Mainframe Room | At least once | Jordan Hayes, Taylor Cruz, Sam Rivera | High | Dulce Base's mainframe room; contains important computers and servers. | 24 |
| Lab | At least once | Jordan Hayes, Taylor Cruz | High | Area within Dulce Base where alien technology is studied. | 15 |
| Server Room | At least once | Sam Rivera, Alex Mercer | Medium | Room containing multiple servers. | 7 |
| Washington D.C. | Multiple | Multiple (unspecified) | High | Government headquarters; source of orders and information. | Unknown |

**Note:** The "Total Interaction Weight" is a rough estimate based on the strength of relationships mentioned in the knowledge graph and the frequency of interactions described in the text. The Washington D.C. entry has an unknown weight because the specific people Alex interacted with there aren't explicitly stated. The frequency of visits to some locations is inferred from the narrative.

**Analysis:** Both responses provide a table, but the graph RAG output incorporates more information and shows a higher level of consistency and stronger analysis of relationships.

**5:** I delve into creative applications by exploring questions related to book cover design.

**Analysis:** Given the subjective nature of such tasks, it's recommended to personally experiment and evaluate the impact of incorporating graph databases. In my own assessment, I've observed that graph-enhanced RAG systems tend to yield more comprehensive and focused responses. To gain further insights, I urge you to engage with the provided code and explore your own creative inquiries.

## Analysing the “Thoughts” of DeepSeek

**General Observations:**

- **Graph RAG's Structured Approach:** Graph RAG consistently begins by consulting the knowledge graph. It identifies relevant entities, relationships, and their strengths, using this structured information to guide its subsequent analysis of the text. This approach is systematic and efficient, demonstrating a clear advantage in navigating and utilising the available knowledge.
- **Standard RAG's Sequential Analysis:** In contrast, standard RAG tends to process the text chunks in a more sequential manner. It carefully reads through each chunk, identifying key information and gradually building its understanding. While thorough, this approach can be less efficient, especially when dealing with complex queries or large amounts of text.
- **Knowledge Integration:** Graph RAG excels at integrating information from both the knowledge graph and the text, resulting in more comprehensive and nuanced responses. It seamlessly combines structured knowledge with textual evidence, creating a richer understanding of the context. Standard RAG sometimes struggles to fully integrate both sources, occasionally missing key connections or relying too heavily on one over the other.
- **Reasoning Abilities:** The "think" sections also reveal differences in reasoning abilities. Graph RAG demonstrates more advanced reasoning capabilities, including the ability to infer information, resolve ambiguities, and make connections between different pieces of information. It can deduce missing details, interpret relationships, and even anticipate potential issues in its analysis. Standard RAG tends to be more literal and less capable of drawing inferences, often sticking closely to the explicit information provided in the text.

**Specific Examples:**

- **Question 2 ("What places and people does Alex Mercer hold dearest?")**: This question highlights the advantage of graph RAG's structured approach. By immediately consulting the knowledge graph, it quickly identifies the relevant entities and relationships, leading to a more focused and accurate response. Standard RAG, relying solely on the text, misses key information about the strength of relationships and the significance of certain locations.
- **Question 3 ("Create a table of people that Alex communicates with...")**: In this question, graph RAG effectively utilises the knowledge graph to determine bond strength and guide its analysis of interaction frequency. It leverages the quantitative information in the graph to create a more objective and nuanced table. Standard RAG, lacking this structured information, resorts to subjective assessments and struggles with quantifying interactions accurately.
- **Question 4 ("Create a table of places that Alex visits...")**: This question demonstrates graph RAG's ability to leverage the knowledge graph to identify relevant locations and relationships, leading to a more comprehensive table. It correctly identifies Washington D.C. as a significant location based on its connection to Alex Mercer in the graph. Standard RAG, focusing only on the text, misses the importance of Washington D.C. due to its absence in the provided text chunks.
- **Question 6 ("Based on Alex Mercer's strongest relationships...")**: This creative question further illustrates graph RAG's advantage. By utilising the knowledge graph, it quickly identifies key relationships and locations, leading to a more focused and relevant scene selection for the book cover. Standard RAG, relying on a more general analysis of the text, takes a broader approach and may not pinpoint the most emotionally charged and relevant scene as effectively.

**Overall, the "think" sections provide compelling evidence that graph RAG consistently outperforms standard RAG in terms of efficiency, accuracy, and depth of analysis. The integration of a knowledge graph empowers graph RAG to access and utilise relevant information more effectively, leading to more comprehensive and insightful responses.**

### Benefits of Graph-Based RAG

- Enhanced Context: Knowledge graphs provide structured, semantically rich context.
- Improved Reasoning: Relationships between entities allow better reasoning and inference.
- Reduced Hallucination: Grounding responses in a knowledge graph reduces the generation of fabricated information.
- Flexibility: The system can query diverse data types and complex questions.

### Conclusion

The fusion of graph databases and Retrieval-Augmented Generation (RAG) unlocks a new level of sophistication in language model applications. By grounding responses in a structured knowledge graph, we empower these models to reason about relationships, infer missing information, and provide more accurate and contextually relevant answers. This approach not only enhances the factual grounding of generated text but also opens doors to more complex and nuanced queries.

Imagine a world where AI assistants can truly understand the intricate connections between concepts, effortlessly navigate through a web of knowledge, and provide insightful answers that go beyond simple information retrieval. This is the promise of GraphRAG. From enhancing customer support interactions to powering advanced research tools, the practical applications are vast and transformative.

As we've seen through the analysis of various sample questions, GraphRAG consistently outperforms standard RAG systems, demonstrating improved accuracy, reduced hallucination, and the ability to handle complex queries with ease. This technology has the potential to revolutionize how we interact with information and unlock new possibilities in fields like education, research, and customer service.

The journey of GraphRAG is just beginning, and its future is filled with exciting potential. As knowledge graphs become more comprehensive and language models grow even more powerful, we can expect even more impressive advancements in the years to come. This is an invitation to join the exploration, experiment with the possibilities, and contribute to the evolution of this groundbreaking technology.

### **Ready to Dive Deeper into GraphRAG?**

This post has just scratched the surface of what's possible with graph-enhanced RAG. Now it's your turn to explore and experiment! Here are some exciting next steps:

- **Get Hands-On:** The best way to understand GraphRAG is to try it yourself. Download the code from the accompanying notebook ([link here!](https://github.com/apireno/graph_rag)) and run the examples. See firsthand how the addition of a graph database impacts the quality and depth of the responses.
- **Experiment with Embeddings:** Explore different embedding models and query strategies to see how they affect the results. Try fine-tuning existing models or even training your own custom embeddings tailored to your specific data. [Here](https://github.com/apireno/generate_fasttext_model_from_recipe_data) is an example of training a FastText model on recipe data.
- **Build Your Own GraphRAG:** Ready for a bigger challenge? Construct your own GraphRAG database using your own corpus of data. This is a fantastic opportunity to delve deeper into knowledge graph construction and explore the versatility of graph databases.
- **Join the Community:** [Connect with other developers](https://discord.com/invite/surrealdb) and researchers who are passionate about GraphRAG. Share your experiences, ask questions, and collaborate on new ideas.
- Check out these resources to get started:
- [Gemini documentation](https://ai.google.dev/gemini-api/docs)
- [DeepSeek ollama documentation](https://ollama.com/library/deepseek-r1)
- [Together AI documentation](https://docs.together.ai/)
- [Get started with SurrealDB](/docs/surrealdb/introduction/start)
- [SurrealDB Security Best Practices](/docs/surrealdb/security/security-best-practices)
- Run the analysis yourself:
- [The Jupyter notebooks](https://github.com/apireno/graph_rag)
- [Pre-requisite embedding repo](https://github.com/apireno/surrealDB_embedding_model)

The world of graph-enhanced RAG is full of possibilities. Start exploring today and unlock the full potential of your RAG applications!
