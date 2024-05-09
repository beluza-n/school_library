from django.shortcuts import render
from .models import Book, Author
from django.db import connection
from django.db.models import Q


def book_list(request):
    books = Book.objects.all().filter(Q(author_id__in=[2, 3, 5]) | Q(author_id__is_active=True)).union(
        Book.objects.all().filter(Q(author_id__in=[7, 8, 9]) | Q(author_id__is_active=True))
        )

    print(books)
    print(connection.queries)

    template = 'book_list.html'
    context = {'books': books}
    return render(request, template, context)