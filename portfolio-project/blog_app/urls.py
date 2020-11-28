from django.urls import path
from . import views

urlpatterns = [
    # url path for the blog page
    path('', views.blog, name='blog'),
    # url path for each blog post
    # in the first argument the id/primary-key of each article is passed
    path('<int:blog_id>/', views.detail, name='detail'),
]