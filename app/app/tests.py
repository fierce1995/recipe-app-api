"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    '''
    test the calc module
    '''

    def test_add_numbers(self):
        '''test adding number function'''
        res = calc.add(8, 9)
        self.assertEqual(res, 17)

