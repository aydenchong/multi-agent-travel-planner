
from langchain_core.messages import AIMessage, ToolMessage

from backend.app.agents.research_agent import (
    create_research_agent,
)


def main():
    agent = create_research_agent()

    questions = [
        "Hello! Who are you?",
        "What are some attractions in Tokyo?"
    ]

    for question in questions:
        print("\n" + "=" * 60)
        print("USER:", question)

        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question,
                    }
                ]
            },
            config={"recursion_limit": 10},
        )

        print("\nEXECUTION TRACE:")

        for message in result["messages"]:
            if isinstance(message, AIMessage):
                if message.tool_calls:
                    for call in message.tool_calls:
                        print(
                            f"[LLM TOOL CALL] "
                            f"{call['name']}({call['args']})"
                        )

            elif isinstance(message, ToolMessage):
                print(
                    f"[TOOL RESULT] {message.content}"
                )

        final_message = result["messages"][-1]

        print("\nFINAL ANSWER:")
        print(final_message.text)


if __name__ == "__main__":
    main()
