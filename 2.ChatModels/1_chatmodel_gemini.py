from langchain_google_genai import ChatGoogleGenerativeAI

import os
from dotenv import load_dotenv
load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY"), temperature=1) # type: ignore

result = chat_model.invoke("write 5 line poem in urdu about paksitan in roman urdu text")
print(result.content)