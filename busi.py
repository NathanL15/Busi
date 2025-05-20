import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_business_insight(user_input):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"""
You are Busi, an assistant that analyzes early-stage business ideas.

Given the following description, output:

1. Executive Summary (1–2 sentences)
2. Strengths (bullet points)
3. Weaknesses (bullet points)
4. Similar Companies (short list)

Business Description: {user_input}
"""
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
