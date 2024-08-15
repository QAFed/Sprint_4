Описание тестов:
1. test_class_init_data_correctly_created - правильность инициализации параметров экземпляра класса при его создании
2. test_add_new_book_if_len_name_out_of_range_not_added - книга не создается если длина имени не входит в диапазон 1-40 символов (КЭиГЗ)
3. test_add_new_book_if_len_name_in_range_added - книга создается если длина имени входит в диапазон 1-40 символов (КЭиГЗ)
4. test_add_new_book_if_book_already_exist_not_rewrite_value - попытка добавить книгу которая уже есть не перезаписывает жанр на пустое значение
5. test_set_book_genre_if_genre_and_name_is_exist - книге присваивается жанр если жанр и книга существуют в соответствующих списках
6. test_set_book_genre_if_genre_not_exist - жанр не присваивается к книге если он отсутствует в списке жанров
7. test_set_book_genre_if_name_not_exist - метод присвоения жанра не создает несуществующую книгу 
8. test_get_book_genre_by_name - возвращается верное значение жанра по названию книги
9. test_get_books_with_specific_genre_if_such_books_exist - возращается список книг заданного жанра
10. test_get_books_with_specific_genre_if_such_books_absent - возращается пустой список если книги заданного жанра отсутствуют в списке книг
11. test_get_books_with_specific_genre_if_book_list_empty - возращается пустой список если список книг пустой
12. test_get_books_with_specific_genre_if_genre_not_in_list - возращается пустой список если жанр отсутствует в списке жанров
13. test_get_books_genre - возвращается список книг переданный ранее в него
14. test_get_books_for_children - возвращает список книг если жанр книги не в списке ограничений жанров
15. test_add_book_in_favorites_if_name_in_list_and_not_in_favorites - в список избранных добавляется книга если она есть в списке книг и ее нет в избранном
16. test_add_book_in_favorites_if_name_not_in_list_and_not_in_favorites_not_added - не добавляется книга имени которой нет в списке книг
17. test_add_book_in_favorites_if_name_in_list_and_in_favorites_not_added - не добавляется книга повторно если она уже есть в избранном
18. test_delete_book_from_favorites - книга удаляется из избранного