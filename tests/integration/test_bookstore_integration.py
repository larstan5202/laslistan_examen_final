from src.bookstore import BookStore

def test_bookstore_integration_add_and_favorite_flow():
    store = BookStore()

    # Lägg till två böcker
    b1 = store.addBook("Author1", "Title1")
    b2 = store.addBook("Author2", "Title2")

    # Favorisera första boken
    store.toggleFavorite(b1["id"])

    # Kontrollera att bara b1 är favorit
    assert b1 in store._favorites._favorites
    assert b2 not in store._favorites._favorites

    # Ta bort favorit
    store.toggleFavorite(b1["id"])
    assert b1 not in store._favorites._favorites
