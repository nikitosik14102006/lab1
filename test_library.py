import pytest
from biblioteka import Library, Book, Member


@pytest.fixture
def test_library():
    lib = Library()
    b1 = Book("Władca Pierścieni", "J.R.R. Tolkien", 1954, "978-0261102385")
    b2 = Book("Diuna", "Frank Herbert", 1965, "978-0441172719")
    m1 = Member("Jan Kowalski", "M001")

    lib.add_book(b1)
    lib.add_book(b2)
    lib.register_member(m1)

    return lib


def test_search_by_title(test_library):
    results = test_library.search_by_title("Władca")
    assert len(results) == 1
    assert results[0].title == "Władca Pierścieni"


def test_search_by_author(test_library):
    results = test_library.search_by_author("Herbert")
    assert len(results) == 1
    assert results[0].author == "Frank Herbert"


def test_borrow_success(test_library):
    test_library.borrow("M001", "978-0261102385")

    book = next(b for b in test_library.books if b.isbn == "978-0261102385")

    assert book.is_available is False
    assert len(test_library._members[0].borrowed_books) == 1


def test_borrow_unavailable(test_library, capsys):
    test_library.borrow("M001", "978-0261102385")

    test_library.borrow("M001", "978-0261102385")

    captured = capsys.readouterr()
    assert "Odmowa" in captured.out or "Błąd" in captured.out

    def test_add_and_register(test_library):
        nowa_ksiazka = Book("Python dla opornych", "Jan Kowalski", 2024, "111-222")
        nowy_czytelnik = Member("Testowy Czytelnik", "M999")

        test_library.add_book(nowa_ksiazka)
        test_library.register_member(nowy_czytelnik)

        assert len(test_library.books) == 3
        assert len(test_library._members) == 2

    def test_return_book(test_library):
        test_library.borrow("M001", "978-0261102385")

        test_library.return_book("M001", "978-0261102385")

        book = next(b for b in test_library.books if b.isbn == "978-0261102385")
        member = test_library._members[0]

        assert book.is_available is True
        assert len(member.borrowed_books) == 0