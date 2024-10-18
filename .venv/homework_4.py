'''
Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników
(uczeń, nauczyciel, wychowawca) a także zarządzania nimi.

Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.

Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
Polecenie "koniec" - Kończy działanie aplikacji.

Proces tworzenia użytkowników:

Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec.
Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
Polecenie "uczeń" -
Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne,
jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
Polecenie "nauczyciel" -
Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie,
jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas,
które prowadzi nauczyciel, aż do otrzymania pustej linii.
Polecenie "wychowawca" -
Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone),
a także nazwę prowadzonej klasy.
Polecenie "koniec" - Wraca do pierwszego menu.

Proces zarządzania użytkownikami:

Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec.
Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów,
którzy należą do tej klasy, a także wychowawcę tejże klasy.
Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie lekcje,
które ma uczeń a także nauczycieli, którzy je prowadzą.
Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy,
które prowadzi nauczyciel.
Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów,
których prowadzi wychowawca.
Polecenie "koniec" - Wraca do pierwszego menu.
'''


class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def __str__(self):
        return f"<Uczeń: {self.imie} {self.nazwisko} - klasa: {self.klasa}>"

    # def get_class(self):
    #     return self.klasa

class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, klasy_lista):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy_lista

    def __str__(self):
        return f"<Nauczyciel: {self.imie} {self.nazwisko} - klasy: {self.klasy}, przedmiot: {self.przedmiot}>"

class Wychowawca:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def __str__(self):
        return f"<Wychowawca: {self.imie} {self.nazwisko} - klasa: {self.klasa}>"

    # def get_class(self):
    #     return self.klasa

def wczytaj_obiekt(typ_obiektu):

    # wczytanie danych
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    if typ_obiektu == "Uczen":
        klasa = input("Podaj klasę: ")
    elif typ_obiektu == "Wychowawca":
        klasa = input("Podaj klasę: ")
    elif typ_obiektu == "Nauczyciel":
        przedmiot = input("Podaj przedmiot: ")
        klasy = input("Podaj klasę: ")
        klasy_lista = []
        klasy_lista.append(klasy)
        while klasy != "":
            klasy = input("Podaj kolejną klasę: ")
            klasy_lista.append(klasy)

    # Utworzenie obiektu
    if typ_obiektu == "Uczen":
        obiekt = Uczen(imie, nazwisko, klasa)
    elif typ_obiektu == "Nauczyciel":
        obiekt = Nauczyciel(imie, nazwisko, przedmiot, klasy_lista)
    elif typ_obiektu == "Wychowawca":
        obiekt = Wychowawca(imie, nazwisko, klasa)
    else:
        obiekt = None
    return obiekt

def fun_akcja_utworz():
    while True:
        akcja_utworz = input("Co chcesz utworzyć? [uczen, nauczyciel, wychowawca, koniec]: ")
        if akcja_utworz == "koniec":
            break
        elif akcja_utworz == "uczen":
            print("Dodaj ucznia")
            nowy_uczen = wczytaj_obiekt("Uczen")
            uczniowie.append(nowy_uczen)

        elif akcja_utworz == "nauczyciel":
            print("Dodaj nauczyciela")
            nowy_nauczyciel = wczytaj_obiekt("Nauczyciel")
            nauczyciele.append(nowy_nauczyciel)

        elif akcja_utworz == "wychowawca":
            print("Dodaj wychowawcę")
            nowy_wychowawca = wczytaj_obiekt("Wychowawca")
            wychowawcy.append(nowy_wychowawca)
        else:
            print(f"Podana komenda w akcji {akcja_utworz} nie istenieje. Spróbuj jeszcze raz")

