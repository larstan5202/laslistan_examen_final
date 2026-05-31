class FavoriteBooks:
    def __init__(self):
        self._favorites = []

    def add(self, book):
        self._favorites.append(book)

    def remove(self, book):
        if book in self._favorites:
            self._favorites.remove(book)
class BookStore:
    def __init__(self):
        self._books = []
        self._favorites = FavoriteBooks()
        self._next_id = 1

    def addBook(self, author, title):
        raise NotImplementedError

    def toggleFavorite(self, book_id):
        raise NotImplementedError
class BookStore:
    def __init__(self):
        self._books = []
        self._favorites = FavoriteBooks()
        self._next_id = 1

    def addBook(self, author, title):
        book = {
            "id": self._next_id,
            "author": author,
            "title": title
        }
        self._books.append(book)
        self._next_id += 1
        return book

    def toggleFavorite(self, book_id):
        # hitta boken
        book = next((b for b in self._books if b["id"] == book_id), None)
        if not book:
            return  # inget att göra

        # om boken redan är favorit → ta bort
        if book in self._favorites._favorites:
            self._favorites.remove(book)
        else:
            self._favorites.add(book)
