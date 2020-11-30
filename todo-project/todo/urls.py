"""todo URL Configuration

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
from django.contrib import admin
from django.urls import path
from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url path for signing up users
    path('signup/', views.user_signup, name='user_signup'),
    # url path for logging out users
    path('logout/', views.user_logout, name='user_logout'),
    # url path for logging in users
    path('login/', views.user_login, name='user_login'),
    # url path for the home page
    path('', views.home, name='home'),
    # url path for the creating tasks
    path('create/', views.create_todo, name='create_todo'),
    # url path for displaying the current todo tasks
    path('current/', views.current_todo, name='current_todo'),
    # url path for displaying each todo task
    path('<int:todo_pk>/', views.view_todo, name='view_todo'),
    # url path for deleting each todo task
    path('<int:todo_pk>/delete/', views.delete_todo, name='delete_todo'),
]
