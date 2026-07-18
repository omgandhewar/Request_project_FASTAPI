from fastapi import FastAPI, Depends, APIRouter
from services.query_services import user_query
from db.database import get_db
from logger import execution


router=APIRouter()



@router.get("/query")
def query(name:str,age:int,db=Depends(get_db)):
    
    execution.append("routes started")
    
    return user_query(name,age,db)