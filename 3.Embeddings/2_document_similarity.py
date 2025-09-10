from sklearn.metrics.pairwise import cosine_similarity
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

doc_embeddings = embeddings.embed_documents(doc)

query = "Pakistan was created by?"

query_embeddings= embeddings.embed_query(query)



# Compare query against all docs
similarities = cosine_similarity([query_embeddings], doc_embeddings)[0]# type: ignore

# similarities is a 1 x N matrix
index, score = sorted(list(enumerate(similarities)), key=lambda x:x[1])[-1]

print(doc[index])