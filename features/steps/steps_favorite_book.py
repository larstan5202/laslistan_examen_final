from behave import given, when, then
from playwright.sync_api import sync_playwright

@when("användaren markerar första boken som favorit")
def step_mark_favorite(context):
    # första boken har en favorit-knapp med data-testid="favorite-button"
    first_button = context.page.get_by_test_id("favorite-button").first
    first_button.click()

@then("ska boken visas i favoritlistan")
def step_favorite_list(context):
    fav_list = context.page.get_by_test_id("favorite-list")
    assert fav_list.is_visible()
    # kontrollera att minst ett favoritkort finns
    fav_cards = context.page.get_by_test_id("favorite-card")
    assert fav_cards.count() > 0
