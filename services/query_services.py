from fastapi import FastAPI
from logger import execution
from sqlalchemy import text



def user_query(name,age,db):
    
    execution.append("service layer started")
    
    execution.append("Database Session Created")
    
    execution.append("Executing SQL Query")
    
    result=db.execute(
        text("SELECT name,age FROM users WHERE name=:name"),
        {
            "name":name
        }
    )
    
    user=result.fetchone()
    
    print(user)
    print(type(user))
    
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