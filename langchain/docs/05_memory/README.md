# Memory & Context

Memory components in LangChain allow chains and agents to retain information across multiple interactions, enabling more natural and contextual conversations.

## Basic Memory Types

### Conversation Buffer Memory

Stores all messages in a buffer and includes them in the prompt.

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.llms import OpenAI

# Initialize memory
memory = ConversationBufferMemory()

# Add messages to memory
memory.save_context({"input": "Hi, my name is Bob"}, {"output": "Hello Bob, nice to meet you"})

# Retrieve memory variables
print(memory.load_memory_variables({}))
# Output: {'history': 'Human: Hi, my name is Bob\nAI: Hello Bob, nice to meet you'}

# Use memory in a conversation chain
conversation = ConversationChain(
    llm=OpenAI(temperature=0),
    memory=ConversationBufferMemory(),
    verbose=True
)

# First interaction
response1 = conversation.predict(input="Hi, my name is Bob")

# Second interaction (the model remembers the name)
response2 = conversation.predict(input="What's my name?")
```

### Conversation Buffer Window Memory

Stores the last K messages in a buffer and includes them in the prompt.

```python
from langchain.memory import ConversationBufferWindowMemory

# Initialize memory with a window size of 2
memory = ConversationBufferWindowMemory(k=2)

# Add messages to memory
memory.save_context({"input": "Hi"}, {"output": "Hello"})
memory.save_context({"input": "How are you?"}, {"output": "I'm good"})
memory.save_context({"input": "What's the weather like?"}, {"output": "It's sunny"})

# Retrieve memory variables (only the last 2 interactions are included)
print(memory.load_memory_variables({}))
# Output: {'history': 'Human: How are you?\nAI: I'm good\nHuman: What's the weather like?\nAI: It's sunny'}

# Use in a conversation chain
conversation = ConversationChain(
    llm=OpenAI(temperature=0),
    memory=ConversationBufferWindowMemory(k=2),
    verbose=True
)
```

### Conversation Summary Memory

Summarizes the conversation history to keep the context concise.

```python
from langchain.memory import ConversationSummaryMemory

# Initialize memory
memory = ConversationSummaryMemory(llm=OpenAI(temperature=0))

# Add messages to memory
memory.save_context({"input": "Hi, my name is Bob"}, {"output": "Hello Bob, nice to meet you"})
memory.save_context({"input": "I'm a software engineer"}, {"output": "That's great! What kind of software do you work on?"})
memory.save_context({"input": "I work on web applications"}, {"output": "Interesting! What technologies do you use?"})

# Retrieve memory variables (a summary of the conversation)
print(memory.load_memory_variables({}))

# Use in a conversation chain
conversation = ConversationChain(
    llm=OpenAI(temperature=0),
    memory=ConversationSummaryMemory(llm=OpenAI(temperature=0)),
    verbose=True
)
```

### Vector Store-Backed Memory

Stores messages in a vector store and retrieves the most relevant ones based on the current input.

```python
from langchain.memory import VectorStoreRetrieverMemory
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Create embeddings
embeddings = OpenAIEmbeddings()

# Create a vector store
vectorstore = Chroma(embedding_function=embeddings, persist_directory="./chroma_db")

# Create a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Initialize memory
memory = VectorStoreRetrieverMemory(retriever=retriever)

# Add messages to memory
memory.save_context({"input": "My favorite food is pizza"}, {"output": "That's great! I like pizza too."})
memory.save_context({"input": "I love Italian cuisine"}, {"output": "Italian cuisine is known for its pasta and pizza."})
memory.save_context({"input": "I visited Rome last year"}, {"output": "Rome is the capital of Italy and has amazing food."})

# Retrieve relevant memories based on the current input
print(memory.load_memory_variables({"input": "What food do I like?"}))
```

## Custom Memory Class

```python
from langchain.memory.chat_message_histories import BaseChatMessageHistory
from langchain.schema import BaseMessage, HumanMessage, AIMessage
from typing import List
import json

class FileChatMessageHistory(BaseChatMessageHistory):
    """Chat message history that stores messages in a JSON file."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        try:
            with open(file_path, 'r') as f:
                self.messages = self._messages_from_dict(json.load(f))
        except (FileNotFoundError, json.JSONDecodeError):
            self.messages = []
    
    def add_message(self, message: BaseMessage) -> None:
        """Add a message to the history."""
        self.messages.append(message)
        with open(self.file_path, 'w') as f:
            json.dump(self._messages_to_dict(), f)
    
    def clear(self) -> None:
        """Clear the message history."""
        self.messages = []
        with open(self.file_path, 'w') as f:
            json.dump([], f)
    
    def _messages_to_dict(self):
        """Convert messages to a dictionary for serialization."""
        return [
            {"type": "human" if isinstance(m, HumanMessage) else "ai", "content": m.content}
            for m in self.messages
        ]
    
    def _messages_from_dict(self, data: List[dict]):
        """Convert dictionary to messages."""
        return [
            HumanMessage(content=m["content"]) if m["type"] == "human" else AIMessage(content=m["content"])
            for m in data
        ]

# Use the custom memory class
from langchain.memory import ConversationBufferMemory

# Initialize memory with custom message history
message_history = FileChatMessageHistory("chat_history.json")
memory = ConversationBufferMemory(chat_memory=message_history)

# Use in a conversation chain
conversation = ConversationChain(
    llm=OpenAI(temperature=0),
    memory=memory,
    verbose=True
)
```

## Memory Management Best Practices

### 1. Choose the Right Memory Type

```python
# For simple conversations
from langchain.memory import ConversationBufferMemory

# For long conversations (limited context)
from langchain.memory import ConversationBufferWindowMemory

# For summarizing long conversations
from langchain.memory import ConversationSummaryMemory
```

### 2. Clear Memory When Needed

```python
# Clear memory when changing topics
conversation.memory.clear()

# Selectively modify memory
conversation.memory.chat_memory.messages = conversation.memory.chat_memory.messages[-4:]
```

### 3. Use Entity Memory for Key Information

```python
from langchain.memory import ConversationEntityMemory

entity_memory = ConversationEntityMemory(llm=OpenAI(temperature=0))
conversation = ConversationChain(llm=OpenAI(temperature=0), memory=entity_memory)
```

## Next Steps

Continue to the [Document Loaders](../06_document_loaders/README.md) section to learn how to load and process documents from various sources.