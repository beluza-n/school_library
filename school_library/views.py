from django.shortcuts import render
from .models import Book, Author
from django.db import connection
from django.db.models import Q


def book_list(request):
    # french_authors = Author.objects.filter(language="Французский").values_list('id', flat=True)


    books = Book.objects.all().filter(Q(author_id__in=[1, 2, 3]) | Q(author_id__is_active=True)).union(
        Book.objects.all().filter(Q(author_id__in=[4, 5, 6]) | Q(author_id__is_active=True))
        )

    print(books)
    print(connection.queries)

    template = 'book_list.html'
    context = {'books': books}
    return render(request, template, context)