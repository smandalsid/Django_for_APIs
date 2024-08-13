from django.test import TestCase
from django.urls import reverse
# Create your tests here.

from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book=Book.objects.create(
            title="title",
            subtitle="subtitle",
            author="author",
            isbn="isbn",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "title")
        self.assertEqual(self.book.subtitle, "subtitle")
        self.assertEqual(self.book.author, "author")
        self.assertEqual(self.book.isbn, "isbn")

    def test_book_listview(self):
        response=self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")
