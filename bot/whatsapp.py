import re

from playwright.sync_api import sync_playwright


class WhatsApp:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch_persistent_context(
            user_data_dir="./whatsapp_profile",
            headless=False
        )

        self.page = (
            self.browser.pages[0]
            if self.browser.pages
            else self.browser.new_page()
        )

        self.page.goto("https://web.whatsapp.com")

        print("Waiting for WhatsApp Web...")

        self.page.wait_for_selector(
            "#pane-side",
            timeout=60000
        )

        print("WhatsApp Web loaded.")

    def get_messages(self):
        messages = self.page.locator(
            "[data-pre-plain-text]"
        )

        results = []

        for i in range(messages.count()):

            message = messages.nth(i)

            try:
                metadata = message.get_attribute(
                    "data-pre-plain-text"
                )

                text_locator = message.locator(
                    '[data-testid="selectable-text"]'
                )

                if text_locator.count() > 0:
                    text = text_locator.first.inner_text().strip()
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
                    f"Could not read message {i}: {e}"
                )

        return results

    def get_latest_message(self):

        messages = self.get_messages()

        if not messages:
            return None

        # Work backwards so empty/media messages are skipped
        for message in reversed(messages):

            text = message["text"].strip()

            if not text:
                continue

            metadata = message["metadata"].strip()

            # Example:
            # [21:23, 01/10/2026] Dishika:
            match = re.search(
                r"\]\s*(.*?):\s*$",
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

    input("\nPress ENTER to close...")

    whatsapp.close()