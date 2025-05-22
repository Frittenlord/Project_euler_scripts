import unittest

def find_multiples(n: int) -> int:
    '''Finds and adds all multiples of 3 and 5 below n'''
    multiples_sieve = [False] * (n)
    multiples_sieve[3] = True
    multiples_sieve[5] = True

    for i in range(0, n, 3):
        multiples_sieve[i] = True
    for j in range(5, n, 5):
        multiples_sieve[j] = True

    multiples = [mt for mt in range(0, n) if multiples_sieve[mt]]
    return sum(multiples)

class TestFindMultiples(unittest.TestCase):
    def test_find_multiples(self):
        self.assertEqual(find_multiples(10), 23)
        self.assertEqual(find_multiples(1000), 233168)

if __name__ == "__main__":
    unittest.main()
