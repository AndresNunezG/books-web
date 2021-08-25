from bookswebAPI.models import Book
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        books_list = list(Book.objects.all().values())
        return render(request, 'index.html',{
            'books_list': books_list,
        })

def new_book(request):
    return render(request, 'new_book.html')

def edit_book(request, isbn):
    book = list(Book.objects.filter(isbn=isbn).values())[0]
    date = str(book['publication_date'])
    print(book)
    return render(request, 'edit_book.html',{
        'book': book,
        'date': date,
    })