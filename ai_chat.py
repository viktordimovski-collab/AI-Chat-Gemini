import os
from google import genai
from dotenv import load_dotenv

# 1. Вчитување на тајните податоци од .env
load_dotenv()
MY_KEY = os.getenv("GEMINI_API_KEY")

# 2. Иницијализација на клиентот
client = genai.Client(api_key=MY_KEY)

def start_chat():
    print("--- ДОБРЕДОЈДЕ ВО TVOJOТ AI ЧЕТ ---")
    print("(Напиши 'izlez' за да прекинеш)")

    # Креирање сесија
    chat = client.chats.create(model="gemini-2.0-flash") # 2.5 е во преглед, 2.0 е стабилен

    while True:
        user_input = input("\nВиктор: ")
        
        if user_input.lower() in ["izlez", "exit", "stop"]:
            print("Пријатно, Викторе!")
            break
            
        try:
            response = chat.send_message(user_input)
            print(f"\nGemini: {response.text}")
        except Exception as e:
            print(f"\nГрешка при комуникација: {e}")

if __name__ == "__main__":
    start_chat()