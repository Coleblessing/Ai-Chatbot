import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def chat(user_message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

def main():
    print("🤖 AI Chatbot - Type 'quit' to exit")
    print("-" * 40)
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
            
        if user_input.strip() == "":
            continue
            
        print("Bot: Thinking...")
        response = chat(user_input)
        print(f"Bot: {response}")
        print()

if __name__ == "__main__":
    main()