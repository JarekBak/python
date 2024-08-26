liczba = 10
print(type(liczba))
liczba2 = 10.5
print(type(liczba2))
liczba3 = "10"
print(type(liczba3))

print(liczba+1)
print(liczba3*3)
print(int(liczba3)+1) #tutaj można przekonwertorować zmienną str na int (ważne musi tu być wpisana liczba)

liczba_3_przekonwertowana = bool(liczba3)
print(liczba_3_przekonwertowana)

#prosty program zachowujący się jak kalkulator
imie = input("Podaj swoje imię: ")
print("\n")

print(f"Cześć {imie}! Jestem kalkulatorem, który wykonuje działania na dwóch liczbach. Podaj swoje liczby \n")
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

dodawanie = a+b
odejmowanie = a-b
mnożenie = a*b
dzielenie = a/b
dzielenie_bez_reszty = a//b
potegowanie = a**b #lub pow(a,b)
reszta_z_dzielenia = a%b

# print(dodawanie)#samo działanie matematyczne
# print("Dodawanie: " +str(dodawanie))#łączenie z tekstem - str
#
# szablon_dodawanie = "Dodawanie: {}"
# print(szablon_dodawanie.format(dodawanie))#lepszy sposób na pokazywanie stringów
#
# SZABLON_DODAWANIE = "Dodawanie: {}"
# print(SZABLON_DODAWANIE.format(dodawanie))#CAPSLOCK możemy dzięki temy zaznaczyć, że jest to STAŁA
#
# # SZABLON_DODAWANIE = "Dodawanie: {}"


print(f"Dodawanie: \t \t {dodawanie}")
print(f"Odejmowanie: \t \t {odejmowanie}")
print(f"Mnożenie: \t \t {mnożenie}")
print(f"Dzielenie: \t \t {dzielenie}")
print(f"Dzielenie bez reszty: \t {dzielenie_bez_reszty}")
print(f"Potęgowanie: \t \t {potegowanie}")
print(f"Reszta z dzielenia: \t {reszta_z_dzielenia}")
