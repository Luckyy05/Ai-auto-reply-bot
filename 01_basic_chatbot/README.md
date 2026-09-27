# Basic Python Chatbot

This is Version 0.1 of my AI Auto-Reply Bot project.

The goal of this stage was to build a simple rule-based chatbot using core Python concepts before introducing AI APIs.

## Features

- Takes user input from the terminal
- Responds to predefined messages
- Runs continuously using a loop
- Exits when the user types `exit`
- Handles unknown inputs

## Python Concepts Used

- `input()`
- Variables
- `while` loop
- `if / elif / else`
- String methods
- `break`

## How to Run

From the project root:

```bash
# python 01_basic_chatbot/chatbot.py

Example
=== My Python Chatbot ===

You: hi
Bot: Hello sir!

You: how are you
Bot: I'm doing great! How can I help you?

You: what is python
Bot: Python is a fundamental programming language.

You: random
Bot: Unknown input.
Sorry sir, I don't understand that yet.

You: exit
Bot: Goodbye!