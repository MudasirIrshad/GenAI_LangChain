from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

from langchain.schema.runnable import RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

tempelate1 = PromptTemplate(
    template="Generate short and simple notes from the following text  \n {text}",
    input_variables=['text'],
    )

tempelate2 = PromptTemplate(
    template="generate quiz from the following notes \n {text}",
    input_variables=['text']
)

tempelate3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document. \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes','quiz']
)

parallel_chain = RunnableParallel({
    'notes': tempelate1 | model | parser,
    'quiz': tempelate2 | model | parser
})

merge_chain = tempelate3 | model | parser

chain  = parallel_chain | merge_chain


text = """
Agentic AI

Agentic AI is the emerging paradigm of artificial intelligence where systems act not only as passive responders but as autonomous, decision-making agents. Unlike traditional AI models that wait for user prompts and return outputs, Agentic AI is designed with initiative, reasoning, and adaptability, enabling it to function more like a digital colleague or assistant that can work independently to achieve objectives.

What is Agentic AI?

At its core, Agentic AI is about giving artificial intelligence agency — the capacity to perceive, plan, and act in pursuit of goals. These systems can set sub-goals, evaluate options, use tools, and learn from outcomes without requiring constant human supervision. They are closer to the idea of “AI agents” that actively help humans, rather than simply answering questions or generating text.

Traditional AI:

Takes input → generates output.

Requires step-by-step prompting for multi-task workflows.

Agentic AI:

Understands a goal → decides steps → uses tools → executes → adapts if conditions change.

Reduces human effort by handling complexity automatically.

Key Characteristics

Autonomy

Works independently once a goal is defined.

Minimizes repetitive prompting or micromanagement.

Reasoning and Planning

Breaks down complex problems into smaller steps.

Chooses the most efficient path to completion.

Tool and API Integration

Uses external resources (APIs, databases, search engines, apps).

Bridges the gap between raw intelligence and real-world actions.

Adaptability

Responds to new information dynamically.

Adjusts strategies when conditions shift.

Memory and Context Awareness

Retains information across interactions.

Improves over time by learning from prior attempts.

Applications of Agentic AI

Business Automation

Automating end-to-end workflows such as report generation, customer support, or invoice handling.

Acting as operational assistants within enterprises.

Research & Data Analysis

Gathering information from multiple sources.

Synthesizing large datasets into actionable insights.

Software Development

Writing, testing, debugging, and deploying code.

Acting as AI coding agents that reduce developer workload.

Healthcare & Education

Personalized learning assistants for students.

Virtual care assistants that provide tailored health guidance.

Personal Productivity

Managing schedules, emails, and personal tasks proactively.

Serving as always-available digital helpers.

Why Agentic AI Matters

The transition from passive AI to agentic systems is as significant as the shift from static web pages to dynamic, interactive applications. With Agentic AI, we move from AI that only answers to AI that takes action. This shift has the potential to:

Unlock new levels of efficiency by reducing manual work.

Provide scalable intelligence that adapts across industries.

Enable collaborative intelligence, where humans and AI complement each other.

Building Agentic AI

Frameworks like LangChain, LangGraph, and OpenAI’s Agents API have become essential for building Agentic AI applications. They provide the infrastructure for:

Prompt Chaining – combining multiple reasoning steps.

Tool Use – connecting the AI to external systems.

Memory Management – giving the AI context retention.

Agent Architectures – building goal-directed workflows.

LangChain popularized the concept of chains and agents, while LangGraph is now pioneering multi-agent systems where multiple AIs can collaborate. Together, they give developers the ability to build advanced agentic workflows that feel much closer to human-like task execution.

Future of Agentic AI

The evolution of Agentic AI is pointing toward systems that are:

Multi-modal (handling text, images, audio, and video together).

Collaborative (multiple agents working in teams).

Trustworthy (transparent decision-making and safety mechanisms).

Domain-specialized (agents tailored for industries like finance, law, medicine, etc.).

As these systems mature, we may see them become embedded into everyday life — from smart personal assistants to enterprise-level digital workforces that operate 24/7.

Conclusion

Agentic AI is not just an incremental upgrade to traditional AI — it is a fundamental leap toward machines that can think, plan, and act with purpose. By combining autonomy, reasoning, and tool use, Agentic AI enables applications that are more powerful, reliable, and impactful. Whether in business, research, or personal life, this new wave of AI has the potential to redefine how humans interact with technology and accelerate innovation across every industry.
"""


result = chain.invoke({
    'text': text
})

print(chain.get_graph().print_ascii())