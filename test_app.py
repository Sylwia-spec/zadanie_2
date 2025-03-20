import unittest
from app import is_valid_email, calculate_area, filter_even_numbers, convert_date_format, is_palindrome

class TestAppFunctions(unittest.TestCase):

    # 1️⃣ TESTY DLA is_valid_email()
    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("user.name+tag@gmail.com"))
        self.assertFalse(is_valid_email("test@@example.com"))  # Podwójne @
        self.assertFalse(is_valid_email("test.example.com"))   # Brak @
        self.assertFalse(is_valid_email("@example.com"))       # Brak nazwy użytkownika
        self.assertFalse(is_valid_email(""))                   # Pusty string

    # 2️⃣ TESTY DLA calculate_area()
    def test_calculate_area_valid(self):
        self.assertEqual(calculate_area("kwadrat", 4), 16)
        self.assertEqual(calculate_area("prostokąt", 4, 5), 20)
        self.assertAlmostEqual(calculate_area("koło", 3), 28.27431)

    def test_calculate_area_invalid_shape(self):
        with self.assertRaises(ValueError):
            calculate_area("trójkąt", 3, 4)  # Nieobsługiwana figura
        with self.assertRaises(ValueError):
            calculate_area("prostokąt")  # Brak wymiarów
        with self.assertRaises(ValueError):
            calculate_area("kwadrat", 3, 4)  # Za dużo argumentów dla kwadratu
        with self.assertRaises(ValueError):
            calculate_area("koło", 3, 4)  # Za dużo argumentów dla koła

    # 3️⃣ TESTY DLA filter_even_numbers()
    def test_filter_even_numbers_valid(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filter_even_numbers([10, 15, 20, 25]), [10, 20])
        self.assertEqual(filter_even_numbers([7, 9, 11]), [])  # Brak parzystych
        self.assertEqual(filter_even_numbers([]), [])  # Pusta lista
        self.assertEqual(filter_even_numbers([2, "a", 4.5, 6]), [2, 6])  # Ignoruje nie-cyfry

    # 4️⃣ TESTY DLA convert_date_format()
    def test_convert_date_format_valid(self):
        self.assertEqual(convert_date_format("2025-03-19", "%Y-%m-%d", "%d/%m/%Y"), "19/03/2025")
        self.assertEqual(convert_date_format("19-03-2025", "%d-%m-%Y", "%Y/%m/%d"), "2025/03/19")

    def test_convert_date_format_invalid(self):
        with self.assertRaises(ValueError):
            convert_date_format("31-02-2025", "%d-%m-%Y", "%Y/%m/%d")  # Luty nie ma 31 dni
        with self.assertRaises(ValueError):
            convert_date_format("19-03-25", "%Y-%m-%d", "%d/%m/%Y")  # Niepełny rok

    # 5️⃣ TESTY DLA is_palindrome()
    def test_is_palindrome_valid(self):
        """Test poprawnego wykrywania palindromów."""
        self.assertTrue(is_palindrome("kajak"))
        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("Ala ma kota, a taK om a la"))  # Bo zawiera spacje!

    def test_is_palindrome_invalid(self):
        self.assertFalse(is_palindrome("test"))
        self.assertFalse(is_palindrome("12345"))

    def test_is_palindrome_empty(self):
        self.assertTrue(is_palindrome(""))  # Pusty string jest palindromem

if __name__ == "__main__":
    unittest.main()
