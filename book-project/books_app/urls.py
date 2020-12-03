"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import BookList,BookDetail
from django.urls import path, include

urlpatterns = [
    # url path for displaying the list of all books
    path('', BookList.as_view(), name='book_list'),
    # url path for displaying each book detail
    # url path will be the primary key of each book
    path('<uuid:pk>/', BookDetail.as_view(), name='book_detail'),
]
