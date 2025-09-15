from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Literal, Optional
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review(BaseModel):
    
    key_themes: list[str] = Field(description="List of the main themes or aspects discussed in the review (e.g., battery, design, performance")
    
    summary: list[str] = Field(description="A concise summary (2–3 sentences) of the overall review")
    
    sentiment: Literal["Pos", "Neg", "Neu", "Mix"] = Field(description="Overall sentiment of the review: pos, neg, neu, or mix")
    
    pros: Optional[list[str]] = Field(description="List of all positive aspects mentioned in the review")

    cons: Optional[list[str]] = Field(description="List of all negative aspects mentioned in the review")

    name: Optional[str] = Field(description="Name of Reviewer")

structured_model = model.with_structured_output(Review) # pyright: ignore[reportArgumentType]
result = structured_model.invoke("""Hello my name is Mudasir Irshad.
The new ultrabook is a fascinating mix of strengths and compromises. Its lightweight design and sleek aluminum chassis make it easy to carry for daily commutes, while the vibrant display provides crisp visuals for work and entertainment. Battery life extends well beyond a typical workday, though the advertised “20 hours” is a stretch in real-world usage. Performance on productivity tasks is excellent, but the integrated graphics struggle with heavy creative workloads or modern AAA games. The keyboard has satisfying travel, but the shallow trackpad sometimes misregisters gestures. Connectivity is decent with multiple USB-C ports, though the absence of HDMI is inconvenient. Speakers are loud enough for casual listening, yet lack bass depth. Thermal management is impressive, with the fans rarely audible under light use. However, the premium price feels slightly inflated given its limitations. Overall, it’s a refined machine best suited for professionals who value mobility and design over raw performance.
""")

print(result)