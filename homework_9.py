import csv
import json
import pickle
import sys

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def load(self):
        raise NotImplementedError("Metoda load musi być zaimplementowana w klasie dziedziczącej.")

    def save(self, output_path):
        raise NotImplementedError("Metoda load musi być zaimplementowana w klasie dziedziczącej.")

    def data_modification(self, changes):
        """
        Funkcja modyfikuje dane na podstawie zadanej listy zmian
        """
        for change in changes:
            col, row, value = change.split(",")
            col, row = int(col), int(row)
            try:
                self.data[row][col] = value
            except (IndexError, ValueError) as blad:
                print(f"Błąd w zmianie {change}: {blad}")

    def data_reader(self):
        """Wyświetla zawartość danych w terminalu."""
        for row in self.data:
            print(row)

class CSVFileHandler(FileHandler):
    def load(self):
        with open(file=self.file_path, mode="r", encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            self.data = list(reader)

    def save(self, output_path):
        with open(file=output_path, mode="w", encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.data)

class TXTFileHandler(FileHandler):
    def load(self):
        with open(file=self.file_path, mode="r", encoding="utf-8") as txt_file:
            self.data = [line.strip().split() for line in txt_file]

    def save(self, output_path):
        with open(file=output_path, mode="w", encoding="utf-8") as txt_file:
            for row in self.data:
                txt_file.write(" ".join(row) + "\n")
class JSONFileHandler(FileHandler):
    def load(self):
        with open(file=self.file_path, mode="r", encoding='utf-8') as json_file:
            self.data = json.load(json_file)

    def save(self, output_path):
        with open(file=output_path, mode="w", encoding='utf-8') as json_file:
            json.dump(self.data, json_file, ensure_ascii=False, indent=4)

class PickleFileHandler(FileHandler):
    def load(self):
        with open(file=self.file_path, mode="rb") as pickle_file:
            self.data = pickle.load(pickle_file)

    def save(self, output_path):
        with open(file=output_path, mode="wb") as pickle_file:
            pickle.dump(self.data, pickle_file)
def file_reader(file_path):
    # Funkcja zwraca odpowiednią klasę do obsługi pliku na podstawie jego rozszerzenia
    if file_path.endswith('.csv'):
        return CSVFileHandler(file_path)
    elif file_path.endswith('.txt'):
        return TXTFileHandler(file_path)
    elif file_path.endswith('.json'):
        return JSONFileHandler(file_path)
    elif file_path.endswith('.pkl'):
        return PickleFileHandler(file_path)
    else:
        raise ValueError(f"Nieobsługiwany format pliku: {file_path}")

def main():
    print("Witaj w programie do modyfikacji danych w plikach")

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

    # Wybór odpowiedniego czytnika
    reader = file_reader(input_file)

    # Odczyt danych z pliku
    reader.load()

    # Zastosowanie zmian na podstwie wpisu w terminalu
    reader.data_modification(changes)

    # Wyświetlenie zmodyfikowanych danych
    print("Zastosowane zmiany:")
    for row in changes:
        print(row)

    # Zapisanie danych do pliku wyjściowego
    reader.save(output_file)
    print(f"Zapisano zmiany do pliku {output_file}")

    # Wyświetlenie danych z pliku wyjściowego
    data_out = reader.data_reader()
    print(data_out)

if __name__ == "__main__":
    main()