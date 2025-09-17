from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.dependencies import get_api_key,get_current_user
from app.services.model_service import predict_student_score

router = APIRouter()


class Studentfeatures(BaseModel):
    comprehension: float
    attention:float
    focus:float
    retention:float
    engagement_time: int

@router.post("/predict")
def predict_score(student : Studentfeatures,user=Depends(get_current_user),_=Depends(get_api_key)):
    prediction  = predict_student_score(student.model_dump())
    return {"predicted_score" : f'{prediction:.2f}'}
