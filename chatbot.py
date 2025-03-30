import json
import os
from openai import OpenAI

# Load API Key (You can store this in an environment variable for security)
API_KEY = "your_openrouter_api_key"

# File to store chat history
CHAT_MEMORY_FILE = "chat_memory.json"

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

# Load existing chat history from JSON file
def load_chat_history():
    if os.path.exists(CHAT_MEMORY_FILE):
        with open(CHAT_MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# Save chat history to JSON file
def save_chat_history(history):
    with open(CHAT_MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

# Chat function
def chat():
    chat_history = load_chat_history()
    print("\n🟢 Welcome to PromptMate! Type '/exit' to quit or '/clear' to reset chat.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "/exit":
            print("👋 Exiting... Chat saved!")
            save_chat_history(chat_history)
            break
        elif user_input.lower() == "/clear":
            chat_history = []
            save_chat_history(chat_history)
            print("✅ Chat history cleared.")
            continue

        # Add user message to chat history
        chat_history.append({"role": "user", "content": user_input})

        try:
            # Send request to OpenRouter API
            response = client.chat.completions.create(
                extra_headers={},
                extra_body={},
                model="deepseek/deepseek-v3-base:free",
                messages=chat_history
            )

            bot_reply = response.choices[0].message.content
            print(f"AI: {bot_reply}\n")

            # Add bot response to chat history
            chat_history.append({"role": "assistant", "content": bot_reply})

            # Save updated chat history
            save_chat_history(chat_history)

        except Exception as e:
            print(f"❌ Error: {e}")

# Run the chatbot
if __name__ == "__main__":
    chat()

