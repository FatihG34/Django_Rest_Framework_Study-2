from ast import arg
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .serializers import BooksSerializer
from .models import Book
# Create your views here.


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

# class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BooksSerializer

#     # List all Books
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # Create a new Book
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
