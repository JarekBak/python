print("--- PROGRAM DO OBSŁUGI WYSYŁKI PACZEK ---")

liczba_el = int(input("Podaj liczbę elementów do wysłania: "))
i = 0
waga_paczki = 0
akt_waga_paczki = 0
max_paczki = 20
l_paczek = 1
nowa_l_paczek = 0
nowa_waga_paczki = 0
waga_sum = 0
nr_paczki_puste_miejsce = 1
max_puste_miejsce = 0
puste_miejsce = 0
n_puste_miejsce = 0

for paczki in range(liczba_el):
    # podajemy dane o elementach do spakowania
    waga_el = float(input(f"Podaj wagę elementu nr {i+1} do wysłania: "))

    i += 1

    # warunek, dla którego nie można wysłać elementu
    if waga_el < 1 or waga_el > 10:
        print("Zła waga elementu - nie nadaje się do wysłania!")

    # zliczanie wagi paczki na podstawie zadeklarowych wag poszczególnych elementów
    else:
        akt_waga_paczki = waga_paczki + waga_el
        nowa_waga_paczki += akt_waga_paczki

        # weryfikacja maksymalnego ciężaru paczki
        if nowa_waga_paczki > max_paczki:
            nowa_waga_paczki = akt_waga_paczki
            #dodanie kolejnej paczki
            l_paczek += 1

        # sumaryczna waga wysłanych elementów
        waga_sum += akt_waga_paczki

        # sprawdzenie pustego miejsca w paczce
        puste_miejsce = max_paczki - nowa_waga_paczki

        print(f"Waga paczki {l_paczek}: {nowa_waga_paczki}")
        print(f"W paczce zostało {puste_miejsce} kg")

        # weryfikacja, w której paczce jest najwięcej pustego miejsca
        if puste_miejsce > max_puste_miejsce:
            max_puste_miejsce = puste_miejsce
            nr_paczki_puste_miejsce = l_paczek
        else:
            n_puste_miejsce = puste_miejsce

print(f"Liczba wysłanych paczek: {l_paczek}")
print(f"W sumie wysłano: {waga_sum} kg")
print(f"Najwięcej pustego miejsca jest w paczce nr {nr_paczki_puste_miejsce}")
print(f"Zostało w niej {n_puste_miejsce} kg")
