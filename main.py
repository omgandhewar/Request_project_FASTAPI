from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from logger import execution
from db.database import Base, engine
from routes.query_routes import router



def create_app():
    
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
    
    
    app.include_router(router)
    
    Base.metadata.create_all(bind=engine)

    
    return app

app=create_app()


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    execution.clear()

    execution.append("Middleware Started")

    response = await call_next(request)

    execution.append("Middleware Finished")

    return response
    
