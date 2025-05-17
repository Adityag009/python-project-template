"""
Unit tests for the hello module.
"""

import pytest
from src.hello import greet

def test_greet_default():
    """Test the default greeting."""
    assert greet() == "Hello, World!"

def test_greet_custom():
    """Test greeting with a custom name."""
    assert greet("Python") == "Hello, Python!"

def test_greet_empty():
    """Test greeting with an empty string."""
    assert greet("") == "Hello, !" 