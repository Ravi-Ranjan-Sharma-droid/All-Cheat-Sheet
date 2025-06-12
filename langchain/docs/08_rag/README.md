# Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) combines retrieval systems with generative models to produce outputs that are both relevant and accurate. This approach helps ground LLM responses in factual information and reduces hallucinations.

## Basic RAG Implementation

```python
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# 1. Load documents
loader = TextLoader("document.txt")
documents = loader.load()

# 2. Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_documents = text_splitter.split_documents(documents)

# 3. Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(split_documents, embeddings)

# 4. Create a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 5. Create a RAG chain
rag_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="stuff",  # Other options: "map_reduce", "refine", "map_rerank"
    retriever=retriever,
    verbose=True
)

# 6. Run the chain
query = "What is the main topic of the document?"
response = rag_chain.run(query)
print(response)
```

## Customizing the RAG Prompt

```python
from langchain.prompts import PromptTemplate

# Create a custom prompt template
prompt_template = """
You are an assistant that answers questions based on the provided context.

Context:
{context}

Question: {question}

Answer the question based only on the provided context. If the context doesn't contain the answer, say "I don't have enough information to answer this question."

Answer:
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# Create a RAG chain with the custom prompt
rag_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": PROMPT}
)
```

## Advanced RAG Techniques

### Map-Reduce Chain

Processes each document separately and then combines the results.

```python
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

# Map prompt (for processing individual documents)
map_template = """The following is a document: {document}

Based on this document, answer the question: {question}

If the document doesn't contain the answer, say "This document doesn't have the information."

Answer:"""
map_prompt = PromptTemplate(template=map_template, input_variables=["document", "question"])
map_chain = LLMChain(llm=OpenAI(temperature=0), prompt=map_prompt)

# Reduce prompt (for combining answers)
reduce_template = """The following are summaries from different documents: {document_summaries}

Based on these summaries, answer the question: {question}

Answer:"""
reduce_prompt = PromptTemplate(template=reduce_template, input_variables=["document_summaries", "question"])
reduce_chain = LLMChain(llm=OpenAI(temperature=0), prompt=reduce_prompt)

# Create the map-reduce chain
map_reduce_chain = MapReduceDocumentsChain(
    llm_chain=map_chain,
    reduce_documents_chain=reduce_chain,
    document_variable_name="document"
)

# Create a RAG chain with the map-reduce approach
rag_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="map_reduce",
    retriever=retriever,
    verbose=True
)
```

### Refine Chain

Processes documents sequentially, refining the answer with each document.

```python
from langchain.chains.question_answering import load_qa_chain

# Create a refine chain
refine_chain = load_qa_chain(
    llm=OpenAI(temperature=0),
    chain_type="refine",
    verbose=True
)

# Create a RAG chain with the refine approach
rag_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="refine",
    retriever=retriever,
    verbose=True
)
```

### Map-Rerank Chain

Processes each document separately and ranks the answers by relevance.

```python
# Create a RAG chain with the map-rerank approach
rag_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="map_rerank",
    retriever=retriever,
    verbose=True
)
```

## Conversational RAG

```python
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Create a memory object
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Create a conversational RAG chain
conversational_rag = ConversationalRetrievalChain.from_llm(
    llm=OpenAI(temperature=0),
    retriever=retriever,
    memory=memory,
    verbose=True
)

# First question
response = conversational_rag({"question": "What is the main topic of the document?"})
print(response["answer"])

# Follow-up question (the chain will use the chat history)
response = conversational_rag({"question": "Can you elaborate on that?"})
print(response["answer"])
```

## Custom RAG Implementation

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class CustomRAG:
    """Custom RAG implementation with hybrid retrieval."""
    
    def __init__(self, llm, retriever, embeddings):
        self.llm = llm
        self.retriever = retriever
        self.embeddings = embeddings
    
    def generate_response(self, query, use_hybrid=True):
        """Generate a response to the query using RAG."""
        # Retrieve relevant documents
        if use_hybrid:
            docs = self._hybrid_retrieval(query)
        else:
            docs = self.retriever.get_relevant_documents(query)
        
        # Format the documents
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # Create a prompt
        prompt_template = """
        You are an assistant that answers questions based on the provided context.
        
        Context:
        {context}
        
        Question: {question}
        
        Answer the question based only on the provided context. If the context doesn't contain the answer, say "I don't have enough information to answer this question."
        
        Answer:
        """
        
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        # Create a chain
        chain = LLMChain(llm=self.llm, prompt=prompt)
        
        # Run the chain
        response = chain.run(context=context, question=query)
        
        return response
    
    def _hybrid_retrieval(self, query, k=4):
        """Combine vector search with keyword search for better retrieval."""
        # Vector search
        vector_docs = self.retriever.get_relevant_documents(query)
        
        # Keyword search (simplified example)
        # In a real implementation, you would use a proper keyword search method
        keyword_docs = [doc for doc in self.retriever.get_relevant_documents(query) 
                       if any(keyword in doc.page_content.lower() 
                              for keyword in query.lower().split())]
        
        # Combine and deduplicate
        all_docs = vector_docs + keyword_docs
        unique_docs = []
        seen_content = set()
        
        for doc in all_docs:
            if doc.page_content not in seen_content:
                seen_content.add(doc.page_content)
                unique_docs.append(doc)
        
        # Return top k documents
        return unique_docs[:k]

# Use the custom RAG implementation
custom_rag = CustomRAG(
    llm=OpenAI(temperature=0),
    retriever=retriever,
    embeddings=embeddings
)

response = custom_rag.generate_response("What is the main topic of the document?")
print(response)
```

## RAG with Re-ranking

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

# Create a document compressor
compressor = LLMChainExtractor.from_llm(OpenAI(temperature=0))

# Create a contextual compression retriever
compression_retriever = ContextualCompressionRetriever(
    base_retriever=retriever,
    base_compressor=compressor
)

# Create a RAG chain with the compression retriever
rag_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    chain_type="stuff",
    retriever=compression_retriever,
    verbose=True
)
```

## Next Steps

Continue to the [LLM Integration](../09_llm_integration/README.md) section to learn how to integrate different LLM providers with LangChain.