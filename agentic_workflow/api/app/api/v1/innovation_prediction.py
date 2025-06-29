"""
@Author: Abhishek Amar
@Date: 2025-06-27
@Description: This module defines the product-related API endpoints for the FastAPI application
""" 
from fastapi import APIRouter 
from dotenv import load_dotenv
import os
import sys

from app.schemas.pojo import PredictionRequest 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../src"))) 
from agentic_workflow.crew import run_workflow
load_dotenv()

innovate = APIRouter()  

@innovate.post("/future-innovation")
async def predict_future_innovation_by_patent_filed(prompt: PredictionRequest):
    print(" Future Innovation Predictor ") 
    result = run_workflow(prompt.search_topic)
    print("\n📄 Final Report:\n")
    print(result)
    return {"result": result}
 