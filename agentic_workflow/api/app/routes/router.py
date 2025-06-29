"""
@Author: Abhishek Amar
@Date: 2025-06-27
"""

from fastapi import  APIRouter
from app.api.v1.innovation_prediction import innovate 

app_router = APIRouter()
app_router.include_router(innovate,prefix="/api/v1/predict", tags=["PREDICT FUTURE INNOVATION / TECHNOLOGY"])

 