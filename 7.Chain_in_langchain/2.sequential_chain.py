from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

tempelate1 = PromptTemplate(
    template="Generate Detailed report about {topic} \n",
    input_variables=['topic'],
    )

tempelate2 = PromptTemplate(
    template="generate top 5 key pointers from this report \n {text}",
    input_variables=['text']
)

chain = tempelate1 | model | parser | tempelate2 | model | parser

result = chain.invoke({
    'topic':"Quetta"
})

print(result)
