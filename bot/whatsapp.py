import pyautogui
import pyperclip
import time

from config import SEARCH_BOX, CHAT_AREA, MESSAGE_INPUT, CHAT_START, CHAT_END


def read_chat():
    # Move to the chat area and select visible text
    pyautogui.moveTo(*CHAT_START)
    pyautogui.dragTo(*CHAT_END, duration=1, button="left")

    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)

    chat_text = pyperclip.paste()
    return chat_text


def click_search_box():
    pyautogui.click(*SEARCH_BOX)


def click_message_input():
    pyautogui.click(*MESSAGE_INPUT)


def search_chat(name):
    click_search_box()

    time.sleep(0.5)
    pyautogui.write(name, interval=0.05)

    time.sleep(1)

    pyautogui.press("enter")


if __name__ == "__main__":
    print("move to whatsapp")
    
    time.sleep(4)
    chat_text = read_chat()
    print("\n ---- CHAT TEXT ----")
    print(chat_text)