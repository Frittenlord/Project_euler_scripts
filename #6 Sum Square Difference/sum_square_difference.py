def square_of_sum(n):
    return int((n*(n+1))/2)**2

def sum_of_square(n):
    result = 0
    for n in range(n+1):
        result += n**2
    return result

print(square_of_sum(100)-sum_of_square(100))
