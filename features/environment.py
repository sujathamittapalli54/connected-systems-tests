import allure
from playwright.sync_api import sync_playwright
from pathlib import Path
from datetime import datetime
import os

# Folder for screenshots
SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)

def before_all(context):
    """Start Playwright before all tests"""
    context.playwright = sync_playwright().start()
    # Headless controlled via environment variable
    headless = os.getenv("HEADLESS", "True").lower() == "true"
    context.browser = context.playwright.chromium.launch(headless=headless, slow_mo=500)
    context.context = context.browser.new_context()
    context.page = context.context.new_page()

def after_scenario(context, scenario):
    """Take a screenshot after each scenario"""
    outcome = "passed" if scenario.status == "passed" else "failed"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_name = scenario.name.replace(" ", "_")
    screenshot_file = SCREENSHOT_DIR / f"{test_name}_{outcome}_{timestamp}.png"

    # Capture screenshot
    context.page.screenshot(path=str(screenshot_file))

    # ✅ Attach to Allure
    allure.attach.file(
        str(screenshot_file),
        name=f"{scenario.name}_{outcome}",
        attachment_type=allure.attachment_type.PNG
    )
    print(f"[INFO] Screenshot ({outcome}) saved: {screenshot_file}")

def after_all(context):
    """Cleanup Playwright"""
    context.page.close()
    context.context.close()
    context.browser.close()
    context.playwright.stop()