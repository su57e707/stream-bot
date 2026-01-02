import asyncio
from pyppeteer import launch
import os

# --- STREAM BOT AGENT ---

# --- CONFIGURATION ---
# These will be loaded from GitHub secrets.
DISCORD_EMAIL = os.environ.get("DISCORD_EMAIL")
DISCORD_PASSWORD = os.environ.get("DISCORD_PASSWORD")
SERVER_NAME = os.environ.get("SERVER_NAME")
VOICE_CHANNEL_NAME = os.environ.get("VOICE_CHANNEL_NAME")

# This is the URL the agent will stream. We will make this dynamic later.
# For now, it's a test URL.
STREAM_URL = "https://www.youtube.com/"

async def main( ):
    print("--- Starting STREAM Bot Agent ---")
    
    if not all([DISCORD_EMAIL, DISCORD_PASSWORD, SERVER_NAME, VOICE_CHANNEL_NAME]):
        print("FATAL ERROR: One or more environment variables (secrets) are missing.")
        return

    browser = None
    try:
        # Launch the browser inside the virtual screen (Xvfb)
        print("Launching browser...")
        browser = await launch(
            headless=False,
            executablePath='/usr/bin/google-chrome-stable',
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--start-maximized',
                '--window-size=1920,1080',
            ],
            env={'DISPLAY': ':99'} # Connects to the virtual screen
        )
        
        page = await browser.newPage()
        await page.setViewport({'width': 1920, 'height': 1080})

        # --- Login to Discord ---
        print("Navigating to Discord login...")
        await page.goto('https://discord.com/login', {'waitUntil': 'networkidle2'} )
        
        print("Entering credentials...")
        await page.type('input[name="email"]', DISCORD_EMAIL)
        await page.type('input[name="password"]', DISCORD_PASSWORD)
        await page.click('button[type="submit"]')
        
        print("Waiting for login to complete...")
        await page.waitForNavigation({'waitUntil': 'networkidle2'})
        await page.waitForSelector("div[aria-label='Servers']", {'timeout': 60000})
        print("Login successful!")
        await asyncio.sleep(5)

        # --- Join Voice Channel ---
        print(f"Searching for server: '{SERVER_NAME}'...")
        server_selector = f"//div[@aria-label='Servers']//div[text()='{SERVER_NAME[0]}']" # Matches server icon by first letter
        server_link = await page.waitForXPath(server_selector)
        await server_link.click()
        print("Server found.")
        await asyncio.sleep(3)

        print(f"Searching for voice channel: '{VOICE_CHANNEL_NAME}'...")
        channel_selector = f"//div[contains(@class, 'channelName')]//div[text()='{VOICE_CHANNEL_NAME}']"
        channel_link = await page.waitForXPath(channel_selector)
        await channel_link.click()
        print("Voice channel joined.")
        await asyncio.sleep(5)

        # --- Open New Tab and Go to Stream URL ---
        print(f"Opening new tab for URL: {STREAM_URL}")
        stream_page = await browser.newPage()
        await stream_page.goto(STREAM_URL, {'waitUntil': 'networkidle2'})
        print("Stream page loaded.")

        # --- FUTURE STEP: Initiate Screen Share ---
        # The logic to click the "Screen Share" button will go here.
        # For now, the agent will just sit in the channel.
        
        print("--- STREAM Bot Agent is running. ---")
        await asyncio.Event().wait() # Keep the script running

    except Exception as e:
        print(f"An error occurred: {e}")
        if page:
            await page.screenshot({'path': 'error.png'})
    finally:
        if browser:
            await browser.close()
        print("--- STREAM Bot Agent has shut down. ---")

if __name__ == "__main__":
    asyncio.run(main())
