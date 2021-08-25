from django.http.response import HttpResponse
from django.shortcuts import redirect
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

def create_book(request, web="False"):
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
            if web == "False":
                return JsonResponse({'200': 'Object created'})
            else:
                return redirect('/')
    else:
        return HttpResponse("<h1>Invalid method</h1>")

def update_book(request, isbn, web="False"):
    if request.method == "POST":
        book_item = Book.objects.filter(isbn=isbn).values()
        book_item.name = request.POST['name']
        book_item.author_name = request.POST['author_name']
        book_item.category = request.POST['category']
        book_item.publication_date = request.POST['publication_date']
        book_item.isbn = request.POST['isbn']
        book_item.update()
        if web == "False":
            return JsonResponse({'200': 'Object updated'})
        else:
            return redirect('/')

def delete_book(request, isbn, web="False"):
    if request.method == "GET":
        book_item = Book.objects.filter(isbn=isbn)
        print(list(book_item.values()))
        book_item.delete()
        if web == "False":
            return JsonResponse({'200': 'Object deleted'})
        else:
            return redirect('/')