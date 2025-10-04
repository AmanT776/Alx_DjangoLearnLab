from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book, Author


class BookAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass123")
        self.staff_user = User.objects.create_user(username="staff", password="pass123", is_staff=True)

        self.author = Author.objects.create(name="Author One")
        self.book = Book.objects.create(title="Book One", author=self.author, publication_year=2020)

        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book.id])
        self.delete_url = reverse("book-delete", args=[self.book.id])

    def test_list_books_requires_auth(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_books_authenticated(self):
        self.client.login(username="user", password="pass123")
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_title(self):
        self.client.login(username="user", password="pass123")
        response = self.client.get(self.list_url, {"title": "Book One"})
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_author(self):
        self.client.login(username="user", password="pass123")
        response = self.client.get(self.list_url, {"author": "Author One"})
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        self.client.login(username="user", password="pass123")
        response = self.client.get(self.list_url, {"search": "Book"})
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books(self):
        self.client.login(username="user", password="pass123")
        Book.objects.create(title="Another Book", author=self.author, publication_year=2021)
        response = self.client.get(self.list_url, {"ordering": "title"})
        self.assertEqual(response.status_code, 200)
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_retrieve_book(self):
        self.client.login(username="user", password="pass123")
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Book One")


    def test_create_book(self):
        self.client.login(username="user", password="pass123")
        data = {"title": "Book Two", "author": self.author.id, "publication_year": 2022}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_duplicate_book_fails(self):
        self.client.login(username="user", password="pass123")
        data = {"title": "Book One", "author": self.author.id, "publication_year": 2020}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("This book already exists.", str(response.data))

    def test_update_book_fails_for_non_staff(self):
        self.client.login(username="user", password="pass123")
        data = {"title": "New Title", "author": self.author.id, "publication_year": 2020}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, 500)  # PermissionError raised

    def test_update_book_success_for_staff(self):
        self.client.login(username="staff", password="pass123")
        data = {"title": "Staff Updated Book", "author": self.author.id, "publication_year": 2020}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Staff Updated Book")

    def test_delete_book(self):
        self.client.login(username="user", password="pass123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Book.objects.count(), 0)
