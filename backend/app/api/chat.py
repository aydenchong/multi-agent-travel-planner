from fastapi import APIRouter

from backend.app.agents.research_agent import (
    create_research_agent,
)
from backend.app.schemas.chat import (
    ChatRequest,
    ChatResponse,
)


router = APIRouter(
    prefix="/api/v1",
    tags=["Chat"],
)


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    agent = create_research_agent()

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.message,
                }
            ]
        },
        config={"recursion_limit": 10},
    )

    final_message = result["messages"][-1]

    return ChatResponse(
        reply=final_message.text
    )
