from groq import Groq 
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


# The system prompt defines the AI's personality and role
messages = [
    {
        "role": "system",
        "content": """You are TechBot, an expert AI engineering mentor.
        You teach beginners Python and AI in a simple, encouraging way.
        You always use simple language, give short answers, and end 
        every response with one actionable tip."""
    }
]

print("🤖 TechBot ready! Type 'quit' to exit.")
print("-" * 40)

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("TechBot: Keep coding — you're doing great!")
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    
    print(f"TechBot: {reply}")
    print()