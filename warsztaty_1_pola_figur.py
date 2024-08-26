#pole trójkąta

print("Ten program liczy pole trójkąta")
imie = input("Cześć! Podaj swoje imię: ")

a = float(input("Podaj długość podstawy trójkąta: "))
h = float(input("Podaj wysokość trójkąta: "))

pole_trojkata = (a*h)/2

print(f"Cześć {imie} - pole Twojego trójkąta wynosi: {pole_trojkata}")

#pole prostokąta

print("Cześć! Jestem programem liczącym pole prostokąta")

a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
pole_prostokata = a*b

print(f"Pole prostokąta o boku {a} oraz {b} wynosi {pole_prostokata}")

# pole trapezu

print("Cześć - obliczmy pole trapezu")
bok_a = float(input("Podaj podstawę a ="))
bok_b = float(input("Podaj podstawę b: "))
wysokosc = float(input("Podaj wysokość trapezu: "))

pole_trapezu = ((bok_b + bok_a)*wysokosc)/2

print(f"Pole Twojego trapezu o podstawach {bok_a} oraz {bok_b} oraz wysokości {wysokosc} wynosi {pole_trapezu}")

#Twierdzenie Pitagorasa
import math
#można też użyć from math import sqrt lub import math as m

print("Program liczy długość przeciwprostokątnej z twierdzenia pitagorasa")
print("Tw. Pitagorasa: a^2 + b^2 = c^2. Liczymy c :) \n\n")

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))

print(f"Wartość a: {a}")
print(f"Wartość b: {b}")

c_kwadrat = a**2 + b**2
c_kwadrat2 = pow(a, 2) + pow(b, 2)

c = math.sqrt(c_kwadrat)# jeżeli korzystamy ze składni "from math import sqrt" powinno to wyglądać tak: c = sqrt(c_kwadrat)
#jeżeli korzystamy import math as m to należy użyć: c = m.sqrt(c_kwadrat)

print(f"c^2 wynosi: {c_kwadrat}")
print(f"c^2 wynosi: {c_kwadrat2}")
print(f"bok c wynosi: {c}")

