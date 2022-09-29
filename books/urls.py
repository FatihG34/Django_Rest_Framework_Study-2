from django.urls import path
from .views import BookDetailAPIView, BookListCreateAPIView, CommentCreateAPIView

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view(), name="book-list"),
    path("books/<int:pk>", BookDetailAPIView.as_view(), name="book-detail"),
    path("books/<int:pk>/comments/",
         CommentCreateAPIView.as_view(), name="comments"),
]
