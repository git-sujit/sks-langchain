from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from langchain_ollama import ChatOllama


def main():
    print("Hello from langchain-course, Sujit K Singh!")
    
    # Validate the API key
    key = validate_openai_key()

    # Create the information
    information = """
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and former public official known for his leadership of Tesla and SpaceX. 
    Musk has been the wealthiest person in the world since 2025; as of June 2026, Forbes estimates his net worth to be US$834 billion. 
    Born into the wealthy Musk family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. 
    He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. 
    In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. 
    Musk also became an American citizen in 2002. In 2002, Musk founded the space technology company SpaceX, becoming its CEO and chief engineer; 
    the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined the automaker Tesla as an early investor in 2004 and became its CEO and product architect in 2008; 
    it has since become a leader in electric vehicles. In 2015, he co-founded OpenAI to advance artificial intelligence (AI) research, but later left; growing discontent with the organization's direction 
    and leadership in the AI boom in the 2020s led him to establish xAI, which became a subsidiary of SpaceX in 2026. In 2022, he acquired the social network Twitter, implementing significant changes, 
    and rebranding it as X in 2023. His other businesses include the neurotechnology company Neuralink, which he co-founded in 2016, and the tunneling company the Boring Company, which he founded in 2017. 
    In November 2025, Tesla approved a pay package worth $1 trillion for Musk, which he is to receive over 10 years if he meets specific goals. Musk is a supporter of global far-right politics, figures, and political parties.
    He was the largest donor in the 2024 U.S. presidential election, where he supported Donald Trump. After Trump was inaugurated as president in January 2025, Musk served as Senior Advisor to the President and as the de facto head of the Department of Government Efficiency (DOGE). 
    Shortly before a public feud with Trump, Musk left the Trump administration in May 2025 and returned to managing his companies. Musk's political activities, statements and views have made him a polarizing figure. 
    He has been criticized for making unscientific and misleading statements, including spreading COVID-19 misinformation, promoting conspiracy theories, and affirming antisemitic, racist, and transphobic comments. 
    His acquisition of Twitter was controversial due to a subsequent increase in hate speech and the spread of misinformation on the service, following his pledge to decrease censorship. 
    His role in the second Trump administration attracted public backlash, particularly in response to DOGE.
    """

    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        template=summary_template, input_variables=["information"]
        )

    # Create an LLM model
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    #llm = ChatOllama(model="gemma3:270m", temperature=0)
    # Create a chain that combines the prompt template and the LLM using the | operator
    chain = summary_prompt_template | llm
    # Invoke the chain with the information
    response = chain.invoke({"information": information})
    print(response.content)

def validate_openai_key() -> str:
    #"""Validates OPENAI_API_KEY from .env and returns it if valid."""
    load_dotenv(override=True)
    
    key = os.getenv("OPENAI_API_KEY")
    
    if key is None:
        raise ValueError("OPENAI_API_KEY is not set in .env file")
    
    if not key.startswith("sk-"):
        raise ValueError(f"OPENAI_API_KEY must start with 'sk-', got: {key[:5]}...")
    
    if len(key) < 40:
        raise ValueError(f"OPENAI_API_KEY too short ({len(key)} chars), likely truncated")
    
    print(f"✅ OPENAI_API_KEY valid — length: {len(key)}, ends with: ...{key[-4:]}")
    return key

if __name__ == "__main__":
    main()
