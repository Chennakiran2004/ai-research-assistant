
from dotenv import load_dotenv
from langchain.agents import create_agent

from src.tools.web_search import web_search
from src.tools.wikipedia_search import wikipedia_search

load_dotenv()


tools = [
    web_search,
    wikipedia_search
]


agent = create_agent(
    model="openai:gpt-4o-mini",
    tools=tools,
    system_prompt="""
    You are an AI research assistant.

    1. Use web_search for recent developments,
       current events, and latest technologies.

    2. Use wikipedia_search for definitions,
       historical information, and general concepts.

    3. Use multiple tools when necessary.

    4. Collect useful research information and source URLs.

    5. Do not invent facts or sources.

    Provide comprehensive research information.
    """
)


def conduct_research(topic: str) -> str:

    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"Research this topic thoroughly: {topic}"
            }
        ]
    })

    return response["messages"][-1].content
