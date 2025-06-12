# Complete LangChain Guide: Beginner to Advanced

## Table of Contents
1. [Overview & Philosophy](#overview--philosophy)
2. [Installation & Setup](#installation--setup)
3. [Core Components](#core-components)
4. [Prompts & Templates](#prompts--templates)
5. [Memory & Context](#memory--context)
6. [Document Loaders](#document-loaders)
7. [Embeddings & Vector Stores](#embeddings--vector-stores)
8. [Retrieval-Augmented Generation (RAG)](#retrieval-augmented-generation-rag)
9. [LLM Integration](#llm-integration)
10. [Evaluation](#evaluation)
11. [Deployment](#deployment)
12. [Best Practices](#best-practices)
13. [Full Example: Local Chatbot with Ollama](#full-example-local-chatbot-with-ollama)
14. [LangChain Cheatsheet](#langchain-cheatsheet)
15. [LangChain vs LlamaIndex](#langchain-vs-llamaindex)

---

## Overview & Philosophy

### What is LangChain?

LangChain is a framework designed to simplify the creation of applications using large language models (LLMs). It provides a unified interface for working with different LLMs, tools for building complex chains of operations, and utilities for common LLM application patterns.

### Core Philosophy

**1. Modularity**: Components are designed to be modular and composable
**2. Standardization**: Unified interfaces across different providers
**3. Production-Ready**: Built with real-world deployment in mind
**4. Extensibility**: Easy to add custom components and integrations

### Key Benefits

- **Provider Agnostic**: Switch between OpenAI, Anthropic, local models, etc.
- **Rich Ecosystem**: Pre-built tools, loaders, and integrations
- **Memory Management**: Built-in conversation and context handling
- **RAG Support**: Native support for retrieval-augmented generation
- **Production Features**: Monitoring, evaluation, and deployment tools

### Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Application   │────│   LangChain     │────│   LLM Provider  │
│   Layer         │    │   Framework     │    │   (OpenAI, etc) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌─────────────────┐              │
         │              │   Vector Store  │              │
         │              │   (Pinecone,    │              │
         │              │   ChromaDB)     │              │
         │              └─────────────────┘              │
         │                       │                       │
    ┌─────────────────────────────────────────────────────────────┐
    │                     Tools & Utilities                      │
    │  • Document Loaders  • Memory Systems  • Evaluation       │
    │  • Embeddings       • Prompt Templates • Monitoring       │
    └─────────────────────────────────────────────────────────────┘
```

---

## Installation & Setup

### Python Installation

```bash
# Basic installation
pip install langchain

# With specific integrations
pip install langchain[openai]
pip install langchain[anthropic]
pip install langchain[llms] # For local models

# Community packages
pip install langchain-community
pip install langchain-experimental

# For vector stores
pip install chromadb
pip install pinecone-client
pip install faiss-cpu

# For document processing
pip install pypdf
pip install docx2txt
pip install beautifulsoup4

# Complete development setup
pip install langchain langchain-community langchain-experimental \
    openai anthropic chromadb pypdf python-dotenv streamlit
```

### JavaScript/TypeScript Installation

```bash
# Core LangChain
npm install langchain

# Specific integrations
npm install @langchain/openai
npm install @langchain/anthropic
npm install @langchain/community

# Vector stores
npm install chromadb
npm install @pinecone-database/pinecone

# Document loaders
npm install pdf-parse
npm install cheerio
```

### Environment Setup

Create a `.env` file:

```bash
# API Keys
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
PINECONE_API_KEY=your_pinecone_key_here

# Local model settings
OLLAMA_BASE_URL=http://localhost:11434

# Vector store settings
CHROMA_PERSIST_DIRECTORY=./chroma_db
```

Python setup:

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Verify environment
print("OpenAI Key:", "✓" if os.getenv("OPENAI_API_KEY") else "✗")
print("Anthropic Key:", "✓" if os.getenv("ANTHROPIC_API_KEY") else "✗")
```

---

## Core Components

### 1. LLMs and Chat Models

#### Basic LLM Usage

```python
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Standard LLM
llm = OpenAI(temperature=0.7, max_tokens=500)
response = llm("What is the capital of France?")
print(response)

# Chat Model (Recommended)
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?")
]
response = chat(messages)
print(response.content)
```

#### Streaming Responses

```python
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

chat = ChatOpenAI(
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=0.7
)

response = chat([HumanMessage(content="Tell me a long story about AI.")])
```

### 2. Chains

Chains are the core abstraction for combining multiple components.

#### Simple Chain

```python
from langchain import LLMChain
from langchain.prompts import PromptTemplate

# Create a prompt template
template = """
You are a {role} helping with {task}.
Question: {question}
Answer:"""

prompt = PromptTemplate(
    input_variables=["role", "question", "task"],
    template=template
)

# Create chain
chain = LLMChain(llm=llm, prompt=prompt)

# Execute
result = chain.run({
    "role": "data scientist",
    "task": "data analysis",
    "question": "How do I clean messy data?"
})
```

#### Sequential Chains

```python
from langchain.chains import SimpleSequentialChain

# First chain: Generate story outline
outline_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Create a story outline about {topic}:"
)
outline_chain = LLMChain(llm=llm, prompt=outline_prompt)

# Second chain: Write full story
story_prompt = PromptTemplate(
    input_variables=["outline"],
    template="Write a full story based on this outline:\n{outline}\n\nStory:"
)
story_chain = LLMChain(llm=llm, prompt=story_prompt)

# Combine chains
full_chain = SimpleSequentialChain(
    chains=[outline_chain, story_chain],
    verbose=True
)

story = full_chain.run("artificial intelligence")
```

#### Router Chains

```python
from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.prompts import PromptTemplate

# Define specialized prompts
physics_template = """You are a physics professor. Answer this question: {input}"""
math_template = """You are a math professor. Answer this question: {input}"""
history_template = """You are a history professor. Answer this question: {input}"""

# Create prompt infos
prompt_infos = [
    {
        "name": "physics",
        "description": "Good for physics questions",
        "prompt_template": physics_template
    },
    {
        "name": "math", 
        "description": "Good for math questions",
        "prompt_template": math_template
    },
    {
        "name": "history",
        "description": "Good for history questions", 
        "prompt_template": history_template
    }
]

# Router chain
destination_chains = {}
for p_info in prompt_infos:
    name = p_info["name"]
    prompt_template = p_info["prompt_template"]
    prompt = PromptTemplate(template=prompt_template, input_variables=["input"])
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain

# Create router
router_template = """Given a raw text input to a language model, select the model prompt best suited for the input.

<< FORMATTING >>
Return a markdown code snippet with a JSON object formatted like this:
```json
{{
    "destination": string \ name of the prompt to use or "DEFAULT"
    "next_inputs": string \ a potentially modified version of the original input
}}
```

<< CANDIDATE PROMPTS >>
{destinations}

<< INPUT >>
{{input}}

<< OUTPUT >>
"""

router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    partial_variables={"destinations": "\n".join([f"{p['name']}: {p['description']}" for p in prompt_infos])}
)

router_chain = LLMRouterChain.from_llm(llm, router_prompt)

# Create multi-prompt chain
chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=LLMChain(llm=llm, prompt=PromptTemplate(template="{input}", input_variables=["input"])),
    verbose=True
)

# Test it
result = chain.run("What is Newton's second law?")
```

### 3. Agents and Tools

Agents can use tools to interact with the external world.

#### Basic Agent Setup

```python
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.tools import BaseTool
import requests

# Custom tool
def get_weather(city: str) -> str:
    """Get current weather for a city"""
    # Mock weather API call
    return f"The weather in {city} is sunny, 75°F"

def calculate(expression: str) -> str:
    """Calculate mathematical expressions"""
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

# Define tools
tools = [
    Tool(
        name="Weather",
        func=get_weather,
        description="Get weather information for a city"
    ),
    Tool(
        name="Calculator",
        func=calculate,
        description="Calculate mathematical expressions"
    )
]

# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Use agent
result = agent.run("What's the weather in New York and what's 25 * 4?")
```

#### Custom Tool Class

```python
from typing import Optional, Type
from pydantic import BaseModel, Field

class WeatherInput(BaseModel):
    city: str = Field(description="City name to get weather for")

class WeatherTool(BaseTool):
    name = "get_weather"
    description = "Useful for getting weather information for a specific city"
    args_schema: Type[BaseModel] = WeatherInput
    
    def _run(self, city: str) -> str:
        """Get weather for city"""
        # Your weather API logic here
        return f"Weather in {city}: Sunny, 72°F"
    
    async def _arun(self, city: str) -> str:
        """Async version"""
        return self._run(city)

# Use custom tool
weather_tool = WeatherTool()
tools = [weather_tool]

agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
```

---

## Prompts & Templates

### Basic Prompt Templates

```python
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate

# Simple template
simple_template = PromptTemplate(
    input_variables=["product"],
    template="Write a marketing slogan for {product}."
)

prompt = simple_template.format(product="eco-friendly water bottle")
print(prompt)

# Chat template
chat_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "You are a helpful assistant that {task}."
    ),
    HumanMessagePromptTemplate.from_template("{question}")
])

formatted = chat_template.format_messages(
    task="explains complex topics simply",
    question="What is quantum computing?"
)
```

### Few-Shot Prompts

```python
from langchain.prompts import FewShotPromptTemplate

# Examples for few-shot learning
examples = [
    {
        "question": "Who lived longer, Muhammad Ali or Alan Turing?",
        "answer": """
Are follow-up questions needed here: Yes.
Follow-up: How old was Muhammad Ali when he died?
Intermediate answer: Muhammad Ali was 74 years old when he died.
Follow-up: How old was Alan Turing when he died?
Intermediate answer: Alan Turing was 41 years old when he died.
So the final answer is: Muhammad Ali
"""
    },
    {
        "question": "When was the founder of craigslist born?",
        "answer": """
Are follow-up questions needed here: Yes.
Follow-up: Who was the founder of craigslist?
Intermediate answer: Craigslist was founded by Craig Newmark.
Follow-up: When was Craig Newmark born?
Intermediate answer: Craig Newmark was born on December 6, 1952.
So the final answer is: December 6, 1952
"""
    }
]

example_template = """
Question: {question}
{answer}
"""

example_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template=example_template
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)

# Use the prompt
question = "Who was older when they died, Aristotle or Plato?"
formatted = few_shot_prompt.format(input=question)
```

### Dynamic Few-Shot with Example Selector

```python
from langchain.prompts.example_selector import LengthBasedExampleSelector

# Create example selector
example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=1000,
    get_text_length=len
)

dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)
```

### Prompt Composition

```python
from langchain.prompts.pipeline import PipelinePromptTemplate

# Component prompts
introduction = PromptTemplate(
    input_variables=["context"],
    template="Given the context: {context}"
)

task = PromptTemplate(
    input_variables=["task"],
    template="Complete this task: {task}"
)

conclusion = PromptTemplate(
    input_variables=[],
    template="Provide a detailed answer."
)

# Combine prompts
full_template = """
{introduction}

{task}

{conclusion}
"""

pipeline_prompt = PipelinePromptTemplate(
    final_prompt=PromptTemplate(
        template=full_template,
        input_variables=["introduction", "task", "conclusion"]
    ),
    pipeline_prompts=[
        ("introduction", introduction),
        ("task", task),
        ("conclusion", conclusion)
    ]
)
```

---

## Memory & Context

### Conversation Buffer Memory

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Basic conversation memory
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=chat,
    memory=memory,
    verbose=True
)

# Have a conversation
response1 = conversation.predict(input="Hi, my name is Alice")
print(response1)

response2 = conversation.predict(input="What's my name?")
print(response2)

# Check memory
print(memory.buffer)
```

### Conversation Buffer Window Memory

```python
from langchain.memory import ConversationBufferWindowMemory

# Keep only last k interactions
window_memory = ConversationBufferWindowMemory(k=2)

conversation = ConversationChain(
    llm=chat,
    memory=window_memory,
    verbose=True
)

# This will only remember the last 2 exchanges
for i in range(5):
    response = conversation.predict(input=f"Message {i}: Tell me about topic {i}")
    print(f"Response {i}: {response}\n")
```

### Conversation Summary Memory

```python
from langchain.memory import ConversationSummaryMemory

# Automatically summarize conversation
summary_memory = ConversationSummaryMemory(llm=chat)

conversation = ConversationChain(
    llm=chat,
    memory=summary_memory,
    verbose=True
)

# Long conversation that gets summarized
conversation.predict(input="Tell me about the history of artificial intelligence")
conversation.predict(input="What were the key breakthroughs?")
conversation.predict(input="Who were the important researchers?")

# Check the summary
print("Summary:", summary_memory.buffer)
```

### Vector Store Memory

```python
from langchain.memory import VectorStoreRetrieverMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.docstore import InMemoryDocstore
import faiss

# Setup vector store for memory
embeddings = OpenAIEmbeddings()
embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore = Chroma(
    embedding_function=embeddings,
    persist_directory="./memory_db"
)

# Vector store memory
retriever = vectorstore.as_retriever(search_kwargs=dict(k=3))
vector_memory = VectorStoreRetrieverMemory(retriever=retriever)

# Add memories
vector_memory.save_context(
    {"input": "My favorite food is sushi"}, 
    {"output": "That's great! Sushi is delicious and healthy."}
)
vector_memory.save_context(
    {"input": "I work as a software engineer"}, 
    {"output": "Software engineering is a great field with lots of opportunities."}
)

# Retrieve relevant memories
relevant_docs = vector_memory.load_memory_variables({"prompt": "What do I like to eat?"})
print(relevant_docs)
```

### Custom Memory Class

```python
from langchain.memory.chat_message_histories import BaseChatMessageHistory
from langchain.schema import BaseMessage, HumanMessage, AIMessage
from typing import List
import json

class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._messages = self._load_messages()
    
    def _load_messages(self) -> List[BaseMessage]:
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                messages = []
                for msg in data:
                    if msg['type'] == 'human':
                        messages.append(HumanMessage(content=msg['content']))
                    else:
                        messages.append(AIMessage(content=msg['content']))
                return messages
        except FileNotFoundError:
            return []
    
    def _save_messages(self):
        data = []
        for msg in self._messages:
            data.append({
                'type': 'human' if isinstance(msg, HumanMessage) else 'ai',
                'content': msg.content
            })
        with open(self.file_path, 'w') as f:
            json.dump(data, f)
    
    @property
    def messages(self) -> List[BaseMessage]:
        return self._messages
    
    def add_message(self, message: BaseMessage) -> None:
        self._messages.append(message)
        self._save_messages()
    
    def clear(self) -> None:
        self._messages = []
        self._save_messages()

# Use custom memory
from langchain.memory import ConversationBufferMemory

file_memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("conversation_history.json"),
    return_messages=True
)
```

---

## Document Loaders

### Text and PDF Loaders

```python
from langchain.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Text file loader
text_loader = TextLoader("document.txt")
documents = text_loader.load()

# PDF loader
pdf_loader = PyPDFLoader("document.pdf")
pdf_documents = pdf_loader.load()

# Directory loader
dir_loader = DirectoryLoader(
    "docs/", 
    glob="**/*.txt",
    loader_cls=TextLoader
)
all_documents = dir_loader.load()

# Split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)

split_docs = text_splitter.split_documents(documents)
print(f"Split into {len(split_docs)} chunks")
```

### Web Loaders

```python
from langchain.document_loaders import WebBaseLoader, SitemapLoader
import requests
from bs4 import BeautifulSoup

# Single web page
web_loader = WebBaseLoader("https://example.com/article")
web_docs = web_loader.load()

# Multiple URLs
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]
multi_web_loader = WebBaseLoader(urls)
multi_docs = multi_web_loader.load()

# Sitemap loader
sitemap_loader = SitemapLoader("https://example.com/sitemap.xml")
sitemap_docs = sitemap_loader.load()

# Custom web scraping
class CustomWebLoader:
    def __init__(self, url: str):
        self.url = url
    
    def load(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Custom extraction logic
        title = soup.find('title').text if soup.find('title') else ""
        content = soup.get_text()
        
        from langchain.schema import Document
        return [Document(
            page_content=content,
            metadata={"url": self.url, "title": title}
        )]
```

### Database and API Loaders

```python
from langchain.document_loaders import SQLDatabaseLoader
from sqlalchemy import create_engine

# SQL Database loader
db_engine = create_engine("sqlite:///example.db")
sql_loader = SQLDatabaseLoader(
    query="SELECT * FROM articles WHERE published = 1",
    db=db_engine
)
db_docs = sql_loader.load()

# Custom API loader
import requests
from typing import List

class APIDocumentLoader:
    def __init__(self, api_url: str, headers: dict = None):
        self.api_url = api_url
        self.headers = headers or {}
    
    def load(self) -> List[Document]:
        response = requests.get(self.api_url, headers=self.headers)
        data = response.json()
        
        documents = []
        for item in data:
            doc = Document(
                page_content=item.get('content', ''),
                metadata={
                    'id': item.get('id'),
                    'title': item.get('title'),
                    'created_at': item.get('created_at')
                }
            )
            documents.append(doc)
        
        return documents

# Use API loader
api_loader = APIDocumentLoader("https://api.example.com/articles")
api_docs = api_loader.load()
```

### Advanced Text Splitting

```python
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    TokenTextSplitter,
    SpacyTextSplitter
)

# Character-based splitting
char_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)

# Recursive splitting (recommended)
recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)

# Token-based splitting
token_splitter = TokenTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# Language-specific splitting
# pip install spacy
# python -m spacy download en_core_web_sm
spacy_splitter = SpacyTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# Custom splitter
class SentenceTextSplitter:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
    
    def split_text(self, text: str) -> List[str]:
        import re
        sentences = re.split(r'[.!?]+', text)
        
        chunks = []
        current_chunk = ""
        
        for sentence in sentences:
            if len(current_chunk + sentence) > self.chunk_size:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                    # Handle overlap
                    words = current_chunk.split()
                    overlap_words = words[-self.chunk_overlap//10:] if len(words) > self.chunk_overlap//10 else words
                    current_chunk = " ".join(overlap_words) + " " + sentence
                else:
                    current_chunk = sentence
            else:
                current_chunk += " " + sentence
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks
```

---

## Embeddings & Vector Stores

### Embeddings

```python
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain.embeddings.base import Embeddings
import numpy as np

# OpenAI embeddings
openai_embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Embed single text
text = "This is a sample document for embedding."
embedding = openai_embeddings.embed_query(text)
print(f"Embedding dimension: {len(embedding)}")

# Embed multiple documents
texts = [
    "First document about AI",
    "Second document about machine learning",
    "Third document about deep learning"
]
doc_embeddings = openai_embeddings.embed_documents(texts)

# Local embeddings with HuggingFace
local_embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

local_embedding = local_embeddings.embed_query(text)
print(f"Local embedding dimension: {len(local_embedding)}")

# Custom embedding class
class CustomEmbeddings(Embeddings):
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed search docs."""
        # Your custom embedding logic here
        # This is a dummy implementation
        return [[0.1] * 768 for _ in texts]
    
    def embed_query(self, text: str) -> List[float]:
        """Embed query text."""
        # Your custom embedding logic here
        return [0.1] * 768

custom_embeddings = CustomEmbeddings()
```

### Vector Stores

#### ChromaDB

```python
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

# Initialize ChromaDB
embeddings = OpenAIEmbeddings()
vectorstore = Chroma(
    collection_name="my_documents",
    embedding_function=embeddings,
    persist_directory="./chroma_db"  # Persist to disk
)

# Add documents
texts = [
    "LangChain is a framework for developing applications powered by language models.",
    "Vector databases store high-dimensional vectors and enable similarity search.",
    "Retrieval-Augmented Generation combines retrieval and generation for better responses."
]

metadatas = [
    {"source": "langchain_docs", "topic": "framework"},
    {"source": "vector_db_guide", "topic": "storage"},
    {"source": "rag_paper", "topic": "architecture"}
]

vectorstore.add_texts(texts, metadatas=metadatas)

# Similarity search
query = "What is LangChain?"
similar_docs = vectorstore.similarity_search(query, k=3)

for doc in similar_docs:
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}\n")

# Similarity search with scores
docs_with_scores = vectorstore.similarity_search_with_score(query, k=3)
for doc, score in docs_with_scores:
    print(f"Score: {score:.4f}")
    print(f"Content: {doc.page_content}\n")
```

#### Pinecone

```python
import pinecone
from langchain.vectorstores import Pinecone

# Initialize Pinecone
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment="us-west1-gcp"  # Your environment
)

# Create or connect to index
index_name = "langchain-demo"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        name=index_name,
        dimension=1536,  # OpenAI embedding dimension
        metric="cosine"
    )

# Create vector store
vectorstore = Pinecone.from_texts(
    texts,
    embeddings,
    index_name=index_name,
    metadatas=metadatas
)

# Search
results = vectorstore.similarity_search(query, k=3)
```

#### FAISS

```python
from langchain.vectorstores import FAISS
import pickle

# Create FAISS vector store
vectorstore = FAISS.from_texts(
    texts,
    embeddings,
    metadatas=metadatas
)

# Save to disk
vectorstore.save_local("faiss_index")

# Load from disk
loaded_vectorstore = FAISS.load_local("faiss_index", embeddings)

# Search
results = loaded_vectorstore.similarity_search(query, k=3)
```

#### Custom Vector Store

```python
from langchain.vectorstores.base import VectorStore
from typing import Any, List, Optional, Tuple
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SimpleVectorStore(VectorStore):
    def __init__(self, embedding_function):
        self.embedding_function = embedding_function
        self.texts = []
        self.embeddings = []
        self.metadatas = []
    
    def add_texts(
        self,
        texts: List[str],
        metadatas: Optional[List[dict]] = None,
        **kwargs: Any,
    ) -> List[str]:
        """Add texts to the vector store."""
        embeddings = self.embedding_function.embed_documents(texts)
        
        self.texts.extend(texts)
        self.embeddings.extend(embeddings)
        self.metadatas.extend(metadatas or [{}] * len(texts))
        
        return [str(i) for i in range(len(texts))]
    
    def similarity_search(
        self, query: str, k: int = 4, **kwargs: Any
    ) -> List[Document]:
        """Return docs most similar to query."""
        query_embedding = self.embedding_function.embed_query(query)
        
        # Calculate similarities
        similarities = cosine_similarity(
            [query_embedding], 
            self.embeddings
        )[0]
        
        # Get top k indices
        top_indices = np.argsort(similarities)[::-1][:k]
        
        # Return documents
        results = []
        for idx in top_indices:
            doc = Document(
                page_content=self.texts[idx],
                metadata=self.metadatas[idx]
            )
            results.append(doc)
        
        return results
    
    @classmethod
    def from_texts(
        cls,
        texts: List[str],
        embedding: Embeddings,
        metadatas: Optional[List[dict]] = None,
        **kwargs: Any,
    ):
        """Create vector store from texts."""
        store = cls(embedding)
        store.add_texts(texts, metadatas)
        return store

# Use custom vector store
custom_store = SimpleVectorStore.from_texts(
    texts, embeddings, metadatas
)
results = custom_store.similarity_search(query, k=2)
```

---

## Retrieval-Augmented Generation (RAG)

### Basic RAG Implementation

```python
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Create retriever from vector store
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Custom prompt for RAG
template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Answer:"""

prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)

# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt},
    return_source_documents=True,
    verbose=True
)

# Ask questions
result = qa_chain("What is LangChain and how does it work?")
print("Answer:", result["result"])
print("\nSources:")
for doc in result["source_documents"]:
    print(f"- {doc.page_content[:100]}...")
```

### Advanced RAG with Multiple Chain Types

```python
from langchain.chains.question_answering import load_qa_chain

# Map-Reduce chain for long documents
map_reduce_chain = load_qa_chain(
    llm=chat,
    chain_type="map_reduce",
    verbose=True
)

# Refine chain for iterative improvement
refine_chain = load_qa_chain(
    llm=chat,
    chain_type="refine",
    verbose=True
)

# Map-Rerank chain for scoring answers
map_rerank_chain = load_qa_chain(
    llm=chat,
    chain_type="map_rerank",
    verbose=True
)

# Use with retriever
def advanced_rag(question: str, chain_type: str = "stuff"):
    docs = retriever.get_relevant_documents(question)
    
    if chain_type == "map_reduce":
        result = map_reduce_chain({"input_documents": docs, "question": question})
    elif chain_type == "refine":
        result = refine_chain({"input_documents": docs, "question": question})
    elif chain_type == "map_rerank":
        result = map_rerank_chain({"input_documents": docs, "question": question})
    else:
        result = qa_chain(question)
    
    return result

# Test different chain types
question = "How do vector databases work in machine learning applications?"
result = advanced_rag(question, "map_reduce")
```

### Conversational RAG

```python
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Setup memory for conversation
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key="answer"
)

# Conversational RAG chain
conv_qa_chain = ConversationalRetrievalChain.from_llm(
    llm=chat,
    retriever=retriever,
    memory=memory,
    return_source_documents=True,
    verbose=True
)

# Have a conversation
response1 = conv_qa_chain({"question": "What is vector similarity search?"})
print("Response 1:", response1["answer"])

response2 = conv_qa_chain({"question": "How is it different from traditional search?"})
print("Response 2:", response2["answer"])

response3 = conv_qa_chain({"question": "Can you give me a practical example?"})
print("Response 3:", response3["answer"])
```

### RAG with Custom Retrieval Logic

```python
from langchain.schema import BaseRetriever
from langchain.callbacks.manager import CallbackManagerForRetrieverRun
from typing import List

class HybridRetriever(BaseRetriever):
    """Custom retriever that combines vector search with keyword search."""
    
    def __init__(self, vectorstore, texts: List[str], k: int = 4):
        self.vectorstore = vectorstore
        self.texts = texts
        self.k = k
    
    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        # Vector similarity search
        vector_docs = self.vectorstore.similarity_search(query, k=self.k//2)
        
        # Simple keyword search
        query_words = set(query.lower().split())
        keyword_matches = []
        
        for i, text in enumerate(self.texts):
            text_words = set(text.lower().split())
            overlap = len(query_words.intersection(text_words))
            if overlap > 0:
                keyword_matches.append((text, overlap, i))
        
        # Sort by overlap and take top matches
        keyword_matches.sort(key=lambda x: x[1], reverse=True)
        keyword_docs = [
            Document(page_content=match[0], metadata={"source": f"keyword_match_{match[2]}"})
            for match in keyword_matches[:self.k//2]
        ]
        
        # Combine and deduplicate
        all_docs = vector_docs + keyword_docs
        seen_content = set()
        unique_docs = []
        
        for doc in all_docs:
            if doc.page_content not in seen_content:
                seen_content.add(doc.page_content)
                unique_docs.append(doc)
        
        return unique_docs[:self.k]

# Use hybrid retriever
hybrid_retriever = HybridRetriever(vectorstore, texts, k=4)

# Create RAG chain with hybrid retriever
hybrid_qa = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type="stuff",
    retriever=hybrid_retriever,
    return_source_documents=True
)

result = hybrid_qa("Tell me about machine learning frameworks")
```

### RAG with Re-ranking

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

# Create compressor that extracts relevant parts
compressor = LLMChainExtractor.from_llm(chat)

# Wrap the retriever with compression
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever
)

# Use compressed retriever in RAG
compressed_qa = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type="stuff",
    retriever=compression_retriever,
    return_source_documents=True
)

result = compressed_qa("How do embeddings work in natural language processing?")
```

---

## LLM Integration

### OpenAI Integration

```python
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Standard OpenAI LLM
openai_llm = OpenAI(
    model_name="gpt-3.5-turbo-instruct",
    temperature=0.7,
    max_tokens=500,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Chat model (recommended)
openai_chat = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    max_tokens=500,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

# Function calling
from langchain.schema import FunctionMessage
from langchain.tools import format_tool_to_openai_function

def get_current_weather(location: str, unit: str = "fahrenheit"):
    """Get the current weather in a given location"""
    return f"The weather in {location} is 72 degrees {unit} and sunny."

# Convert function to OpenAI format
weather_function = {
    "name": "get_current_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA",
            },
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
    },
}

# Use function calling
function_chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
).bind(functions=[weather_function])

response = function_chat.invoke([HumanMessage(content="What's the weather in Boston?")])
print(response)
```

### Anthropic Claude Integration

```python
from langchain.llms import Anthropic
from langchain.chat_models import ChatAnthropic

# Anthropic LLM
anthropic_llm = Anthropic(
    model="claude-2",
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
    max_tokens_to_sample=500
)

# Chat model
anthropic_chat = ChatAnthropic(
    model="claude-3-sonnet-20240229",
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"),
    max_tokens=500
)

# Use with chains
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

template = "Explain {topic} in simple terms:"
prompt = PromptTemplate(template=template, input_variables=["topic"])

anthropic_chain = LLMChain(llm=anthropic_chat, prompt=prompt)
result = anthropic_chain.run(topic="quantum computing")
```

### Local Models with Ollama

```python
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Initialize Ollama
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

ollama_llm = Ollama(
    model="llama2",
    base_url="http://localhost:11434",
    callback_manager=callback_manager,
    verbose=True
)

# Test the model
response = ollama_llm("Explain machine learning in simple terms")
print(response)

# Use with different models
models = ["llama2", "codellama", "mistral"]

def test_multiple_models(prompt: str):
    for model in models:
        print(f"\n--- {model.upper()} ---")
        llm = Ollama(model=model, base_url="http://localhost:11434")
        response = llm(prompt)
        print(response)

test_multiple_models("Write a Python function to calculate fibonacci numbers")
```

### HuggingFace Integration

```python
from langchain.llms import HuggingFacePipeline
from langchain.llms import HuggingFaceHub
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Local HuggingFace model
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Create pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=100,
    temperature=0.7,
    do_sample=True
)

# LangChain wrapper
hf_pipeline = HuggingFacePipeline(pipeline=pipe)

# Use in chain
template = "Question: {question}\nAnswer:"
prompt = PromptTemplate(template=template, input_variables=["question"])
hf_chain = LLMChain(llm=hf_pipeline, prompt=prompt)

# HuggingFace Hub (requires API key)
hf_hub_llm = HuggingFaceHub(
    repo_id="google/flan-t5-large",
    model_kwargs={"temperature": 0.7, "max_length": 100},
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_TOKEN")
)
```

### Custom LLM Wrapper

```python
from langchain.llms.base import LLM
from typing import Optional, List, Any
import requests

class CustomAPILLM(LLM):
    """Custom LLM wrapper for any API."""
    
    api_url: str
    api_key: str
    model_name: str = "custom-model"
    temperature: float = 0.7
    max_tokens: int = 500
    
    @property
    def _llm_type(self) -> str:
        return "custom_api"
    
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[Any] = None,
        **kwargs: Any,
    ) -> str:
        """Call the custom API."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "prompt": prompt,
            "model": self.model_name,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop": stop or []
        }
        
        response = requests.post(self.api_url, json=data, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        return result.get("text", "")
    
    @property
    def _identifying_params(self) -> dict:
        """Get the identifying parameters."""
        return {
            "api_url": self.api_url,
            "model_name": self.model_name,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        }

# Use custom LLM
custom_llm = CustomAPILLM(
    api_url="https://api.example.com/v1/generate",
    api_key="your-api-key"
)

# Test it
response = custom_llm("What is the capital of France?")
```

### Model Comparison and Selection

```python
from langchain.model_laboratory import ModelLaboratory
from langchain.chains import LLMChain

# Define models to compare
models = [
    OpenAI(temperature=0.7),
    ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
    Ollama(model="llama2"),
]

# Create chains for each model
chains = [LLMChain(llm=model, prompt=prompt) for model in models]

# Model laboratory for comparison
lab = ModelLaboratory.from_llms(models)

# Compare responses
prompt_text = "Explain the benefits of renewable energy"
lab.compare(prompt_text)

# Programmatic comparison
def compare_models(prompt: str, models: List[LLM]):
    results = {}
    for i, model in enumerate(models):
        try:
            result = model(prompt)
            results[f"Model_{i}"] = {
                "response": result,
                "model_type": model._llm_type,
                "length": len(result)
            }
        except Exception as e:
            results[f"Model_{i}"] = {"error": str(e)}
    
    return results

comparison = compare_models("What is artificial intelligence?", models)
for model, result in comparison.items():
    print(f"{model}: {result}")
```

---

## Evaluation

### Basic Evaluation

```python
from langchain.evaluation import load_evaluator
from langchain.evaluation.criteria import CriteriaEvalChain

# Criteria-based evaluation
evaluator = load_evaluator("criteria", criteria="helpfulness")

# Evaluate a response
eval_result = evaluator.evaluate_strings(
    prediction="LangChain is a framework for building LLM applications. It provides tools for chaining operations, managing memory, and integrating with various services.",
    input="What is LangChain?",
)

print("Evaluation Score:", eval_result["score"])
print("Reasoning:", eval_result["reasoning"])

# Custom criteria
custom_evaluator = load_evaluator(
    "criteria",
    criteria={
        "accuracy": "Is the response factually accurate?",
        "completeness": "Does the response fully address the question?",
        "clarity": "Is the response clear and easy to understand?"
    }
)

custom_result = custom_evaluator.evaluate_strings(
    prediction="Your response here",
    input="Your question here"
)
```

### QA Evaluation

```python
from langchain.evaluation.qa import QAEvalChain
from langchain.evaluation.qa import ContextQAEvalChain

# Basic QA evaluation
qa_evaluator = QAEvalChain.from_llm(chat)

examples = [
    {
        "question": "What is the capital of France?",
        "answer": "The capital of France is Paris."
    },
    {
        "question": "What is 2+2?", 
        "answer": "2+2 equals 4."
    }
]

predictions = [
    {"result": "Paris is the capital of France."},
    {"result": "The answer is 4."}
]

graded_outputs = qa_evaluator.evaluate(
    examples,
    predictions,
    question_key="question",
    answer_key="answer",
    prediction_key="result"
)

for output in graded_outputs:
    print(f"Question: {output['query']}")
    print(f"Expected: {output['answer']}")
    print(f"Predicted: {output['result']}")
    print(f"Grade: {output['results']}\n")

# Context-aware QA evaluation
context_evaluator = ContextQAEvalChain.from_llm(chat)

context_examples = [
    {
        "question": "What is LangChain?",
        "context": "LangChain is a framework for developing applications powered by language models.",
        "answer": "A framework for LLM applications"
    }
]

context_predictions = [
    {"result": "LangChain is a framework for building language model applications"}
]

context_grades = context_evaluator.evaluate(
    context_examples,
    context_predictions,
    question_key="question",
    answer_key="answer",
    prediction_key="result"
)
```

### RAG Evaluation

```python
from langchain.evaluation.qa import QAGenerateChain
from langchain.docstore.document import Document

# Generate QA pairs from documents
doc_texts = [
    "LangChain is a framework for developing applications powered by language models. It enables applications that are data-aware and agentic.",
    "Vector databases store high-dimensional vectors and enable similarity search. They are crucial for RAG applications.",
    "Retrieval-Augmented Generation combines retrieval of relevant documents with language generation."
]

docs = [Document(page_content=text) for text in doc_texts]

# Generate QA pairs
qa_generator = QAGenerateChain.from_llm(chat)
qa_pairs = qa_generator.apply_and_parse([{"doc": doc} for doc in docs])

print("Generated QA pairs:")
for qa in qa_pairs:
    print(f"Q: {qa['query']}")
    print(f"A: {qa['answer']}\n")

# Evaluate RAG system
def evaluate_rag_system(qa_chain, qa_pairs):
    results = []
    
    for qa_pair in qa_pairs:
        question = qa_pair["query"]
        expected_answer = qa_pair["answer"]
        
        # Get prediction from RAG system
        prediction = qa_chain(question)
        
        # Evaluate
        eval_result = qa_evaluator.evaluate(
            [{"question": question, "answer": expected_answer}],
            [{"result": prediction["result"]}],
            question_key="question",
            answer_key="answer",
            prediction_key="result"
        )[0]
        
        results.append({
            "question": question,
            "expected": expected_answer,
            "predicted": prediction["result"],
            "grade": eval_result["results"]
        })
    
    return results

# Run evaluation
if 'qa_chain' in locals():
    evaluation_results = evaluate_rag_system(qa_chain, qa_pairs)
    
    # Calculate metrics
    correct = sum(1 for r in evaluation_results if r["grade"] == "CORRECT")
    total = len(evaluation_results)
    accuracy = correct / total
    
    print(f"Accuracy: {accuracy:.2%} ({correct}/{total})")
```

### Custom Evaluation Metrics

```python
from langchain.evaluation.schema import EvaluatorType
from langchain.evaluation.loading import load_evaluator
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SemanticSimilarityEvaluator:
    """Custom evaluator for semantic similarity."""
    
    def __init__(self, embeddings):
        self.embeddings = embeddings
    
    def evaluate(self, prediction: str, reference: str) -> float:
        """Calculate semantic similarity between prediction and reference."""
        pred_embedding = self.embeddings.embed_query(prediction)
        ref_embedding = self.embeddings.embed_query(reference)
        
        similarity = cosine_similarity(
            [pred_embedding], 
            [ref_embedding]
        )[0][0]
        
        return similarity
    
    def evaluate_batch(self, predictions: List[str], references: List[str]) -> List[float]:
        """Evaluate multiple predictions."""
        scores = []
        for pred, ref in zip(predictions, references):
            score = self.evaluate(pred, ref)
            scores.append(score)
        return scores

# Use custom evaluator
semantic_evaluator = SemanticSimilarityEvaluator(openai_embeddings)

predictions = ["Paris is the capital of France", "The French capital is Paris"]
references = ["France's capital city is Paris", "Paris is France's capital"]

scores = semantic_evaluator.evaluate_batch(predictions, references)
print("Semantic similarity scores:", scores)

# Comprehensive evaluation framework
class ComprehensiveEvaluator:
    def __init__(self, llm, embeddings):
        self.llm = llm
        self.embeddings = embeddings
        self.criteria_evaluator = load_evaluator("criteria", criteria="helpfulness")
        self.semantic_evaluator = SemanticSimilarityEvaluator(embeddings)
    
    def evaluate_response(self, question: str, prediction: str, reference: str = None):
        """Comprehensive evaluation of a response."""
        results = {}
        
        # Criteria-based evaluation
        criteria_result = self.criteria_evaluator.evaluate_strings(
            prediction=prediction,
            input=question
        )
        results["helpfulness_score"] = criteria_result["score"]
        results["helpfulness_reasoning"] = criteria_result["reasoning"]
        
        # Semantic similarity (if reference provided)
        if reference:
            semantic_score = self.semantic_evaluator.evaluate(prediction, reference)
            results["semantic_similarity"] = semantic_score
        
        # Length metrics
        results["response_length"] = len(prediction.split())
        
        # Readability (simple metric)
        sentences = prediction.split('.')
        avg_sentence_length = np.mean([len(s.split()) for s in sentences if s.strip()])
        results["avg_sentence_length"] = avg_sentence_length
        
        return results

# Use comprehensive evaluator
comprehensive_evaluator = ComprehensiveEvaluator(chat, openai_embeddings)

eval_results = comprehensive_evaluator.evaluate_response(
    question="What is machine learning?",
    prediction="Machine learning is a subset of artificial intelligence that enables computers to learn and make decisions from data without being explicitly programmed.",
    reference="Machine learning is a method of data analysis that automates analytical model building using algorithms that iteratively learn from data."
)

print("Comprehensive Evaluation Results:")
for metric, score in eval_results.items():
    print(f"{metric}: {score}")
```

---

## Deployment

### Local Deployment with FastAPI

```python
# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import uvicorn
import os

app = FastAPI(title="LangChain API", version="1.0.0")

# Initialize LLM and memory
llm = OpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

# Request/Response models
class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    response: str
    session_id: str

# Session management
sessions = {}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Get or create session
        if request.session_id not in sessions:
            sessions[request.session_id] = ConversationChain(
                llm=llm, 
                memory=ConversationBufferMemory()
            )
        
        conversation = sessions[request.session_id]
        
        # Generate response
        response = conversation.predict(input=request.message)
        
        return ChatResponse(
            response=response,
            session_id=request.session_id
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.delete("/session/{session_id}")
async def clear_session(session_id: str):
    if session_id in sessions:
        del sessions[session_id]
        return {"message": f"Session {session_id} cleared"}
    return {"message": "Session not found"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```bash
# Run the application
pip install fastapi uvicorn
python app.py

# Test the API
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"message": "Hello, how are you?", "session_id": "user123"}'
```

### Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

```yaml
# docker-compose.yml
version: '3'

services:
  langchain-app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./app:/app
```

```bash
# Build and run with Docker Compose
docker-compose up --build
```

### Cloud Deployment

#### AWS Lambda Deployment

```python
# lambda_function.py
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import json
import os

# Initialize LLM and chain
llm = OpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory()
)

def lambda_handler(event, context):
    try:
        # Parse input
        body = json.loads(event.get('body', '{}'))
        message = body.get('message', '')
        
        # Generate response
        response = conversation.predict(input=message)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'response': response
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
```

#### Serverless Framework Configuration

```yaml
# serverless.yml
service: langchain-service

provider:
  name: aws
  runtime: python3.9
  region: us-east-1
  environment:
    OPENAI_API_KEY: ${env:OPENAI_API_KEY}

functions:
  chat:
    handler: lambda_function.lambda_handler
    events:
      - http:
          path: chat
          method: post
          cors: true
```

### Monitoring and Logging

```python
from langchain.callbacks import StdOutCallbackHandler
from langchain.callbacks.tracers import LangChainTracer
from langchain.callbacks.tracers.langchain import wait_for_all_tracers
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup callbacks
handlers = [
    StdOutCallbackHandler(),
    LangChainTracer(project_name="my_langchain_app")
]

# Initialize LLM with callbacks
llm = OpenAI(
    temperature=0.7,
    callbacks=handlers
)

# Log usage and performance
def log_usage(user_id, query, response, latency):
    logger.info(f"User: {user_id} | Query: {query} | Latency: {latency}ms")
    # You could also send this to a monitoring service

# Example usage
start_time = time.time()
response = llm("What is LangChain?")
latency = (time.time() - start_time) * 1000

log_usage("user123", "What is LangChain?", response, latency)
wait_for_all_tracers()
```

### Streamlit Web App

```python
# streamlit_app.py
import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
import os

st.set_page_config(page_title="LangChain Chat App", page_icon="🤖")

# Initialize session state
if "conversation" not in st.session_state:
    llm = OpenAI(temperature=0.7, openai_api_key=os.getenv("OPENAI_API_KEY"))
    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory()
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for configuration
st.sidebar.title("Configuration")
mode = st.sidebar.selectbox("Mode", ["Chat", "Document Q&A"])

if mode == "Document Q&A":
    uploaded_file = st.sidebar.file_uploader("Upload a document", type=['txt', 'pdf'])
    
    if uploaded_file and "qa_chain" not in st.session_state:
        # Process uploaded document
        with st.spinner("Processing document..."):
            # Read file content
            content = uploaded_file.read().decode('utf-8')
            
            # Create vector store
            from langchain.text_splitter import RecursiveCharacterTextSplitter
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = text_splitter.split_text(content)
            
            embeddings = OpenAIEmbeddings()
            vectorstore = Chroma.from_texts(chunks, embeddings)
            
            # Create QA chain
            st.session_state.qa_chain = RetrievalQA.from_chain_type(
                llm=OpenAI(temperature=0),
                chain_type="stuff",
                retriever=vectorstore.as_retriever()
            )
        
        st.sidebar.success("Document processed successfully!")

# Main chat interface
st.title("🤖 LangChain Chat Application")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            if mode == "Chat":
                response = st.session_state.conversation.predict(input=prompt)
            else:  # Document Q&A mode
                if "qa_chain" in st.session_state:
                    response = st.session_state.qa_chain.run(prompt)
                else:
                    response = "Please upload a document first to use Q&A mode."
            
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat button
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    if "conversation" in st.session_state:
        st.session_state.conversation.memory.clear()
    st.rerun()

---

## Best Practices

### Prompt Engineering

1. **Be Specific and Clear**
   ```python
   # Bad prompt
   bad_prompt = PromptTemplate(template="Write about {topic}.")
   
   # Good prompt
   good_prompt = PromptTemplate(
       template="Write a detailed explanation of {topic} covering its history, key concepts, and practical applications. Include specific examples."
   )
   ```

2. **Use System Messages Effectively**
   ```python
   from langchain.schema import SystemMessage, HumanMessage
   
   messages = [
       SystemMessage(content="You are a senior data scientist with expertise in machine learning. Provide technical, accurate responses with code examples when appropriate."),
       HumanMessage(content="Explain how to handle imbalanced datasets")
   ]
   ```

3. **Include Few-Shot Examples**
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

### Memory Management

1. **Choose the Right Memory Type**
   ```python
   # For simple conversations
   from langchain.memory import ConversationBufferMemory
   
   # For long conversations (limited context)
   from langchain.memory import ConversationBufferWindowMemory
   
   # For summarizing long conversations
   from langchain.memory import ConversationSummaryMemory
   ```

2. **Clear Memory When Needed**
   ```python
   # Clear memory when changing topics
   conversation.memory.clear()
   
   # Selectively modify memory
   conversation.memory.chat_memory.messages = conversation.memory.chat_memory.messages[-4:]
   ```

3. **Use Entity Memory for Key Information**
   ```python
   from langchain.memory import ConversationEntityMemory
   
   entity_memory = ConversationEntityMemory(llm=llm)
   conversation = ConversationChain(llm=llm, memory=entity_memory)
   ```

### Performance Optimization

1. **Batch Processing**
   ```python
   # Process documents in batches
   from langchain.docstore.document import Document
   
   docs = [Document(page_content=text) for text in texts]
   batch_size = 10
   
   for i in range(0, len(docs), batch_size):
       batch = docs[i:i+batch_size]
       embeddings_batch = embeddings.embed_documents([doc.page_content for doc in batch])
   ```

2. **Caching Results**
   ```python
   from langchain.cache import InMemoryCache
   import langchain
   
   # Setup cache
   langchain.llm_cache = InMemoryCache()
   
   # First call (not cached)
   result1 = llm("What is the capital of France?")
   
   # Second call (cached)
   result2 = llm("What is the capital of France?")
   ```

3. **Use Streaming for Better UX**
   ```python
   from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
   
   llm = OpenAI(
       streaming=True,
       callbacks=[StreamingStdOutCallbackHandler()],
       temperature=0.7
   )
   ```

### Error Handling and Reliability

1. **Implement Retry Logic**
   ```python
   from langchain.llms import OpenAI
   from tenacity import retry, stop_after_attempt, wait_random_exponential
   
   @retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(5))
   def generate_with_retry(prompt):
       try:
           return llm(prompt)
       except Exception as e:
           print(f"Error: {e}")
           raise
   ```

2. **Validate Outputs**
   ```python
   from pydantic import BaseModel, validator
   
   class GeneratedResponse(BaseModel):
       content: str
       
       @validator('content')
       def content_not_empty(cls, v):
           if not v.strip():
               raise ValueError("Generated content cannot be empty")
           return v
   ```

3. **Implement Fallbacks**
   ```python
   def get_response(prompt):
       try:
           # Try primary model
           return primary_llm(prompt)
       except Exception:
           try:
               # Fallback to secondary model
               return fallback_llm(prompt)
           except Exception:
               # Final fallback
               return "I'm sorry, I'm having trouble processing your request right now."
   ```

### Security Best Practices

1. **Sanitize Inputs**
   ```python
   import re
   
   def sanitize_input(user_input):
       # Remove potential prompt injection attempts
       patterns = [
           r"ignore previous instructions",
           r"ignore all instructions"
       ]
       for pattern in patterns:
           user_input = re.sub(pattern, "", user_input, flags=re.IGNORECASE)
       return user_input
   ```

2. **Use Environment Variables for API Keys**
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   
   llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
   ```

3. **Implement Rate Limiting**
   ```python
   import time
   from functools import wraps
   
   def rate_limit(max_per_minute):
       interval = 60 / max_per_minute
       last_called = [0.0]
       
       def decorator(func):
           @wraps(func)
           def wrapper(*args, **kwargs):
               elapsed = time.time() - last_called[0]
               if elapsed < interval:
                   time.sleep(interval - elapsed)
               result = func(*args, **kwargs)
               last_called[0] = time.time()
               return result
           return wrapper
       return decorator
   
   @rate_limit(max_per_minute=60)  # 60 requests per minute
    def call_llm(prompt):
        return llm(prompt)
    ```

---

## Full Example: Local Chatbot with Ollama

This example demonstrates how to build a complete local chatbot using LangChain with Ollama, a tool for running LLMs locally.

### 1. Setup and Installation

```bash
# Install required packages
pip install langchain ollama python-dotenv streamlit

# Run Ollama and pull a model (in a separate terminal)
ollama pull llama2
```

### 2. Create the Chatbot Application

```python
# app.py
import os
import streamlit as st
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "conversation" not in st.session_state:
    # Initialize Ollama LLM
    llm = Ollama(
        model="llama2",
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
        temperature=0.7,
    )
    
    # Create a conversation memory
    memory = ConversationBufferMemory()
    
    # Create a conversation chain
    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

# Streamlit UI
st.title("🦙 Local LLM Chatbot with Ollama")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask something..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Get response from LLM
        response = st.session_state.conversation.predict(input=prompt)
        
        # Simulate streaming
        for chunk in response.split():
            full_response += chunk + " "
            message_placeholder.markdown(full_response + "▌")
            import time
            time.sleep(0.01)
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with options
with st.sidebar:
    st.title("Options")
    
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.session_state.conversation.memory.clear()
        st.rerun()
    
    st.divider()
    
    # Model selection
    model = st.selectbox(
        "Select Model",
        ["llama2", "mistral", "vicuna", "orca-mini"],
        index=0
    )
    
    # Temperature slider
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )
    
    # Apply settings button
    if st.button("Apply Settings"):
        # Reinitialize LLM with new settings
        llm = Ollama(
            model=model,
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
            temperature=temperature,
        )
        
        # Update conversation chain
        memory = ConversationBufferMemory()
        st.session_state.conversation = ConversationChain(
            llm=llm,
            memory=memory,
            verbose=True
        )
        
        st.success(f"Settings applied! Using {model} with temperature {temperature}")
```

### 3. Run the Application

```bash
streamlit run app.py
```

### 4. Adding Document Q&A Capabilities

```python
# Add these imports to the top of app.py
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import tempfile

# Add this to the sidebar
with st.sidebar:
    # ... existing sidebar code ...
    
    st.divider()
    st.subheader("Document Q&A")
    
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt"])
    
    if uploaded_file is not None:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        
        # Load document based on file type
        if uploaded_file.name.endswith(".pdf"):
            loader = PyPDFLoader(tmp_path)
        else:  # txt file
            loader = TextLoader(tmp_path)
        
        documents = loader.load()
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(documents)
        
        with st.spinner("Processing document..."):
            # Create embeddings and vector store
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            vectorstore = Chroma.from_documents(chunks, embeddings)
            
            # Create QA chain
            st.session_state.qa_chain = RetrievalQA.from_chain_type(
                llm=Ollama(model=model),
                chain_type="stuff",
                retriever=vectorstore.as_retriever()
            )
        
        st.success("Document processed! You can now ask questions about it.")
        
        # Add a toggle for switching between chat and QA modes
        st.session_state.mode = st.radio(
            "Mode",
            ["Chat", "Document Q&A"],
            index=0
        )

# Modify the chat input section to handle both modes
if prompt := st.chat_input("Ask something..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Get response based on mode
        if hasattr(st.session_state, "mode") and st.session_state.mode == "Document Q&A":
            if "qa_chain" in st.session_state:
                response = st.session_state.qa_chain.run(prompt)
            else:
                response = "Please upload a document first to use Q&A mode."
        else:
            response = st.session_state.conversation.predict(input=prompt)
        
        # Simulate streaming
        for chunk in response.split():
            full_response += chunk + " "
            message_placeholder.markdown(full_response + "▌")
            import time
            time.sleep(0.01)
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
```

---

## LangChain Cheatsheet

### Core Components

#### LLMs & Chat Models
```python
# OpenAI
from langchain.llms import OpenAI
llm = OpenAI(temperature=0.7)

# Chat models
from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI(temperature=0.7)

# Local models with Ollama
from langchain.llms import Ollama
local_llm = Ollama(model="llama2")
```

#### Prompts
```python
# Simple prompt template
from langchain.prompts import PromptTemplate
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?"
)

# Chat prompt template
from langchain.prompts import ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}")
])

# Few-shot prompt template
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}",
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Give the antonym of every input",
    suffix="Input: {adjective}\nOutput:",
    input_variables=["adjective"],
)
```

#### Chains
```python
# LLMChain
from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Sequential Chain
from langchain.chains import SimpleSequentialChain, SequentialChain
chain1 = LLMChain(llm=llm, prompt=prompt1)
chain2 = LLMChain(llm=llm, prompt=prompt2)

# Simple sequential chain (single input/output)
simple_chain = SimpleSequentialChain(chains=[chain1, chain2])

# Sequential chain (multiple inputs/outputs)
sequential_chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["topic"],
    output_variables=["title", "summary"]
)

