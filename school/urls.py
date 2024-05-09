from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('school_library.urls', namespace='school_library')),
    path('admin/', admin.site.urls),
]
