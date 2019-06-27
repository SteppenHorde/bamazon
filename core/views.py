from django.views import generic, View
from django.core.paginator import Paginator

from .models.bamazon import Author, Tag, Book



class Main(generic.TemplateView): # основная страничка магазина
    template_name = 'core/main.html'


class Books(generic.ListView): # список книг
    template_name = 'core/books.html'
    model = Book
    context_object_name = 'books_list'
    paginate_by = 2 # пагинация

    def get_queryset(self):
        # вытаскиваем все книги, затем формируем список кортежей из книги, авторов и тэгов
        # этот список кортежей раскладываем в шаблоне
        all_books_list = Book.objects.all().order_by('-pub_date')
        books_list = list()
        for book in all_books_list:
            authors = book.authors.all()
            tags = book.tags.all()
            books_list.append((book, authors, tags))

        return books_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShowBook(generic.TemplateView): # отдельная книга
    template_name = 'core/show_book.html'

    def get_context_data(self, *args, **kwargs):
        # вытаскиваем книгу из БД по id и отправляем в контекст шаблона
        book_id = kwargs['book_id']
        book = Book.objects.get(pk=book_id)
        context = {
            'book': book,
        }

        return context


class Authors(generic.ListView): # авторы
    template_name = 'core/authors.html'
    model = Author
    context_object_name = 'authors_list'
    paginate_by = 3 # пагинация (в шаблоне 3 колонки)

    def get_context_data(self, **kwargs):
        # тут вообще вьюха всё делает за нас - вытаскивает всех авторов и пагинирует
        context = super().get_context_data(**kwargs)
        return context


class ShowAuthor(generic.TemplateView): # отдельный блог со всеми постами
    template_name = 'core/show_author.html'

    def get_context_data(self, *args, **kwargs):
        # вытаскиваем все книги определённого автора
        # затем формируем список кортежей из книги, авторов и тэгов
        # этот список кортежей раскладываем в шаблоне
        author_id = kwargs['author_id']
        author = Author.objects.get(pk=author_id)
        all_books_list = author.book_set.all().order_by('-pub_date')
        books_list = list()
        for book in all_books_list:
            authors = book.authors.all()
            tags = book.tags.all()
            books_list.append((book, authors, tags))

        context = {
            'author': author,
            'books_list': books_list,
        }

        return context
