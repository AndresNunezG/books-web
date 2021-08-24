from django.urls import path
from .views import booksListView, booksDetailView

urlpatterns = [
    path('books/', booksListView.as_view(), name='books_list'),
    path('book/<int:pk>/', booksDetailView.as_view(), name="book_get"),
]