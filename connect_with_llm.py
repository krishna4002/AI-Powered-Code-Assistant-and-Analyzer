import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "open-r1/olympiccoder-32b:free"

def call_openrouter(history, temperature=0.7):
    """Call OpenRouter API with chat history and temperature control."""
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "temperature": temperature,  # ✅ Support temperature
                "messages": [
                    {"role": "system", "content": (
                        "You are a helpful code assistant. Ask clarifying questions when needed, "
                        "and generate clean, well-commented code."
                    )},
                    *history
                ]
            }
        )
        result = response.json()
        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        elif "error" in result:
            return f"❌ API Error: {result['error'].get('message', 'Unknown error')}"
        else:
            return "❌ Unexpected response format."
    except Exception as e:
        return f"❌ Exception occurred: {str(e)}"


# Optional helpers

def generate_code(task, language):
    """Generate code from a task description in a specific language."""
    prompt = f"Write a complete program in {language} that does the following:\n\n{task}\n\nUse comments and best practices."
    return call_openrouter([{"role": "user", "content": prompt}])

def explain_code(code):
    """Explain given code step-by-step."""
    prompt = f"Explain the following code step-by-step:\n\n{code}"
    return call_openrouter([{"role": "user", "content": prompt}])

def convert_code(code, target_language):
    """Convert given code to a target language."""
    prompt = f"Convert the following code to {target_language}:\n\n{code}"
    return call_openrouter([{"role": "user", "content": prompt}])

def generate_tests(code):
    """Generate unit tests for the provided code."""
    prompt = f"Write unit test cases for the following code:\n\n{code}"
    return call_openrouter([{"role": "user", "content": prompt}])