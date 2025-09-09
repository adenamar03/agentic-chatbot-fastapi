# AI Agent Chatbot with FastAPI, LangGraph, Langchain

# Step #1: Set up API keys for Groq, OpenAI, and Tavily
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Step #2: Setup LLMs and the tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage, SystemMessage  

openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

# Extract max 2 results from search
search_tool = TavilySearch(max_results=2)

# Step #3: Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent

# Define the system prompt
system_prompt = "Act as an AI chatbot who is smart and friendly"

agent = create_react_agent(
    model=groq_llm,
    tools=[search_tool]
)


query = "Tell me about the trend in crypto markets"
state = {
    "messages": [
        SystemMessage(content=system_prompt),  
        HumanMessage(content=query)  # User query as HumanMessage
    ]
}
response = agent.invoke(state)
print(response['messages'][-1].content)