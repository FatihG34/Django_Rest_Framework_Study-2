from rest_framework.generics import (
    # GenericAPIView,
    get_object_or_404
)
from rest_framework import generics
# from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .serializers import BooksSerializer, CommentSerializer
from .models import Book, Comment
# Create your views here.


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        book = get_object_or_404(Book, pk=pk)
        serializer.save(book=book)

# class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BooksSerializer

#     # List all Books
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # Create a new Book
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
