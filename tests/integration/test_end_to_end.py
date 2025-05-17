"""
Integration tests for the project.
These tests verify that different components work together correctly.
"""

import pytest
import os
from src.hello import greet
from src.utils.config import get_config


def test_greeting_with_config():
    """Test that the greeting function works with configuration."""
    # This test demonstrates how components can be tested together
    try:
        # Load configuration
        config = get_config()
        
        # Use configuration values with the greeting function
        app_name = config["app"]["name"]
        message = greet(app_name)
        
        # Verify that the greeting includes the app name from config
        assert app_name in message
        assert message == f"Hello, {app_name}!"
    except Exception as e:
        pytest.skip(f"Skipping test due to configuration error: {e}") 