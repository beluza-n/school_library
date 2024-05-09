from django.contrib import admin
from django.urls import path, include

from school_library.views import book_list
from assets.views import asset_list

urlpatterns = [
    path('books', book_list, name='books'),
    path('assets', asset_list, name='assets'),
    path('admin/', admin.site.urls),
]
