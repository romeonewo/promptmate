```
chatbot/
│── chatbot.py         # Main script
│── config.json        # Store API key (optional)
│── chat_memory.json   # Stores conversation history
```
# Vortex - Terminal AI Assistant



A lightweight Python-based terminal chatbot powered by OpenAI's API through OpenRouter.

## Features

- 💬 Interactive terminal chat interface
- � Persistent chat history (saved to JSON)
- 🌈 Color-coded messages for better readability
- ⚙️ Simple configuration via `config.json`
- 🔄 Chat memory management (`/clear` to reset)
- 🤖 Customizable AI personality

## Quick Start

1. **Prerequisites**:
   - Python 3.x
   - `requests` and `colorama` packages (`pip install requests colorama`)

2. **Setup**:
   ```bash
   git clone https://github.com/yourusername/vortex-chat.git
   cd vortex-chat
  ```
# Configuration:

3. **Create config.json with your OpenRouter API key:**

```
{
  "openai_api_key": "your-api-key-here"
}
```

4. #Customization
**customize the prompt to change behaviour**
```
system_message = {
    "role": "system",
    "content": "Customize this prompt to change my behavior..."
}
```
