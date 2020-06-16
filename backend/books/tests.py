from django.test import TestCase

from .models import Book

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='test book')

    def test_title_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.title}'
        self.assertEquals(expected_object_name, 'test book')
