import gradio as gr

from agents.agent01_symptom_agent import extract_symptoms
from agents.agent02_hypothesis_agent import generate_diseases
from agents.agent03_reasoning_agent import decision
from agents.agent04_risk_validator_agent import validate_risk
from agents.agent05_severity_agent import classify_severity_llm
from agents.agent06_safety_moderation_agent import generate_safe_response


def apply_guardrails(reasoning_text):

    return (
        "Based on the symptoms, there may be an underlying medical condition. "
        "Many common and non-serious causes such as infections, cysts, or hormonal "
        "changes can produce similar symptoms.\n\n"
        "Some serious conditions are also possible, but symptoms alone cannot confirm them. "
        "Accurate diagnosis requires clinical evaluation and medical tests.\n\n"
        "Please consult a qualified healthcare professional for proper assessment."
    )


def chatbot(user_input):

    output = ""

    output += "\n--- Agent 1: Extracting Symptoms ---\n"
    symptoms = extract_symptoms(user_input)
    output += f"{symptoms}\n\n"

    output += "--- Agent 2: Generating Disease Candidates ---\n"
    diseases = generate_diseases(symptoms)
    output += f"{diseases}\n\n"

    output += "--- Agent 3: Medical Reasoning ---\n"
    reasoning = decision(symptoms, diseases)

    risk = validate_risk(symptoms, reasoning)
    output += f"\nRisk Validation: {risk}\n"

    if risk == "UNSAFE":
        severity = "HIGH"
    else:
        severity = classify_severity_llm(reasoning).strip().upper()

    output += f"\nSeverity Level: {severity}\n"

    if severity == "HIGH":
        guarded = apply_guardrails(reasoning)

        output += "\n--- Patient Safe Output ---\n"
        safe_output = generate_safe_response(symptoms, guarded)
        output += safe_output

    else:
        output += "\n--- Final Medical Output ---\n"
        output += reasoning

    output += "\n\n⚠️ Disclaimer:\n"
    output += "This system is an academic AI prototype and does NOT provide medical diagnosis.\n"
    output += "Please consult a qualified healthcare professional for evaluation."

    return output


demo = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(lines=3),
    outputs=gr.Textbox(lines=25),
    allow_flagging="never",
    title="Women Health Agentic AI",
    description="Multi-Agent AI System for Women's Health"
)

if __name__ == "__main__":
    demo.launch()