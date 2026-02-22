from llm import run_llama

def generate_safe_response(symptoms, guarded_message):

    prompt = f"""
You are a medical safety moderation AI.

Symptoms:
{symptoms}

Patient-safe base message:
{guarded_message}

Rewrite the result for patients in a calm, non-alarming way.

Rules:
- Never say diagnosis is confirmed
- Use "possible" or "may indicate"
- If cancer appears, say "cannot be confirmed without clinical tests"
- Encourage professional medical consultation

Return a patient-friendly response.
"""

    return run_llama(prompt)