import unittest
import math

def find_multiples(limit: list) -> int:
    # This works fine for smaller number ranges but will take a considerable time when calculating larger ranges
    start = 1 if limit[0] == 0 else limit[0]
    end = limit[1]
    current_number = end
    while True:
        for n in range(start, end+1):
            if current_number % n == 0:
                if n == end:
                    return current_number
                else:
                    continue
            else:
                break
        current_number += 1

def find_multiples2(limit: list) -> int:
    # This is massively faster but a bit more complicated
    start = 1 if limit[0] == 0 else limit[0]
    end = limit[1]

    prime_factors = []
    counted_factors = {}
    product = []
    
    for number in range(start, end):
        prime_factors.append(find_prime_factors(number))
    
    for factor in prime_factors:
        factor_set = set(factor)
        for i in factor_set:
            counted_factors[i] = 0 if not i in counted_factors.keys() else counted_factors[i]
            count = factor.count(i)
            if count > counted_factors[i]:
                counted_factors[i] = count

    for counted in counted_factors:
        product.append(counted**counted_factors[counted])

    return math.prod(product)

def find_prime_factors(n: int) -> list:
    factors = []
    factor = 2
    while (n >= 2):
        if n % factor == 0:
            factors.append(factor)
            n = n / factor
        else:
            factor += 1
    return factors


class TestSmallestMultiple(unittest.TestCase):
    def test_find_multiples(self):
        self.assertEqual(find_multiples([1,10]), 2520)

    def test_find_multiples2(self):
        self.assertEqual(find_multiples2([1,10]), 2520)

if __name__ == '__main__':
    # unittest.main()
    print(find_multiples([1, 20]))
    print(find_multiples2([1, 20]))
