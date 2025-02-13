from calendar import c
from django.shortcuts import render
from django.http import HttpResponse

data = {"blogs":[
        {
        "id":1,
        "title":"C++ Ile Programlama",
        "image":"1.png",
        "is_active":True,
        "is_home" : True,
        "description":"Tam aradiginiz kurs  burada", 
        },

         {
        "id":2,
        "title":"Excelle Programlama",
        "image":"2.png",
        "is_active":True,
        "is_home" : True,
        "description":"Tam aradiginiz kurs  burada", 
        },
        
         {
        "id":3,
        "title":"Python Ile Programlama",
        "image":"3.png",
        "is_active":True,
        "is_home" : True,
        "description":"Tam aradiginiz kurs  burada", 
        },

         {
        "id":4,
        "title":"SQL Ile Programlama",
        "image":"4.png",
        "is_active":True,
        "is_home" : True,
        "description":"Tam aradiginiz kurs  burada", 
        }


]}


# Create your views here.
def index(request):
    context = {"blogs":data["blogs"]}
    return render(request,"index.html",context)

def blogs(request):
    context = {"blogs":data["blogs"]}
    return render(request,"blogs.html",context)

def blogsdetails(request, id):
    blogs = data["blogs"]
    selected_blog = None
    for blog in blogs:
        if blog["id"] == id:
            selected_blog = blog
            break
    return render(request, 'blogs-detail.html', {"blog":selected_blog})

