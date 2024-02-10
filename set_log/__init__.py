from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()  # ブラウザを立ち上げる
        page = browser.new_page()  # タブを開く
        page.goto('http://playwright.dev')  # URLを開く
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()