from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv
load_dotenv()

access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")


llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=access_token
) # type: ignore

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of Pakistan?")

print(result.content)