
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import AIMessage

from src.tools.web_search import web_search
from src.tools.wikipedia_search import wikipedia_search

load_dotenv()

tools = [web_search, wikipedia_search]

agent = create_agent(
    model="openai:gpt-4o-mini",
    tools=tools,
    system_prompt="""
        You are an AI research assistant.

        Tool selection rules:

        1. Use web_search for recent developments, current events,
           news, and latest technologies.

        2. Use wikipedia_search for definitions, historical
           information, and general concepts.

        3. Use multiple tools when a research question requires
           information from different sources.

        Provide clear and accurate answers based on retrieved information.
    """
)

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": (
                "Explain the history of artificial intelligence "
                "and discuss the latest developments in AI agents in 2026."
            )
        }
    ]
})



# print(response["messages"][-1].content)

print("\n========== MESSAGE FLOW ==========\n")

for message in response["messages"]:

    print("Message Type:", type(message).__name__)
    print("Content:", message.content)

    if isinstance(message, AIMessage) and message.tool_calls:
        print("Tool Calls:", message.tool_calls)

    print("-" * 50)
