import unittest

from src.main import FindNextNatural


class FindNextNaturalTest(unittest.TestCase):
    def test_findNext_samedigits_success(self):
        digits = "123"
        self.assertEqual(132, FindNextNatural.find_next(digits))

    def test_findNext_sumOfDigits_success(self):
        digits = "0200"
        self.assertEqual(1001, FindNextNatural.find_next(digits))

    def test_findNext_nomatch_success(self):
        digits = "90"
        self.assertEqual(-1, FindNextNatural.find_next(digits))

    def test_findNext_nomatch_2_success(self):
        digits = "9999"
        self.assertEqual(-1, FindNextNatural.find_next(digits))
