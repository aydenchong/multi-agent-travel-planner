from langchain_google_genai import ChatGoogleGenerativeAI

from backend.app.core.config import get_settings

def get_llm() -> ChatGoogleGenerativeAI:
    settings = get_settings()

    if not settings.gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not configured")

    return ChatGoogleGenerativeAI(
        model=settings.gemini_model,
        api_key=settings.gemini_api_key,
        temperature=0,
        max_retries=2,
    )
