import pandas as pd
import global_var
from constans import BAZA_PRODUKT, KONTO, SALDO
from global_var import produkt_all, saldo
from datetime import datetime

def wczytaj_produkt(file_path = BAZA_PRODUKT):
    """
    Funkcja wczytująca produkty z pliku produkt_all.txt.
    Zwraca produkt_all, do którego odwołują się pozostałe funkcje i wyliczenia
    """
    with open(BAZA_PRODUKT, "r", encoding='utf-8') as plik:
        for linia in plik:
            nazwa, ilosc, cena = linia.strip().split(",")
            produkt_all[nazwa] = [int(ilosc), int(cena)]
    return produkt_all

def wczytaj_liste(produkt_all):
    """
    Tworzy listę produktów z pliku pordukt_all.txt.
    """
    for nazwa, [ilosc, cena] in produkt_all.items():
        print(f"Produkt: {nazwa} - ilość w magazynie: {int(ilosc)}, cena jednostkowa: {int(cena)}")
    return produkt_all

def aktualizuj_produkt_all(produkt_all):
    """
    funkcja aktualizuje bazę produktów do pliku produkt_all.txt
    """
    with open(BAZA_PRODUKT, "w", encoding='utf-8') as plik:
        for nazwa, [ilosc, cena] in produkt_all.items():
            plik.write(f"{nazwa}, {ilosc}, {cena}\n")

def oblicz_materialy(produkt_all, suma_materialow):
    """
    funkcja wyliczająca wartość wszystkich materiałów na magazynie.
    """
    lista = wczytaj_produkt(produkt_all)
    # pętla wyliczająca sumę wszystkich materiałów na podstawie pliku produkt_all.txt
    for nazwa, [ilosc, cena] in lista.items():
        materialy = ilosc * cena
        suma_materialow += materialy
    return suma_materialow

def zapisz_stan_konta(file_path = KONTO):
    """
    funkcja nadpisująca plik stan_konta.txt, w celu przechowania informacji o stanie konta
    """
    with open(KONTO, "w") as konto:
        stan_konta = global_var.suma_konta
        konto.write(str(stan_konta))

def odczytaj_stan_konta(file_path = KONTO):
    """
    Funkcja odczytująca plik stan_konta.txt, gdzie przechowywana jest informacja o stanie konta
    """
    try:
        with open(KONTO, "r") as konto:
            return konto.read()
    except FileNotFoundError:
        return None

def aktualizuj_operacje(file_path = SALDO):
    """
    Funkcja dopisująca operacje kupna i sprzedaży materiałów do pliku operacje_konto.txt
    """
    with open(SALDO, "a", encoding='utf-8') as operacja:
        for czas, [nazwa_operacji, kwota] in saldo.items():
            operacja.write(f"{czas}, {nazwa_operacji}, {kwota}\n")

def wyswietl_pomoc():
    print("""
    lISTA KOMEND W PROGRAMIE:
    1. SALDO - wyświetla listę operacji dokonanych na koncie
    2. SPRZEDAZ - zmniejsza stan magazynu, zwiększa stan konta
    3. ZAKUP - wprowadza nowe produkty do magazynu lub zwiększa jego stan dla istniejących produktów, zmniejsza stan konta
    4. KONTO - wyświetla aktualny stan konta, oraz wartość produktów na magazynie
    5. LISTA - wyświetla całkowity stan magazynu
    6. MAGAZYN - wyświtla stan magazynu dla konkretnego produktu
    7. PRZEGLAD - wyświetla listę operacji wykonywanych w programie
    8. HELP - wyświetla listę dostępnych komend w programie
    9. KONIEC - zakończenie działania programu
    """)

def wyswietl_powitanie():
    print(5 * "-" + "SYSTEM KSIĘGOWO-MAGAZYNOWY v 2.0" + 5 * "-")

