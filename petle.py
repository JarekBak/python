#for i in range(10): #range(lewa strona zakresu, prawa strona zakresu, o ile ma "skakać dany zakres)
    #print(i) # wynik będzie w zakresie od 0 do 9

#PETLA - przyklad 1
# suma = 0
# ile_liczb = int(input("Ile liczb chcesz do siebie dodać?"))
# for i in range(ile_liczb):
#     nowa_liczba = int(input(f"Liczba {i} "))
#     suma = suma + nowa_liczba
#
# print(f"Suma liczb wynosi {suma}")

#PETLA - while

ile_liczb = int(input("Ile liczb chcesz do siebie dodać?"))
suma = 0
i = 0
while i < ile_liczb:
    print(f"i: {i}")
    print(f"Suma: {suma}")

    nowa_liczba = int(input(f"Liczba {i} "))
    suma = suma + nowa_liczba
    i = i+1
    #i += 1 #to jest taki sam zapis jak i = i+1

print(f"Suma liczb wynosi {suma}")