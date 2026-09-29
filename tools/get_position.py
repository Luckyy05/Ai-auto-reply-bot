import time
import pyautogui

print("Move your mouse to the target location.")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"\rX: {x:4}   Y: {y:4}", end="", flush=True)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n\nStopped.")