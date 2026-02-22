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


def main():
    user_input = input("Describe your symptoms: ")

    print("\n--- Agent 1: Extracting Symptoms ---")
    symptoms = extract_symptoms(user_input)
    print(symptoms)

    print("\n--- Agent 2: Generating Disease Candidates ---")
    diseases = generate_diseases(symptoms)
    print(diseases)

    print("\n--- Agent 3: Medical Reasoning ---")
    reasoning = decision(symptoms, diseases)

    # Agent 4: Risk validation (SAFE / UNSAFE)
    risk = validate_risk(symptoms, reasoning)
    print("\nRisk Validation:", risk)

    # Agent 5: Severity classification
    if risk == "UNSAFE":
        severity = "HIGH"
    else:
        severity = classify_severity_llm(reasoning).strip().upper()

    print("\nSeverity Level:", severity)

    # Agent 6: Safety moderation
    if severity == "HIGH":
        guarded = apply_guardrails(reasoning)

        print("\n--- Patient Safe Output ---")
        safe_output = generate_safe_response(symptoms, guarded)
        print(safe_output)

    else:
        print("\n--- Final Medical Output ---")
        print(reasoning)

    print("\n⚠️ Disclaimer:")
    print("This system is an academic AI prototype and does NOT provide medical diagnosis.")
    print("Please consult a qualified healthcare professional for evaluation.")


if __name__ == "__main__":
    main()