from django.shortcuts import render
from rest_framework import generics
from .models import Book,Author
from .serializers import BookSerializer
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import filters
# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title','publication_year']
    ordering_fields = ['title','publication_year']
    
    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get("title")
        author = self.request.query_params.get("author")
        if title:
            queryset = queryset.filter(title=title)
        if author:
            queryset = queryset.filter(author__name__icontains=author)
        return queryset

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthenticated]
    authentication_classes = [BasicAuthentication]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError({"message": "This book already exists."})

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def perform_update(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionError("only staff can update books")
        serializer.save()
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthenticated]
    authentication_classes = [BasicAuthentication]
