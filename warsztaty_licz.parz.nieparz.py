# sprawdzenie czy liczba jest parzysta/nieparzysta

print("Ten program sprawdza czy liczba jest parzysta/nieparzysta")
liczba = int(input("Podaj liczbę całkowitą do sprawdzenia: "))

reszta = liczba %2

if (reszta ==0):
    print ("Liczba jest parzysta")
else:
    print ("Liczba jest nieparzysta")