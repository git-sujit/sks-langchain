# Option 1: Official Tavily SDK (tavily-python)
from dotenv import load_dotenv

load_dotenv(override=True)
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

# Create an LLM model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from sks-langchain => Search Agent!")
    result = agent.invoke({"messages": HumanMessage(content="Job search for AI engineers having expertise in LangChain, in Bay Area in the LinkedIn")})
    print(result)

if __name__ == "__main__":
    main()
