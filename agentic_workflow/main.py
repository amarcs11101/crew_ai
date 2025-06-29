from src.agentic_workflow.crew import run_workflow
import sys
import os
# Entry Point
if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    print(" Future Innovation Predictor ")
    user_topic = input("Enter the research topic (e.g., Lithium Battery): ")
    result = run_workflow(user_topic)
    print("\n📄 Final Report:\n")
    print(result)
