import pytest
from data import test_data
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
    def test_add_new_book_if_len_name_out_of_range_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    @pytest.mark.parametrize('name', [
        "1",
        "40Cорок40!40Sorok40!40сорок40!40сорок40!",
        "20dvadcatД20dvadcatД"
    ])
    def test_add_new_book_if_len_name_in_range_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    def test_add_new_book_if_book_already_exist_not_rewrite_value(self):
        collector = BooksCollector()
        duble_book = "Duble book"
        genre_book = 'Мультфильмы'
        collector.add_new_book(duble_book)
        collector.set_book_genre(duble_book, genre_book)
        collector.add_new_book(duble_book)
        assert collector.get_books_genre()[duble_book] == genre_book

    def test_set_book_genre_if_genre_and_name_is_exist(self):
        collector = BooksCollector()
        new_book = "New book"
        genre_book = 'Мультфильмы'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, genre_book)
        assert collector.get_books_genre()[new_book] == genre_book

    def test_set_book_genre_if_genre_not_exist(self):
        collector = BooksCollector()
        new_book = 'Лунтик'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book,'Хоррор')
        assert collector.get_books_genre()[new_book] == ''

    def test_set_book_genre_if_name_not_exist(self):
        collector = BooksCollector()
        new_book = "New book"
        collector.set_book_genre(new_book, 'Мультфильмы')
        assert collector.get_books_genre().get(new_book) == None

    def test_get_book_genre_by_name(self):
        collector = BooksCollector()
        new_book = "New book"
        genre = 'Мультфильмы'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, genre)
        assert collector.get_book_genre(new_book) == genre


    def test_get_books_with_specific_genre_if_such_books_exist(self, load_test_data):
        collector = load_test_data
        assert collector.get_books_with_specific_genre('Фантастика') == ['Доллар по 30', 'Дороги без ям']

    def test_get_books_with_specific_genre_if_such_books_absent(self, load_test_data):
        collector = load_test_data
        assert collector.get_books_with_specific_genre('Мультфильмы') == []

    def test_get_books_with_specific_genre_if_book_list_empty(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_with_specific_genre_if_genre_not_in_list(self):
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre('Хоррор') == []

    def test_get_books_genre(self, load_test_data):
        collector = load_test_data
        assert collector.get_books_genre() == test_data

    def test_get_books_for_children(self, load_test_data):
        collector = load_test_data
        assert collector.get_books_for_children() == ['Доллар по 30','Дороги без ям']

    def test_add_book_in_favorites_if_name_in_list_and_not_in_favorites(self, load_test_data):
        collector = load_test_data
        fav_book = 'Синий трактор'
        collector.add_book_in_favorites(fav_book)
        assert collector.get_list_of_favorites_books()[0] == fav_book

    def test_add_book_in_favorites_if_name_not_in_list_and_not_in_favorites_not_added(self, load_test_data):
        collector = load_test_data
        fav_book = 'Залётная книга'
        collector.add_book_in_favorites(fav_book)
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_if_name_in_list_and_in_favorites_not_added(self, load_test_data):
        collector = load_test_data
        fav_book = 'Кто правит исходники на GIT'
        collector.add_book_in_favorites(fav_book)
        collector.add_book_in_favorites(fav_book)
        assert collector.get_list_of_favorites_books() == ['Кто правит исходники на GIT']

    def test_delete_book_from_favorites(self, load_test_data):
        collector = load_test_data
        fav_book = 'Кто правит исходники на GIT'
        collector.add_book_in_favorites(fav_book)
        collector.delete_book_from_favorites(fav_book)
        assert fav_book not in collector.get_list_of_favorites_books()