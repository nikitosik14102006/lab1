def silnia_iteracyjna(n):
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

def silnia_rekurencyjna(n):
    if n <= 1:
        return 1
    return n * silnia_rekurencyjna(n - 1)

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def czy_pierwsza(n):

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 0:
        return []
    wynik = [0, 1]
    while len(wynik) < n:
        wynik.append(wynik[-1] + wynik[-2])
    return wynik[:n]


if __name__ == "__main__":
    print(f"Silnia (10): {silnia_iteracyjna(10)}")
    print(f"NWD(48, 18): {nwd(48, 18)}")
    print(f"Fibonacci(8): {fibonacci(8)}")