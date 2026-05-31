from behave import given, then
from playwright.sync_api import sync_playwright

@then("ska bokkatalogen visas")
def step_catalog_visible(context):
    # katalogen har data-testid="book-list"
    catalog = context.page.get_by_test_id("book-list")
    assert catalog.is_visible()
