from crewai import Task
from .agents import (
    search_agent,
    extractor_agent,
    trend_analyzer_agent,
    predictor_agent,
    report_agent)

def create_tasks(topic: str):
    return [
        Task(
            description=f"Search and list recent (last 3 years) patents about '{topic}' from public sources.",
            agent=search_agent,
            expected_output="List of 10-15 recent patents with title and URL",
        ),
        Task(
            description="Extract metadata (title, abstract, publication date) from the listed patents.",
            agent=extractor_agent,
            expected_output="Structured metadata for each patent",
        ),
        Task(
            description="Analyze all patent data and identify innovation trends, new tech, and focus areas.",
            agent=trend_analyzer_agent,
            expected_output="Innovation trend report",
        ),
        Task(
            description="Predict future innovations in the next 2-3 years for the topic based on identified trends.",
            agent=predictor_agent,
            expected_output="Prediction summary of future innovations",
        ),
        Task(
            description="Write a professional report combining all insights and predictions.",
            agent=report_agent,
            expected_output="Final summarized report on recent patents and predicted future tech",
        )
    ]
