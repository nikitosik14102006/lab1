
wejscie = input("Podaj oceny oddzielone spacją (np. 3 4.5 5 2): ")

oceny = [float(x) for x in wejscie.split()]


n = len(oceny)
if n == 0:
    print("Brak danych do analizy!")
else:

    s_min = oceny[0]
    s_max = oceny[0]
    suma = 0

    for o in oceny:
        if o < s_min: s_min = o
        if o > s_max: s_max = o
        suma += o

    srednia = suma / n


    posortowane = sorted(oceny)
    if n % 2 == 0:
        mediana = (posortowane[n // 2 - 1] + posortowane[n // 2]) / 2
    else:
        mediana = posortowane[n // 2]


    powyzej_sredniej = [o for o in oceny if o > srednia]


    wyniki = {
        "srednia": round(srednia, 2),
        "mediana": mediana,
        "min": s_min,
        "max": s_max,
        "liczba_ponad_srednia": len(powyzej_sredniej)
    }


    print(f"\nAnaliza ocen: {wyniki}")
    powyzej = []
    for o in oceny:
        if o > srednia:
            powyzej.append(o)
            powyzej = [o for o in oceny if o > srednia]