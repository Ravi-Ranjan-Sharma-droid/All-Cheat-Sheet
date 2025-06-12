# Prompts & Templates

Prompts are the instructions given to language models. LangChain provides tools for creating, managing, and optimizing prompts.

## Basic Prompt Templates

```python
from langchain.prompts import PromptTemplate

# Simple prompt template
template = "Tell me a {adjective} joke about {subject}."
prompt = PromptTemplate(
    input_variables=["adjective", "subject"],
    template=template,
)

# Format the prompt with specific values
formatted_prompt = prompt.format(adjective="funny", subject="chickens")
print(formatted_prompt)  # "Tell me a funny joke about chickens."

# Use with an LLM
from langchain.llms import OpenAI
llm = OpenAI(temperature=0.7)
response = llm(formatted_prompt)
```

## Chat Prompt Templates

```python
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

# Create message templates
system_template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# Combine the message templates into a chat prompt template
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# Format the chat prompt
formatted_messages = chat_prompt.format_messages(
    input_language="English",
    output_language="French",
    text="I love programming."
)

# Use with a chat model
chat = ChatOpenAI(temperature=0)
response = chat(formatted_messages)
print(response.content)  # "J'aime la programmation."
```

## Few-Shot Prompt Templates

```python
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

# Define examples
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]

# Define the format for each example
example_formatter_template = "Input: {input}\nOutput: {output}"
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template=example_formatter_template,
)

# Create the few-shot prompt template
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Give the antonym of every input\n\n",
    suffix="\nInput: {adjective}\nOutput:",
    input_variables=["adjective"],
    example_separator="\n\n",
)

# Format the prompt with a specific input
formatted_prompt = few_shot_prompt.format(adjective="light")
print(formatted_prompt)

# Use with an LLM
response = llm(formatted_prompt)
print(response)  # "dark"
```

## Dynamic Few-Shot with Example Selector

```python
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

# Create an example selector that selects examples based on semantic similarity
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    OpenAIEmbeddings(),
    Chroma,
    k=2  # Select 2 most similar examples
)

# Create the few-shot prompt template with the example selector
dynamic_few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="Give the antonym of every input\n\n",
    suffix="\nInput: {adjective}\nOutput:",
    input_variables=["adjective"],
    example_separator="\n\n",
)

# Format the prompt with a specific input
formatted_prompt = dynamic_few_shot_prompt.format(adjective="light")
print(formatted_prompt)

# Use with an LLM
response = llm(formatted_prompt)
print(response)  # "dark"
```

## Prompt Composition

```python
from langchain.prompts import PipelinePromptTemplate

# Define the full template string
full_template = """You are an expert on {topic}.

{questions}

Please provide detailed answers:"""

# Define the questions template
question_template = """Questions:
1. What is {topic}?
2. Why is {topic} important?
3. What are some examples of {topic}?"""

# Create the prompt templates
full_prompt = PromptTemplate.from_template(full_template)
question_prompt = PromptTemplate.from_template(question_template)

# Create the pipeline prompt template
pipeline_prompt = PipelinePromptTemplate(
    final_prompt=full_prompt,
    pipeline_prompts=[("questions", question_prompt)],
)

# Format the prompt with a specific topic
formatted_prompt = pipeline_prompt.format(topic="artificial intelligence")
print(formatted_prompt)

# Use with an LLM
response = llm(formatted_prompt)
```

## Prompt Optimization Techniques

### 1. Be Specific and Clear

```python
# Bad prompt
bad_prompt = PromptTemplate(template="Write about {topic}.")

# Good prompt
good_prompt = PromptTemplate(
    template="Write a detailed explanation of {topic} covering its history, key concepts, and practical applications. Include specific examples."
)
```

### 2. Use System Messages Effectively

```python
from langchain.schema import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="You are a senior data scientist with expertise in machine learning. Provide technical, accurate responses with code examples when appropriate."),
    HumanMessage(content="Explain how to handle imbalanced datasets")
]
```

### 3. Include Few-Shot Examples

```python
few_shot_prompt = """
Classify the sentiment of the text as positive, negative, or neutral.

Text: The food was amazing and the service was excellent.
Sentiment: Positive

Text: The room was dirty and the staff was rude.
Sentiment: Negative

Text: The movie was okay, nothing special.
Sentiment: Neutral

Text: {input_text}
Sentiment:
"""
```

## Next Steps

Continue to the [Memory & Context](../05_memory/README.md) section to learn how to maintain context across multiple interactions.