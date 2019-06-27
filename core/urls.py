from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views



urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('books/', views.Books.as_view(), name='books'),
    path('books/<int:book_id>', views.ShowBook.as_view(), name='show_book'),
    path('authors', views.Authors.as_view(), name='authors'),
    path('authors/<int:author_id>', views.ShowAuthor.as_view(), name='show_author'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
