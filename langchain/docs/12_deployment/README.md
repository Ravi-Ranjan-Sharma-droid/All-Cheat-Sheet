# Deployment

This section covers various deployment options for LangChain applications, from local development to cloud-based solutions.

## Local Deployment with FastAPI

```python
# app.py
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

# Initialize FastAPI app
app = FastAPI(title="LangChain API")

# Initialize LangChain components
llm = OpenAI(temperature=0.7)
template = """You are a helpful assistant. Answer the following question: {question}"""
prompt = PromptTemplate(template=template, input_variables=["question"])
chain = LLMChain(llm=llm, prompt=prompt)

# Define request and response models
class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

# Define API endpoints
@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        # Run the chain
        response = chain.run(question=request.question)
        return AnswerResponse(answer=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

To run the FastAPI application:

```bash
pip install fastapi uvicorn
python app.py
```

Or using uvicorn directly:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## Docker Deployment

### Dockerfile

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### requirements.txt

```
langchain==0.0.267
openai==0.27.8
fastapi==0.103.1
uvicorn==0.23.2
pydantic==2.3.0
python-dotenv==1.0.0
```

### docker-compose.yml

```yaml
# docker-compose.yml
version: '3'

services:
  langchain-api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - .:/app
    restart: unless-stopped
```

To build and run the Docker container:

```bash
# Build the Docker image
docker build -t langchain-api .

# Run the container
docker run -p 8000:8000 -e OPENAI_API_KEY=your-api-key langchain-api
```

Or using Docker Compose:

```bash
docker-compose up -d
```

## Cloud Deployment

### AWS Lambda Deployment

```python
# lambda_function.py
import json
import os
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Initialize LangChain components
def initialize_chain():
    llm = OpenAI(temperature=0.7)
    template = """You are a helpful assistant. Answer the following question: {question}"""
    prompt = PromptTemplate(template=template, input_variables=["question"])
    return LLMChain(llm=llm, prompt=prompt)

