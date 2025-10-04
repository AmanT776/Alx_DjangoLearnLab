from django.shortcuts import render
from rest_framework import generics
from .models import Book,Author
from .serializers import BookSerializer
# Create your views here.

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
