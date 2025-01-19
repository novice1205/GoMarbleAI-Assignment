from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://2717recovery.com/products/recovery-cream")
    print(page.content())  # Verify page is loading properly
    browser.close()
