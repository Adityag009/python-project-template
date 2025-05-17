#!/usr/bin/env python
"""
Setup script for creating development environment.
This is an example utility script showing how to use the scripts directory.
"""

import os
import sys
import subprocess
from pathlib import Path


def create_virtual_environment():
    """Create a virtual environment for the project."""
    print("Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    print("Virtual environment created successfully.")


def install_dependencies():
    """Install project dependencies."""
    print("Installing dependencies...")
    
    # Determine the correct pip command based on OS
    pip_cmd = os.path.join("venv", "Scripts", "pip") if os.name == "nt" else os.path.join("venv", "bin", "pip")
    
    # Install the project in development mode with dev dependencies
    subprocess.run([pip_cmd, "install", "-e", ".[dev]"], check=True)
    print("Dependencies installed successfully.")


def create_directories():
    """Create necessary directories if they don't exist."""
    directories = [
        "data/raw",
        "data/processed",
        "notebooks",
        "config",
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        # Create .gitkeep files to preserve empty directories in git
        gitkeep_file = Path(directory) / ".gitkeep"
        if not gitkeep_file.exists():
            gitkeep_file.touch()
    
    print("Directories created successfully.")


def main():
    """Main function to set up the project environment."""
    print("Setting up project environment...")
    create_virtual_environment()
    install_dependencies()
    create_directories()
    print("Project setup complete!")


if __name__ == "__main__":
    main() 