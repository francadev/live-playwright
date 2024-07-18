from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        color_scheme='dark',
        record_video_dir='.', 
        record_video_size={"width": 640, "height": 480}
    )

    page = context.new_page()
    page.goto('https://playwright.dev')

    page.screenshot(
        path='ss.png',
        full_page=True
    )

    print(page.title())
    sleep(2)
    browser.close()