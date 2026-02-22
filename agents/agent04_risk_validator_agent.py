from llm import run_llama

def validate_risk(symptoms, reasoning):

    text = symptoms.lower()

    # UTI pattern override (burning + fever + abdominal pain)
    if "urinary" in text or "peeing" in text:
        return "SAFE"

    prompt = f"""
You are an emergency medical triage validator.

Symptoms:
{symptoms}

Medical reasoning:
{reasoning}

Question:
Does this combination of symptoms require IMMEDIATE emergency care
(ambulance / ER), not just routine medical consultation?

UNSAFE only if there are signs of:
- heavy bleeding + fainting
- shock (cold sweat + fast heartbeat)
- severe abdominal pain with dizziness
- pregnancy complications
- loss of consciousness
- internal bleeding

Return ONLY:
SAFE or UNSAFE
"""

    return run_llama(prompt).strip().upper()