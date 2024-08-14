import pytest
from data import test_data
from main import BooksCollector

@pytest.fixture
def load_test_data():
    collector = BooksCollector()
    for name, genre in test_data.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector