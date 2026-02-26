import json
import os
from openai import OpenAI
from .config import OPENAI_API_KEY

USE_MOCK = os.getenv("USE_MOCK_GPT", "true").lower() == "true"

# -----------------------------
# Load system prompt once
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROMPT_PATH = os.path.join(BASE_DIR, "prompts", "system_prompt.txt")

with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


def analyze_with_gpt(text: str):

    if USE_MOCK:
        return {
            "emotional_state": "Anxiety",
            "risk_level": "Low",
            "cognitive_patterns": ["rumination"],
            "behavioral_markers": ["avoidance"],
            "note": "Mock GPT response"
        }

    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0.2
    )

    return json.loads(response.choices[0].message.content)