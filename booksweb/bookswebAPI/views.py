from django.http.response import HttpResponse
from django.views import View
from .models import Book
from django.http import JsonResponse
from django.forms import model_to_dict

# Create your views here.
def book_list(request):
    if request.method == 'GET':
        if ('name' in request.GET):
            book_list = Book.objects.filter(name__contains=request.GET['name'])
        else:
            book_list = Book.objects.all()
        return JsonResponse(list(book_list.values()), safe=False)
    else:
        return HttpResponse("<h1>Invalid method</h1>")

def book(request, pk):
    if request.method == 'GET':
        if pk > len(list(Book.objects.all().values())):
            return HttpResponse("<h1>Index Exceeded</h1>")
        else:
            book_detail = Book.objects.get(pk=pk)
        return JsonResponse(model_to_dict(book_detail))
    else:
        return HttpResponse("<h1>Invalid method</h1>")

def create_book(request):
    if request.method ==  "POST":
        isbn = request.POST['isbn']
        if isbn not in Book.objects.filter(name__contains=isbn):
            name = request.POST['name']
            author_name = request.POST['author_name']
            category = request.POST['category']
            publication_date = request.POST['publication_date']
            book_item = Book(
                name = name,
                author_name = author_name,
                category = category,
                isbn = isbn,
                publication_date = publication_date,
            )
            book_item.save()
            return HttpResponse("<h1>Book saved</h1>")
    else:
        return HttpResponse("<h1>Invalid method</h1>")
    
def edit_book(request):
    if request.method == "POST":
        return HttpResponse("<h1>Book Updated</h1>")
    else:
        return HttpResponse("<h1>Invalid method</h1>")