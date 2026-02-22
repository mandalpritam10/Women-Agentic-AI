from llm import run_llama

def classify_severity_llm(reasoning_text):

    prompt = f"""
You are an emergency triage AI.

Given this medical reasoning:

{reasoning_text}

Determine patient risk level.

Rules:

HIGH:
- Any possibility of life-threatening condition
- Internal bleeding
- severe pain + dizziness
- shock symptoms
- loss of consciousness
- rapidly worsening condition
- cancer suspicion
- pregnancy complications
- anything that could endanger life without urgent care

MEDIUM:
- chronic or serious conditions but stable
- infections without shock
- hormonal disorders

LOW:
- mild or common issues

IMPORTANT:
Do NOT classify based on disease name.
Classify based on risk to life.

Return ONLY:
LOW
MEDIUM
HIGH
"""

    return run_llama(prompt).strip()