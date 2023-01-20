from rest_framework import serializers
from molodkina_books.models import Book, Author, Country

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=('id', 'Title', 'Language', 'YearOfPublication', 'Author_id')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields=('id', 'Name', 'YearOfBirth', 'YearOfDeath', 'PlaceOfBirth', 'PlaceOfDeath')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields=('id', 'Name')