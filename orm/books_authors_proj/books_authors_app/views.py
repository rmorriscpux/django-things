from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'index.html')

def books_list(request):
    context = {
        'all_books' : Book.objects.all()
    }
    return render(request, 'books_list.html', context)

def book_info(request, book_id):
    try:
        book_request = Book.objects.get(id=book_id)
    except:
        return redirect('/books/') # Go to base book list if book_id value does not exist.
    else:
        context = {
            'selected_book' : book_request,
            'book_authors' : book_request.authors.all(),
            'non_authors' : Author.objects.all().difference(book_request.authors.all()),
        }
        return render(request, 'book_info.html', context)

def authors_list(request):
    context = {
        'all_authors' : Author.objects.all()
    }
    return render(request, 'authors_list.html', context)

def author_info(request, author_id):
    try:
        author_request = Author.objects.get(id=author_id)
    except:
        return redirect('/authors/') # Go to base author list if author_id value does not exist.
    else:
        context = {
            'selected_author' : author_request,
            'authored_books' : author_request.books.all(),
            'not_authored_books' : Book.objects.all().difference(author_request.books.all()),
        }
        return render(request, 'author_info.html', context)

def add_book_to_author(request, author_id):
    # Ideally change logic to ensure that the book is valid.
    if request.method == "POST":
        if request.POST['book_id'] != "":
            Author.objects.get(id=author_id).books.add(Book.objects.get(id=int(request.POST['book_id'])))
    return redirect('/authors/' + str(author_id) + '/') # End on going back to author_info

def add_author_to_book(request, book_id):
    # Ideally change logic to ensure that the author is valid.
    if request.method == "POST":
        if request.POST['author_id'] != "":
            Book.objects.get(id=book_id).authors.add(Author.objects.get(id=int(request.POST['author_id'])))
    return redirect('/books/' + str(book_id) + '/') # End on going back to book_info