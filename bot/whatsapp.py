import re
import time 
from playwright.sync_api import sync_playwright
from pathlib import Path
from playwright.sync_api import sync_playwright

class WhatsApp:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        # self.playwright = sync_playwright().start()

        # self.browser = self.playwright.chromium.launch_persistent_context(
        #     user_data_dir="./whatsapp_profile",
        #     headless=False
        # )

        # self.page = (
        #     self.browser.pages[0]
        #     if self.browser.pages
        #     else self.browser.new_page()
        # )

        # self.page.goto("https://web.whatsapp.com")

        # print("Waiting for WhatsApp Web...")

        # self.page.wait_for_selector(
        #     "#pane-side",
        #     timeout=60000
        # )

        # print("WhatsApp Web loaded.")
        self.playwright = sync_playwright().start()

    # Resolve the profile relative to the project root
        profile_path = (
                Path(__file__).resolve().parent.parent / "whatsapp_profile"
        )
        profile_path.mkdir(parents=True, exist_ok=True)

        print(f"Using WhatsApp profile: {profile_path}")

        self.browser = self.playwright.chromium.launch_persistent_context(
                user_data_dir=str(
                Path(__file__).resolve().parent.parent / "whatsapp_test_profile"
),
                headless=False
            )

        self.page = (
                self.browser.pages[0]
                if self.browser.pages
                else self.browser.new_page()
        )

        self.page.goto("https://web.whatsapp.com")

        print("Waiting for WhatsApp Web...")

        self.page.wait_for_selector("#pane-side", timeout=60000)  

        print("WhatsApp Web loaded.")

    def get_messages(self):

        messages = self.page.locator(
            "[data-pre-plain-text]"
        )

        results = []
        # take a snapshot of the currnet number pf messages
        message_count =  messages.count()

        for i in range(messages.count()):

            message = messages.nth(i)

            try:
                metadata = message.get_attribute(
                    "data-pre-plain-text",
                    timeout=2000                )

                text_locator = message.locator(
                    '[data-testid="selectable-text"]'
                )

                if text_locator.count() > 0:
                    text = text_locator.first.inner_text(
                        timeout=2000
                    ).strip()
                else:
                    text = ""

                results.append({
                    "metadata": metadata.strip()
                    if metadata
                    else "",
                    "text": text
                })

            except Exception as e:
                print(
                    f"Skipping  message {i}: {type(e).__name__}"
                )

        return results

    def get_latest_message(self):

        messages = self.get_messages()

        if not messages:
            return None

        for message in reversed(messages):

            text = message["text"].strip()

            if not text:
                continue

            metadata = message["metadata"].strip()

            # Example:
            # [21:23, 01/10/2026] Dishika:
            match = re.search(
                r"\]\s([^:]+):\s*$",
                metadata
            )

            if match:
                sender = match.group(1).strip()
            else:
                sender = ""

            return {
                "sender": sender,
                "text": text,
                "metadata": metadata
            }

        return None

    def send_message(self, message):

        message_box = self.page.locator(
            'div[contenteditable="true"][data-tab="10"]'
        )

        message_box.click()

        message_box.fill(message)

        self.page.keyboard.press("Enter")

    def wait_for_new_message(self, old_message):
        while True:
            latest = self.get_latest_message()

            if latest and latest["metadata"] != old_message["metadata"]:
                return latest
            time.sleep(3)

    def close(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()


if __name__ == "__main__":

    whatsapp = WhatsApp()

    whatsapp.start()

    input(
        "Open the chat you want to monitor, "
        "then press ENTER..."
    )

    latest = whatsapp.get_latest_message()

    print("\n--- LATEST MESSAGE ---")

    if latest:
        print("Sender:", latest["sender"])
        print("Message:", latest["text"])
        print("Metadata:", latest["metadata"])
    else:
        print("No text message found.")

    whatsapp.send_message("Hi")

    input("\nPress ENTER to close...")

    whatsapp.close()