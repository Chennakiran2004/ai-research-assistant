from dotenv import load_dotenv
from langchain_openai import ChatOpenAI 
from langchain_core.messages import ToolMessage

from src.tools.web_search import web_search

from langchain_core.messages import HumanMessage, ToolMessage

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

tools = [web_search]

llm_with_tools = llm.bind_tools(tools)
query = "what are the latest developments in RAG?"

response = llm_with_tools.invoke(query)

tool_call = response.tool_calls[0] 

result = web_search.invoke(tool_call["args"])

tool_message = ToolMessage(
    content=result,
    tool_call_id=tool_call["id"]
)

# print(tool_message)

messages = [
    HumanMessage(content=query),
    response,
    tool_message
]

final_response = llm_with_tools.invoke(messages)
print(final_response.content)