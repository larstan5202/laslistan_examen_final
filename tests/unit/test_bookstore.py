from src.bookstore import BookStore

def test_addBook_adds_book_with_id():
    store = BookStore()
    book = store.addBook("Author", "Title")
    assert book["author"] == "Author"
    assert book["title"] == "Title"
    assert "id" in book
    assert book in store._books


def test_toggleFavorite_adds_book_to_favorites_when_not_favorite():
    store = BookStore()
    book = store.addBook("A", "B")
    store.toggleFavorite(book["id"])
    assert book in store._favorites._favorites


def test_toggleFavorite_removes_book_from_favorites_when_already_favorite():
    store = BookStore()
    book = store.addBook("A", "B")
    store.toggleFavorite(book["id"])  # add
    store.toggleFavorite(book["id"])  # remove
    assert book not in store._favorites._favorites
