from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

messages = [
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain in 3 lines")
]


result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)