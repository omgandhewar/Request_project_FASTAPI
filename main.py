from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logger import execution




app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/query")
def query(name:str,age:int):
    
    execution.clear()
    
    execution.append("routes started")
    
    resposnse={
        "name":name,
        "age":"age"
    }
    
    execution.append("Dictionary created")
    
    execution.append("Returning response")
    
    return{
        "execution":execution,
        "message":resposnse
    }
    
