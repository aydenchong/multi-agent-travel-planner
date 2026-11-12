from backend.app.core.llm import get_llm
from backend.app.tools.place_tools import search_places


def main():
    llm = get_llm()

    llm_with_tools = llm.bind_tools([search_places])

    questions = [
        "Hello! How are you?",
        "What are some attractions in Tokyo?"
    ]

    for question in questions:
        print(f"\nUSER: {question}")

        response = llm_with_tools.invoke(question)

        print("MODEL TEXT:", response.text)
        print("TOOL CALLS:", response.tool_calls)

        for tool_call in response.tool_calls:
            if tool_call["name"] == "search_places":
                result = search_places.invoke(
                    tool_call["args"]
                )
                print("TOOL RESULT:", result)


if __name__ == "__main__":
    main()
