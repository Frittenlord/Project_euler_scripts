import unittest

def add_even_fib(start_sequence: tuple, limit: int) -> list:
    '''Generate a List of Fibonacci numbers up to the limit'''
    fibs = [start_sequence[0], start_sequence[1]]
    fib_sum = 0
    for fib in fibs:
        fib_sum += fib if fib % 2 == 0 else 0
    
    while True:
        fib = fibs[-1] + fibs[-2]
        fibs.append(fib)
        fib_sum += fib if fib % 2 == 0 else 0
        if fib > limit:
            break
    return fib_sum

class TestAddEvenFib(unittest.TestCase):
    def test_add_even_fib(self):
        self.assertEqual(add_even_fib((1,2), 10), 10)
        self.assertEqual(add_even_fib((1,2),100), 188)
        self.assertEqual(add_even_fib((2,3), 100), 188)

if __name__ == '__main__':
    # unittest.main()
    print(add_even_fib((1, 2), 4000000))
