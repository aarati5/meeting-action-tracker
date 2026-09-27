import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_action_items(transcript: str) -> list:
    system_prompt = """You are a meeting assistant. Extract action items from the meeting transcript below.

Return ONLY a valid JSON array, no other text, in this exact format:
[
  {"task": "description of task", "owner": "person name", "deadline": "date or 'not specified'"}
]

Rules:
- Only extract clear, actionable items (not general discussion)
- If owner isn't mentioned, use "unassigned"
- If deadline isn't mentioned, use "not specified"
- Return an empty array [] if no action items are found
"""

    model = genai.GenerativeModel(
        model_name="gemini-3.8-flash",
        system_instruction=system_prompt
    )

    response = model.generate_content(transcript)
    raw_text = response.text.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        print("Warning: Could not parse response as JSON. Raw output:")
        print(raw_text)
        return []