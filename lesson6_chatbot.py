from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

#this stores the full coversaton hstory
messages= []

print("🤖 AI Chatbot ready! Type 'quit' to exit.")
print("-" * 40)

while True:
    # Get input from user
    user_input = input("You: ")

    # Exit if user types quit
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Add user message to history
    messages.append({"role": "user", "content": user_input})

    # Send full conversation history to AI
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    # Get AI reply
    reply = response.choices[0].message.content

    # Add AI reply to history too (so it remembers it said this)
    messages.append({"role": "assistant", "content": reply})

    print(f"AI: {reply}")
    print()
