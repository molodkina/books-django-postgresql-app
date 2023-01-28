from rest_framework import serializers
from molodkina_books.models import Book, Author, Residence

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=('id', 'Title', 'Language', 'YearOfPublication', 'Author_id')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields=('id', 'Name', 'YearOfBirth', 'YearOfDeath', 'PlaceOfBirth', 'PlaceOfDeath')

class ResidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residence
        fields=('id', 'Name')