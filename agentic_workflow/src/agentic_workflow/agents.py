from crewai import Agent
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv
load_dotenv()


MODEL= os.getenv("MODEL","llama3-70b-8192")
print(f"Using model: {MODEL}")
llm = ChatGroq(model=MODEL)

# Tool for web search
search_tool = SerperDevTool()


# Agent 1: Search Agent
search_agent = Agent(
    role="Patent Search Expert",
    goal="Find recent patents (last 3 years) on a given topic",
    backstory="An expert in finding up-to-date technical documents, patents, and research",
    tools=[search_tool],
    llm=llm,
    verbose=True,
)

# Agent 2: Patent Extractor
extractor_agent = Agent(
    role="Patent Information Extractor",
    goal="Extract metadata like title, abstract, and filing date from the identified patents",
    backstory="An NLP wizard specialized in parsing patent databases",
    llm=llm,
    verbose=True,
)

# Agent 3: Trend Analyzer
trend_analyzer_agent = Agent(
    role="Trend Analyst",
    goal="Analyze extracted patent data to detect innovation patterns",
    backstory="A trend analyst with deep tech foresight",
    llm=llm,
    verbose=True,
)

# Agent 4: Future Predictor
predictor_agent = Agent(
    role="Futurist LLM Agent",
    goal="Predict upcoming innovations and technologies from current patent trends",
    backstory="A visionary AI that understands trends and predicts future directions",
    llm=llm,
    verbose=True,
)

# Agent 5: Report Generator
report_agent = Agent(
    role="Technical Report Generator",
    goal="Generate a final report combining patent findings and future predictions",
    backstory="Specializes in writing professional technical summaries",
    llm=llm,
    verbose=True,
)