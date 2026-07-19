from fastapi import FastAPI, HTTPException
from logger import execution
from fastapi.responses import JSONResponse
from sqlalchemy import text



def user_query(name,age,db):
    
    execution.append("service layer started")
    
    execution.append("Executing SQL Query")
    
    result=db.execute(
        text("SELECT name,age FROM users WHERE name=:name"),
        {
            "name":name
        }
    )
    
    user=result.fetchone()
    
    if user is None:
        
        execution.append("User Not Found")
        
        return JSONResponse(
    status_code=404,
    content={
        "execution": execution,
        "detail": "User not found"
    }
)
    
    execution.append("Dictionary created")
    
    resposnse={
        "name":user[0],
        "age":user[1]
    }
    
    execution.append("Returning response")
    
    return{
        "execution":execution,
        "message":resposnse
    }