import unittest

def nth_prime(target):
    sieve = [True] * (target+1)
    sieve[0] = sieve[1] = False
    
    while True:
        for n in range(2, len(sieve)):
            if sieve[n]:
                for i in range(n*n, len(sieve), n):
                    sieve[i] = False
        
        primes = [p for p in range(2, len(sieve)) if sieve[p]]

        if len(primes) <= target:
            sieve.extend(True for j in range(target))
        else:
            break
    target_prime = primes[target-1]
    return target_prime

class TestNthPrime(unittest.TestCase):
    def test_nth_prime(self):
        self.assertEqual(nth_prime(6), 13)

if __name__ == '__main__':
    # unittest.main()
    print(nth_prime(10001))
