import math
import unittest

def find_prime_factors(n):
    limit = int(math.sqrt(n))
    sieve = [True] * limit
    sieve[0] = sieve[1] = False

    for i in range(2, limit):
      if sieve[i]:
         for j in range(i*i, limit, i):
            sieve[j] = False

    primes = [p for p in range(2, limit) if sieve[p]]

    prime_factors = []
    for p in primes:
        if n % p == 0:
            f = n // p
            prime_factors.append(p)
    return max(prime_factors)

class TestLargestPrimeFactor(unittest.TestCase):
    def test_find_prime_factors(self):
        self.assertEqual(find_prime_factors(13195), 29)
        
if __name__ == "__main__":
    # unittest.main()
    print(find_prime_factors(600851475143)) 
