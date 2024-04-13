from django.urls import path
from django.contrib import admin

from book.views.book import (BookListView, BookListView,
                             BookRetrieveView,
                             BookUpdateView,
                             BookCreateView, BookDestroyView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookRetrieveView.as_view(), name='book_detail'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('delete/<int:pk>/', BookDestroyView.as_view(), name='book_delete'),
]