# Lambda handler
def lambda_handler(event, context):
    try:
        # Parse request body
        body = json.loads(event.get('body', '{}'))
        question = body.get('question')
        
        if not question:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Question is required'})
            }
        
        # Initialize and run the chain
        chain = initialize_chain()
        response = chain.run(question=question)
        
        return {
            'statusCode': 200,
            'body': json.dumps({'answer': response})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
```

### Serverless Framework Configuration

```yaml
# serverless.yml
service: langchain-api

provider:
  name: aws
  runtime: python3.9
  region: us-east-1
  environment:
    OPENAI_API_KEY: ${env:OPENAI_API_KEY}

functions:
  ask:
    handler: lambda_function.lambda_handler
    events:
      - http:
          path: ask
          method: post
          cors: true

plugins:
  - serverless-python-requirements

custom:
  pythonRequirements:
    dockerizePip: true
    zip: true
    slim: true
```

To deploy using the Serverless Framework:

```bash
# Install Serverless Framework
npm install -g serverless

# Install plugins
npm install --save-dev serverless-python-requirements

# Deploy
sls deploy
```

## Streamlit Web App

```python
# app.py
import streamlit as st
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# Set page config
st.set_page_config(page_title="LangChain Chat App", page_icon="💬")

# Initialize session state for memory
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

# Initialize LangChain components
@st.cache_resource
def get_chain():
    llm = OpenAI(temperature=0.7)
    template = """You are a helpful assistant. 
    
    Current conversation:
    {chat_history}
    
    Human: {question}
    AI Assistant:"""
    prompt = PromptTemplate(template=template, input_variables=["chat_history", "question"])
    return LLMChain(
        llm=llm,
        prompt=prompt,
        memory=st.session_state.memory,
        verbose=True
    )

# App title
st.title("💬 LangChain Chat App")

# Display chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    chain = get_chain()
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chain.run(question=prompt)
            st.markdown(response)
    
    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with options
with st.sidebar:
    st.title("Options")
    
    # Clear conversation button
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.session_state.memory.clear()
        st.rerun()
    
    # About section
    st.markdown("---")
    st.markdown("# About")
    st.markdown("This is a simple chat application built with Streamlit and LangChain.")
    st.markdown("[View Source Code](https://github.com/yourusername/langchain-chat-app)")
```

To run the Streamlit app:

```bash
pip install streamlit
streamlit run app.py
```

## Monitoring and Logging

```python
import logging
from langchain.callbacks import StdOutCallbackHandler
from langchain.callbacks.tracers import LangChainTracer
from langchain.callbacks.tracers.langchain import wait_for_all_tracers
from langchain.llms import OpenAI

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create a custom callback handler for logging
class LoggingCallbackHandler(StdOutCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        logger.info(f"Starting LLM with prompts: {prompts}")
    
    def on_llm_end(self, response, **kwargs):
        logger.info(f"LLM response: {response}")
    
    def on_llm_error(self, error, **kwargs):
        logger.error(f"LLM error: {error}")
    
    def on_chain_start(self, serialized, inputs, **kwargs):
        logger.info(f"Starting chain with inputs: {inputs}")
    
    def on_chain_end(self, outputs, **kwargs):
        logger.info(f"Chain outputs: {outputs}")
    
    def on_chain_error(self, error, **kwargs):
        logger.error(f"Chain error: {error}")

# Initialize LangChain with callbacks
logger.info("Initializing LangChain components")

# Create callback handlers
callback_handlers = [
    LoggingCallbackHandler(),
    LangChainTracer()  # For LangSmith tracing (if configured)
]

# Initialize LLM with callbacks
llm = OpenAI(temperature=0.7, callbacks=callback_handlers)

# Example usage
try:
    logger.info("Running LLM")
    response = llm("Tell me a joke about programming")
    logger.info(f"LLM response received: {response}")
except Exception as e:
    logger.error(f"Error running LLM: {e}")
finally:
    # Wait for all tracers to finish
    wait_for_all_tracers()
```

## Performance Optimization

```python
from langchain.cache import InMemoryCache, RedisCache
from langchain.globals import set_llm_cache
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import redis
import time

# Option 1: In-memory cache
set_llm_cache(InMemoryCache())

# Option 2: Redis cache
# redis_client = redis.Redis.from_url("redis://localhost:6379")
# set_llm_cache(RedisCache(redis_client))

# Initialize LLM
llm = OpenAI(temperature=0)

# Measure performance
def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

# First call (no cache)
query = "What is the capital of France?"
response1, time1 = measure_execution_time(llm, query)
print(f"First call (no cache): {time1:.2f} seconds")

# Second call (with cache)
response2, time2 = measure_execution_time(llm, query)
print(f"Second call (with cache): {time2:.2f} seconds")
print(f"Speed improvement: {time1/time2:.2f}x faster")

# Streaming for better user experience
streaming_llm = OpenAI(
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=0
)

print("\nStreaming response:")
streaming_llm("Write a short poem about artificial intelligence.")
```

## Error Handling and Retry Logic

```python
from langchain.llms import OpenAI
from langchain.schema import OutputParserException
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List
import time
import json

# Define the output schema
class Recipe(BaseModel):
    name: str = Field(description="Name of the recipe")
    ingredients: List[str] = Field(description="List of ingredients")
    steps: List[str] = Field(description="Steps to prepare the recipe")

# Initialize the output parser
parser = PydanticOutputParser(pydantic_object=Recipe)

# Initialize LLM
llm = OpenAI(temperature=0.7)

# Function to generate and parse with retry logic
def generate_with_retry(prompt, max_retries=3, backoff_factor=2):
    retries = 0
    while retries <= max_retries:
        try:
            # Generate response
            response = llm(prompt)
            
            # Try to parse the response
            parsed_response = parser.parse(response)
            return parsed_response
        
        except OutputParserException as e:
            retries += 1
            if retries <= max_retries:
                # Log the error
                print(f"Attempt {retries} failed: {e}")
                
                # Add more specific instructions for the retry
                prompt += "\n\nPlease make sure to respond with a valid JSON object that includes 'name', 'ingredients', and 'steps' fields. The 'ingredients' and 'steps' should be lists of strings."
                
                # Wait before retrying (exponential backoff)
                wait_time = backoff_factor ** retries
                print(f"Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
            else:
                print(f"Failed after {max_retries} retries.")
                # Fallback: Try to extract whatever we can from the response
                return fallback_parser(response)
        
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

# Fallback parser for when all retries fail
def fallback_parser(text):
    try:
        # Try to find JSON-like content
        start_idx = text.find('{')
        end_idx = text.rfind('}')
        
        if start_idx >= 0 and end_idx > start_idx:
            json_str = text[start_idx:end_idx+1]
            data = json.loads(json_str)
            
            # Create a Recipe with whatever fields we could extract
            return Recipe(
                name=data.get("name", "Unknown Recipe"),
                ingredients=data.get("ingredients", ["Could not parse ingredients"]),
                steps=data.get("steps", ["Could not parse steps"])
            )
        else:
            # If no JSON-like content, create a minimal Recipe
            return Recipe(
                name="Parsing Failed",
                ingredients=["Could not parse ingredients"],
                steps=["Could not parse steps"]
            )
    except:
        # Last resort fallback
        return Recipe(
            name="Parsing Failed",
            ingredients=["Could not parse ingredients"],
            steps=["Could not parse steps"]
        )

# Example usage
prompt = f"""Generate a recipe for a chocolate cake.

{parser.get_format_instructions()}
"""

recipe = generate_with_retry(prompt)
print("\nParsed Recipe:")
print(f"Name: {recipe.name}")
print("Ingredients:")
for ingredient in recipe.ingredients:
    print(f"- {ingredient}")
print("Steps:")
for i, step in enumerate(recipe.steps, 1):
    print(f"{i}. {step}")
```

## Next Steps

Continue to the [Best Practices](../13_best_practices/README.md) section to learn about best practices for building LangChain applications.