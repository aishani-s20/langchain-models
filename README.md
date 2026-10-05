# LangChain Models: Study Notes

This repository contains basic study notes and concepts regarding the different types of models used in LangChain.

## 1. Overview of Models

In LangChain, models are primarily divided into two main categories:

* **Language Models:** Used for generating and processing text.

* **Embedding Models:** Used for converting text into numerical representations.

## 2. Language Models

Language models are further broken down into two distinct types: **LLMs** and **Chat Models**.

### LLMs (Large Language Models)

* **Purpose:** General-purpose models used for raw text generation.

* **Input/Output:** They take a simple string (plain text) as input and return a string (plain text) as output.

* **Current Usage:** These are traditionally older models and are not used as much in modern applications.

### Chat Models

* **Purpose:** Specialized specifically for conversational tasks and optimized for multi-turn conversations.

* **Input/Output:** They take a sequence of messages as input and return chat messages as output.

* **Current Usage:** These are newer models compared to LLMs and are the standard for most modern applications.

## 3. Embedding Models

* **Purpose:** Embedding models are used to convert text into numbers (numerical data or vectors).

* **Why it matters:** This allows machines to understand the semantic meaning of the text, which is essential for tasks like document retrieval and similarity searches.

## 4. Open-Source vs. Closed-Source Models

Both Language and Embedding models can be either open-source or closed-source. Here is a breakdown of the differences:

| Feature | Open-Source Models | Closed-Source Models | 
| ----- | ----- | ----- | 
| **Cost** | Free to use (no API costs). | Paid API usage (e.g., OpenAI charges per token). | 
| **Control** | Can modify, fine-tune, and deploy anywhere. | Locked to the provider's infrastructure. | 
| **Data Privacy** | Runs locally (no data sent to external servers). | Sends queries to provider's external servers. | 
| **Customization** | Can fine-tune on specific datasets. | No access to fine-tuning in most cases. | 
| **Deployment** | Can be deployed on on-premise servers or in the cloud. | Must use the vendor's API. | 

### Using Open-Source Models

When working with Open-Source models, you generally have two options:

1. **Using API:** A convenient way to access models, often providing a free tier for developers.

2. **Running Locally:** Downloading the model and running it directly on your own hardware for maximum privacy and control.