def podaj_saldo():
    """
    Funkcja, która na podstawie pliku produkt_all tworzy tabelę z wykorzystaniem pandas i odczytuje ostatnią zapisaną operację
    """
    # Utworzenie tabeli z pliku operacje_konto.txt, wraz z nazwaniem kolumn.
    saldo_data_headers = ['Czas operacji', 'Rodzaj operacji na koncie', 'Kwota']
    table = pd.read_table(SALDO, delimiter=",", names=saldo_data_headers, header=None)
    # Sprawdzenie czy tabela jest pusta
    if table.empty:
        print("Brak zapisanych operacji.")
    else:
        # Odczytanie ostatniego wiersza w tabeli
        ostatnia_operacja = table.index[-1]
        # Ustalenie zmiennych do wyświetlenia potrzebnych informacji na koniec działania funkcji
        rodzaj_operacji = table.loc[ostatnia_operacja,'Rodzaj operacji na koncie']
        kwota_operacji = table.loc[ostatnia_operacja,'Kwota']
        stan_konta = odczytaj_stan_konta()
        print(f"Ostatnia wykonana operacja: {rodzaj_operacji}. Kwota zrealizowanej operacji: {kwota_operacji}.")
        print(f"Stan konta po zrealizowanej operacji: {stan_konta}")

def sprzedaz_produktu(produkt_all):
    produkt_nazwa = input("Podaj nazwę sprzedawanego produktu: ")

    # sprawdzamy czy produkt jest dostępny w magazynie
    if produkt_nazwa in produkt_all:
        print(f"Sprzedajesz produkt: {produkt_nazwa}")
        liczba = int(input(f"Podaj liczbę sprzedawanych produktów dla: {produkt_nazwa}: "))

        # weryfikacja ilości produktów w magazynie
        if produkt_all[produkt_nazwa][0] >= liczba:
            produkt_all[produkt_nazwa][0] -= liczba
            # wyliczenie kwoty, którą należy dodać do konta
            kwota_sprzedazy = (liczba * produkt_all[produkt_nazwa][1])
            stan_konta = int(odczytaj_stan_konta())
            global_var.suma_konta = stan_konta + kwota_sprzedazy
            zapisz_stan_konta()

            # zapisanie wykonanej czynności w historii operacji na koncie
            saldo.update({datetime.now():['zwiekszenie stanu konta', kwota_sprzedazy]})
            aktualizuj_operacje(saldo)

            print(f"Zakutalizowano liczbę produktów w magazynie dla produktu: {produkt_nazwa}")
            print(f"Kwota sprzedaży: {kwota_sprzedazy}")

            # warunek dla którego jeżeli liczba = 0 produkt jest usuwany z listy produktów na magazynie
            if produkt_all[produkt_nazwa][0] == 0:
                del produkt_all[produkt_nazwa]
            aktualizuj_produkt_all(produkt_all)
        else:
            print(f"Brak wystarczającej liczby produktów w magazynie - dostępne {produkt_all[produkt_nazwa][0]} szt.")

    else:
        print("Brak takiego towaru w magazynie. Transakcja niemożliwa")

    return produkt_nazwa

def zakup_produktu(produkt_all):
    # Sprawdzamy dwa przypadki: [1] produkt już jest magazynie lub [2] dodajemy nowy produkt do magazynu
    produkt_nazwa = input("Podaj nazwę produktu: ")

    # Przypadek [1]
    if produkt_nazwa in produkt_all:
        print(f"Produkt {produkt_nazwa} jest już w magazynie.")
        liczba = int(input(f"Podaj liczbę produktów do dodania dla {produkt_nazwa}: "))

        # wyliczenie kwoty do ściągnięcia z konta
        kwota_zakupu = liczba * produkt_all[produkt_nazwa][1]
        # weryfikacja stanu konta
        stan_konta = int(odczytaj_stan_konta())
        if kwota_zakupu > stan_konta:
            print("Brak odpowiednich środków na koncie. Transakcja niemożliwa")
        else:
            produkt_all[produkt_nazwa][0] += liczba
            global_var.suma_konta = stan_konta - kwota_zakupu
            zapisz_stan_konta()
            print(f"Zakutalizowano liczbę produktów w magazynie dla produktu: {produkt_nazwa}")
            print(f"Kwota zakupu (przypadek 1): {kwota_zakupu}")

    # Przypadek [2]
    else:
        print("Brak towaru. Dodaję towar do magazynu")
        produkt = []
        liczba = int(input(f"Podaj liczbę produktów do dodania dla {produkt_nazwa}: "))
        produkt.append(liczba)
        cena = int(input("Podaj cenę jednostkową produktu: "))
        produkt.append(cena)
        # wyliczenie kwoty do ściągnięcia z konta
        kwota_zakupu = (liczba * cena)
        # weryfikacja stanu konta
        stan_konta = int(odczytaj_stan_konta())
        if kwota_zakupu > stan_konta:
            print("Brak odpowiednich środków na koncie. Transakcja niemożliwa")
        else:
            produkt_all[produkt_nazwa] = produkt
            global_var.suma_konta = stan_konta - kwota_zakupu
            zapisz_stan_konta()
            print(f"Dodano produkt: {produkt_nazwa} do magazynu. Ilość produktu: {liczba}")
            print(f"Kwota zakupu (przypadek 2): {kwota_zakupu}")

    # zapisanie wykonanej czynności w historii operacji na koncie
    saldo.update({datetime.now(): ['zmniejszenie stanu konta', kwota_zakupu]})
    aktualizuj_operacje(saldo)

    aktualizuj_produkt_all(produkt_all)
    return produkt_nazwa

