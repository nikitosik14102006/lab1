from dataclasses import dataclass, field
from typing import List, Optional
@dataclass
class Book:
    title: str
    author: str
    year: int
    isbn: str
    is_available: bool = True
    def __str__(self) -> str:
        status = "Dostępna" if self.is_available else "Wypożyczona"
        return f"'{self.title}' - {self.author} ({self.year}) [{status}]"
    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, isbn={self.isbn!r}, is_available={self.is_available})"
@dataclass
class EBook(Book):
    format: str = "pdf"

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str} [Format: {self.format}]"


class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self.borrowed_books: List[Book] = []

    def __str__(self) -> str:
        return f"Czytelnik: {self.name} (ID: {self.member_id}), Wypożyczonych: {len(self.borrowed_books)}"

    def __repr__(self) -> str:
        return f"Member(name={self.name!r}, member_id={self.member_id!r}, borrowed_books={self.borrowed_books!r})"


class Library:
    def __init__(self):
        self._books: List[Book] = []
        self._members: List[Member] = []
    @property
    def books(self) -> List[Book]:
        return self._books

    def add_book(self, book: Book) -> None:
        self._books.append(book)
        print(f"Dodano książkę: {book.title}")

    def register_member(self, member: Member) -> None:
        self._members.append(member)
        print(f"Zarejestrowano czytelnika: {member.name}")

    def search_by_title(self, title: str) -> List[Book]:
        return [book for book in self._books if title.lower() in book.title.lower()]

    def search_by_author(self, author: str) -> List[Book]:
        return [book for book in self._books if author.lower() in book.author.lower()]

    def borrow(self, member_id: str, isbn: str) -> None:
        member = next((m for m in self._members if m.member_id == member_id), None)
        book = next((b for b in self._books if b.isbn == isbn), None)

        if not member:
            print(f"Błąd: Nie znaleziono czytelnika o ID '{member_id}'.")
            return
        if not book:
            print(f"Błąd: Nie znaleziono książki o ISBN '{isbn}'.")
            return
        if not book.is_available:
            print(f"Odmowa: Książka '{book.title}' jest obecnie wypożyczona.")
            return
        book.is_available = False
        member.borrowed_books.append(book)
        print(f"Sukces: Czytelnik '{member.name}' wypożyczył '{book.title}'.")

    def return_book(self, member_id: str, isbn: str) -> None:
        member = next((m for m in self._members if m.member_id == member_id), None)
        if not member:
            print(f"Błąd: Nie znaleziono czytelnika o ID '{member_id}'.")
            return

        book = next((b for b in member.borrowed_books if b.isbn == isbn), None)
        if not book:
            print(f"Błąd: Czytelnik '{member.name}' nie ma wypożyczonej książki o ISBN '{isbn}'.")
            return

        book.is_available = True
        member.borrowed_books.remove(book)
        print(f"Sukces: Czytelnik '{member.name}' zwrócił '{book.title}'.")

    def __str__(self) -> str:
        return f"Biblioteka Główna | Księgozbiór: {len(self._books)} | Czytelnicy: {len(self._members)}"

    def __repr__(self) -> str:
        return f"Library(books_count={len(self._books)}, members_count={len(self._members)})"


if __name__ == "__main__":
    my_library = Library()

    b1 = Book("Władca Pierścieni", "J.R.R. Tolkien", 1954, "978-0261102385")
    b2 = Book("Diuna", "Frank Herbert", 1965, "978-0441172719")
    eb1 = EBook("Czysty kod", "Robert C. Martin", 2008, "978-8328302341", format="epub")

    m1 = Member("Jan Kowalski", "M001")
    m2 = Member("Anna Nowak", "M002")
    my_library.add_book(b1)
    my_library.add_book(b2)
    my_library.add_book(eb1)
    my_library.register_member(m1)
    my_library.register_member(m2)

    print("\n--- Testowanie metod ---")
    my_library.borrow("M001", "978-0261102385")
    my_library.borrow("M002", "978-0261102385")
    my_library.borrow("M002", "978-8328302341")

    print("\n--- Stan systemu ---")
    print(b1)
    print(eb1)
    print(m1)
    print(my_library)

    print("\n--- Testowanie zwrotów ---")
    my_library.return_book("M001", "978-0261102385")
    print(b1)