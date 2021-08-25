from django.urls import path, include

urlpatterns = [
    path('', include(('bookswebAPI.urls', 'createbook'), namespace='createbook')),
]