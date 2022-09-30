from rest_framework.generics import (
    # GenericAPIView,
    get_object_or_404
)
from rest_framework import (
    generics,
    permissions,
    )
from rest_framework.exceptions import ValidationError
# from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .serializers import BooksSerializer, CommentSerializer
from .models import Book, Comment
from .permissions import IsAdminUserOrReadOnly, IsCommentOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        book = get_object_or_404(Book, pk=pk)
        user = self.request.user
        comments = Comment.objects.filter(book=book,comments_owner=user)
        if comments.exists():
            raise ValidationError("You can not add another comment, for this book !")
        serializer.save(book=book, comments_owner=user)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwnerOrReadOnly]




    

# class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BooksSerializer

#     # List all Books
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # Create a new Book
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
