from behave import when, then

@when('användaren lägger till en ny bok med författare "Testförfattare" och titel "Testtitel"')
def step_add_book(context):
    page = context.page

    # öppna formuläret
    page.get_by_role("button", name="Lägg till bok").click()

    # fyll i formuläret via label i stället för test-id
    page.get_by_label("Författare").fill("Testförfattare")
    page.get_by_label("Titel").fill("Testtitel")

    # skicka formuläret
    page.get_by_role("button", name="Spara").click()

@then("ska den nya boken visas i katalogen")
def step_book_visible(context):
    page = context.page
    catalog = page.get_by_test_id("book-list")
    assert catalog.get_by_text("Testtitel").is_visible()

