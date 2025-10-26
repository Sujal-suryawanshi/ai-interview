import json
import re
from litellm import completion
import os

LLM_MODEL = os.environ.get("LLM_MODEL", "mistral/mistral-large-latest")


def get_response_from_llm(prompt: str) -> str:
    """
    Calls the LLM and returns the response.

    Args:
        prompt (str): The string to prompt the LLM with.

    Returns:
        str: The response from the LLM.
    """
    response = completion(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

def parse_json_response(response_text: str) -> dict:
    if not response_text or not isinstance(response_text, str):
        return {"raw_text": ""}

    try:
        # Remove Markdown code fences like ```json ... ```
        response_text = re.sub(r"^```(?:json)?|```$", "", response_text, flags=re.MULTILINE).strip()

        # Normalize smart quotes
        response_text = (
            response_text.replace("‘", "\"")
            .replace("’", "\"")
            .replace("“", "\"")
            .replace("”", "\"")
        )

        # Remove trailing commas before closing braces/brackets
        response_text = re.sub(r",(\s*[}\]])", r"\1", response_text)

        # Parse clean JSON
        parsed = json.loads(response_text)
        return parsed if isinstance(parsed, dict) else {"raw_text": str(parsed)}

    except json.JSONDecodeError:
        # Fallback: Try to extract score manually if JSON failed
        score_match = re.search(r'"score"\s*:\s*(\d+)', response_text)
        feedback_match = re.search(r'"feedback"\s*:\s*"([^"]+)"', response_text)
        return {
            "score": int(score_match.group(1)) if score_match else 0,
            "feedback": feedback_match.group(1) if feedback_match else "Could not generate feedback.",
            "raw_text": response_text,
        }

