import os
from google import genai
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Initialize the Gemini client
client = genai.Client(api_key=API_KEY)

def start_chat():
    print("--- WELCOME TO YOUR AI CHAT ---")
    print("(Type 'exit' or 'quit' to end the session)")

    # Create chat session
    chat = client.chats.create(model="gemini-2.0-flash")

    while True:
        user_input = input("\nViktor: ")
        
        # Check for exit commands
        if user_input.lower() in ["exit", "quit", "stop"]:
            print("Goodbye, Viktor!")
            break
            
        try:
            response = chat.send_message(user_input)
            print(f"\nGemini: {response.text}")
        except Exception as e:
            print(f"\nCommunication error: {e}")

if __name__ == "__main__":
    start_chat()