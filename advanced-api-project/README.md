# Django Book API

This project is a **RESTful API** for managing books and authors built with **Django REST Framework (DRF)**.  
It allows authenticated users to **view, create, update, and delete books**, and supports **filtering, searching, and ordering**.

---

## 📦 Models

### Author
- `name`: CharField (max 30) – the name of the author.
  
### Book
- `title`: CharField (max 30) – the book title.
- `publication_year`: IntegerField – the year the book was published.
- `author`: ForeignKey to `Author` – links each book to an author.

---

## ⚡ API Views

### 1. **BookListView**
- **Type:** `ListAPIView`
- **URL:** `/books/`
- **Permissions:** Authenticated users only (`IsAuthenticated`)
- **Features:**
  - **Filtering:** by `title` or `author` using query parameters:
    ```
    /books/?title=Harry
    /books/?author=Rowling
    ```
  - **Search:** supports DRF `SearchFilter` on `title` and `publication_year`:
    ```
    /books/?search=1997
    ```
  - **Ordering:** supports DRF `OrderingFilter` on `title` and `publication_year`:
    ```
    /books/?ordering=title
    /books/?ordering=-publication_year
    ```

---

### 2. **BookDetailView**
- **Type:** `RetrieveAPIView`
- **URL:** `/books/<id>/`
- **Permissions:** Read-only for unauthenticated users, full access for authenticated (`IsAuthenticatedOrReadOnly`)
- **Description:** Retrieve details of a single book by ID.

---

### 3. **BookCreateView**
- **Type:** `CreateAPIView`
- **URL:** `/books/create/`
- **Permissions:** Authenticated users (`IsAuthenticated`)
- **Description:** Create a new book.
- **Validation:** Prevents creating duplicate books with the same title.

---

### 4. **BookUpdateView**
- **Type:** `UpdateAPIView`
- **URL:** `/books/update/<id>/`
- **Permissions:** Only staff users can update books.
- **Description:** Update existing book details.
- **Validation:** Raises a `PermissionError` if a non-staff user tries to update.

---

### 5. **BookDeleteView**
- **Type:** `DestroyAPIView`
- **URL:** `/books/delete/<id>/`
- **Permissions:** Authenticated users (`IsAuthenticated`)
- **Description:** Delete a book.

---

## 🔑 Authentication & Permissions

- **Authentication:** `BasicAuthentication`  
- **Permissions:** Mixed use of `IsAuthenticated` and `IsAuthenticatedOrReadOnly` depending on the view.  
- Only staff users can update books.

---

## 🛠 Features Summary

| Feature                 | Endpoint                       | Description                                               |
|--------------------------|--------------------------------|-----------------------------------------------------------|
| List books               | `/books/`                      | List all books with optional search, filter, and ordering|
| Retrieve book            | `/books/<id>/`                 | Get details of a single book                              |
| Create book              | `/books/create/`               | Add a new book (unique title enforced)                  |
| Update book              | `/books/update/<id>/`          | Update book (staff only)                                  |
| Delete book              | `/books/delete/<id>/`          | Delete a book                                            |

---

## 🔍 Query Parameters

- `title` – Filter by book title (exact match or change to `icontains` for partial match)  
- `author` – Filter by author's name (case-insensitive partial match)  
- `search` – DRF SearchFilter (`title`, `publication_year`)  
- `ordering` – DRF OrderingFilter (`title`, `publication_year`)



