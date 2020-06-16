from django.test import TestCase

from .models import Course

class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Course.objects.create(title='test course')

    def test_title_content(self):
        course = Course.objects.get(id=1)
        expected_object_name = f'{course.title}'
        self.assertEquals(expected_object_name, 'test course')