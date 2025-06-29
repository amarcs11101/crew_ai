from pydantic import BaseModel

class PredictionRequest(BaseModel):
    search_topic:str 
 
       
    