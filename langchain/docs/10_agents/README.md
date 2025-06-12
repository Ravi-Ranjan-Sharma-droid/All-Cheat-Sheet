# Agents

LangChain agents are autonomous systems that use LLMs to determine which actions to take and in what order. Agents can use tools, maintain state, and adapt to user inputs.

## Basic Agent Setup

```python
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

# Initialize the LLM
llm = OpenAI(temperature=0)

# Load tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Initialize the agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent
agent.run("What was the high temperature in SF yesterday? What is that number raised to the 0.023 power?")
```

## Available Agent Types

```python
from langchain.agents import AgentType

# Zero-shot ReAct agent (uses ReAct prompting to determine actions)
zero_shot_agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Structured chat agent (better for chat applications)
structured_chat_agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# OpenAI Functions agent (uses OpenAI's function calling capability)
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI(temperature=0)
openai_functions_agent = initialize_agent(
    tools,
    chat_model,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# ReAct agent with memory
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(memory_key="chat_history")
react_agent_with_memory = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)
```

## Custom Tools

```python
from langchain.agents import Tool
from langchain.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field

# Simple function-based tool
def get_weather(location: str) -> str:
    """Get the current weather in a given location"""
    # In a real implementation, you would call a weather API here
    return f"The weather in {location} is sunny and 75 degrees Fahrenheit."

weather_tool = Tool(
    name="Weather",
    func=get_weather,
    description="Useful for getting the current weather in a given location"
)

# Class-based tool with schema
class CalculatorInput(BaseModel):
    """Input for the calculator tool."""
    expression: str = Field(description="Mathematical expression to evaluate")

class Calculator(BaseTool):
    """Tool that evaluates mathematical expressions."""
    name = "calculator"
    description = "Useful for evaluating mathematical expressions"
    args_schema: Type[BaseModel] = CalculatorInput
    
    def _run(self, expression: str) -> str:
        """Evaluate a mathematical expression."""
        try:
            return str(eval(expression))
        except Exception as e:
            return f"Error evaluating expression: {e}"
    
    async def _arun(self, expression: str) -> str:
        """Asynchronously evaluate a mathematical expression."""
        return self._run(expression)

# Create a custom tool
calculator_tool = Calculator()

# Use custom tools with an agent
custom_tools = [weather_tool, calculator_tool]

agent = initialize_agent(
    custom_tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("What's the weather in San Francisco? Also, what is 15 * 27?")
```

## Agent with Custom Prompt

```python
from langchain.agents import ZeroShotAgent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain

# Define a custom prompt
prefix = """You are an AI assistant that helps users find information and solve problems.

You have access to the following tools:"""

suffix = """Begin!

Previous conversation history:
{chat_history}

New question: {input}
{agent_scratchpad}"""

# Format the prompt
prompt = ZeroShotAgent.create_prompt(
    tools,
    prefix=prefix,
    suffix=suffix,
    input_variables=["input", "chat_history", "agent_scratchpad"]
)

# Set up memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Create the LLM chain
llm_chain = LLMChain(llm=llm, prompt=prompt)

# Create the agent
agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True
)

# Run the agent
agent_executor.run("What's the weather in New York?")
```

## Agent with Tool Retrieval

```python
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools.retriever import create_retriever_tool
from langchain.retrievers import TavilySearchAPIRetriever

# Create a retriever tool
retriever = TavilySearchAPIRetriever()
retriever_tool = create_retriever_tool(
    retriever,
    "search",
    "Search for information on the web. Use this tool whenever you need to answer questions about current events or the current state of the world."
)

# Create a list of tools
tools = [retriever_tool]

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use the tools provided to answer the user's question."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# Create an agent
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run the agent
agent_executor.run("What's the latest news about artificial intelligence?")
```

## Plan-and-Execute Agent

```python
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

# Initialize the LLM
llm = ChatOpenAI(temperature=0)
planner = ChatOpenAI(temperature=0)

# Load tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Initialize the agent
agent = initialize_agent(
    tools,
    llm,
    planner=planner,
    agent=AgentType.PLAN_AND_EXECUTE,
    verbose=True
)

# Run the agent
agent.run(
    "Find the current temperature in San Francisco. Then calculate what temperature would be if it increased by 15%."
)
```

## Multi-Agent System

```python
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.prompts import MessagesPlaceholder

# Initialize LLMs for different agents
researcher_llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
writer_llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")
critic_llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

# Create the researcher agent
researcher_tools = load_tools(["serpapi", "tavily-search"], llm=researcher_llm)
researcher_agent = initialize_agent(
    researcher_tools,
    researcher_llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# Create a tool that uses the researcher agent
def research(query):
    return researcher_agent.run(query)

research_tool = Tool(
    name="Research",
    func=research,
    description="Useful for researching information on a topic. Input should be a search query."
)

# Create the writer agent
writer_system_message = SystemMessage(
    content="You are a creative writer who creates content based on research provided. "
            "Craft engaging and informative content."
)

writer_prompt = ChatPromptTemplate.from_messages([
    writer_system_message,
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

writer_agent = initialize_agent(
    [research_tool],
    writer_llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    prompt=writer_prompt,
    verbose=True
)

# Create a tool that uses the writer agent
def write_content(topic):
    return writer_agent.run(f"Write a comprehensive article about {topic}")

write_tool = Tool(
    name="WriteContent",
    func=write_content,
    description="Useful for writing content on a topic. Input should be a topic to write about."
)

# Create the critic agent
critic_system_message = SystemMessage(
    content="You are a critical editor who reviews content for accuracy, clarity, and engagement. "
            "Provide constructive feedback to improve the content."
)

critic_prompt = ChatPromptTemplate.from_messages([
    critic_system_message,
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

critic_agent = initialize_agent(
    [],
    critic_llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    prompt=critic_prompt,
    verbose=True
)

# Create a tool that uses the critic agent
def review_content(content):
    return critic_agent.run(f"Review this content and provide feedback: {content}")

review_tool = Tool(
    name="ReviewContent",
    func=review_content,
    description="Useful for reviewing and improving content. Input should be the content to review."
)

# Create the main agent that orchestrates the process
main_tools = [research_tool, write_tool, review_tool]

main_system_message = SystemMessage(
    content="You are a content production manager. Your job is to produce high-quality content "
            "on a given topic by coordinating research, writing, and review processes."
)

main_prompt = ChatPromptTemplate.from_messages([
    main_system_message,
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

main_agent = initialize_agent(
    main_tools,
    ChatOpenAI(temperature=0),
    agent=AgentType.OPENAI_FUNCTIONS,
    prompt=main_prompt,
    verbose=True
)

# Run the multi-agent system
main_agent.run("Create content about the impact of artificial intelligence on healthcare")
```

## Agent Supervision

```python
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner

# Initialize the LLM
planner = ChatOpenAI(temperature=0)
executor = ChatOpenAI(temperature=0)

# Load tools
tools = load_tools(["serpapi", "llm-math"], llm=executor)

# Create the planner and executor
planner_agent = load_chat_planner(planner)
executor_agent = load_agent_executor(executor, tools, verbose=True)

# Create the supervised agent
supervised_agent = PlanAndExecute(
    planner=planner_agent,
    executor=executor_agent,
    verbose=True
)

# Run the agent
supervised_agent.run(
    "Find the current temperature in San Francisco. Then calculate what temperature would be if it increased by 15%."
)
```

## Next Steps

Continue to the [Evaluation](../11_evaluation/README.md) section to learn how to evaluate the performance of your LangChain applications.