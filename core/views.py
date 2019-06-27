from django.views import generic, View

from .models.blog import Author, Tag, Book



class Main(generic.TemplateView): # основная страничка магазина
    template_name = 'core/main.html'


class Books(generic.ListView): # список книг
    template_name = 'core/books.html'
    model = Book
    paginate_by = 2 # пагинация

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context


class ShowBook(generic.TemplateView): # отдельная книга
    template_name = 'core/show_book.html'

    def get_context_data(self, *args, **kwargs):
        book_id = kwargs['book_id']
        book = Book.objects.get(pk=book_id)
        context = {
            'book': book,
        }

        return context


class Authors(generic.ListView): # автор
    template_name = 'core/authors.html'
    model = Author
    paginate_by = 5 # пагинация

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context


class ShowAuthor(generic.TemplateView): # отдельный блог со всеми постами
    template_name = 'core/show_author.html'

    def get_context_data(self, *args, **kwargs):
        author_id = kwargs['author_id']
        author = Author.objects.get(pk=author_id)
        books_list = author.books_set.all().order_by('-pub_date')
        context = {
            'books_list': books_list,
        }

        return context
