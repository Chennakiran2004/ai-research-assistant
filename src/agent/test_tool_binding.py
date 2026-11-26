
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from src.tools.web_search import web_search

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

llm_with_tools = llm.bind_tools([web_search])

response = llm_with_tools.invoke(
    "What are the latest developments in RAG?"
)

print(response)
print(response.tool_calls)
