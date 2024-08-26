# jeżeli wzrost >= 140 możesz wejść do sklepu
#  - jeżeli wzrost 120-140 and wiek > 14 lat - możesz wejść do sklepu
# jeżeli wzrost < 140 nie możesz wejść do sklepu
# jeżeli wiek >= 16 możesz wejść do sklepu
# jeżeli wiek < 16 nie możesz wejść do sklepu
# błędne wartości

wiek = 0
while not (wiek >0 and wiek <= 122):
    wiek = int(input("Podaj wiek: "))

    if (wiek > 0 and wiek <=122):
        print("Wiek poprawny. Dziękuję bardzo")
    else:
        print("Niepoprawny wiek! Wprowadź ponownie")

wzrost = 0.0
while not (wzrost >30 and wiek <= 260):
    wzrost = float(input("Podaj wzrost: "))

    if (wzrost >30 and wiek <=260):
        print("Poprawny wzrost. Dziękuję bardzo :)")
    else:
        print("Niepoprawny wzrost. Wprowadź ponownie")



