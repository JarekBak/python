suma_ocen = 0
liczba_ocen = 0

while True:
    ocena = input("Podaj ocenę")

    if ocena:
        ocena_float = float(ocena)
        suma_ocen += ocena_float
        liczba_ocen += 1
    else:
        break

srednia_ocen = suma_ocen / liczba_ocen
print(f"Średnia ocen: {srednia_ocen}")