from llm import run_llama

def decision(symptoms, diseases):
    
    prompt=f"""
You are a medical reasoning agent(academic prototype).

Symptoms:
{symptoms}

Candiadte disease:
{diseases}

Pick ONE most likely disease.
Give explanation.
Give confidence percentage.

Format:

Disease:
Explanation:
Confidence:
"""
    
    return run_llama(prompt)