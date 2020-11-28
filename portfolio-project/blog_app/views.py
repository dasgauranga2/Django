from django.shortcuts import render,get_object_or_404
from . models import Blog

def blog(request):
    # read all the data from the database
    articles = Blog.objects.all()

    return render(request, 'blog.html', {'articles':articles})

def detail(request, blog_id):
    # read only the data from the database 
    # where the primary key of the row matches with the 'blog_id'
    article = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'article':article})

