n = int(input("N = "))

def fibonacci_n(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n >= 3:
        return fibonacci_n(n-1) + fibonacci_n(n-2)

print(fibonacci_n(n))
