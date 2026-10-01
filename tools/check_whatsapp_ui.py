import time
import pyautogui
import pyperclip

print("Switch to WhatsApp in 3 seconds...")
time.sleep(3)

pyperclip.copy("")

# Click somewhere in the chat message area
pyautogui.click(1000, 600)

time.sleep(0.5)

# Try selecting text using keyboard
pyautogui.hotkey("ctrl", "a")

time.sleep(0.5)

pyautogui.hotkey("ctrl", "c")

time.sleep(1)

print("Copied:", repr(pyperclip.paste()))