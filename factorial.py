def factorial(n):
    if n is 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(4))