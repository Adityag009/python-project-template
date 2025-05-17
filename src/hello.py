"""
A simple hello world module to test the project setup.
"""

def greet(name: str = "World") -> str:
    """
    Return a greeting message.
    
    Args:
        name (str): Name to greet. Defaults to "World".
    
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}!"

def main():
    """Main function to demonstrate the greeting."""
    print(greet())
    print(greet("Python Developer"))

if __name__ == "__main__":
    main() 