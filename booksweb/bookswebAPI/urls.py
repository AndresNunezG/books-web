from django.urls import path
from .views import book_list, book, create_book, delete_book, update_book

urlpatterns = [
    path('books/', book_list, name='books_list'),
    path('book/<int:pk>/', book, name="book_get"),
    path('create-book/', create_book, name="createbook"),
    path('create-book/<str:web>', create_book, name="createbook"),
    path('update-book/<int:isbn>/', update_book, name="updatebook"),
    path('delete-book/<int:isbn>/', delete_book, name="deletebook"),
    path('update-book/<int:isbn>/<str:web>/', update_book, name="updatebook"),
    path('delete-book/<int:isbn>/<str:web>/', delete_book, name="deletebook"),
]