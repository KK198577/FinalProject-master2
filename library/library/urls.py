"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from viewer.views import *

from account.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', new_books, name='home'),
    path('new_books/', new_books, name='new_books'),
    path('authors/', authors, name='authors'),
    path('genres/', genres, name='genres'),
    path('authors_ad/', authors_ad, name='authors_ad'),
    path('languages/', languages, name='languages'),
    path('conditions/', conditions, name='conditions'),
    path('author/<pk>/', author, name='author'),

    path('books/', BooksView.as_view(), name='books'),
    path('books/<page>', BooksView.as_view(), name='books'),

    path('new_book/', BookCreateView.as_view(), name='new_book'),
    path('book_update/<pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<pk>/', BookDeleteView.as_view(), name='book_delete'),

    path('new_author/', AuthorCreateView.as_view(), name='new_author'),
    path('author_update/<pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('author_delete/<pk>/', AuthorDeleteView.as_view(), name='author_delete'),

    path('new_genre/', GenreCreateView.as_view(), name='new_genre'),
    path('genre_update/<pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('genre_delete/<pk>/', GenreDeleteView.as_view(), name='genre_delete'),

    path('new_language/', LanguageCreateView.as_view(), name='new_language'),
    path('language_update/<pk>/', LanguageUpdateView.as_view(), name='language_update'),
    path('language_delete/<pk>/', LanguageDeleteView.as_view(), name='language_delete'),

    path('search/', search, name='search'),

    path('book/<pk>/', book, name='book'),

    path('accounts/signup', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),


]
