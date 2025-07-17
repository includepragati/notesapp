import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize this meeting: {text}"}],
        temperature=0.5
    )
    return response['choices'][0]['message']['content']
