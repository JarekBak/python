import os
import csv
import sys

def odczyt_danych(file_path_in):
    """
    Funkcja odczytuje plik in.csv i zwraca jako listę list
    """
    file_path_in = os.path.join("data", "in.csv")

    with open(file=file_path_in, mode="r", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def modyfikacja_danych(data, changes):
    """
    Funkcja modyfikuje dane na podstawie zadanej listy zmian
    """
    for change in changes:
        try:
            col, row, value = change.split(",")
            col, row = int(col), int(row)
            data[row][col] = value
        except (IndexError, ValueError) as blad:
            print(f"Błąd w zmianie {change}: {blad}")
    return data

def zapisanie_danych(file_path_out, data):
    """
    Funkcja zapisuje dane do nowego pliku out.csv
    """
    file_path_out = os.path.join("data", "out.csv")
    with open(file=file_path_out, mode="w",newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def main():
    print("Witaj w programie do modyfikacji danych w plikach csv.")

    # Sprawdzamy czy została podana odpowiednia liczba argumentów
    if len(sys.argv) < 4:
        print("Podano zbyt małą liczbę argumentów!")
        print("Wymagany format w terminalu: python homework_6.py in.csv out.csv <zmiana 1> <zmiana 2> <zmiana n>")
        print("Zmiany podawaj w formacie [nr wiersza], [nr kolumny], 'wartość'")
        sys.exit(1)

    # Pobranie danych i argumentów do programu z poziomu terminala
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    changes = sys.argv[3:]

    # Odczytanie danych z pliku in.csv
    data = odczyt_danych(input_file)

    # Zastosowanie zmian
    change_data = modyfikacja_danych(data, changes)

    # Wyświetlenie zmodyfikowanych danych
    print("Zastosowane zmiany:")
    for row in change_data:
        print(row)

    # Zapisanie danych do pliku out.csv
    zapisanie_danych(output_file, change_data)
    print(f"Zapisano zmiany do pliku {output_file}")

if __name__ == "__main__":
    main()
