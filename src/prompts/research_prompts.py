
from langchain_core.prompts import ChatPromptTemplate


research_report_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert research analyst.

        Your task is to analyze the research information
        provided to you and generate a structured research report.

        Follow these guidelines:

        1. Create a clear and meaningful title.
        2. Provide a concise summary.
        3. Extract the most important key findings.
        4. Include the relevant source URLs provided in the research.
        5. Write a conclusion based on the findings.

        Do not invent facts or sources.
        """
    ),
    (
        "human",
        """
        Research Topic:
        {topic}

        Research Information:
        {research_data}

        Generate a research report based on this information.
        """
    )
])



