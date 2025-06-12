# Document Loaders

Document loaders in LangChain are used to load documents from various sources, such as files, websites, and databases. These documents can then be processed, embedded, and used for retrieval-augmented generation (RAG).

## Text and PDF Loaders

```python
from langchain.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Text file loader
text_loader = TextLoader("document.txt")
documents = text_loader.load()

# PDF loader
pdf_loader = PyPDFLoader("document.pdf")
documents = pdf_loader.load()

# Directory loader (load all text files in a directory)
directory_loader = DirectoryLoader("./data", glob="**/*.txt", loader_cls=TextLoader)
documents = directory_loader.load()

# Process the loaded documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_documents = text_splitter.split_documents(documents)
```

## Web Loaders

```python
from langchain.document_loaders import WebBaseLoader, SitemapLoader

# Load content from a single web page
web_loader = WebBaseLoader("https://www.example.com")
documents = web_loader.load()

# Load content from multiple web pages
web_loader = WebBaseLoader(["https://www.example.com/page1", "https://www.example.com/page2"])
documents = web_loader.load()

# Load content from a sitemap
sitemap_loader = SitemapLoader("https://www.example.com/sitemap.xml")
documents = sitemap_loader.load()
```

### Custom Web Loader

```python
from langchain.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup

class CustomWebLoader(WebBaseLoader):
    """Custom web loader that extracts specific content from web pages."""
    
    def parse(self, html: str) -> str:
        """Parse the HTML content and extract the main content."""
        soup = BeautifulSoup(html, "html.parser")
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()
        
        # Extract main content (customize based on the website structure)
        main_content = soup.find("main") or soup.find("article") or soup.find("div", {"class": "content"})
        
        if main_content:
            return main_content.get_text(separator="\n", strip=True)
        else:
            return soup.get_text(separator="\n", strip=True)

# Use the custom web loader
custom_loader = CustomWebLoader("https://www.example.com")
documents = custom_loader.load()
```

## Database and API Loaders

```python
from langchain.document_loaders import DataFrameLoader, JSONLoader, CSVLoader, SQLDatabaseLoader
import pandas as pd

# Load from a pandas DataFrame
df = pd.read_csv("data.csv")
df_loader = DataFrameLoader(df, page_content_column="text")
documents = df_loader.load()

# Load from a CSV file
csv_loader = CSVLoader("data.csv")
documents = csv_loader.load()

# Load from a JSON file
json_loader = JSONLoader(
    file_path="data.json",
    jq_schema=".messages[].content",
    text_content=False
)
documents = json_loader.load()

# Load from a SQL database
from sqlalchemy import create_engine

engine = create_engine("sqlite:///example.db")
sql_loader = SQLDatabaseLoader(engine, "SELECT * FROM documents")
documents = sql_loader.load()
```

## Text Splitting

After loading documents, it's often necessary to split them into smaller chunks for processing.

### Character Text Splitter

```python
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)

texts = text_splitter.split_text("Your long document text here...")
```

### Recursive Character Text Splitter

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)

texts = text_splitter.split_text("Your long document text here...")
```

### Token Text Splitter

```python
from langchain.text_splitter import TokenTextSplitter

text_splitter = TokenTextSplitter(
    chunk_size=100,  # in tokens
    chunk_overlap=20  # in tokens
)

texts = text_splitter.split_text("Your long document text here...")
```

### Spacy Text Splitter

```python
from langchain.text_splitter import SpacyTextSplitter

text_splitter = SpacyTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_text("Your long document text here...")
```

### Custom Sentence Splitter

```python
from langchain.text_splitter import TextSplitter
import re
from typing import List

class SentenceSplitter(TextSplitter):
    """Split text into sentences."""
    
    def split_text(self, text: str) -> List[str]:
        """Split text into sentences."""
        # Simple sentence splitting using regex
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s for s in sentences if s.strip()]

# Use the custom sentence splitter
splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)
texts = splitter.split_text("Hello world. How are you? I'm fine, thank you!")
```

## Document Processing Pipeline

```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# 1. Load documents
loader = PyPDFLoader("document.pdf")
documents = loader.load()

# 2. Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_documents = text_splitter.split_documents(documents)

# 3. Create embeddings and store in a vector database
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(split_documents, embeddings)

# 4. Create a retriever for later use
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
```

## Next Steps

Continue to the [Embeddings & Vector Stores](../07_embeddings/README.md) section to learn how to create and use embeddings for semantic search and retrieval.