# LangChain vs LlamaIndex

This section compares LangChain and LlamaIndex (formerly GPT Index), two popular frameworks for building LLM-powered applications.

## Overview

| Feature | LangChain | LlamaIndex |
|---------|-----------|------------|
| **Primary Focus** | General-purpose framework for LLM applications | Specialized in data indexing and retrieval |
| **Core Strength** | Flexible components for diverse LLM applications | Advanced data connectors and indexing strategies |
| **Use Cases** | Chatbots, agents, chains, RAG, summarization | Document Q&A, knowledge bases, structured data retrieval |
| **Learning Curve** | Moderate to steep | Moderate |
| **Customizability** | Highly customizable | Focused customization for data retrieval |
| **Community Size** | Larger | Growing |

## When to Use LangChain

- You need a comprehensive framework for diverse LLM applications
- You're building complex agent-based systems
- You require flexible chains of operations
- You need a wide variety of tools and integrations
- You want to leverage a large ecosystem of components

## When to Use LlamaIndex

- Your primary focus is data ingestion and retrieval
- You need advanced indexing strategies for large document sets
- You're working with structured data sources
- You need specialized data connectors
- You want simpler abstractions for RAG applications

## Code Comparison

### Basic RAG Implementation

#### LangChain

```python
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Load documents
loader = TextLoader("document.txt")
documents = loader.load()

# Split documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_documents = text_splitter.split_documents(documents)

# Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(split_documents, embeddings)

# Create a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# Create a RAG chain
rag_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="stuff",
    retriever=retriever,
    verbose=True
)

# Run the chain
query = "What is the main topic of the document?"
response = rag_chain.run(query)
print(response)
```

#### LlamaIndex

```python
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, ServiceContext
from langchain.llms import OpenAI

# Load documents
documents = SimpleDirectoryReader(input_files=["document.txt"]).load_data()

# Create LLM predictor
llm_predictor = LLMPredictor(llm=OpenAI(temperature=0))

# Create service context
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# Create index
index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

# Create query engine
query_engine = index.as_query_engine()

# Run query
query = "What is the main topic of the document?"
response = query_engine.query(query)
print(response)
```

### Advanced Features

#### LangChain Agents

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
agent.run("What was the high temperature in SF yesterday? What is that number raised to the 0.023 power?")
```

#### LlamaIndex Composable Indices

```python
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, GPTListIndex, ComposableGraph
from llama_index.indices.composable import ComposableGraph
from IPython.display import Markdown, display

# Load documents
documents = SimpleDirectoryReader("data").load_data()

# Split documents by source
wiki_docs = [doc for doc in documents if "wiki" in doc.metadata["source"]]
news_docs = [doc for doc in documents if "news" in doc.metadata["source"]]
research_docs = [doc for doc in documents if "research" in doc.metadata["source"]]

# Create indices for each source
wiki_index = GPTVectorStoreIndex.from_documents(wiki_docs)
news_index = GPTVectorStoreIndex.from_documents(news_docs)
research_index = GPTVectorStoreIndex.from_documents(research_docs)

# Create summary indices
wiki_summary_index = GPTListIndex.from_documents(wiki_docs)
news_summary_index = GPTListIndex.from_documents(news_docs)
research_summary_index = GPTListIndex.from_documents(research_docs)

# Create composable graph
graph = ComposableGraph.from_indices(
    GPTListIndex,
    [
        wiki_index,
        news_index,
        research_index
    ],
    [
        wiki_summary_index,
        news_summary_index,
        research_summary_index
    ],
    index_summaries=[
        "Wikipedia articles about AI",
        "Recent news about AI developments",
        "Research papers on AI"
    ]
)

# Create query engine
query_engine = graph.as_query_engine()

# Run query
response = query_engine.query("What are the latest developments in AI according to both news and research?")
print(response)
```

## Integrating LlamaIndex with LangChain

You can use LlamaIndex and LangChain together to leverage the strengths of both frameworks.

```python
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index.langchain_helpers.agents import IndexToolConfig, LlamaIndexTool
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory

# Load documents and create indices
wiki_docs = SimpleDirectoryReader("data/wiki").load_data()
news_docs = SimpleDirectoryReader("data/news").load_data()

wiki_index = GPTVectorStoreIndex.from_documents(wiki_docs)
news_index = GPTVectorStoreIndex.from_documents(news_docs)

# Create LlamaIndex tools for LangChain
wiki_tool_config = IndexToolConfig(
    query_engine=wiki_index.as_query_engine(),
    name="WikipediaIndex",
    description="Useful for answering questions about general knowledge from Wikipedia",
)

news_tool_config = IndexToolConfig(
    query_engine=news_index.as_query_engine(),
    name="NewsIndex",
    description="Useful for answering questions about recent events and news",
)

wiki_tool = LlamaIndexTool.from_tool_config(wiki_tool_config)
news_tool = LlamaIndexTool.from_tool_config(news_tool_config)

# Create LangChain agent with LlamaIndex tools
llm = OpenAI(temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history")

agent = initialize_agent(
    tools=[wiki_tool, news_tool],
    llm=llm,
    agent="conversational-react-description",
    memory=memory,
    verbose=True
)

# Run the agent
agent.run("What can you tell me about artificial intelligence? Also, what are the recent developments in this field?")
```

## Conclusion

Both LangChain and LlamaIndex are powerful frameworks with different strengths:

- **LangChain** excels as a comprehensive framework for building diverse LLM applications, with a focus on flexibility and composability.
- **LlamaIndex** specializes in data ingestion, indexing, and retrieval, making it particularly strong for document Q&A and knowledge base applications.

The best choice depends on your specific use case, and in many scenarios, you can leverage both frameworks together to build powerful LLM applications.

## Next Steps

Continue to the [Resources](../15_resources/README.md) section for additional learning materials and references.