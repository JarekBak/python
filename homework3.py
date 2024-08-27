print("--- PROGRAM DO OBSŁUGI WYSYŁKI PACZEK ---")

liczba_el = int(input("Podaj liczbę elementów do wysłania: "))
i = 0
waga_paczki = 0

for paczki in range(liczba_el):
    # podajemy dane o elementach do spakowania
    waga_el = float(input(f"Podaj wagę elementu nr {i+1} do wysłania: "))
    i += 1
    # warunek, dla którego nie można wysłać elementu
    if waga_el < 1 or waga_el > 10:
        print("Zła waga elementu - nie nadaje się do wysłania!")
    else:
        waga_paczki = waga_paczki + waga_el

print(f"\n--- PODSUMOWANIE --- \n Liczba elementów w paczce: {i} \n Waga paczki: {waga_paczki} kg")
