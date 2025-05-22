import unittest

def add_even_fib(limit: int) -> list:
    '''Generate a List of Fibonacci numbers up to the limit'''
    fibs = [1, 2]
    fib_sum = 2
    while True:
        fib = fibs[-1] + fibs[-2]
        fibs.append(fib)
        fib_sum += fib if fib % 2 == 0 else 0
        if fib > limit:
            break
    return fib_sum

class TestAddEvenFib(unittest.TestCase):
    def test_add_even_fib(self):
        self.assertEqual(add_even_fib(10), 10)
        self.assertEqual(add_even_fib(100), 188)

if __name__ == '__main__':
    # unittest.main()
    print(add_even_fib(4000000))
