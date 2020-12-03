from django.views.generic import ListView,DetailView
from .models import Book

# ListView is used for displaying a list of objects
class BookList(ListView):
    model = Book
    template_name = 'book_list.html'

# DetailView is used for displaying a single object
class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'