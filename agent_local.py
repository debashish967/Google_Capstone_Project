# agent_local.py
from dotenv import load_dotenv
import os
from google.genai import Client
from fraud_detector_agent.tools import test_tool

# Load .env file
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

class FraudDetectorAgent:
    def __init__(self):
        self.client = Client(api_key=os.environ["GOOGLE_API_KEY"])

    def run(self, message: str) -> str:
        result = self.client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=message
        )
        return result.text

    def debug(self, msg: str) -> str:
        return test_tool(msg)

# Optional: create instance
agent = FraudDetectorAgent()