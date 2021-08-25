from bookswebAPI.models import Book
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    books_list = list(Book.objects.all().values())
    html = ''
    header = """
        <h1>Books Viewer</h1>
    """
    for book in books_list:
        html += "<ul>"
        html+=f"<li>{book['name']}</li>"
        html+=f"<li>{book['author_name']}</li>"
        html+=f"<li>{book['category']}</li>"
        html+=f"<li>{book['isbn']}</li>"
        html+=f"<li>{book['publication_date']}</li>"
        html += "</ul>"
    return HttpResponse(html)