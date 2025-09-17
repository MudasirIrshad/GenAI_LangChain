from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

tempelate = PromptTemplate(
    template="Generate 5 interesting facts about {topic} \n",
    input_variables=['topic'],
    )

chain = tempelate | model | parser

result = chain.invoke({
    'topic':"Quetta"
})

print(result)