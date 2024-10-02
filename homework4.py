import pandas as pd

# lista słowników poszczególnych towaów dodanych do magazynu
produkt_all = {
        "Stół 120x90": [3, 250],
        "Stół 90x90": [5, 150],
        "Krzesło model 1": [12, 100],
        "Krzesło model 2": [6, 120],
        "Szafa 200x220": [1, 1200],
        "Szafa 180x220": [2, 1000]
}
suma_konta = 0
kwota_zakupu = 0
kwota_sprzedazy = 0
saldo = []
# Główna pętla programu
while True:
    print(5 * "-" + "SYSTEM KSIĘGOWO-MAGAZYNOWY" + 5 * "-")
    komenda = input("\nWprowadź komendę lub 'HELP' jeżeli chcesz listę komend w programie: ").upper()
    # warunek po wprowadzeniu komendy przez użytkownika
    if komenda == "KONIEC":
        print("Zamykam program")
        break
    elif komenda == "HELP":
        print("""
        lISTA KOMEND W PROGRAMIE:
        1. SALDO - wyświetla listę operacji dokonanych na koncie
        2. SPRZEDAZ - zmniejsza stan magazynu, zwiększa stan konta
        3. ZAKUP - wprowadza nowe produkty do magazynu lub zwiększa jego stan dla istniejących produktów, zmniejsza stan konta
        4. KONTO - wyświetla aktualny stan konta, oraz wartość produktów na magazynie
        5. LISTA - wyświetla całkowity stan magazynu
        6. MAGAZYN - wyświtla stan magazynu dla konkretnego produktu
        7. PRZEGLAD
        8. HELP - wyświetla listę dostępnych komend w programie
        9. KONIEC - zakończenie działania programu
        """)

    elif komenda == "SALDO":
        # przedstawienie wyników w formie tabelarycznej. Lista uzupełnia się tylko w trakcie działąnia programu
        print("Lista operacji na koncie")
        print("-" * 30)

        saldo_data_headers = ['Rodzaj transakcji', 'Kwota']
        table = pd.DataFrame(saldo, columns=saldo_data_headers)
        print(table)

        print("-" * 30)

    elif komenda == "SPRZEDAZ":
        produkt_nazwa = input("Podaj nazwę sprzedawanego produktu: ")
        saldo_zwiekszenie = []

        # sprawdzamy czy produkt jest w magazynie
        if produkt_nazwa in produkt_all:

            print(f"Sprzedajesz produkt: {produkt_nazwa}")
            liczba = int(input(f"Podaj liczbę sprzedawanych produktów dla: {produkt_nazwa}: "))
            # weryfikacja ilości produktów w magazynie
            if produkt_all[produkt_nazwa][0] >= liczba:
                produkt_all[produkt_nazwa][0] -= liczba
                # wyliczenie kwoty, którą należy dodać do konta
                kwota_sprzedazy = (liczba * produkt_all[produkt_nazwa][1])
                suma_konta += kwota_sprzedazy
                saldo_zwiekszenie.append('zwiekszenie')
                saldo_zwiekszenie.append(kwota_sprzedazy)
                print(f"Zakutalizowano liczbę produktów w magazynie dla produktu: {produkt_nazwa}")
                print(f"Kwota sprzedaży: {kwota_sprzedazy}")
                # warunek dla którego jeżeli liczba = 0 produkt jest usuwany z listy produktów na magazynie
                if produkt_all[produkt_nazwa][0] == 0:
                    del produkt_all[produkt_nazwa]
            else:
                print(f"Brak wystarczającej liczby produktów w magazynie - dostępne {produkt_all[produkt_nazwa][0]} szt.")

        else:
            print("Brak takiego towaru w magazynie. Transakcja niemożliwa")

        saldo.append(saldo_zwiekszenie)

    elif komenda == "ZAKUP":
        # Sprawdzamy dwa przypadki: [1] produkt już jest magazynie lub [2] dodajemy nowy produkt do magazynu
        produkt_nazwa = input("Podaj nazwę produktu: ")
        saldo_zmniejszenie = []

        # Przypadek [1]
        if produkt_nazwa in produkt_all:
            print(f"Produkt {produkt_nazwa} jest już w magazynie.")
            liczba = int(input(f"Podaj liczbę produktów do dodania dla {produkt_nazwa}: "))
            produkt_all[produkt_nazwa][0] += liczba
            # wyliczenie kwoty do ściągnięcia z konta
            kwota_zakupu = liczba * produkt_all[produkt_nazwa][1]
            # weryfikacja stanu konta
            if kwota_zakupu > suma_konta:
                print("Brak odpowiednich środków na koncie. Transakcja niemożliwa")
            else:
                suma_konta -= kwota_zakupu
                saldo_zmniejszenie.append("zmniejszenie")
                saldo_zmniejszenie.append(kwota_zakupu)
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
            if kwota_zakupu < suma_konta:
                suma_konta -= kwota_zakupu
                produkt_all[produkt_nazwa] = produkt
                saldo_zmniejszenie.append("zmniejszenie")
                saldo_zmniejszenie.append(kwota_zakupu)
                print(f"Dodano produkt: {produkt_nazwa} do magazynu. Ilość produktu: {liczba}")
                print(f"Kwota zakupu (przypadek 2): {kwota_zakupu}")
            else:
                print("Brak odpowiednich środków na koncie. Transakcja niemożliwa")

        saldo.append(saldo_zmniejszenie)

    elif komenda == "KONTO":
        suma_materialow = 0
        # wylicza wartość magazynu na podstawie iloczynu liczby posiadanych produktów i ich cen jednostkowych
        for nazwa, wartosc in produkt_all.items():
            konto = wartosc[0] * wartosc[1]
            suma_materialow += konto

        print(f"Wartość materiałów na magazynie: {suma_materialow}")
        print(f"Stan konta magazynu wynosi: {suma_konta}")

    elif komenda == "LISTA":
        # wyświetlenie wszystkich produktów w magazynie
        for nazwa, wartosc in produkt_all.items():
            print(f"Produkt: {nazwa} - ilość w magazynie: {wartosc[0]}, cena jednostkowa: {wartosc[1]}")

    elif komenda == "MAGAZYN":
        # wyszukiwanie produktu w magazynie
        produkt_nazwa = input("Podaj nazwę produktu: ")
        if produkt_nazwa in produkt_all:
            print(f"Produkt {produkt_nazwa} jest już w magazynie. Liczba sztuk w magazynie: {produkt_all[produkt_nazwa][0]}")
        else:
            print("Brak towaru w magazynie")

    elif komenda == "PRZEGLAD":
        print(f"Wprowadziłeś komendę {komenda}")

    else:
        print("Nieznana komenda. Wpisz 'HELP', aby uzyskać informację na temat dostępnych komend w programie")
