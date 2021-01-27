from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo

# Create your views here.

def my_render(request, template_path, context_dict):
    '''
    Using Template File
    '''
    temp = loader.get_template(template_path)
    # 2. Pass Data to Template
    context = {}
    # 3. Render Template
    res_html = temp.render(context, request)
    # 4. Return to Browser
    return HttpResponse(res_html)

# 1. Define View Function, HttpRequest
# 2. Configure URL, map URL to View
# http://127.0.0.1:8000/index
def index(request):
    # Processing, interact with M and T
    # Return HttpResponse Object to Browser
    # return my_render(request, 'booktest/index.html')
    return render(request, 'booktest/index.html', {'content': 'Hello World', 'date': date.today(), 'list': list(range(10))})

def show_books(request):
    # 1. Get Book Data from Database using M
    books = BookInfo.objects.all()
    return render(request, 'booktest/show_books.html', {'books': books})

def detail(request, bid):
    '''
    Queries Characters of Books
    '''
    # 1. Queries Book according to bid
    book = BookInfo.objects.get(id=bid)
    # 2. Queries Characters related to the Book
    heros = book.character_set.all()
    # 3. Show Data using Template
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})


    
