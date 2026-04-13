import requests
def add(a, b): return a + b
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a

print(f"Dodawanie: {add(10, 5)}")
print(f"Fibonacci: {fibonacci(5)}")
print(f"Requests wersja: {requests.__version__}")
