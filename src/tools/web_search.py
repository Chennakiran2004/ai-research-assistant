from tavily import TavilyClient
from dotenv import load_dotenv

from langchain_core.tools import tool
import json

load_dotenv()

client = TavilyClient()

# response = client.search(
#     query="What is the capital of France?",
# )

# print(response)

@tool
def web_search(query: str) -> str:
    """
    Search the internet for current information about a given topic.
    Useful for researching topics and finding recent information.
    """

    response = client.search(
        query=query,
        max_results=5,
    )

    return json.dumps(
        response["results"],
        ensure_ascii=False
    )
    


# if __name__ == "__main__":
#     result = web_search.invoke({
#         "query": "Latest developments in RAG"
#     })

#     print(result)