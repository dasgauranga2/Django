from django.contrib import admin
from django.urls import path
from generator import views

# urlpatterns contains all valid available url paths
# each url path is linked to a function in views file
urlpatterns = [
    path('admin/', admin.site.urls),
    # url path for home page
    path('', views.home),
    # url path for generated password page
    path('generated_password/', views.password, name='password')
]
