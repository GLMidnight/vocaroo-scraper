import asyncio
import random
import string
from pyppeteer import launch
# DO NOT TOUCH BELOW
ERROR = ('<div class="ContentBox ContentBox--error"><div class="ContainerBox__header ContainerBox__header--error">Error</div>Sorry, the requested media could not be found. It may have expired or been deleted.</div>')
# DO NOT TOUCH ABOVE

EXECUTABLE_PATH = r'C:\Program Files\Google\Chrome\Application\chrome.exe' # CHANGE TO YOUR BROWSER IF REQUIRED. (CHROMIUM-BASED BROWSERS ONLY)

OUTPUT_FILE = "valid_links.txt"

def generate_vocaroo_id():
    if random.random() < 0.5:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=11))
    else:
        return '1' + ''.join(random.choices(string.ascii_letters + string.digits, k=11))

async def check_vocaroo_id(vocaroo_id, browser, sleep_delay):
    url = f'https://vocaroo.com/{vocaroo_id}'
    page = await browser.newPage()
    try:
        await page.goto(url)
        await asyncio.sleep(sleep_delay)
        content = await page.content()
        if ERROR in content:
            return False, vocaroo_id
        return True, vocaroo_id
    except Exception as e:
        print(f"Error checking ID {vocaroo_id}: {e}")
        return False, vocaroo_id
    finally:
        await page.close()

async def main():
    try:
        num_attempts = int(input("How many attempts? {default: 50} "))
    except ValueError:
        print("Using default value.")
        num_attempts = 50

    try:
        sleep_delay = float(input("How long to wait per attempt in seconds? {default: 3} "))
    except ValueError:
        print("Using default value.")
        sleep_delay = 3

    browser = await launch(
        executablePath=EXECUTABLE_PATH,
        headless=True,
        args=['--no-sandbox', '--disable-setuid-sandbox']
    )

    valid_ids = []
    for attempt in range(num_attempts):
        vocaroo_id = generate_vocaroo_id()
        is_valid, vid = await check_vocaroo_id(vocaroo_id, browser, sleep_delay)
        url = f"https://vocaroo.com/{vid}"
        status = "✅VALID" if is_valid else "❌INVALID"
        print(f"[{attempt + 1}/{num_attempts}] {status}: {url}")

        if is_valid:
            valid_ids.append(url)
            with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                f.write(url + "\n")

    await browser.close()

    if valid_ids:
        print(f"\n{len(valid_ids)} Valid Vocaroo URL(s) saved to '{OUTPUT_FILE}':")
        for url in valid_ids:
            print(url)
    else:
        print("\nNo valid Vocaroo URLs found.")

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())