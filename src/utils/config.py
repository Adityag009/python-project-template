"""
Configuration utilities for loading and managing configuration files.
"""

import os
import yaml
from typing import Dict, Any, Optional


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load a YAML configuration file.
    
    Args:
        config_path (str): Path to the YAML configuration file.
        
    Returns:
        Dict[str, Any]: The configuration as a dictionary.
        
    Raises:
        FileNotFoundError: If the configuration file does not exist.
        yaml.YAMLError: If the YAML file is malformed.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, 'r') as f:
        try:
            config = yaml.safe_load(f)
            return config
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML configuration: {e}")


def get_config(config_name: str = "default", config_dir: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a configuration by name.
    
    Args:
        config_name (str): Name of the configuration file without extension.
        config_dir (Optional[str]): Directory containing configuration files.
            Defaults to the 'config' directory in the project root.
            
    Returns:
        Dict[str, Any]: The configuration as a dictionary.
    """
    if config_dir is None:
        # Get the project root directory (assuming this file is in src/utils)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
        config_dir = os.path.join(project_root, "config")
    
    config_path = os.path.join(config_dir, f"{config_name}.yaml")
    return load_config(config_path) 