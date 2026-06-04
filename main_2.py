# Option 2: LangChain integration (langchain-tavily) — recommended for LangChain agents
from dotenv import load_dotenv

load_dotenv(override=True)
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

search_tool = TavilySearch(max_results=3)

# Create an LLM model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [search_tool]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from sks-langchain => Search Agent!")
    result = agent.invoke({"messages": HumanMessage(content="Job search for AI engineers having expertise in LangChain, in Bay Area in the LinkedIn")})
    print(result)

if __name__ == "__main__":
    main()
