print("Podaj swoje imię")
imie = input()
print("Podaj swój wiek")
wiek = input()
print("Podaj swój ulubiony język programowania")
ulubiony_jezyk_programowania = input()

print("Cześć " + imie)
print("Masz " + wiek + " lat")
print("Mój ulubiony jezyk programowaina to też " +ulubiony_jezyk_programowania)

wiek_za_2_lata = int(wiek) + 2
print("Za dwa lata będziesz miał "+ str(wiek_za_2_lata))

print("Podaj swoje imię")
imie = str(input("IMIĘ: "))
print("Podaj swój wiek")
wiek = int(input("WIEK: "))
print("Cześć " + imie)
print("Masz " + str(wiek) + " lat")

print("Podaj swoje imię")
imie = str(input("IMIĘ: "))
print("Podaj swój wiek")
wiek = int(input("WIEK: "))
wiek_za_2_lata = int(wiek) + 2
szablon = "Cześć {}! Masz {} za 2 lata będziesz miał {}"
print(szablon.format(imie, wiek, wiek_za_2_lata))

print(f"Cześć {imie}! Masz {wiek} za 2 lata będziesz miał {wiek_za_2_lata}")#ta forma chyba najfajniejsza

#wieloliniowy model (przeglądnąć film i uzupełnić kod)


