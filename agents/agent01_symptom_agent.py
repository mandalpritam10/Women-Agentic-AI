from llm import run_llama

def extract_symptoms(user_text):

    prompt= f"""
You are a medical NLP agent.

Extract symptoms from this text.
Fix spelling.
Normalize medical wording.

Return ONLY pure JSON.
No explanation.
No markdown.
No extra text.

Text:
{user_text}

Format:
{{
    "symptoms": ["symptom1", "symptom2"]
}}
"""
    
    return run_llama(prompt)