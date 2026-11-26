from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from src.schemas.research_report import ResearchReport
from src.prompts.research_prompts import research_report_prompt

load_dotenv()

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

structured_llm = llm.with_structured_output(
    ResearchReport
)

research_chain = research_report_prompt | structured_llm


# if __name__ == "__main__":

#     result = research_chain.invoke({
#         "topic": "AI Agents",
#         "research_data": """
#         AI agents are systems that can perceive information,
#         make decisions, and execute tasks.

#         They can use external tools such as web search APIs.

#         Modern AI agents can use planning, memory,
#         and multiple tools to complete complex tasks.
#         """
#     })

#     print("\n========== RESEARCH REPORT ==========\n")

#     print(result)

#     print("\n========== PYTHON DICTIONARY ==========\n")

#     print(result.model_dump())

#     print("\n========== JSON OUTPUT ==========\n")

#     print(result.model_dump_json(indent=4))