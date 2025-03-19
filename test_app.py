import unittest
from app import is_valid_email, calculate_area, filter_even_numbers, convert_date_format, is_palindrome

class TestAppFunctions(unittest.TestCase):

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("test@@example.com"))

    def test_calculate_area(self):
        self.assertEqual(calculate_area("kwadrat", 4), 16)
        self.assertEqual(calculate_area("prostokąt", 4, 5), 20)
        self.assertAlmostEqual(calculate_area("koło", 3), 28.27431)

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4]), [2, 4])

    def test_convert_date_format(self):
        self.assertEqual(convert_date_format("2025-03-19", "%Y-%m-%d", "%d/%m/%Y"), "19/03/2025")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("kajak"))
        self.assertFalse(is_palindrome("test"))

if __name__ == "__main__":
    unittest.main()
