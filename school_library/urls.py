from django.urls import path
from . import views

app_name = 'school_library'

urlpatterns = [
    path('', views.book_list, name='index'),
]