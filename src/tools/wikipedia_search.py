from langchain_core.tools import tool
import wikipedia

@tool
def wikipedia_search(query : str) -> str:

    """

    Search Wikipedia for background information about a topic.
    Useful for understanding concepts, history, and genral knowledge

    """


    search_results = wikipedia.search(query)

    if not search_results:
        return "No Wikipedia results found."

    
    page_title = search_results[0]


    summary = wikipedia.summary(
        page_title,
        sentences=5,
        auto_suggest=False
    )

    return summary



if __name__ == "__main__":
    result = wikipedia_search.invoke({
        "query": "Retrieval Augmented Generation"
    })

    print(result)