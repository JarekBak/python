# liczba = int(input("Podaj liczbę całkowita: "))
#
# if liczba %2 == 0:
#     print("Liczba parzysta")#wcięcie bardzo istotne
#
# if liczba %2 != 0:
#     print("Liczba nieparzysta")
#
# print("Koniec programu")

#Program sprawdzający odpowiedni wiek, aby wejść do klubu

wiek = int(input("Ile masz lat?: "))
imie = input("Podaj swoje imię: ")

#do klubu może wejść każdy kto ma 18 lat

if wiek >= 18 and imie != "Kuba":
    print("Możesz wejść do klubu")
#if wiek < 18: # to też zadziała, ale poniżej lepszy sposób
else: #to jest lepsze rozwiązanie
    print("Nie możesz wejść do klubu")

#inna możliwość zapisania powyższego przy użyciu zagnieżdżonego kodu
if wiek <18:
    print("Nie możesz wejść do klubu")
else:
    if imie == "Kuba"
        print("Nie możesz wejść do Klubu")
    else:
        print("Możesz wejść do Klubu")