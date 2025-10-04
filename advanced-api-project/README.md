# 📚 Django REST Framework – Book API

This project provides a simple **Book API** built with Django REST Framework (DRF). It demonstrates how to use **generic class-based views** with authentication, permissions, validation, and CRUD operations.

---

## 🚀 Features
- **List all books**  
- **Retrieve a single book by ID**  
- **Create a new book (with duplicate title validation)**  
- **Update an existing book (staff-only rule)**  
- **Delete a book**  
- **Authentication and permissions** applied to all endpoints  

---

## 🔐 Authentication & Permissions
- **Authentication** → Uses DRF’s `BasicAuthentication`.  
- **Permissions** → Requires `IsAuthenticated` and `IsAdminUser`.  
  - Only logged-in users who are **admins/staff** can access the API.  

---

## 📂 Views Overview

### 1. List Books
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [BasicAuthentication]
### 2.Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [BasicAuthentication]
### 3. create book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [BasicAuthentication]

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError({"message": "This book already exists."})

### 4. update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [BasicAuthentication]

    def perform_update(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionError("Only staff can update books")
        serializer.save()
### 5. delete a book 
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    authentication_classes = [BasicAuthentication]


