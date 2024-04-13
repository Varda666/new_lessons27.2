from rest_framework.generics import (CreateAPIView, UpdateAPIView,
                                     RetrieveAPIView, DestroyAPIView,
                                     ListAPIView)
from rest_framework.permissions import IsAuthenticated

from books.models import Book
from books.permissions import IsModerator
from books.serializers.book import BookSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsModerator]


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsModerator]


class BookRetrieveView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsModerator]


class BookDestroyView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsModerator]


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]




