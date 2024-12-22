from typing import Union
from fastapi import FastAPI
from src.controllers.routes import allRoutes
from src.database import Base, engine

app = FastAPI()
app.include_router(allRoutes)

@app.on_event("startup")
def create_tables():
    print("Creating all tables that doesn't exist...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")


@app.get("/")
def root():
    return {"message": "Welcome to the API"}