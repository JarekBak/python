#lista słowników poszczególnych towaów dodanych do magazynu
produkt_all = [
        {"towar": "Stół 120x90", "liczba_towaru": 3, "cena_jedn_towaru": 450},
        {"towar": "Stół 90x90", "liczba_towaru": 5, "cena_jedn_towaru": 350},
        {"towar": "Krzesło model 1", "liczba_towaru": 12, "cena_jedn_towaru": 150},
        {"towar": "Krzesło model 2", "liczba_towaru": 6, "cena_jedn_towaru": 170},
        {"towar": "Szafa 200x220", "liczba_towaru": 1, "cena_jedn_towaru": 1200},
        {"towar": "Szafa 180x220", "liczba_towaru": 2, "cena_jedn_towaru": 1000}
]
key_produkt = ["towar", "liczba_towaru", "cena_jedn_towaru"]

# stworzyć listę, zawierjacą słowniki poszczególnych produktów. Program będzie się odwoływał do listy, a dalej do poszczególnych słowników

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
        1. SALDO
        2. SPRZEDAZ
        3. ZAKUP - wprowadza nowe produkty do magazynu lub zwiększa jego stan dla istniejących produktów
        4. KONTO
        5. LISTA - wyświetla całkowity stan magazynu
        6. MAGAZYN - wyświtla stan magazynu dla konkretnego produktu
        7. PRZEGLAD
        8. HELP - wyświetla listę dostępnych komend w programie
        9. KONIEC - zakończenie działania programu
        """)
    # for i in produkt_all:
    elif komenda == "SALDO":
        print(f"Wprowadziłeś komendę {komenda}")

    elif komenda == "SPRZEDAZ":
        print(f"Wprowadziłeś komendę {komenda}")

    elif komenda == "ZAKUP":
        produkt = []
        produkt_nazwa = input("Podaj nazwę produktu: ")
        for key_produkt in produkt_all:
            if key_produkt["towar"] != produkt_nazwa:
                produkt.append(produkt_nazwa)
                produkt_liczba = int(input("Podaj liczbę zakupionych produktów: "))
                produkt.append(produkt_liczba)
                produkt_cena_jednostkowwa = int(input("Podaj cenę jednostkową zakupionego produktu: "))
                produkt.append(produkt_cena_jednostkowwa)
                break

            # wprowadzanie nowych produktów do magazynu
            produkt_all.append(dict(zip(key_produkt, produkt)))
        # Sprawdzamy dwa przypadki: produkt już jest magazynie lub dodajemy nowy produkt do magazynu

        print(f"Produkt {produkt_nazwa} został wprowadzony na listę magazynową")

    elif komenda == "KONTO":
        print(f"Wprowadziłeś komendę {komenda}")

    elif komenda == "LISTA":
        # wyświetlenie wszystkich produktów w magazynie
        for key_produkt in produkt_all:
            print("Produkt: "+ str(key_produkt["towar"]) + " - liczba szt.: " + str(key_produkt["liczba_towaru"]) + " cena jednostkowa: " + str(key_produkt["cena_jedn_towaru"]))

    elif komenda == "MAGAZYN":
        # wyszukiwanie produktu w magazynie
        produkt_j = input("Podaj nazwę produktu: ")
        for key_produkt in produkt_all:
            if key_produkt["towar"] == produkt_j:
                print(f"Produkt: " + str(key_produkt["towar"]) + " jest w magazynie - liczba szt.: " + str(key_produkt["liczba_towaru"]))
        if key_produkt["towar"] != produkt_j:
            print("Brak produktu w magazynie.")

    elif komenda == "PRZEGLAD":
        print(f"Wprowadziłeś komendę {komenda}")

else:
    print("Nieznana komenda. Wpisz 'HELP', aby uzyskać informację na temat dostępnych komend w programie")
