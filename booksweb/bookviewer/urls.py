from django.urls import path, include
from .views import edit_book

urlpatterns = [
    path('', include(('bookswebAPI.urls', 'createbook'), namespace='createbook')),
    path('edit/<int:isbn>', edit_book, name="editbook"),
]