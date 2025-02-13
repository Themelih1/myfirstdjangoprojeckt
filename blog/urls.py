from django.urls import path
from . import views


#  url =http://127.0.0.1:8000               ==> index
#  url =http://127.0.0.1:8000/index       ==> index
#  url =http://127.0.0.1:8000/blogs        ==> blogs
#  url =http://127.0.0.1:8000/blogs/5         ==> blogs-detail


# blogapp/urls.py
urlpatterns = [
    path("", views.index, name="Home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("blogs/<int:id>", views.blogsdetails, name="blogs-details"),  # 'blogs-details' doğru tanımlanmalı
]
