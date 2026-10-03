==================================================
README.md
==================================================

# 🤖 AI Auto-Reply Bot

An AI-powered WhatsApp auto-reply bot built with Python, Playwright, and Groq AI.

The project is being developed step-by-step to understand how browser automation, message processing, AI APIs, and project architecture work together.

## 🚀 Current Status

The current version can:

✅ Open WhatsApp Web using Playwright  
✅ Maintain a persistent WhatsApp session  
✅ Read messages from the currently opened chat  
✅ Extract message metadata and text  
✅ Identify the latest message  
✅ Ignore messages that should not receive a reply  
✅ Generate an AI response using Groq  
✅ Maintain conversation history for AI responses  
✅ Send the generated response back to WhatsApp  

The following features are still under development:

- Automatically selecting chats
- Continuously monitoring for new messages
- Preventing duplicate replies
- Better error handling
- Logging and reliability improvements

## 🔄 Current Flow

Start
  ↓
🌐 Open WhatsApp Web
  ↓
💬 Select / Open Chat
  ↓
📥 Read Messages
  ↓
🔎 Find Latest Message
  ↓
🧠 Reply Logic
  ↓
❓ Should Reply?
  ↓
🤖 Groq AI
  ↓
✍️ Generate Response
  ↓
📤 Send Response

## 📁 Project Structure

ai-auto-reply-bot/
│
├── 01_basic_chatbot/
│   ├── chatbot.py
│   └── README.md
│
├── bot/
│   ├── __init__.py
│   ├── config.py
│   ├── groq_api.py
│   ├── reply_logic.py
│   └── whatsapp.py
│
├── tools/
│
├── .env
├── .gitignore
├── main.py
└── README.md

## 🛠️ Technologies Used

- 🐍 Python
- 🎭 Playwright
- 🤖 Groq API
- 🔐 python-dotenv
- 📋 Pyperclip
- 🌿 Git
- 🐙 GitHub

## ⚙️ Setup

### 1. Clone the repository

git clone https://github.com/Luckyy05/Ai-auto-reply-bot.git
cd Ai-auto-reply-bot

### 2. Create a virtual environment

python -m venv .venv

Activate it on Windows:

.venv\Scripts\Activate.ps1

### 3. Install dependencies

pip install playwright groq python-dotenv pyperclip

Install the Playwright browser:

playwright install chromium

### 4. Configure the Groq API

Create a `.env` file in the project root:

GROQ_API_KEY=your_api_key_here

Replace `your_api_key_here` with your actual Groq API key.

Do not commit the `.env` file to GitHub.

### 5. WhatsApp Web Session

The bot uses a persistent Playwright browser profile.

The session is stored locally in:

whatsapp_profile/

On the first run, you may need to scan the WhatsApp Web QR code.

After that, the saved session can be reused.

Do not commit `whatsapp_profile/` to GitHub.

## ▶️ Running the Bot

Run:

python main.py

The bot will:

1. Open WhatsApp Web.
2. Reuse the saved WhatsApp session if available.
3. Wait for you to open the desired chat.
4. Read the latest message.
5. Decide whether a reply is needed.
6. Generate a response using Groq AI.
7. Send the response to WhatsApp.
8. Close the browser.

## 🧩 Architecture

### main.py

The main entry point of the project.

It is responsible for connecting all components together and controlling the overall flow.

### bot/whatsapp.py

Handles WhatsApp Web automation using Playwright.

Responsibilities include:

- Starting WhatsApp Web
- Maintaining the browser session
- Reading messages
- Finding the latest message
- Sending messages

### bot/reply_logic.py

Contains the logic that decides whether the bot should reply.

For example, it can ignore:

- Messages sent by the bot's own account
- Empty messages
- Very long messages
- Common messages such as `ok`, `okay`, `good morning`, and `good night`

### bot/groq_api.py

Handles communication with the Groq API.

It is responsible for:

- Sending user messages to the AI
- Generating responses
- Maintaining conversation history

### bot/config.py

Contains project configuration such as WhatsApp UI-related settings and other constants used by the project.

## 🎯 Learning Purpose

This project is also being used as a practical Python project to learn:

- Python project structure
- Modules and packages
- APIs
- Environment variables
- Browser automation
- Playwright
- AI integration
- Conversation history
- Git and GitHub
- Debugging and incremental development

## 📌 Important Notes

The project currently requires the user to manually open/select the WhatsApp chat before the bot processes the message.

The WhatsApp session is stored locally using a persistent Playwright profile so that WhatsApp Web does not need to be logged in every time.

The local session folder should never be committed to GitHub.

## ⚠️ Disclaimer

This project is intended for learning and experimentation with Python, browser automation, and AI APIs.

Use WhatsApp automation responsibly and in accordance with WhatsApp's terms and applicable policies.


==================================================
.gitignore
==================================================

.env
.venv/
__pycache__/
*.pyc
whatsapp_profile/


==================================================
FILES TO DELETE
==================================================

Delete these files:

bot/gemini_api.py
tools/get_position.py
tools/check_whatsapp_ui.py

For whatsapp_profile:

DO NOT delete the local folder from your PC.

Only remove it from Git tracking:

git rm -r --cached whatsapp_profile


==================================================
GIT COMMANDS
==================================================

First check the current status:

git status

Check the changes:

git diff

Check for formatting errors:

git diff --check

Stage the changes:

git add README.md .gitignore bot tools

Then commit:

git commit -m "chore: clean project and update README"

Finally push:

git push


==================================================
IMPORTANT
==================================================

Keep whatsapp_profile/ on your computer.

It contains the saved WhatsApp Web session.

It should be ignored by Git and should NOT be uploaded to GitHub.
```
