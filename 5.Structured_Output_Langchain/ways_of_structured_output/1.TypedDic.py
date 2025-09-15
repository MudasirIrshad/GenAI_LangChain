

# LETS UNDERSTAND THIS WITH SIMPLE EXAMPLE FIRST THAN WE WILL GO TOWARDS LLM MODELS

# class Person(TypedDict):
#     name: str
#     age: int


# new_person: Person = {
#     'name':"Mudasir",
#     'age': 24
# }


from typing import TypedDict, Annotated, Optional, Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review(TypedDict):
    key_themes: Annotated[
        list[str],
        "List of the main themes or aspects discussed in the review (e.g., battery, design, performance)"
    ]

    summary: Annotated[
        str,
        "A concise summary (2–3 sentences) of the overall review"
    ]

    sentiment: Annotated[
        Literal["pos", "neg", "neu", "mix"],
        "Overall sentiment of the review: pos, neg, neu, or mix"
    ]

    pros: Annotated[
        Optional[list[str]],
        "List of all positive aspects mentioned in the review"
    ]

    cons: Annotated[
        Optional[list[str]],
        "List of all negative aspects mentioned in the review"
    ]

    rating: Annotated[
        Optional[float],
        "Overall rating of the product from 1.0 to 5.0 if it can be inferred, else None"
    ]

    target_audience: Annotated[
        Optional[str],
        "Who this product is most suitable for (e.g., students, gamers, professionals)"
    ]

    tone: Annotated[
        Optional[Literal["formal", "casual", "enthusiastic", "critical"]],
        "The overall tone of the review"
    ]


structured_model = model.with_structured_output(Review) # pyright: ignore[reportArgumentType]
result = structured_model.invoke("""
The new ultrabook is a fascinating mix of strengths and compromises. Its lightweight design and sleek aluminum chassis make it easy to carry for daily commutes, while the vibrant display provides crisp visuals for work and entertainment. Battery life extends well beyond a typical workday, though the advertised “20 hours” is a stretch in real-world usage. Performance on productivity tasks is excellent, but the integrated graphics struggle with heavy creative workloads or modern AAA games. The keyboard has satisfying travel, but the shallow trackpad sometimes misregisters gestures. Connectivity is decent with multiple USB-C ports, though the absence of HDMI is inconvenient. Speakers are loud enough for casual listening, yet lack bass depth. Thermal management is impressive, with the fans rarely audible under light use. However, the premium price feels slightly inflated given its limitations. Overall, it’s a refined machine best suited for professionals who value mobility and design over raw performance.
""")

print(result)