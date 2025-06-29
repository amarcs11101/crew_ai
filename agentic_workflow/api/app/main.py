"""
@Author: Abhishek Amar
@Date: 2025-06-27
@Description: Main entry point for the FastAPI application.

"""
import uvicorn
from fastapi import FastAPI 
from app.routes.router import app_router 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(app_router)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000,reload=True)