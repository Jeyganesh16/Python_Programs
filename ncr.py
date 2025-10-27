def factorial(value):
    fact = 1
    i = 1
    while value >= i:
        fact = fact * i
        i = i + 1
    return fact

n = int(input("Enter n value"))
r = int(input("Enter r value"))

print("The NcR is:",factorial(n) / (factorial(r) * factorial(n-r)))
