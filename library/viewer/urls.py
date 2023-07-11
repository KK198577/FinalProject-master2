from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', new_books, name='home'),
    path('new_books/', new_books, name='new_books'),
    path('authors/', authors, name='authors'),

    path('books/', BooksView.as_view(), name='books'),
    path('books/<page>', BooksView.as_view(), name='books'),

    path('new_book/', BookCreateView.as_view(), name='new_book'),
    path('update/<pk>/', BookUpdateView.as_view(), name='book_update'),
    path('delete/<pk>/', BookDeleteView.as_view(), name='book_delete'),

    path('book/<pk>/', book, name='book')
]