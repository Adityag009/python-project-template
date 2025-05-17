"""
Main FastAPI application file.
This file defines the FastAPI application and its endpoints.
"""

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

from src.hello import greet
from src.utils.config import get_config

# Create the FastAPI application
app = FastAPI(
    title="Python Project Template API",
    description="A simple API for the Python Project Template",
    version="0.1.0",
)


# Define data models
class GreetingRequest(BaseModel):
    """Request model for the greeting endpoint."""
    name: Optional[str] = None


class GreetingResponse(BaseModel):
    """Response model for the greeting endpoint."""
    message: str


class ConfigResponse(BaseModel):
    """Response model for the config endpoint."""
    config: Dict[str, Any]


# Dependency to get configuration
def get_app_config():
    """Get the application configuration."""
    try:
        return get_config()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading configuration: {str(e)}")


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint that returns basic API information."""
    return {
        "message": "Welcome to the Python Project Template API",
        "docs": "/docs",
        "version": "0.1.0",
    }


@app.post("/greeting", response_model=GreetingResponse, tags=["Greetings"])
async def greeting(request: GreetingRequest):
    """
    Create a personalized greeting.
    
    - **name**: Optional name to greet. If not provided, "World" will be used.
    """
    name = request.name if request.name else "World"
    message = greet(name)
    return GreetingResponse(message=message)


@app.get("/config", response_model=ConfigResponse, tags=["Configuration"])
async def config(config: Dict[str, Any] = Depends(get_app_config)):
    """
    Get the application configuration.
    
    This endpoint returns the current application configuration.
    """
    return ConfigResponse(config=config) 