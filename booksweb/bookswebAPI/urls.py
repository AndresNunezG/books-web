from django.urls import path
from .views import book_list, book, create_book

urlpatterns = [
    path('books/', book_list, name='books_list'),
    path('book/<int:pk>/', book, name="book_get"),
    path('create-book/', create_book, name="createbook"),
]