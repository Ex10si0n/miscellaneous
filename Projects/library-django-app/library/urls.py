from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookView.as_view(), name='book'),
    path('book/new/', views.BookCreateView.as_view(), name='new_book'),
    path('copy/new/', views.BookCopiesCreateView.as_view(), name='new_copy'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book_desc/<int:pk>/', views.BookDescView.as_view(), name='book_desc'),
    path('authors/', views.AuthorView.as_view(), name='author'),
    path('authors/new/', views.AuthorCreateView.as_view(), name='new_author'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('copies/<uuid:pk>/', views.BookCopiesUpdateView.as_view(), name='copies_manage'),
    path('copies_list/', views.BookCopiesView.as_view(), name='copies_list'),
    path('myBooks/', views.MyBooksView.as_view(), name='my_books'),
    path('allBorrowedBooks/', views.AllBorrowedBooks.as_view(), name='all_borrowed_books'),
    path('search/', views.search, name='search'),
    path('search_copies/', views.search_copies, name='search_copies'),
]
