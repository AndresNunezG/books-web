from django.urls import path, include
from .views import edit_book, index, new_book

urlpatterns = [
    path('', index, name="index"),
    path('new/', new_book, name="newbook"),
    path('edit/<int:isbn>', edit_book, name="editbook"),
    path('', include(('bookswebAPI.urls', 'createbook'), namespace='createbook')),
    path('', include(('bookswebAPI.urls', 'updatebook'), namespace='updatebook')),
]