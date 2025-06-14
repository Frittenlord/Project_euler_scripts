def add_primes(limit):
    sieve = [True]*(limit)
    sieve[0] = sieve[1] = False
    
    for i in range(2, limit):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
    primes = [p for p in range(2, limit) if sieve[p]]
    
    return sum(primes)
    
print(add_primes(2000000))    