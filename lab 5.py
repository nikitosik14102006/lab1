import json
import logging
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("dziennik.log", encoding='utf-8'),
        logging.StreamHandler()  # To sprawia, że logi widać też w konsoli PyCharma
    ]
)

PLIK_JSON = Path("wydatki.json")

class NegativeAmountError(Exception):
    pass


def wczytaj_dane():
    try:
        if not PLIK_JSON.exists():
            logging.warning("Plik nie istnieje. Tworzę nową bazę.")
            return []
        with open(PLIK_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        logging.error("Błąd formatu pliku JSON! Zwracam pustą listę.")
        return []


def zapisz_dane(dane):
    try:
        with open(PLIK_JSON, 'w', encoding='utf-8') as f:
            json.dump(dane, f, indent=4)
        logging.info("Dane zostały pomyślnie zapisane.")
    except Exception as e:
        logging.error(f"Nie udało się zapisać pliku! Błąd: {e}")


def dodaj_wydatek():
    try:
        kat = input("Kategoria: ")
        kwota = float(input("Kwota: ").replace(',', '.'))

        if kwota < 0:
            raise NegativeAmountError("Kwota nie może być ujemna!")

        opis = input("Opis: ")

        wydatki = wczytaj_dane()
        wydatki.append({"kategoria": kat, "kwota": kwota, "opis": opis})
        zapisz_dane(wydatki)

    except ValueError:
        logging.error("Błędne dane! Kwota musi być liczbą.")
    except NegativeAmountError as e:
        logging.warning(f"Próba wpisania ujemnej kwoty: {e}")


def pokaz_sumy():
    wydatki = wczytaj_dane()
    sumy = {}
    for w in wydatki:
        kat = w['kategoria']
        sumy[kat] = sumy.get(kat, 0) + w['kwota']

    print("\n--- PODSUMOWANIE ---")
    for k, s in sumy.items():
        print(f"{k}: {s:.2f} PLN")
    logging.info("Wygenerowano podsumowanie wydatków.")


if __name__ == "__main__":
    logging.info("Aplikacja wystartowała")
    while True:
        print("\n1. Dodaj | 2. Wyświetl sumy | 3. Wyjście")
        wybor = input("Wybór: ")
        if wybor == '1':
            dodaj_wydatek()
        elif wybor == '2':
            pokaz_sumy()
        elif wybor == '3':
            logging.info("Zamykanie aplikacji.")
            break