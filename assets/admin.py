from django.contrib import admin
from .models import Book, Magazine, Newspaper, Asset

admin.site.register(Book)
admin.site.register(Magazine)
admin.site.register(Newspaper)
admin.site.register(Asset)