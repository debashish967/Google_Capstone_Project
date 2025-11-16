# tools.py
from google.genai import Client

def test_tool(message: str) -> str:
    return f"Tool received: {message}"