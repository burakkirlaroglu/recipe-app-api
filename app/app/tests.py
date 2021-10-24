from django.test import TestCase

from .calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        self.assertEqual(add(3, 7), 10)

    def test_suctract_numbers(self):
        self.assertEqual(subtract(5, 7), 2)
