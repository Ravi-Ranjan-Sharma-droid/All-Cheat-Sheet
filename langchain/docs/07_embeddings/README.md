# Embeddings & Vector Stores

Embeddings convert text into numerical vectors that capture semantic meaning. Vector stores are databases that store these vectors and enable efficient similarity search. Together, they form the foundation for retrieval-augmented generation (RAG) systems.

## Embeddings

### OpenAI Embeddings

```python
from langchain.embeddings import OpenAIEmbeddings

# Initialize embeddings
embeddings = OpenAIEmbeddings()

# Create embeddings for a single text
text = "This is a sample text."
embedding = embeddings.embed_query(text)

# Create embeddings for multiple texts
texts = ["Text 1", "Text 2", "Text 3"]
embeddings_list = embeddings.embed_documents(texts)
```

### HuggingFace Embeddings

```python
from langchain.embeddings import HuggingFaceEmbeddings

# Initialize embeddings with a specific model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cuda"},  # Use GPU if available
    encode_kwargs={"normalize_embeddings": True}
)

# Create embeddings
text = "This is a sample text."
embedding = embeddings.embed_query(text)
```

### Custom Embeddings

```python
from langchain.embeddings.base import Embeddings
from typing import List
import numpy as np

class RandomEmbeddings(Embeddings):
    """Random embeddings for testing purposes."""
    
    def __init__(self, dim: int = 1536):
        self.dim = dim
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Generate random embeddings for documents."""
        return [self._get_random_embedding() for _ in texts]
    
    def embed_query(self, text: str) -> List[float]:
        """Generate random embedding for query."""
        return self._get_random_embedding()
    
    def _get_random_embedding(self) -> List[float]:
        """Generate a random embedding vector."""
        return list(np.random.rand(self.dim).astype(float))

# Use the custom embeddings
random_embeddings = RandomEmbeddings(dim=1536)
embedding = random_embeddings.embed_query("This is a test.")
```

## Vector Stores

### ChromaDB

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

# Initialize embeddings
embeddings = OpenAIEmbeddings()

# Create documents
documents = [
    Document(page_content="LangChain is a framework for developing applications powered by language models."),
    Document(page_content="LangChain provides many modules that can be used to build language model applications."),
    Document(page_content="The most important concept in LangChain is the Chain, which combines components to solve a task.")
]

# Create a vector store from documents
vectorstore = Chroma.from_documents(documents, embeddings)

# Alternatively, create from texts
texts = [doc.page_content for doc in documents]
metadatas = [{"source": f"document_{i}"} for i in range(len(texts))]
vectorstore = Chroma.from_texts(texts, embeddings, metadatas=metadatas)

# Persist to disk
vectorstore = Chroma.from_documents(
    documents, embeddings, persist_directory="./chroma_db"
)
vectorstore.persist()

# Load from disk
loaded_vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# Similarity search
query = "What is LangChain?"
docs = vectorstore.similarity_search(query, k=2)

# Similarity search with score
docs_and_scores = vectorstore.similarity_search_with_score(query, k=2)
```

### Pinecone

```python
from langchain.vectorstores import Pinecone
import pinecone

# Initialize Pinecone
pinecone.init(
    api_key="your-api-key",
    environment="your-environment"
)

# Create or get an index
index_name = "langchain-demo"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        name=index_name,
        dimension=1536,  # Dimension of OpenAI embeddings
        metric="cosine"
    )

# Get the index
index = pinecone.Index(index_name)

# Create a vector store
vectorstore = Pinecone.from_documents(documents, embeddings, index_name=index_name)

# Similarity search
query = "What is LangChain?"
docs = vectorstore.similarity_search(query, k=2)
```

### FAISS

```python
from langchain.vectorstores import FAISS

# Create a vector store
vectorstore = FAISS.from_documents(documents, embeddings)

# Save to disk
vectorstore.save_local("faiss_index")

# Load from disk
loaded_vectorstore = FAISS.load_local("faiss_index", embeddings)

# Similarity search
query = "What is LangChain?"
docs = vectorstore.similarity_search(query, k=2)

# Similarity search by vector
query_embedding = embeddings.embed_query(query)
docs = vectorstore.similarity_search_by_vector(query_embedding, k=2)
```

### Custom Vector Store

```python
from langchain.vectorstores.base import VectorStore
from langchain.docstore.document import Document
from typing import List, Dict, Any, Optional, Tuple
import numpy as np

class SimpleVectorStore(VectorStore):
    """A simple in-memory vector store."""
    
    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.vectors = []
        self.documents = []
    
    def add_texts(
        self,
        texts: List[str],
        metadatas: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any,
    ) -> List[str]:
        """Add texts to the vector store."""
        if metadatas is None:
            metadatas = [{} for _ in texts]
        
        # Create embeddings
        embeddings = self.embeddings.embed_documents(texts)
        
        # Store vectors and documents
        for i, (text, metadata, embedding) in enumerate(zip(texts, metadatas, embeddings)):
            self.vectors.append(embedding)
            self.documents.append(Document(page_content=text, metadata=metadata))
        
        # Return IDs (just use indices for simplicity)
        return [str(i) for i in range(len(self.vectors) - len(texts), len(self.vectors))]
    
    def similarity_search(
        self, query: str, k: int = 4, **kwargs: Any
    ) -> List[Document]:
        """Return documents most similar to the query."""
        # Create query embedding
        query_embedding = self.embeddings.embed_query(query)
        
        # Calculate similarities
        similarities = [self._cosine_similarity(query_embedding, vector) for vector in self.vectors]
        
        # Get top k indices
        indices = np.argsort(similarities)[-k:][::-1]
        
        # Return documents
        return [self.documents[i] for i in indices]
    
    def _cosine_similarity(self, a: List[float], b: List[float]) -> float:
        """Calculate cosine similarity between two vectors."""
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Use the custom vector store
simple_vectorstore = SimpleVectorStore(embeddings)
simple_vectorstore.add_texts(["Text 1", "Text 2", "Text 3"])
docs = simple_vectorstore.similarity_search("Query", k=2)
```

## Hybrid Search

```python
from langchain.retrievers import BM25Retriever, EnsembleRetriever

# Create a BM25 retriever for keyword search
bm25_retriever = BM25Retriever.from_documents(documents)
bm25_retriever.k = 5  # Return 5 documents

# Create a vector retriever for semantic search
vectorstore_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# Create an ensemble retriever that combines both
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vectorstore_retriever],
    weights=[0.5, 0.5]  # Equal weights
)

# Retrieve documents
docs = ensemble_retriever.get_relevant_documents("What is LangChain?")
```

## Next Steps

Continue to the [Retrieval-Augmented Generation (RAG)](../08_rag/README.md) section to learn how to use embeddings and vector stores for building RAG systems.