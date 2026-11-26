
from pydantic import BaseModel, Field


class ResearchReport(BaseModel):
    title: str = Field(
        description="The title of the research report"
    )

    summary: str = Field(
        description="A brief overview of the research"
    )

    key_findings: list[str] = Field(
        description="The important findings discovered during research"
    )

    sources: list[str] = Field(
        description="The URLs of the sources used for research"
    )

    conclusion: str = Field(
        description="The final conclusion based on the research"
    )


# if __name__ == "__main__":

#     report = ResearchReport(
#         title="AI Agents in 2026",
#         summary="AI agents are becoming more autonomous.",
#         key_findings=[
#             "Multi-agent systems",
#             "Persistent agents",
#             "Edge deployment"
#         ],
#         sources=[
#             "https://example.com/article"
#         ],
#         conclusion="AI agents are transforming workflows."
#     )

#     print(report)
#     print(report.model_dump())
#     print(report.model_dump_json(indent=4))