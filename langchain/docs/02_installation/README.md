# Installation & Setup

## Python Installation

```python
# Install the core LangChain package
pip install langchain

# Install provider-specific packages
pip install langchain-openai  # For OpenAI models
pip install langchain-anthropic  # For Anthropic models
pip install langchain-google-genai  # For Google models

# Install vector store packages
pip install chromadb  # For ChromaDB vector store
pip install faiss-cpu  # For FAISS vector store
pip install pinecone-client  # For Pinecone vector store

# Install document loader dependencies
pip install pypdf  # For PDF loading
pip install docx2txt  # For Word document loading
pip install beautifulsoup4  # For web scraping
```

## JavaScript/TypeScript Installation

```bash
# Install the core LangChain.js package
npm install langchain

# Install provider-specific packages
npm install @langchain/openai
npm install @langchain/anthropic

# Install vector store packages
npm install @langchain/chroma
npm install @langchain/pinecone
```

## Environment Setup

```python
# Set up environment variables for API keys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access API keys
openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
```

Example `.env` file:
```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
PINCONE_API_KEY=...
PINCONE_ENVIRONMENT=...
```

## Basic Configuration

```python
# Configure LangChain to use specific LLM providers
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# Initialize LLM with API key from environment
llm = OpenAI(temperature=0.7)

# Initialize Chat model
chat_model = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")

# Test the LLM
response = llm("What is LangChain?")
print(response)
```

## Logging and Debugging

```python
# Enable verbose mode for debugging
import langchain
langchain.verbose = True

# Set up logging
import logging
logging.basicConfig()
logging.getLogger("langchain").setLevel(logging.DEBUG)
```

## Next Steps

Continue to the [Core Components](../03_core_components/README.md) section to learn about the fundamental building blocks of LangChain.