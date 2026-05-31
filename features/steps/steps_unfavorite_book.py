from behave import given, when, then

@given("att användaren har en favoritbok")
def step_user_has_favorite(context):
    # Vi utgår från att common_steps.py redan har öppnat sidan
    # Om inte: se till att feature-filen först har steget
    # "Given att användaren öppnar webbsidan"
    first_button = context.page.get_by_test_id("favorite-button").first
    first_button.click()

@when("användaren avmarkerar boken som favorit")
def step_unfavorite(context):
    fav_card = context.page.get_by_test_id("favorite-card").first
    fav_button = fav_card.get_by_test_id("favorite-button")
    fav_button.click()

@then("ska boken inte längre visas i favoritlistan")
def step_not_in_favorites(context):
    fav_cards = context.page.get_by_test_id("favorite-card")
    assert fav_cards.count() == 0

