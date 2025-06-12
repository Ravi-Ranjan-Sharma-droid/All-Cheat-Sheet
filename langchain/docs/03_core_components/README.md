# Core Components

LangChain is built around several core components that work together to create powerful LLM applications.

## 1. LLMs and Chat Models

LLMs (Large Language Models) are the foundation of LangChain applications. LangChain provides a unified interface for working with different LLM providers.

```python
# Using OpenAI's GPT models
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# Text completion model
llm = OpenAI(temperature=0.7)
response = llm("Write a poem about AI")

# Chat completion model
chat_model = ChatOpenAI()
from langchain.schema import HumanMessage, SystemMessage
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello, how are you doing?")
]
response = chat_model(messages)
```

## 2. Chains

Chains are the core abstraction for combining multiple components.

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

# Create a chain that combines the prompt and LLM
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
result = chain.run(product="eco-friendly water bottles")
print(result)
```

### Sequential Chains

```python
from langchain.chains import SimpleSequentialChain

# First chain: Generate a company name
first_prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
first_chain = LLMChain(llm=llm, prompt=first_prompt)

# Second chain: Generate a slogan based on the company name
second_prompt = PromptTemplate(
    input_variables=["company_name"],
    template="Write a catchy slogan for {company_name}.",
)
second_chain = LLMChain(llm=llm, prompt=second_prompt)

# Combine the chains
overall_chain = SimpleSequentialChain(
    chains=[first_chain, second_chain],
    verbose=True
)

# Run the chain
result = overall_chain.run("eco-friendly water bottles")
```

### Router Chains

```python
from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain
from langchain.prompts import PromptTemplate

# Define different prompt templates for different topics
prompt_infos = [
    {
        "name": "physics", 
        "description": "Good for answering questions about physics", 
        "prompt_template": "You are a physics expert. Answer: {input}"
    },
    {
        "name": "math", 
        "description": "Good for answering math questions", 
        "prompt_template": "You are a math expert. Answer: {input}"
    }
]

# Create a default chain for topics that don't match any category
default_chain = LLMChain(llm=llm, prompt=PromptTemplate(template="{input}", input_variables=["input"]))

# Create a router chain that routes to the appropriate prompt based on the input
router_chain = MultiPromptChain.from_prompts(
    llm, 
    prompt_infos, 
    default_chain=default_chain,
    verbose=True
)

# Run the chain with different inputs
physics_result = router_chain.run("Explain the theory of relativity")
math_result = router_chain.run("Solve for x: 2x + 5 = 13")
```

## 3. Agents and Tools

Agents can use tools to interact with the external world.

```python
from langchain.agents import load_tools, initialize_agent, AgentType

# Load tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Initialize agent
agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent
agent.run("What was the high temperature in SF yesterday? What is that number raised to the .023 power?")
```

### Custom Tools

```python
from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field

# Define the input schema for the tool
class CalculatorInput(BaseModel):
    expression: str = Field()

# Create a custom tool
class Calculator(BaseTool):
    name = "calculator"
    description = "useful for when you need to calculate math expressions"
    args_schema: Type[BaseModel] = CalculatorInput

    def _run(self, expression: str) -> str:
        return str(eval(expression))

    def _arun(self, expression: str) -> str:
        return str(eval(expression))

# Use the custom tool with an agent
tools = [Calculator()]
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
result = agent.run("What is 12 * 34 + 7?")
```

## 4. Memory

Memory components allow chains and agents to retain information across multiple interactions.

```python
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Create a conversation chain with memory
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory(),
    verbose=True
)

# First interaction
response1 = conversation.predict(input="Hi, my name is Bob")

# Second interaction (the model remembers the name)
response2 = conversation.predict(input="What's my name?")
```

## 5. Embeddings and Vector Stores

Embeddings and vector stores are used for semantic search and retrieval.

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create a vector store
texts = ["LangChain is a framework for working with LLMs", "Embeddings are vector representations of text"]
vectorstore = Chroma.from_texts(texts, embeddings)

# Search for similar documents
results = vectorstore.similarity_search("What is LangChain?")
```

## Next Steps

Continue to the [Prompts & Templates](../04_prompts/README.md) section to learn how to create effective prompts for LLMs.