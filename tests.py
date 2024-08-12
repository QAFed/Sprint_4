import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('param_name, param_value', [
        ('books_genre',{}),
        ('favorites',[]),
        ('genre',['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']),
        ('genre_age_rating', ['Ужасы', 'Детективы'])
    ])
    def test_class_init_data_correctly_created(self, param_name, param_value):
        collector = BooksCollector()
        assert getattr(collector, param_name) == param_value

    @pytest.mark.parametrize('name', [
        "",
        "41сорокОдин41сорокОдин41сорокОдин41сорONE",
        "50пятьДесятFIFTEEN5050пятьДесятFIFTEEN501111111111"
    ])
    def test_add_new_book_with_len_name_out_of_range_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    @pytest.mark.parametrize('name', [
        "1",
        "40Cорок40!40Sorok40!40сорок40!40сорок40!",
        "20dvadcatД20dvadcatД"
    ])
    def test_add_new_book_with_len_name_in_range_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    def test_add_new_book_then_book_already_exist_not_create(self):
        collector = BooksCollector()
        duble_book = "Duble_book"
        genre_book = 'Мультфильмы'
        collector.add_new_book(duble_book)
        collector.set_book_genre(duble_book, genre_book)
        collector.add_new_book(duble_book)
        assert collector.get_books_genre()[duble_book] == genre_book