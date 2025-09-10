from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()

access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    # huggingfacehub_api_token=access_token
) # type: ignore

doc = [
    "Pakistan is my country",
    "My name is Mudasir",
    "Quaid is founder of Pakistan"
]

vector = embeddings.embed_documents(doc)

print(vector)