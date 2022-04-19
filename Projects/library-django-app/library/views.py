from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import *

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'home'
        return context

class BookView(ListView):
    '''
    A Book List Page
    '''
    model = Book
    template_name = 'book_list.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'book'
        return context

class AuthorView(ListView):
    '''
    An Author of books List Page
    '''
    model = Author
    template_name = 'author_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'author'
        return context

class BookDetailView(DetailView):
    '''
    A Book Detailed Renting Page
    '''
    model = Book   # FK -> BookCopies
    template_name = 'book.html'

class BookDescView(DetailView):
    '''
    A Book Detailed Renting Page
    '''
    model = Book   # FK -> BookCopies
    template_name = 'book_desc.html'

class AuthorDetailView(DetailView):
    '''
    Author Detailed View Page
    '''
    model = Author
    template_name = 'author.html'

class MyBooksView(LoginRequiredMixin, ListView):
    model = BookCopies
    template_name = 'my_books.html'
    paginate_by = 5

    def get_queryset(self):
        return BookCopies.objects.filter(borrower=self.request.user).order_by('due_back')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'my_books'
        return context

class BookCopiesView(LoginRequiredMixin, ListView):
    model = BookCopies
    template_name = 'copies_list.html'
    paginate_by = 15

    # def get_queryset(self):
    #     return BookCopies.objects.filter(borrower=self.request.user).order_by('due_back')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'copies_list'
        return context

class AllBorrowedBooks(LoginRequiredMixin, ListView):
    model = BookCopies
    template_name = 'all_borrowed_books.html'
    paginate_by = 2

    def get_queryset(self):
        return BookCopies.objects.filter(status='o').order_by('due_back')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'all_borrowed_books'
        return context

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'new_book.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'new_book'
        return context

class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'new_author.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'new_author'
        return context

class BookCopiesCreateView(LoginRequiredMixin, CreateView):
    model = BookCopies
    template_name = 'new_copy.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'new_copy'
        return context

class BookCopiesUpdateView(LoginRequiredMixin, UpdateView):
    model = BookCopies
    template_name = 'copies_manage.html'
    fields = ['due_back', 'borrower', 'status']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'copies_manage'
        return context

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'search_result.html', {'books': books, 'query': q})
    else:
        return render(request, 'book_list.html')

def search_copies(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        copies = BookCopies.objects.filter(book__title__icontains=q)
        return render(request, 'search_copies_result.html', {'books': copies, 'query': q})
    else:
        return render(request, 'copies_list.html')