# Router Chain
from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain
from langchain.prompts import PromptTemplate

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

router_chain = MultiPromptChain.from_prompts(
    llm, prompt_infos, default_chain=default_chain
)
```

#### Memory
```python
# Conversation Buffer Memory
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
memory.save_context({"input": "hi"}, {"output": "hello"})

# Conversation Buffer Window Memory
from langchain.memory import ConversationBufferWindowMemory
memory = ConversationBufferWindowMemory(k=5)  # last 5 interactions

# Conversation Summary Memory
from langchain.memory import ConversationSummaryMemory
memory = ConversationSummaryMemory(llm=llm)

# Entity Memory
from langchain.memory import ConversationEntityMemory
memory = ConversationEntityMemory(llm=llm)

# Using memory in a chain
conversation = ConversationChain(
    llm=llm, 
    memory=memory,
    verbose=True
)
```

#### Embeddings & Vector Stores
```python
# Embeddings
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# Local embeddings
from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Chroma Vector Store
from langchain.vectorstores import Chroma
vectorstore = Chroma.from_texts(
    texts, embeddings, metadatas=[{"source": i} for i in range(len(texts))]
)

# FAISS Vector Store
from langchain.vectorstores import FAISS
vectorstore = FAISS.from_texts(texts, embeddings)

