from src.bookstore import FavoriteBooks

def test_add_adds_book_to_favorites():
    fav = FavoriteBooks()
    book = {"id": 1, "author": "Test", "title": "Bok"}
    fav.add(book)
    assert book in fav._favorites


def test_remove_removes_book_from_favorites():
    fav = FavoriteBooks()
    book = {"id": 1, "author": "Test", "title": "Bok"}
    fav._favorites.append(book)  # Arrange
    fav.remove(book)             # Act
    assert book not in fav._favorites
