from langchain.agents import create_agent

from backend.app.core.llm import get_llm
from backend.app.tools.place_tools import search_places


def create_research_agent():
    return create_agent(
        model=get_llm(),
        tools=[search_places],
        system_prompt=(
            "You are VoyageAI's Travel Research Agent. "
            "Help users explore destinations and attractions. "
            "Use search_places when you need attraction data. "
            "Do not call tools for ordinary greetings. "
            "The current search tool returns MOCK DATA only. "
            "Clearly label mock results and never present "
            "them as verified live travel information."
        ),
        name="research_agent",
    )