def sprawdz_konto(produkt_all, suma_materialow):
    """
    funkcja podaje dwa parametry:
    1. wartość materiałów - wyliczona na podstawie funkcji oblicz_materialy;
    2. stan konta - pobierany jest ze zmiennej stałej zlokalizowanej w global_var.py
    """
    materialy = oblicz_materialy(produkt_all, suma_materialow)
    stan_konta = odczytaj_stan_konta()

    print(f"Wartość materiałów na magazynie: {materialy}")
    print(f"Stan konta magazynu wynosi: {stan_konta}")

def sprawdz_magazyn(produkt_all):
    """
    funkcja sprawdza czy dany produkt jest dostępny w magazynie i w jakiej ilości
    """
    produkt_nazwa = input("Podaj nazwę produktu: ")
    if produkt_nazwa in produkt_all:
        print(
            f"Produkt {produkt_nazwa} jest już w magazynie. Liczba sztuk w magazynie: {produkt_all[produkt_nazwa][0]}")
    else:
        print("Brak towaru w magazynie")
    return produkt_nazwa

def przeglad_operacji():
    # przedstawienie wyników w formie tabelarycznej na bazie informacji zapisanych w pliku operacje_konto.txt

    print("-" * 30)
    # tworzenie tabeli z listą komend wpisywanych w programie
    saldo_data_headers = ['Czas operacji', 'Rodzaj operacji na koncie', 'Kwota']
    table = pd.read_table(SALDO, delimiter=",", names=saldo_data_headers, header=None)
    liczba_komend = len(table)
    print(f"Liczba wpisanych komend w programie: {liczba_komend}")
    print("-" * 30)
    # print(table)

    od = input("Podaj nr [OD] operacji w programie: ")
    # warunek dla pustego wpisu
    while True:
        if od == '':
            od = 1
        # warunek dla wpisania zbyt dużej wartości odnośnie listy komend
        elif int(od) > liczba_komend:
            print(f"Podałeś zbyt dużą wartość - liczba wykonanych komend: {liczba_komend}")
            break
        else:
            od = od

        do = input("Podaj nr [DO] operacji w programie: ")
        # warunek dla pustego wpisu
        if do == '':
            do = liczba_komend
        # warunek dla wpisania zbyt dużej wartości odnośnie listy komend
        elif int(do) > liczba_komend:
            print(f"Podałeś zbyt dużą wartość - liczba wykonanych komend: {liczba_komend}")
            break
        else:
            do = do

        # warunek, gdy użytkownik wpisze tę samą wartość w obie pozycje
        if od == do:
            tr = table.iloc[int(od) - 1: int(od)]
        else:
            tr = table.iloc[int(od) - 1:int(do)]
        print("-" * 30, "\n")
        print("Lista operacji na koncie:")
        print("-" * 30)
        print(tr)
        print("-" * 30, "\n")
        break