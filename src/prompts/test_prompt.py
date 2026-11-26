
from src.prompts.research_prompts import research_report_prompt

prompt_value = research_report_prompt.invoke({
    "topic": "AI Agents",
    "research_data": "AI agents use tools to perform tasks. "
                     "They can plan and execute multiple steps."
})

print(prompt_value)
