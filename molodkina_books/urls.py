from django.urls import path, include
from rest_framework_nested import routers
from molodkina_books import views
from molodkina_books.views import BookViewSet, CountryViewSet, BookFilterViewSet, AuthorViewSet

default_router = routers.DefaultRouter()
default_router.register(r'authors', AuthorViewSet, basename='authors')
# default_router.register(r'books', BookFilterViewSet, basename='books')
# default_router.register(r'books', BookFilterViewSetMVS, basename='books')

book_router = routers.NestedSimpleRouter(default_router, r'authors', lookup='author')
book_router.register(r'books', BookViewSet, basename='books')

country_router = routers.NestedSimpleRouter(default_router, r'authors', lookup='author')
country_router.register(r'countries', CountryViewSet, basename='countries')


urlpatterns = [
    path('', views.hello, name='hello'),
    path(r'', include(default_router.urls)),
    path(r'', include(book_router.urls)),
    path(r'', include(country_router.urls)),
    path(r'books/', BookFilterViewSet.as_view(), name = 'books')
]