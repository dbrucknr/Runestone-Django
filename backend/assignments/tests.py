from django.test import TestCase

from .models import Assignment

class AssignmentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Assignment.objects.create(title='test assignment')

    def test_title_content(self):
        assignment = Assignment.objects.get(id=1)
        expected_object_name = f'{assignment.title}'
        self.assertEquals(expected_object_name, 'test assignment')
