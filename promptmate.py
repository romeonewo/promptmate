import json
import requests
import os

# Load the API key from config.json
def load_config():
    try:
        with open("config.json", "r", encoding="utf-8") as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print("❌ config.json file not found. Please ensure it exists.")
        exit()

# Load the config and get the API key
config = load_config()
API_KEY = config.get("openai_api_key")

# Check if the API key exists
if not API_KEY:
    print("❌ API key not found in config.json. Please check your file.")
    exit()

# File to store chat history
CHAT_MEMORY_FILE = "chat_memory.json"

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
            # Send request to OpenRouter API using 'requests' method
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional. Replace with your site URL.
                    "X-Title": "<YOUR_SITE_NAME>",  # Optional. Replace with your site title.
                },
                data=json.dumps({
                    "model": "deepseek/deepseek-chat-v3-0324:free",
                    "messages": chat_history
                })
            )

            # Check if the response is successful
            if response.status_code == 200:
                bot_reply = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
                print(f"AI: {bot_reply}\n")

                # Add bot response to chat history
                chat_history.append({"role": "assistant", "content": bot_reply})

                # Save updated chat history
                save_chat_history(chat_history)
            else:
                print(f"❌ Error: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"❌ Error: {e}")

# Run the chatbot
if __name__ == "__main__":
    chat()
