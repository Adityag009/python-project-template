"""
Server module for running the FastAPI application.
"""

import uvicorn
import argparse
import os
from src.utils.config import get_config


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run the API server")
    parser.add_argument(
        "--host", type=str, default="127.0.0.1", help="Host to bind the server to"
    )
    parser.add_argument(
        "--port", type=int, default=8000, help="Port to bind the server to"
    )
    parser.add_argument(
        "--reload", action="store_true", help="Enable auto-reload for development"
    )
    return parser.parse_args()


def main():
    """Run the FastAPI application."""
    args = parse_args()
    
    # Load configuration
    try:
        config = get_config()
        print(f"Loaded configuration: API version {config['app']['version']}")
    except Exception as e:
        print(f"Warning: Could not load configuration: {e}")
    
    # Start the server
    print(f"Starting server at http://{args.host}:{args.port}")
    print("API documentation available at http://127.0.0.1:8000/docs")
    
    uvicorn.run(
        "src.api.app:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
    )


if __name__ == "__main__":
    main() 