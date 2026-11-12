from langchain.tools import tool


@tool
def search_places(city: str) -> str:
    """Search tourist attractions in a city.

    Use this tool when the user asks about attractions
    or places to visit in a destination.

    Do not use it for greetings or general conversation.
    """
    print(f"[TOOL EXECUTED] search_places(city={city})")

    mock_places = {
        "tokyo": [
            "Senso-ji Temple",
            "Akihabara",
            "Shibuya Crossing"
        ],
        "osaka": [
            "Osaka Castle",
            "Dotonbori",
            "Universal Studios Japan"
        ]
    }

    places = mock_places.get(city.lower())

    if places is None:
        return f"No mock attraction data available for {city}."

    return (
        f"MOCK DATA ONLY - attractions in {city}: "
        + ", ".join(places)
    )
