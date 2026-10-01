import time
import pyautogui
import pyperclip
import pygetwindow as gw

from bot.config import (
    SEARCH_BOX,
    CHAT_AREA,
    MESSAGE_INPUT,
    CHAT_START,
    CHAT_END
)


def activate_whatsapp():
    windows = [
        window
        for window in gw.getAllWindows()
        if "WhatsApp" in window.title
        and not window.isMinimized
        and window.width > 500
        and window.height > 500
    ]

    if not windows:
        raise RuntimeError("WhatsApp Desktop window not found.")

    # Use the largest visible WhatsApp window
    whatsapp_window = max(
        windows,
        key=lambda window: window.width * window.height
    )

    whatsapp_window.activate()

    time.sleep(2)

    print("WhatsApp activated.")


def read_chat():
    # Keep this for now, but we are NOT relying on it yet
    pyautogui.moveTo(*CHAT_START)
    pyautogui.dragTo(*CHAT_END, duration=1, button="left")

    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)

    return pyperclip.paste()


def click_search_box():
    pyautogui.click(*SEARCH_BOX)


def click_message_input():
    pyautogui.click(*MESSAGE_INPUT)


def search_chat(name):
    click_search_box()

    time.sleep(0.5)

    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(name, interval=0.05)

    time.sleep(1)

    pyautogui.press("enter")

    time.sleep(1)
def send_message(message):
    click_message_input()

    time.sleep(0.3)

    # Copy the complete message to the clipboard
    pyperclip.copy(message)

    # Paste the message into WhatsApp
    pyautogui.hotkey("ctrl", "v")

    time.sleep(0.3)

    # Send
    pyautogui.press("enter")

    time.sleep(0.5)

    print("Message sent.")

if __name__ == "__main__":
    activate_whatsapp()

    send_message("what is python?")