def fun_klasa():
    wyszukaj_klase = input("Podaj nr klasy: ")
    print(f"Lista uczniów klasy {wyszukaj_klase}:")
    for uczen in uczniowie:
        if uczen.klasa == wyszukaj_klase:
            print(f"- {uczen.imie} {uczen.nazwisko}")
    for wychowawca in wychowawcy:
        if wychowawca.klasa == wyszukaj_klase:
            print(f"Wychowawca klasy {wyszukaj_klase}: {wychowawca.imie} {wychowawca.nazwisko}")

def fun_uczen():
    imie_ucz = input("Podaj imię ucznia: ")
    nazwisko_ucz = input("Podaj nazwisko ucznia: ")
    for uczen in uczniowie:
        if imie_ucz == uczen.imie and nazwisko_ucz == uczen.nazwisko:
            print(f"Uczeń {imie_ucz} {nazwisko_ucz} uczestniczy w następujących lekcjach:")
            print(uczen.klasa)
            for nauczyciel in nauczyciele:
                if uczen.klasa in nauczyciel.klasy:
                    print(f"- {nauczyciel.przedmiot} - {nauczyciel.imie} {nauczyciel.nazwisko}")

def fun_nauczyciel():
    imie_nauczyciela = input("Podaj imię nauczyciela: ")
    nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela: ")
    for nauczyciel in nauczyciele:
        if imie_nauczyciela == nauczyciel.imie and nazwisko_nauczyciela == nauczyciel.nazwisko:
            print(f"Lista prowadzonych klas przez {nauczyciel.imie} {nauczyciel.nazwisko}:")
            for klasy in nauczyciel.klasy[:-1]:
                print(f"- {klasy}")

def fun_wychowawca():
    imie_wych = input("Podaj imię wychowawcy: ")
    nazwisko_wych = input("Podaj nazwisko wychowawcy: ")
    for wychowawca in wychowawcy:
        if imie_wych == wychowawca.imie and nazwisko_wych == wychowawca.nazwisko:
            print(f"Lista uczniów klasy {wychowawca.klasa}, których wychowacą jest {wychowawca.imie} {wychowawca.nazwisko}:")
            for uczen in uczniowie:
                if wychowawca.klasa == uczen.klasa:
                    print(f"- {uczen.imie} {uczen.nazwisko}")

def fun_akcja_zarzadzaj():
    while True:
        akcja_zarzadzaj = input("Czym chcesz zarządzić? [klasa, uczen, nauczyciel, wychowawca, koniec]: ")
        if akcja_zarzadzaj == "koniec":
            break
        elif akcja_zarzadzaj == "klasa":
            print("Panel zarządzania klasą")
            fun_klasa()
        elif akcja_zarzadzaj == "uczen":
            print("Panel zarządzania uczniem")
            fun_uczen()
        elif akcja_zarzadzaj == "nauczyciel":
            print("Panel zarządzania nauczycielem")
            fun_nauczyciel()
        elif akcja_zarzadzaj == "wychowawca":
            print("Panel zarządzania wychowawcą")
            fun_wychowawca()
        else:
            print(f"Podana komenda w akcji {akcja_zarzadzaj} nie istenieje. Spróbuj jeszcze raz")

nauczyciele = []
uczniowie = []
wychowawcy = []

print("Witaj w programie bazy szkolnej")

while True:
    akcja = input("Co chcesz zrobić: [utworz/zarzadzaj/koniec]: ")

    if akcja == "koniec":
        break

    elif akcja == "utworz":
        print("Utwórz: [uczen, nauczyciel, wychowawca, koniec]")
        fun_akcja_utworz()

    elif akcja == "zarzadzaj":
        print("Zarządzaj: [klasa, uczen, nauczyciel, wychowawca, koniec]")
        fun_akcja_zarzadzaj()

    else:
        print(f"Podana komenda {akcja} nie istnieje! Spróbój jeszcze raz!")

for uczen in uczniowie:
    print(uczen)
print("-"*100)
for nauczyciel in nauczyciele:
    print(nauczyciel)
print("-"*100)
for wychowawca in wychowawcy:
    print(wychowawca)
