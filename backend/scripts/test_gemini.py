from backend.app.core.llm import get_llm


def main():
    print("Connecting to Gemini...")

    llm = get_llm()

    response = llm.invoke(
        "You are VoyageAI, a travel assistant. "
        "Introduce yourself in one short sentence."
    )

    print("\nGemini Response:")
    print(response.text)


if __name__ == "__main__":
    main()
