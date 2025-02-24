from decouple import config
from groq import Groq

GROQ_API_KEY = config("GROQ_API_KEY", default=None)
GROQ_MODEL = "llama-3.3-70b-versatile"


def get_client():
    return Groq(api_key=GROQ_API_KEY)


def get_llm_response(gpt_message):
    client = get_client()
    print("Sending messages to Groq API:", gpt_message)  # Debugging
    completion = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=gpt_message
    )
    print("Received response from Groq API:", completion)  # Debugging
    return completion.choices[0].message.content


