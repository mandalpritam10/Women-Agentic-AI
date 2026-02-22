import subprocess

def run_llama(prompt):

    command=[
        "ollama",
        "run",
        "llama3",
        ]

    result=subprocess.run(
        command,
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()