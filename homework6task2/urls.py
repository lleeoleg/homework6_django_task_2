from django.contrib import admin
from django.urls import path
from app.views import create_child, create_parent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', create_parent),
    path('create_child/', create_child)
]
