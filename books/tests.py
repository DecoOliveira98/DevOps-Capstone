from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Author Example",
            isbn="1234567890",
            published_date="2022-01-01"
        )

    def test_list_books(self):
        url = reverse('book-list')  # URL for listing books
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Test Book', response.content.decode())

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            "title": "Another Book",
            "author": "Another Author",
            "isbn": "0987654321",
            "published_date": "2022-02-02"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
