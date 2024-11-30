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
            col, row, value = change.split(",", 2)
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
        with open(file=self.file_path, mode="r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            self.data = [row for row in reader]

    def save(self, output_path, output_format="csv"):
        # zapis pliku w zależności od formatu
        if output_format == "csv":
            with open(file=output_path, mode="w", encoding="utf-8", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(self.data)
        elif output_format == "json":
            with open(file=output_path, mode="w", encoding="utf-8") as json_file:
                json.dump(self.data, json_file, ensure_ascii=False, indent=4)
        elif output_format == "txt":
            with open(file=output_path, mode="w", encoding="utf-8") as txt_file:
                for row in self.data:
                    txt_file.write(",".join(row) + "\n")
        elif output_format == "pkl":
            with open(file=output_path, mode="wb") as pickle_file:
                pickle.dump(self.data, pickle_file)
        else:
            raise ValueError(f"Nieobsługiwany format zapisu: {output_format}")

class TXTFileHandler(FileHandler):
    def load(self):
        with open(file=self.file_path, mode="r", encoding="utf-8") as txt_file:
            self.data = [line.strip().split(",") for line in txt_file]

    def save(self, output_path, output_format="txt"):
        # zapis pliku w zależności od formatu
        if output_format == "txt":
            with open(file=output_path, mode="w", encoding="utf-8") as txt_file:
                for row in self.data:
                    txt_file.write(",".join(row) + "\n")
        elif output_format == "json":
            with open(output_path, mode="w", encoding="utf-8") as json_file:
                json.dump(self.data, json_file, ensure_ascii=False, indent=4)
        elif output_format == "csv":
            with open(output_path, mode="w", encoding="utf-8", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(self.data)
        elif output_format == "pkl":
            with open(file=output_path, mode="wb") as pickle_file:
                pickle.dump(self.data, pickle_file)
        else:
            raise ValueError(f"Nieobsługiwany format zapisu: {output_format}")
class JSONFileHandler(FileHandler):
    def load(self):
        with open(file=self.file_path, mode="r", encoding="utf-8") as json_file:
            self.data = json.load(json_file)

    def save(self, output_path, output_format="json"):
        # zapis pliku w zależności od formatu
        if output_format == "json":
            with open(file=output_path, mode="w", encoding="utf-8") as json_file:
                json.dump(self.data, json_file, ensure_ascii=False, indent=4)
        elif output_format == "csv":
            if isinstance(self.data, list) and all(isinstance(row, list) for row in self.data):
                with open(file=output_path, mode="w", encoding="utf-8", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerows(self.data)
        elif output_format == "txt":
            with open(file=output_path, mode="w", encoding="utf-8") as txt_file:
                for row in self.data:
                    line = ','.join(map(str, row))  # Konwersja elementów listy na string i łączenie przecinkami
                    txt_file.write(line + '\n')
        elif output_format == "pkl":
            with open(file=output_path, mode="wb") as pickle_file:
                pickle.dump(self.data, pickle_file)
        else:
            raise ValueError(f"Nieobsługiwany format zapisu: {output_format}")

class PickleFileHandler(FileHandler):
    def load(self):
        with open(file=self.file_path, mode="rb") as pickle_file:
            self.data = pickle.load(pickle_file)

    def save(self, output_path, output_format="pkl"):
        # zapis pliku w zależności od formatu
        if output_format == "pkl":
            with open(file=output_path, mode="wb") as pickle_file:
                pickle.dump(self.data, pickle_file)
        elif output_format == "json":
            with open(file=output_path, mode="w", encoding="utf-8") as json_file:
                json.dump(self.data, json_file, ensure_ascii=False, indent=4)
        elif output_format == "txt":
            with open(file=output_path, mode="w", encoding="utf-8") as txt_file:
                for row in self.data:
                    line = ','.join(map(str, row))  # Konwersja elementów listy na string i łączenie przecinkami
                    txt_file.write(line + '\n')
        elif output_format == "csv":
            if isinstance(self.data, list) and all(isinstance(row, list) for row in self.data):
                with open(file=output_path, mode="w", encoding="utf-8", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerows(self.data)
        else:
            raise ValueError(f"Nieobsługiwany format zapisu: {output_format}")
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
    if len(sys.argv) < 3:
        print("Podano zbyt małą liczbę argumentów!")
        print("Wymagany format w terminalu: python homework_9.py in.csv out.csv <zmiana 1> <zmiana 2> <zmiana n>")
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
    if changes:
        reader.data_modification(changes)

    # Wyświetlenie zmodyfikowanych danych
    print("Zastosowane zmiany:")
    for row in changes:
        print(row)

    # Sprawdzenie formatu wyjściowego na podstawie rozszerzenia pliku
    if output_file.endswith('.csv'):
        output_format = "csv"
    elif output_file.endswith('.json'):
        output_format = "json"
    elif output_file.endswith('.txt'):
        output_format = "txt"
    elif output_file.endswith('.pkl'):
        output_format = "pkl"
    else:
        raise ValueError(f"Nieobsługiwany format pliku wyjściowego: {output_file}")

    # Zapisanie danych do pliku wyjściowego
    reader.save(output_file, output_format=output_format)
    print(f"Zapisano zmiany do pliku {output_file}")

    # Wyświetlenie danych z pliku wyjściowego
    data_out = reader.data_reader()
    print(data_out)

if __name__ == "__main__":
    main()