# Save and load FAISS index
vectorstore.save_local("faiss_index")
loaded_vectorstore = FAISS.load_local("faiss_index", embeddings)

# Similarity search
docs = vectorstore.similarity_search(query, k=4)

# Similarity search with score
docs_and_scores = vectorstore.similarity_search_with_score(query, k=4)
```

#### Document Loaders
```python
# Text Loader
from langchain.document_loaders import TextLoader
loader = TextLoader("./data/example.txt")
documents = loader.load()

# PDF Loader
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("./data/example.pdf")
documents = loader.load()

# Web Loader
from langchain.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://example.com")
documents = loader.load()

# Directory Loader
from langchain.document_loaders import DirectoryLoader
loader = DirectoryLoader("./data/", glob="**/*.txt")
documents = loader.load()
```

#### Text Splitters
```python
# Character Text Splitter
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_splitter.split_text(text)

# Recursive Character Text Splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_splitter.split_documents(documents)
```

#### Retrievers
```python
# Vector Store Retriever
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
docs = retriever.get_relevant_documents(query)

# Contextual Compression Retriever
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

base_retriever = vectorstore.as_retriever()
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)
```

#### Retrieval QA
```python
# Basic RetrievalQA
from langchain.chains import RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=retriever,
    chain_type="stuff"
)
result = qa_chain.run(query)

