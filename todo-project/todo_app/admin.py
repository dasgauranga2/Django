from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title', 'memo', 'user')

admin.site.register(Todo,TodoAdmin)