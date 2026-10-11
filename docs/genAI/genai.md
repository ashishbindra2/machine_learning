# GEN

## What is generative AI?

Generative AI, sometimes called gen AI, is artificial intelligence (AI) that can create original content such as text, images, video, audio or software code in response to a user’s prompt or request.

It can learn human language, programming languages, art, chemistry, biology, or any complex subject matter

For example, it can learn English vocabulary and create a poem from the words it processes.

our organization can use generative AI for various purposes, like chatbots, media creation, product development, and design.

## How generative AI works

For the most part, generative AI operates in three phases:

1. Training
2. Tuning
3. Generation, evaluation and retuning

---

## 1. Training

The most common foundation models today are large language models (LLMs), created for text generation applications,

For training generative AI (GenAI), you can use several types of models and architectures,

- primarily

    Transformer-based models, Diffusion models, and Generative Adversarial Networks (GANs).

- Other models like

    Variational Autoencoders (VAEs) and autoregressive models

During training, the algorithm performs and evaluates millions of ‘fill in the blank’ exercises, trying to predict the next element in a sequence e.g., the next word in a sentence, the next element in an image, the next command in a line of code and continually adjusting itself to minimize the difference between its predictions and the actual data

The result of this training is a neural network of parameters, encoded representations of the entities, patterns and relationships in the data, that can generate content autonomously in response to inputs, or prompts.

### Choosing a Model

The best model type depends on the specific task:

- For `text and code generation`, Transformer-based models are the current state-of-the-art.

- For `high-quality images and video`, Diffusion models and GANs are often preferred.

- For `synthetic data` generation in specialized fields like medical imaging or finance, GANs and VAEs are common choices.

This training process is compute-intensive, time-consuming and expensive: it requires thousands of clustered (GPUs) and weeks of processing, all of which costs millions of dollars. Open-source foundation model projects, such as Meta's Llama-2, enable gen AI developers to avoid this step and its costs.

How reduce the cost

significantly reduces the cost and burden associated with it by providing powerful, pre-trained base models that can be fine-tuned with much smaller, high-quality, task-specific datasets. This bypasses the enormous cost of training a model from scratch on trillions of tokens of data.

### Synthetic data

Synthetic data is artificial data that mimics real-world data, created using algorithms and machine learning techniques like deep learning or GANs. It is used for training AI models, testing software, and research, especially when real data is scarce, sensitive, or difficult to access due to privacy concerns.

## 2.Tuning

- often can’t generate specific types of output with desired accuracy.

- the model must be tuned to a specific content generation task. This can be done in a variety of ways.

1. Fine tuning

2. Reinforcement learning with human feedback (RLHF)

### 1. Fine tuning

Fine tuning involves feeding the model labeled data specific to the content generation application questions or prompts the application is likely to receive, and corresponding correct answers in the desired format.

development team is trying to create a customer service chatbot, it would create hundreds or thousands of documents containing labeled customers service questions and correct answers, and then feed those documents to the model.

Fine-tuning is labor-intensive. Developers often outsource the task to companies with large data-labeling workforces.

### 2. Reinforcement learning with human feedback (RLHF)

- In RLHF, human users respond to generated content with evaluations the model can use to update the model for greater accuracy or relevance

- RLHF involves people ‘scoring’ different outputs in response to the same prompt.

- it can be as simple as having people type or talk back to a chatbot or virtual assistant, correcting its output.

## 3. Generation, evaluation, more tuning

Developers and users continually assess the outputs of their generative AI apps, and further tune the model even as often as once a week for greater accuracy or relevance

the foundation model itself is updated much less frequently, perhaps every year or 18 months

Another option for improving a gen AI app's performance is retrieval augmented generation (RAG).
