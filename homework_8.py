import requests
import csv
from datetime import datetime, timedelta
from constants import LATITUDE, LONGITUDE, CSV_FILE

class WeatherForecast:
    def __init__(self, latitude, longitude, csv_file=CSV_FILE):
        self.latitude = latitude
        self.longitude = longitude
        self.csv_file = csv_file
        self.data = {}

        self.check_weather_in_csv()

    def check_weather_in_csv(self):
        """
        Funkcja sprawdzająca czy podana data przez użytkownika oraz wynik weryfikacji nie zostały już zapisane w pliku csv.
        Ścieżka do pliku csv zapisana jest jako stała w constants.py
        """
        try:
            with open(CSV_FILE, mode="r", encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = {row["date"]: row["result"] for row in reader}
        except FileNotFoundError:
            self.data = {}

    def save_to_csv(self):
        """
        Funkcja zapisująca dane do pliku csv - ścieżka dostępu do pliku zapisana jako stała w constants.py
        """
        with open(CSV_FILE, mode="w", newline="", encoding='utf-8') as file:
            fieldnames = ["date", "result"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for date, result in self.data.items():
                writer.writerow({"date": date, "result": result})

    def get_weather_data(self, date):
        """
        Funkcja wyszukująca dane z API po stałych współrzędnych przypisanych dla położenia Warszawy
        Odwołanie współrzędnych jest w funkcji -main-
        """
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={self.latitude}&longitude={self.longitude}&hourly=rain&"
            f"daily=rain_sum&timezone=Europe%2FLondon&start_date={date}&end_date={date}"
        )
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            rain_sum = data.get("daily", {}).get("rain_sum", [None])[0]

            # Warunki jakie należy spełnić, aby wpisać do pliku odpowiedni wynik weryfikacji
            if rain_sum is None or rain_sum < 0:
                return "Nie wiem"
            elif rain_sum > 0.0:
                return "Będzie padać"
            elif rain_sum == 0.0:
                return "Nie będzie padać"
            else:
                return "Nie wiem"
        # Wyświetlenie komunikatu w przypadku problemami z połączeniem z API
        except requests.RequestException as e:
            print(f"Wystąpił błąd w komunikacji z API: {e}")
            return "Nie wiem"

    def __setitem__(self, date, result):
        # Ustawia wynik dla podanej daty
        self.data[date] = result
        self.save_to_csv()

    def __getitem__(self, date):
        # Zwraca wynik dla podanej daty, pobierając go z API, jeśli nie istnieje
        if date not in self.data:
            self.data[date] = self.get_weather_data(date)
            self.save_to_csv()
        return self.data[date]

    def __iter__(self):
        # Zwraca iterator po datach
        return iter(self.data)

    def items(self):
        # Generuje wyniki: <data: wynik weryfikacji>
        return ((date, result) for date, result in self.data.items())


# Funkcja główna
def main():
    # Współrzędne geograficzne pobierane ze stałych zapisanych w constans.py
    latitude = LATITUDE
    longitude = LONGITUDE

    # Utworzenie obiektu WeatherForecast
    weather_forecast = WeatherForecast(latitude, longitude)

    # Pobranie daty od użytkownika
    input_date = input("Podaj datę w formacie YYYY-mm-dd (lub naciśnij Enter, aby sprawdzić następny dzień): ").strip()

    # W przypadku pustego pola system podstawia kolejny dzień po "now"
    if not input_date:
        input_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    # Sprawdzenie poprawności formatu daty
    try:
        datetime.strptime(input_date, "%Y-%m-%d")
    except ValueError:
        print("Podano nieprawidłowy format daty. Użyj formatu YYYY-mm-dd.")
        return

    # Pobranie wyniku dla podanej daty
    result = weather_forecast[input_date]
    print(f"Dla daty {input_date} wynik: {result}")

    # Wyświetlenie wyników
    print("\nZapisane dane pogodowe:")
    for date, result in weather_forecast.items():
        print(f"{date}: {result}")


if __name__ == "__main__":
    main()