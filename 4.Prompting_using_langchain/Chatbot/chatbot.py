from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

import os
from langchain_core.prompts import PromptTemplate
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


chat_history = [
    SystemMessage(content="You are a helpful assistant")
]
while True:
    user_input = input("You: ")
    
    chat_history.append(HumanMessage(content=user_input)) # type: ignore

    if user_input == "exit":
        break

    result = model.invoke(chat_history)
    
    chat_history.append(AIMessage(content=result.content)) # type: ignore
    
    print(result.content)

print(chat_history)