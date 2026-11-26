from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from src.tools.web_search import web_search

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

tools = [web_search]

llm_with_tools = llm.bind_tools(tools)

response = llm_with_tools.invoke(
    "What are the latest development in RAG?"
)

for tool_call in response.tool_calls:
    if tool_call["name"] == "web_search":

        result = web_search.invoke(
            tool_call["args"]
        )

        print("Tool Result:")
        print(result)