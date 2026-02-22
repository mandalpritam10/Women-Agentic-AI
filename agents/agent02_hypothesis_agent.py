from llm import run_llama

def generate_diseases(symptoms_json):

    prompt=f"""
You are a women-health AI.

Based ONLY on these symptoms:
{symptoms_json}

Return Top 5 likely women-related diseases.

Return ONLY JSON.
No explanation.
No markdown.

Format:
{{
    "possible_diseases": ["d1","d2","d3","d4","d5"]

}}
"""
    
    return run_llama(prompt)