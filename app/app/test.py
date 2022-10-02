"""
sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbre(self):
        """Test adding numbers togerther."""
        res = calc.add(5,6)

        self.assertEqual(res, 12)