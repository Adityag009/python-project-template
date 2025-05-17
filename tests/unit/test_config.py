"""
Unit tests for the configuration utilities.
"""

import os
import pytest
import tempfile
import yaml
from src.utils.config import load_config, get_config


def test_load_config():
    """Test loading a configuration file."""
    # Create a temporary YAML file
    with tempfile.NamedTemporaryFile(suffix=".yaml", mode="w+", delete=False) as temp_file:
        temp_file.write("""
        app:
          name: test-app
          version: 1.0.0
        """)
        temp_file_path = temp_file.name
    
    try:
        # Test loading the configuration
        config = load_config(temp_file_path)
        assert config is not None
        assert "app" in config
        assert config["app"]["name"] == "test-app"
        assert config["app"]["version"] == "1.0.0"
    finally:
        # Clean up temporary file
        os.unlink(temp_file_path)


def test_load_config_file_not_found():
    """Test file not found error when loading configuration."""
    with pytest.raises(FileNotFoundError):
        load_config("non_existent_file.yaml")


def test_load_config_invalid_yaml():
    """Test invalid YAML error when loading configuration."""
    # Create a temporary YAML file with invalid YAML
    with tempfile.NamedTemporaryFile(suffix=".yaml", mode="w+", delete=False) as temp_file:
        temp_file.write("""
        app:
          name: test-app
          version: 1.0.0
          invalid: *&^%$
        """)
        temp_file_path = temp_file.name
    
    try:
        # Test loading the configuration
        with pytest.raises(yaml.YAMLError):
            load_config(temp_file_path)
    finally:
        # Clean up temporary file
        os.unlink(temp_file_path) 