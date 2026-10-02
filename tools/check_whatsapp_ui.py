
from playwright.sync_api import sync_playwright


def get_messages(page):
    messages = page.locator("[data-pre-plain-text]")

    results = []

    for i in range(messages.count()):
        message = messages.nth(i)

        try:
            metadata = message.get_attribute("data-pre-plain-text")

            text_locator = message.locator(
                '[data-testid="selectable-text"]'
            )

            if text_locator.count() > 0:
                text = text_locator.first.inner_text().strip()
            else:
                text = ""

            results.append({
                "metadata": metadata.strip() if metadata else "",
                "text": text
            })

        except Exception as e:
            print(f"Could not read message {i}: {e}")

    return results


with sync_playwright() as p:

    browser = p.chromium.launch_persistent_context(
        user_data_dir="./whatsapp_profile",
        headless=False
    )

    page = browser.pages[0] if browser.pages else browser.new_page()

    page.goto("https://web.whatsapp.com")

    print("Waiting for WhatsApp Web...")

    page.wait_for_selector("#pane-side", timeout=60000)

    print("WhatsApp Web loaded.")

    input("Open the chat you want to monitor, then press ENTER...")

    messages = get_messages(page)

    print(f"\nFound {len(messages)} messages.\n")

    for message in messages:
        print(f"Metadata: {message['metadata']}")
        print(f"Text: {message['text']}")
        print("-" * 50)

    input("\nPress ENTER to close...")

    browser.close()