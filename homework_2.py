import datetime as d

print("Witamy w generatorze życzeń urodzinowych!")
imie_nad = input("Podaj swoje imię: ")
imie_odb = input("Podaj imię solenizanta: ")
rok_ur = int(input("Podaj rok urodzenia solenizanta: "))
personal = input("Co chciałbyś dodać do życzeń od siebie?: ")

rok_akt = d.date.today().year
liczba_lat = rok_akt - rok_ur

print("Poniżej Twoje życzenia: \n")
print(f"{imie_odb} \nWszystkiego najlepszego z okazji {liczba_lat} urodzin. \n{personal} \n{imie_nad}")

