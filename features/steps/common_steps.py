from behave import given
from playwright.sync_api import sync_playwright

@given("att användaren öppnar webbsidan")
def step_open_page(context):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    context.page = browser.new_page()
    context.browser = browser
    context.page.goto("https://tap-ht25-testverktyg.github.io/exam/")
