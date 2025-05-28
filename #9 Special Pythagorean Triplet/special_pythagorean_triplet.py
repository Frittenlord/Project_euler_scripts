
def find_py_triplet(n):
    """
    Generating triples by using Euklids formulas:

    a = (x**2)-(y**2)
    b = 2*(x*y)
    c = (x**2)+(y**2)

    a+b+c = 2x(x+y) = n

    Then just trying every number combination up to n
    """

    triples = {}
    for x in range(2, n):
        for y in range(1, x):
            if 2*x*(x+y) == n:
                a = (x**2)-(y**2)
                b = 2*(x*y)
                c = (x**2)+(y**2)
                if a > 0 and b > 0 and c > 0: # make sure we stay positive
                    triples[(a, b, c)] = a*b*c
    return triples


print(find_py_triplet(1000))
