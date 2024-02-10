from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser_type = p.chromium
    browser = browser_type.launch()  # ブラウザを立ち上げる
    page = browser.new_page()  # タブを開く
    page.goto('https://setwithfriends.com/profile/Dx5H21FV8nRrhtM1jUV8ZopXFUj1')  # URLを開く
    ele = page.wait_for_selector("table")
    print(ele.inner_text())
    # page.screenshot(path=f'example-{browser_type.name}.png')
    browser.close()


