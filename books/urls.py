from django.urls import path
from .views import BookDetailAPIView, BookListCreateAPIView, CommentCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view(), name="book-list"),
    path("books/<int:pk>", BookDetailAPIView.as_view(), name="book-detail"),
    path("books/<int:pk>/comments/",CommentCreateAPIView.as_view(), name="comments"),
    path("comments/<int:pk>/", CommentDetailAPIView.as_view(), name="comments-update"),
]
