
from src.agent.research_agent import conduct_research
from src.chains.research_chain import research_chain
from src.utils.report_saver import save_report_json


def generate_research_report(topic: str):

    research_data = conduct_research(topic)

    report = research_chain.invoke({
        "topic": topic,
        "research_data": research_data
    })

    report_path = save_report_json(report)

    return report

