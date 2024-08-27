print("--- PROGRAM DO OBSŁUGI WYSYŁKI PACZEK ---")

liczba_el = int(input("Podaj liczbę elementów do wysłania: "))

i=0
waga_paczki = 0
while i < liczba_el:
    waga_el = float(input(f"Podaj wagę elementu nr {i+1} do wysłania: ")) #podajemy dane o elementach do spakowania
#
    if waga_el <1 or waga_el >10: #warunek, dla którego nie można wysłać elementu
        print("Zła waga elementu - nie nadaje się do wysłania!")

    else: #sumuje wagę dopuszczonych do wysyłki elementów
        waga_paczki = waga_paczki + waga_el
        #ile_wysylka = liczba_el - ile
        i += 1
#     for waga_el in range (liczba_el):
#         if waga_el <1 or waga_el >10: #warunek, dla którego nie można wysłać elementu
#             print("Zła waga elementu - nie nadaje się do wysłania!")
#         else:
#             waga_paczki = waga_paczki + waga_el
#         i += 1

print(f"\n--- PODSUMOWANIE --- \n Liczba elementów w paczce: {i} \n Waga paczki: {waga_paczki} kg")
