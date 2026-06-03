from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Explain what artificial intelligence is in 3 simple sentences."}]
)

print(chat.choices[0].message.content)