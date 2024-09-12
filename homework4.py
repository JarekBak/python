print(5*"-"+"SYSTEM KSIĘGOWO-MAGAZYNOWY"+5*"-")
komenda = input("\nWprowadź komendę lub 'HELP' jeżeli chcesz listę komend w programie: ")

# warunek po wprowadzeniu komendy przez użytkownika
if komenda == "koniec":
    print("Zamykam program")
else:
    if komenda == "saldo":
        print("saldo")
    elif komenda == "sprzedaz":
        print("sprzedaz")
    elif komenda == "zakup":
        print("zakup")
    elif komenda == "konto":
        print("konto")
    elif komenda == "lista":
        print("lista")
    elif komenda == "magazyn":
        print("magazyn")
    elif komenda == "przeglad":
        print("przeglad")
    elif komenda == "HELP":
        print("""lISTA KOMEND W PROGRAMIE:
    saldo
    sprzedaz
    zakup
    konto
    lista
    magazyn
    przeglad
    koniec""")
