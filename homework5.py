from utils import (
    wyswietl_powitanie,
    wyswietl_pomoc,
    wczytaj_produkt,
    wczytaj_liste,
    podaj_saldo,
    sprzedaz_produktu,
    zakup_produktu,
    sprawdz_konto,
    sprawdz_magazyn,
    przeglad_operacji
)

from global_var import suma_materialow

produkt_all = wczytaj_produkt()

# Główna pętla programu
while True:
    wyswietl_powitanie()
    komenda = input("\nWprowadź komendę lub wpisz 'HELP' jeżeli chcesz poznać listę komend w programie: ").upper()
    # warunek po wprowadzeniu komendy przez użytkownika
    if komenda == "KONIEC":
        print("Zamykam program")
        break
    elif komenda == "HELP":
        wyswietl_pomoc()

    elif komenda == "SALDO":
        podaj_saldo()

    elif komenda == "SPRZEDAZ":
        sprzedaz_produktu(produkt_all)

    elif komenda == "ZAKUP":
        zakup_produktu(produkt_all)

    elif komenda == "KONTO":
        sprawdz_konto(produkt_all, suma_materialow)

    elif komenda == "LISTA":
        # wyświetlenie wszystkich produktów w magazynie
        wczytaj_liste(produkt_all)

    elif komenda == "MAGAZYN":
        sprawdz_magazyn(produkt_all)

    elif komenda == "PRZEGLAD":
        przeglad_operacji()

    else:
        print("Nieznana komenda. Wpisz 'HELP', aby uzyskać informację na temat dostępnych komend w programie")
