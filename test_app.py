# Poniżej link do repozytorium na github.com
# https://github.com/Sylwia-spec/zadanie_2

import unittest
from app import is_valid_email, calculate_area, filter_even_numbers, convert_date_format, is_palindrome

class TestAppFunctions(unittest.TestCase):


    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("user.name+tag@gmail.com"))
        self.assertFalse(is_valid_email("test@@example.com"))  
        self.assertFalse(is_valid_email("test.example.com"))
        self.assertFalse(is_valid_email("@example.com"))
        self.assertFalse(is_valid_email(""))


    def test_calculate_area_valid(self):
        self.assertEqual(calculate_area("kwadrat", 4), 16)
        self.assertEqual(calculate_area("prostokąt", 4, 5), 20)
        self.assertAlmostEqual(calculate_area("koło", 3), 28.27431)

    def test_calculate_area_invalid_shape(self):
        with self.assertRaises(ValueError):
            calculate_area("trójkąt", 3, 4)
        with self.assertRaises(ValueError):
            calculate_area("prostokąt")
        with self.assertRaises(ValueError):
            calculate_area("kwadrat", 3, 4)
        with self.assertRaises(ValueError):
            calculate_area("koło", 3, 4)


    def test_filter_even_numbers_valid(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filter_even_numbers([10, 15, 20, 25]), [10, 20])
        self.assertEqual(filter_even_numbers([7, 9, 11]), [])
        self.assertEqual(filter_even_numbers([]), [])
        self.assertEqual(filter_even_numbers([2, "a", 4.5, 6]), [2, 6])


    def test_convert_date_format_valid(self):
        self.assertEqual(convert_date_format("2025-03-21", "%Y-%m-%d", "%d/%m/%Y"), "21/03/2025")
        self.assertEqual(convert_date_format("22-03-2025", "%d-%m-%Y", "%Y/%m/%d"), "2025/03/22")

    def test_convert_date_format_invalid(self):
        with self.assertRaises(ValueError):
            convert_date_format("31-02-2025", "%d-%m-%Y", "%Y/%m/%d")
        with self.assertRaises(ValueError):
            convert_date_format("19-03-25", "%Y-%m-%d", "%d/%m/%Y")


    def test_is_palindrome_valid(self):
        """Test poprawnego wykrywania palindromów."""
        self.assertTrue(is_palindrome("owocowo"))
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("Ala ma kota , atok am alA"))

    def test_is_palindrome_invalid(self):
        self.assertFalse(is_palindrome("cośtam"))
        self.assertFalse(is_palindrome("67890"))

    def test_is_palindrome_empty(self):
        self.assertTrue(is_palindrome(""))

if __name__ == "__main__":
    unittest.main()
