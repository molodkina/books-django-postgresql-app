from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.viewsets import ViewSet, ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework import generics

from molodkina_books.models import Book, Author, Country
from molodkina_books.serializers import BookSerializer, AuthorSerializer, CountrySerializer

def hello(request):
    return HttpResponse('<h1> Exophonic Writers</h1>')

class AuthorViewSet(ViewSet):
    serializer_class = AuthorSerializer

    def list(self, request):
        queryset = Author.objects.filter()
        serializer = AuthorSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.filter()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data, safe=False)

class BookViewSet(ViewSet):
    serializer_class = BookSerializer

    def list(self, request, author_pk=None):
        queryset = Book.objects.filter(Author_id=author_pk)
        serializer = BookSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None, author_pk=None):
        queryset = Book.objects.filter(pk=pk, Author_id=author_pk)
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data, safe=False)

class CountryViewSet(ViewSet):

    def list(self, request, author_pk=None):
        queryset = Country.objects.filter(author=author_pk)
        serializer_class = CountrySerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)
 
class BookFilterViewSet(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer(queryset, many = True)
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['Language', 'YearOfPublication']

    def get(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        filtered_serializer_class = BookSerializer(filtered_queryset, many = True)
        return JsonResponse(filtered_serializer_class.data, safe = False)


# class BookFilterViewSetMVS(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     filter_backends = [DjangoFilterBackend]
#     filter_fields = ['Language', 'YearOfPublication']

#     def list(self, request, *args, **kwargs):
#         filtered_queryset = self.filter_queryset(self.get_queryset())
#         filtered_serializer_class = BookSerializer(filtered_queryset, many = True)
#         return JsonResponse(filtered_serializer_class.data, safe = False)
    
#     def retrieve(self, request, *args, **kwargs):
#         filtered_queryset = self.filter_queryset(self.get_queryset())
#         filtered_serializer_class = BookSerializer(filtered_queryset, many = True)
#         return JsonResponse(filtered_serializer_class.data, safe = False)

#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

