from crewai import  Crew 
from .tasks import create_tasks
from .agents import (
    search_agent,
    extractor_agent,
    trend_analyzer_agent,
    predictor_agent,
    report_agent)


def run_workflow(topic: str):
    try:
        tasks = create_tasks(topic)
        crew = Crew(
            agents=[search_agent, extractor_agent, trend_analyzer_agent, predictor_agent, report_agent],
            tasks=tasks,
            verbose=True
        )
        return crew.kickoff()
    except Exception as e: 
        return {"error": e, "message": "An error occurred while running the workflow."}