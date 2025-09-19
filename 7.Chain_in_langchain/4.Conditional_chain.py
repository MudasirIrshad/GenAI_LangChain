from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Literal
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from langchain.schema.runnable import RunnableBranch, RunnableLambda

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(description="Overall sentiment of the feedback: positive, negative")

structured_model = model.with_structured_output(Feedback)

parser = StrOutputParser()

parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template="classify the sentiment of the following feedback \n {feedback}",
    input_variables=['feedback']
)


classifier_chain = prompt1 | structured_model

print(classifier_chain.invoke({
    'feedback':"very bad mobile"
}))
positive_feedback_prompt = PromptTemplate(
    template="write an appropriate reply message to this positive feedback nothing more or nothing less \n {feedback}",
    input_variables=['feedback']
)
negative_feedback_prompt = PromptTemplate(
    template="write an appropriate reply message to this negative feedback nothing more or nothing less \n {feedback}",
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive', positive_feedback_prompt | model | parser), # type: ignore

    (lambda x:x.sentiment == 'Negative', negative_feedback_prompt | model | parser), # type: ignore
    
    RunnableLambda (lambda x: "could not find any sentiment")
)

chain = classifier_chain | branch_chain
result= chain.invoke({
    'feedback':"This is a terrible phone"
})

print(result)