from django.urls import path
from .views import BookDetailAPIView, BookListCreateAPIView

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view(), name="book-list"),
    path("books/<int:pk>", BookDetailAPIView.as_view(), name="book-detail"),
]
