# LLM Integration

LangChain supports integration with various LLM providers. This section covers how to use different LLM providers with LangChain, including configuration options and best practices.

## OpenAI Integration

```python
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import os

# Set your API key
os.environ["OPENAI_API_KEY"] = "your-api-key"

# Initialize a text completion model
llm = OpenAI(
    model_name="text-davinci-003",  # or "gpt-3.5-turbo-instruct"
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Use the model
response = llm("Explain quantum computing in simple terms")
print(response)

# Initialize a chat model
chat_model = ChatOpenAI(
    model_name="gpt-3.5-turbo",  # or "gpt-4"
    temperature=0.7,
    max_tokens=256
)

# Use the chat model with messages
from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant that explains complex concepts in simple terms."),
    HumanMessage(content="Explain quantum computing in simple terms")
]

response = chat_model(messages)
print(response.content)
```

## Anthropic Integration

```python
from langchain.llms import Anthropic
from langchain.chat_models import ChatAnthropic
import os

# Set your API key
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

# Initialize a text completion model
llm = Anthropic(
    model="claude-2",
    temperature=0.7,
    max_tokens_to_sample=256
)

# Use the model
response = llm("Explain quantum computing in simple terms")
print(response)

# Initialize a chat model
chat_model = ChatAnthropic(
    model="claude-2",
    temperature=0.7,
    max_tokens_to_sample=256
)

# Use the chat model with messages
from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant that explains complex concepts in simple terms."),
    HumanMessage(content="Explain quantum computing in simple terms")
]

response = chat_model(messages)
print(response.content)
```

## Hugging Face Integration

```python
from langchain.llms import HuggingFaceHub
import os

# Set your API key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your-api-token"

# Initialize a model from Hugging Face Hub
llm = HuggingFaceHub(
    repo_id="google/flan-t5-xxl",  # or any other model on Hugging Face
    model_kwargs={
        "temperature": 0.7,
        "max_length": 256
    }
)

# Use the model
response = llm("Explain quantum computing in simple terms")
print(response)
```

## Local Models with Ollama

```python
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Initialize Ollama with streaming
llm = Ollama(
    model="llama2",  # or any other model you have pulled in Ollama
    temperature=0.7,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

# Use the model with streaming output
response = llm("Explain quantum computing in simple terms")

# Initialize Ollama for chat
from langchain.chat_models import ChatOllama

chat_model = ChatOllama(model="llama2")

# Use the chat model with messages
from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant that explains complex concepts in simple terms."),
    HumanMessage(content="Explain quantum computing in simple terms")
]

response = chat_model(messages)
print(response.content)
```

## Azure OpenAI Integration

```python
from langchain.llms import AzureOpenAI
from langchain.chat_models import AzureChatOpenAI
import os

# Set your Azure OpenAI credentials
os.environ["AZURE_OPENAI_API_KEY"] = "your-api-key"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://your-endpoint.openai.azure.com"

# Initialize a text completion model
llm = AzureOpenAI(
    deployment_name="your-text-deployment-name",
    model_name="text-davinci-003",
    temperature=0.7,
    max_tokens=256
)

# Use the model
response = llm("Explain quantum computing in simple terms")
print(response)

# Initialize a chat model
chat_model = AzureChatOpenAI(
    deployment_name="your-chat-deployment-name",
    model_name="gpt-35-turbo",
    temperature=0.7,
    max_tokens=256
)

# Use the chat model with messages
from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant that explains complex concepts in simple terms."),
    HumanMessage(content="Explain quantum computing in simple terms")
]

response = chat_model(messages)
print(response.content)
```

## Google Vertex AI Integration

```python
from langchain.llms import VertexAI
from langchain.chat_models import ChatVertexAI
import os

# Set up Google Cloud authentication
# You need to have the Google Cloud SDK installed and configured
# or set the GOOGLE_APPLICATION_CREDENTIALS environment variable

# Initialize a text completion model
llm = VertexAI(
    model_name="text-bison",
    temperature=0.7,
    max_output_tokens=256
)

# Use the model
response = llm("Explain quantum computing in simple terms")
print(response)

# Initialize a chat model
chat_model = ChatVertexAI(
    model_name="chat-bison",
    temperature=0.7,
    max_output_tokens=256
)

# Use the chat model with messages
from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant that explains complex concepts in simple terms."),
    HumanMessage(content="Explain quantum computing in simple terms")
]

response = chat_model(messages)
print(response.content)
```

## Custom LLM Integration

You can create a custom LLM wrapper for any model API:

```python
from langchain.llms.base import LLM
from typing import Any, List, Mapping, Optional
import requests

class CustomLLM(LLM):
    """Custom LLM wrapper for an external API."""
    
    api_url: str
    api_key: str
    
    @property
    def _llm_type(self) -> str:
        return "custom"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        """Call the external API."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "prompt": prompt,
            "max_tokens": 256,
            "temperature": 0.7
        }
        
        if stop:
            data["stop"] = stop
        
        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()
        
        return response.json()["output"]
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"api_url": self.api_url}

# Use the custom LLM
custom_llm = CustomLLM(
    api_url="https://your-api-endpoint.com/generate",
    api_key="your-api-key"
)

response = custom_llm("Explain quantum computing in simple terms")
print(response)
```

## LLM Caching

```python
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache
import langchain

# Set up in-memory cache
set_llm_cache(InMemoryCache())

# Or use Redis cache
from langchain.cache import RedisCache
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)
set_llm_cache(RedisCache(redis_client))

# Now, identical LLM calls will use the cache
llm = OpenAI(temperature=0)

# First call (will call the API)
response1 = llm("What is the capital of France?")

# Second call (will use the cache)
response2 = llm("What is the capital of France?")

# You can also disable caching for specific calls
response3 = llm("What is the capital of France?", cache=False)
```

## Streaming Responses

```python
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Initialize the model with streaming
llm = OpenAI(
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=0
)

# The response will be streamed to stdout
llm("Write a short poem about artificial intelligence.")

# Custom streaming handler
from langchain.callbacks.base import BaseCallbackHandler

class CustomStreamingHandler(BaseCallbackHandler):
    def __init__(self):
        self.text = ""
        
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        # Process each token as it comes
        print(f"Token: {token}")

# Use the custom handler
handler = CustomStreamingHandler()
llm = OpenAI(
    streaming=True,
    callbacks=[handler],
    temperature=0
)

llm("Write a short poem about artificial intelligence.")

# Access the full generated text
print(f"\nFull text: {handler.text}")
```

## Next Steps

Continue to the [Agents](../10_agents/README.md) section to learn how to create autonomous agents that can use tools and make decisions.