# With custom prompt
from langchain.prompts import PromptTemplate

prompt_template = """Use the following pieces of context to answer the question at the end.

{context}

Question: {question}
Answer:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": PROMPT}
)
```

#### Agents
```python
# Initialize agent with tools
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType

tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run agent
agent.run("What was the high temperature in SF yesterday? What is that number raised to the .023 power?")

# Custom tools
from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field

class CalculatorInput(BaseModel):
    expression: str = Field()

class Calculator(BaseTool):
    name = "calculator"
    description = "useful for when you need to calculate math expressions"
    args_schema: Type[BaseModel] = CalculatorInput

    def _run(self, expression: str) -> str:
        return str(eval(expression))

    def _arun(self, expression: str) -> str:
        return str(eval(expression))

tools = [Calculator()]
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
```

#### Callbacks
```python
# Custom callback handler
from langchain.callbacks import BaseCallbackHandler

class MyCustomHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print(f"\n\n\nLLM started: {prompts}\n\n\n")
        
    def on_llm_end(self, response, **kwargs):
        print(f"\n\n\nLLM ended: {response}\n\n\n")

# Using callbacks
llm = OpenAI(callbacks=[MyCustomHandler()])
llm("Tell me a joke")

# Streaming
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
llm("Tell me a joke")
```

#### Evaluation
```python
# Basic evaluation
from langchain.evaluation import load_evaluator

evaluator = load_evaluator("qa")
evaluation = evaluator.evaluate_strings(
    prediction="The capital of France is Paris",
    reference="Paris is the capital of France"
)

# Criteria evaluation
from langchain.evaluation import load_evaluator

evaluator = load_evaluator("criteria", criteria="correctness")
evaluation = evaluator.evaluate_strings(
    prediction="The capital of France is Paris",
    input="What is the capital of France?"
)

# Custom criteria
evaluator = load_evaluator(
    "criteria",
    criteria={
        "accuracy": "Is the response accurate based on the context?",
        "conciseness": "Is the response concise and to the point?"
    }
)
```

---

## LangChain vs LlamaIndex

### Overview

| Feature | LangChain | LlamaIndex |
|---------|-----------|------------|
| **Primary Focus** | General-purpose framework for LLM applications | Specialized in data indexing and retrieval |
| **Core Strength** | Flexibility and modularity | Data connection and structured retrieval |
| **Learning Curve** | Steeper due to broader scope | Gentler for data retrieval use cases |
| **Community Size** | Larger community and ecosystem | Growing community |
| **Integration** | Works well with many tools including LlamaIndex | Can be used as a component within LangChain |

### When to Use LangChain

- Building complex LLM applications with multiple components
- Creating agents that use tools and reasoning
- Implementing custom chains and workflows
- Need for advanced memory systems
- Integrating with a wide variety of tools and services

### When to Use LlamaIndex

- Primarily focused on data ingestion and retrieval
- Working with structured data sources
- Need for advanced indexing strategies
- Simpler RAG applications with less custom logic
- Working with hierarchical or graph-structured data

### Code Comparison

#### Basic RAG Implementation

**LangChain:**
```python
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Load document
loader = TextLoader("document.txt")
documents = loader.load()

# Split text
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(texts, embeddings)

# Create QA chain
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# Query
query = "What is the main topic of the document?"
result = qa.run(query)
```

**LlamaIndex:**
```python
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, ServiceContext
from langchain.llms import OpenAI

# Load documents
documents = SimpleDirectoryReader("./").load_data()

# Create LLM predictor and service context
llm_predictor = LLMPredictor(llm=OpenAI())
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# Create index
index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

# Create query engine
query_engine = index.as_query_engine()

# Query
response = query_engine.query("What is the main topic of the document?")
```

#### Advanced Features

**LangChain (Agent with Tools):**
```python
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

# Initialize LLM
llm = OpenAI(temperature=0)

# Load tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Initialize agent
agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run agent
agent.run("What was the high temperature in SF yesterday? What is that number raised to the .023 power?")
```

**LlamaIndex (Composable Indices):**
```python
from llama_index import SimpleDirectoryReader, GPTListIndex, GPTVectorStoreIndex, LLMPredictor, ServiceContext
from llama_index.indices.composability import ComposableGraph
from langchain.llms import OpenAI

# Load documents for different topics
docs_economics = SimpleDirectoryReader("./economics").load_data()
docs_politics = SimpleDirectoryReader("./politics").load_data()

# Create LLM predictor and service context
llm_predictor = LLMPredictor(llm=OpenAI())
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# Create indices for each topic
index_economics = GPTVectorStoreIndex.from_documents(docs_economics, service_context=service_context)
index_politics = GPTVectorStoreIndex.from_documents(docs_politics, service_context=service_context)

# Create summary indices
summary_economics = GPTListIndex.from_documents(docs_economics, service_context=service_context)
summary_politics = GPTListIndex.from_documents(docs_politics, service_context=service_context)

# Create composable graph
graph = ComposableGraph.from_indices(
    GPTListIndex,
    [index_economics, index_politics],
    [summary_economics, summary_politics],
    index_summaries=["Economics documents", "Politics documents"],
    service_context=service_context
)

# Query the graph
query_engine = graph.as_query_engine()
response = query_engine.query("How do economic policies affect political decisions?")
```

### Integration Example

**Using LlamaIndex with LangChain:**
```python
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index.langchain_helpers.text_splitter import LangChainTextSplitter
from llama_index.langchain_helpers.chain_wrapper import LLMPredictor
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter

# Load documents using LlamaIndex
documents = SimpleDirectoryReader("./data").load_data()

# Use LangChain text splitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = text_splitter.split_text([doc.text for doc in documents])

# Create LlamaIndex from splits
llm_predictor = LLMPredictor(llm=OpenAI())
index = GPTVectorStoreIndex.from_documents(documents, llm_predictor=llm_predictor)

# Convert to LangChain retriever
retriever = index.as_langchain_retriever()

# Use in LangChain RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=retriever
)

# Query
result = qa_chain.run("What insights can we extract from the documents?")
```

### Conclusion

Both LangChain and LlamaIndex are powerful tools in the LLM ecosystem with different strengths:

- **LangChain** excels at providing a comprehensive framework for building complex LLM applications with its modular components and agent capabilities.

- **LlamaIndex** shines in data indexing and retrieval scenarios, offering specialized data structures and retrieval mechanisms.

For many projects, using both frameworks together provides the best of both worlds: LlamaIndex for sophisticated data indexing and retrieval, and LangChain for orchestrating the overall application flow and integrating with other tools.