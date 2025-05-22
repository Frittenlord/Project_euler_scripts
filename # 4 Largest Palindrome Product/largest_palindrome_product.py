import unittest


def is_palindrome(n: str) -> bool:
    n_list = list(n)
    reversed_n = n_list[::-1]
    if n_list == reversed_n:
        return True
    return False
    
def generate_numbers(number_range: list) -> list:
    
    products = []
    start = number_range[0]
    end = number_range[1]

    for a in range(start, end):
        for b in range(start, end):
            products.append(a * b)
    return list(set(products))

def find_largest_palindrome(number_range: list) -> int:
    palindromes = []
    numbers = generate_numbers(number_range)
    for n in numbers:
        if is_palindrome(str(n)):
            palindromes.append(n)
    return max(palindromes) if palindromes else None


class TestLargestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("121"))
        self.assertFalse(is_palindrome("123"))

    def test_generate_numbers(self):
        self.assertEqual(generate_numbers([1, 4]), [1, 2, 3, 4, 6, 9])

    def test_find_largest_palindrome(self):
        self.assertEqual(find_largest_palindrome([1, 4]), 9)

if __name__ == "__main__":
    
    # unittest.main()

    print(find_largest_palindrome([100, 1000]))
    

