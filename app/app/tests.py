from django.test import TestCase
from .calc import add

class CalcTests(TestCase):

    def test_add(self):
        self.assertEqual(add(2,3), 5)


