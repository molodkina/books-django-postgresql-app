from django.contrib import admin
from .models import Book, Author, Country

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Country)