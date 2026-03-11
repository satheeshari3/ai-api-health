from groq import Groq
import os

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key) if api_key else None


def explain_error(status_code):

    if not client:
        return "AI explanation unavailable (API key missing)."

    prompt = f"""
You are an API monitoring assistant.

Status code: {status_code}

Explain briefly:
1. What this status code usually means
2. Possible reasons the API might return this
3. One quick suggestion a developer could try

Keep the explanation under 2 sentences.
"""


    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": "You explain API failures simply."},
        {"role": "user", "content": prompt}
    ]
)

    return response.choices[0].message.content