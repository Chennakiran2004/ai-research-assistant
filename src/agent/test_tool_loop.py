
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, ToolMessage

from src.tools.web_search import web_search

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

tools = [web_search]

llm_with_tools = llm.bind_tools(tools)

tool_map = {
    tool.name: tool
    for tool in tools
}

query = "What are the latest developments in RAG?"

messages = [HumanMessage(content=query)]

response = llm_with_tools.invoke(messages)

messages.append(response)

for tool_call in response.tool_calls:

    tool = tool_map[tool_call["name"]]

    result = tool.invoke(tool_call["args"])

    tool_message = ToolMessage(
        content=result,
        tool_call_id=tool_call["id"]
    )

    messages.append(tool_message)

final_response = llm_with_tools.invoke(messages)

print(final_response.content)
