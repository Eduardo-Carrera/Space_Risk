from fastapi import FastAPI
from app.routes import risk_assessment

app = FastAPI(
    title="Space Risk API",
    description="API for assessing space mission risks based on various factors.",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Space Risk API! Use /docs for API documentation."
        }