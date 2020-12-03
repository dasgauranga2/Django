from django.contrib import admin
from .models import Book,Review

class ReviewInline(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    # the admin interface has the ability to create/edit other models on the same page as a parent model
    # these are called inlines
    inlines = [ReviewInline]
    # specify which fields we want to display in the admin page
    list_display = ('title','author','price')

# register the 'Book' model in the admin page
admin.site.register(Book,BookAdmin)
