# Poniżej link do repozytorium na github.com
# https://github.com/Sylwia-spec/zadanie_2 

import re
from datetime import datetime

def is_valid_email(email: str) -> bool:
    """Sprawdza, czy podany adres e-mail jest poprawny."""
    return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email))

def calculate_area(shape: str, *dimensions) -> float:
    """Oblicza pole figury."""
    if shape == "kwadrat":
        if len(dimensions) != 1:
            raise ValueError("Kwadrat wymaga 1 argumentu")
        return dimensions[0] ** 2
    elif shape == "prostokąt":
        if len(dimensions) != 2:
            raise ValueError("Prostokąt wymaga 2 argumentów")
        return dimensions[0] * dimensions[1]
    elif shape == "koło":
        if len(dimensions) != 1:
            raise ValueError("Koło wymaga 1 argumentu")
        return 3.14159 * dimensions[0] ** 2
    else:
        raise ValueError("Niepoprawne parametry")

def filter_even_numbers(numbers: list[int]) -> list[int]:
    """Zwraca parzyste liczby z listy."""
    return [num for num in numbers if isinstance(num, int) and num % 2 == 0]

def convert_date_format(date_str: str, current_format: str, target_format: str) -> str:
    """Konwertuje format daty."""
    try:
        return datetime.strptime(date_str, current_format).strftime(target_format)
    except ValueError:
        raise ValueError("Niepoprawny format daty")

def is_palindrome(text: str) -> bool:
    """Sprawdza, czy tekst jest palindromem."""
    clean_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return clean_text == clean_text[::-1]
