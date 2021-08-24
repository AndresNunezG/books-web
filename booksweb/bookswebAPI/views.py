from django.views import View
from .models import Book
from django.http import JsonResponse
from django.forms import model_to_dict

# Create your views here.
class booksListView(View):
    def get(self, request):
        if ('name' in request.GET):
            book_list = Book.objects.filter(name__contains=request.GET['name'])
        else:
            book_list = Book.objects.all()
        return JsonResponse(list(book_list.values()), safe=False)

class booksDetailView(View):
    def get(self, request, pk):
        if pk > len(list(Book.objects.all().values())):
            return JsonResponse({})
        else:
            book_detail = Book.objects.get(pk=pk)
        return JsonResponse(model_to_dict(book_detail))