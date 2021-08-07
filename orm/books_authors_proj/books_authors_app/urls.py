from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/', views.books_list),
    path('books/<int:book_id>/', views.book_info),
    path('books/<int:book_id>/add_author/', views.add_author_to_book),
    path('authors/', views.authors_list),
    path('authors/<int:author_id>/', views.author_info),
    path('authors/<int:author_id>/add_book/', views.add_book_to_author),
]