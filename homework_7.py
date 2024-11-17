import requests
import csv
from datetime import datetime, timedelta
import os
from constants import API_URL, LATITUDE, LONGITUDE, CSV_FILE

def get_weather_data(searched_date):
    """
    Funkcja wyszukująca dane z api po stałych współrzędnych przypisanych dla położenia Warszawy
    """
    url = API_URL.format(latitude=LATITUDE, longitude=LONGITUDE, searched_date=searched_date)
    response = requests.get(url)
    # Sprawdzenie czy zapytanie do api zakończyło się sukcesem
    if response.status_code == 200:
        data = response.json()
        rain_sum = data['daily']['rain_sum'][0]
        return rain_sum
    return None

def save_to_csv(date, rain_status):
    """
    Funkcja zapisująca dane do pliku csv - ścieżka dostępu do pliku zapisana jako stała
    """
    with open(CSV_FILE, mode="a", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date, rain_status])

def check_weather_in_csv(date):
    """
    Funkcja sprawdzająca czy podana data przez użytkownika oraz wynik weryfikacji nie zostały już zapisane w pliku csv.
    """
    if not os.path.exists(CSV_FILE):
        return None
    with open(CSV_FILE, mode="r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == date:
                return row[1]
    return None

def get_rain_status(rain_sum):
    """
    Funkcja zwracająca odpowiednią odpowiedź (status) w zależności od wielkości opadów w danym dniu.
    """
    if rain_sum is None or rain_sum < 0:
        return "Nie wiem"
    elif rain_sum > 0:
        return "Będzie padać"
    else:
        return "Nie będzie padać"

def main():
    # pobranie daty od użytkownika
    user_date = input("Podaj datę (YYYY-mm-dd), aby sprawdzić pogodę. Jeżeli będzie puste - pogoda będzie dla jutra:  ")
    if user_date:
        # sprawdzenie poprawności formatu wpisanej daty przez użytkownika. W przypadku błędu wyświetli się odpowiedni komunikat.
        try:
            date = datetime.strptime(user_date, "%Y-%m-%d")
        except ValueError:
            print("Niepoprawny format daty. Wprowadź datę w formacie YYYY-mm-dd.")
            return
    # przypisanie wartości date w przypadku pozostawienia pustego miejsca o dacie
    else:
        date = datetime.now() + timedelta(days=1)

    searched_date = date.strftime("%Y-%m-%d")

    # Sprawdzenie, czy wynik jest już zapisany w CSV
    saved_status = check_weather_in_csv(searched_date)
    if saved_status:
        print(f"Wynik z pliku: {saved_status}")
        return

    # Pobranie danych pogodowych z API
    rain_sum = get_weather_data(searched_date)
    rain_status = get_rain_status(rain_sum)

    # Zapis wyniku do CSV
    save_to_csv(searched_date, rain_status)
    print(f"Wynik: {rain_status}")

    # Dla nowych dat (brak w pliku csv) - weryfikacja sumy opadów z api
    print("-" * 100)
    print("Brak danych w pliku *.csv. Weryfikacja danych z api:")
    print(f"Suma opadów w dniu {user_date}: {rain_sum}")


if __name__ == "__main__":
    main()