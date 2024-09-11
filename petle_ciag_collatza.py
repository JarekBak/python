x = int(input("Podaj liczbę z zakresu od 1 do 100: "))
if x > 100:
    print("Podałeść zbyt dużą liczbę. Spróbuj jeszcze raz")
else:
    for i in range(1, 101):
        if x == 1:
            break
        else:
            if x % 2 == 0:
                x = x / 2
            else:
                x = (3 * x) + 1
            print(x)