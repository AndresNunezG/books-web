from bookswebAPI.models import Book
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    books_list = list(Book.objects.all().values())
    return render(request, 'index.html',{
        'books_list': books_list,
    })