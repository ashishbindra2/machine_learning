# task

## Hallucination

examples

```
whos is the person behind youtbube channel codebasic? give sort ans

it will ans the question but

if you ask No the actuak name of person is ashish " it wil immedialy aggre
```

If you dont know the truth you can mislead easly

If LLm model chat bot dont know the ans then they create wrong ans

Hallucination is big challenge
 in AI world

Why Hallucination happend

1. Predicting Patterns vs True understanding

- It just see your text and try to predict the next word It is just like parrot, they cant understand  
- for eg a sef never ever did a signle work in an restro. He just took degree from college and study a tone of books.If anybudy ask for recipy he will tell everyting
- "give me a recipy of wheatgrass kheer" it will literly give wheatgrass kheer recipy
- It is probabilty based model it just try to do prediction.
- It happen lack of traning data and fine tunning
- If we ask "Give me tobacco kheer " then it will give resonable response
- they have given some data like tobako then it should have me more appopreate reponse.
- LLM just predicting next word.
- Fine tuning is taking feedback from the users contniusly and imove contniously. For eg in starting chatgpy do alot of mistak but over the time it impove alot due to fine tuning.
- one of the reson is incomplete and amibcous prompt example first question about "what is abc" or what is age"
 i am not specify abc is company or age of gpt model or my age

## How to tackle hallucination?

- Representative datasets: Means all senarious permutation combination all types of data.Theses types of data is alot of big already all gpts have trained on billions of datasets but needs to train alot of data.
- Fine Tunning and validation: Like in chatgpt we are continously geting thumpsup down by clicking it we can give feedbacks. THere should be different ways to get feeds and incoprate that .
- Knowledge based system: LLM should train on local database for company itself. use my databse  where i have my frequently asked questions and only use this to ans the questionsdont use your generic knownlage.Beacuse if llm start use generic knownlage it will start making up.Only use this knowlage source which i am give dont use anything else

## RAG vs Fine Tuning

Suppose you making chatbot faq

question -> LLM -> ANS

### 1. Fine tuning

File tuning a Large language model (llm) is the process of retraing a pre-trained model(or a foundational model)for a specific task, dataset , tone or format.

#### Benefits of Fine Tuning

- Handles emotions/slang
- Answers with brand tone

#### pros

- Produces consistent style and response
- Faster at runtime(no external retrieval)
- Tailored for very specific task/domains

#### crons

- Expensive and time-cosuming to retrain
- Hard to update(requires retraing for new data)

### Two Types of Fine Tuning

1. Full Fine Tuning: all parameter of netro we have to change like 70b paramter need to change and retrain for cust dataset
2. Parameter Efficient Fine tuning(PEFT): Train some layers of model like transer lerning, we are changing some parametere only. THere are two popular technoque

- LoRA
- QLoRA  
It is effecient and cost is less

### RAG

#### pros

- Easy to update knowlege without retraing
- Can handle large and dynamic datasets
- Lower cost compared to fine-tuning

#### crons

- Slower at runtime (needs retrival step)
- Output depends on quality of retrieval
- May give inconsistent style/format

we can use RAG + Fine tuning for best resut also

## Gen AI vs AI Agent vs Agentic AI

- Generative AI:
Generative AI is a type of artificial intelligence that create new content such as text, image, or audio based on patterens learned from existing data.

- The heart of gen ai is LLM
- eg Chatgpt, claude, gemni
- Theses model train of billions of reords and data. based on pretraing data it will ans the prompt
- eg "Plan a 3-day trip to austrilia, I love nature and koalas"

The LLM / GenAI will not give ans of "What is the price of Emirates fight from New York to Delhi tomorrow"

But LLM with tool can ans the abouve prompt (LLM+Expedia(API))

- AI Agent

Prompt2 "Book me the cheapest Emirates fight from New York to Delhi tomorrow?"

So above task can complete by AI agent like below

1. Searches Flights
2. Decides the cheapest one
3. Book it

AI Agent is a program that takes input thinks and acts to complete a task using tools, memory and knowledge.

eg. Book me a flight for my 7days trip to delhi in  may the wheather should be sunny all days. flight budget < 1600 $ No layovers

## Agentic AI

is a system where one or more AI agents woeks automously, often over long task, making decisions, using tools and even other agents to reach a goal.

Agentic Ai often uses Generative AI as a core component.

Agentic AI framworks

- Agno
- Crew AI
- Langgraph
- Microsoft Autogen

## LLM (Large Learning MOdel)

A Language model is somewhat like a stochastic parrot.
It use nuronetrok to complete the sentance

supose we train moview related artical on wikipedia  to  now it will comple any movie stetance

LLM are train on huge volume of datasets

RLHF(Reinforcement Learning with Human Feedback)

## What is a neuron?

Binary classification

we are giving age and getting have a incurance or not
a logistic regression is algorith that used for classfication problem.
using leaner regression we can draw a best fit linebut if outlier are ther then best fit line wont show acurate result
