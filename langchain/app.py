from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
import os
import uvicorn

# LangChain imports
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain, RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader, DirectoryLoader

# Initialize FastAPI app
app = FastAPI(title="LangChain API", version="1.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check for API key
if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Initialize LLM
llm = ChatOpenAI(temperature=0.7)

# Initialize memory
memory = ConversationBufferMemory(return_messages=True)

# Initialize conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# Initialize vector store if data directory exists
vector_store = None
if os.path.exists("data"):
    try:
        # Load documents
        loader = DirectoryLoader("data", glob="**/*.txt")
        documents = loader.load()
        
        # Split documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        texts = text_splitter.split_documents(documents)
        
        # Create vector store
        embeddings = OpenAIEmbeddings()
        vector_store = Chroma.from_documents(texts, embeddings, persist_directory="chroma_db")
        
        # Initialize retrieval QA chain
        retrieval_qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever()
        )
    except Exception as e:
        print(f"Error initializing vector store: {e}")

# Request models
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = "default"

class QueryRequest(BaseModel):
    query: str

class HealthResponse(BaseModel):
    status: str
    version: str

# Routes
@app.get("/health", response_model=HealthResponse)
async def health_check():
    return {"status": "healthy", "version": app.version}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = conversation.predict(input=request.message)
        return {"response": response, "session_id": request.session_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
async def query(request: QueryRequest):
    if not vector_store:
        raise HTTPException(status_code=400, detail="Vector store not initialized")
    
    try:
        response = retrieval_qa.run(request.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# AWS Lambda handler
def lambda_handler(event, context):
    # Simple Lambda handler for AWS deployment
    message = event.get("message", "")
    session_id = event.get("session_id", "default")
    
    response = conversation.predict(input=message)
    
    return {
        "statusCode": 200,
        "body": {
            "response": response,
            "session_id": session_id
        }
    }

# Run the app
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)