import pgzrun  # importujemy bibliotekę
# Pygame Zero

# tworzymy obiekt klasy Actor, gracza
# pierwszy argument - nazwa grafiki
# drugi argument - krotka, pozycja
gracz = Actor('p3_stand', (100, 484))

stan_gry = 0  # zmienna reprezentująca
# stan gry
# 0 - gra nie rozpoczęta
# 1 - rozpoczyna rozgrywkę
# 2 - ekran końcowy

klatka = 0  # zmienna globalna


# reprezentujaca która klatka
# animacji ma być aktualnie odtworzona

def draw():  # funkcja rysująca
    global stan_gry  # ustawienie zmiennej stan_gry
    # jako zmiennej globalnej
    screen.clear()  # metoda czyszcząca ekran
    screen.fill('#cff4f7')
    # metoda wypełniająca kolorem
    for i in range((screen.width // 70) + 1):
        screen.blit('grass', (i * 70, screen.height - 70))
        # rysuje grafikę o nazwie
        # grass w punkcie 0,0
    gracz.draw()  # rysujemy obiekt gracza
    if stan_gry == 0:
        # jeśli gra się nie rozpoczęła
        screen.draw.text(
            "Wciśnij spację",
            center=(screen.width / 2, screen.height / 2),
            color="orange",
            fontsize=60
        )
        # wyświetla napis "Wciśnij spację" 
        # na środku ekranu


def update():  # funkcja wykonuje się co klatkę
    global stan_gry  # ustawienie zmiennej stan_gry
    if keyboard.SPACE:  # sprawdza czy został
        # wciśnięty klawisz spacji
        # jeśli tak
        stan_gry = 1
    animacja()


def animacja():  # funkcja odpowiedzialna za
    # animacje postaci gracza
    global klatka  # zmienna globalna
    # decydujaca, która klatka
    # animacji ma zostać aktualnie wyświetlona
    if stan_gry == 1:  # jeśli gra się rozpoczęła

        # jeśli klatka jest równa 0
        # zmień kostium gracza na ten
        # z pliku p3_walk01
        if klatka == 0:
            gracz.image = 'p3_walk01'

        # jeśli klatka jest równa 1
        # zmień kostium gracza na ten
        # z pliku p3_walk02         
        elif klatka == 1:
            gracz.image = 'p3_walk02'

        # jeśli klatka jest równa 2
        # zmień kostium gracza na ten
        # z pliku p3_walk03
        elif klatka == 2:
            gracz.image = 'p3_walk03'

        # jeśli klatka jest równa 3
        # zmień kostium gracza na ten
        # z pliku p3_walk04
        elif klatka == 3:
            gracz.image = 'p3_walk04'

        # jeśli klatka jest równa 4
        # zmień kostium gracza na ten
        # z pliku p3_walk05
        elif klatka == 4:
            gracz.image = 'p3_walk05'

        # jeśli klatka jest równa 5
        # zmień kostium gracza na ten
        # z pliku p3_walk06
        elif klatka == 5:
            gracz.image = 'p3_walk06'

        # jeśli klatka jest równa 6
        # zmień kostium gracza na ten
        # z pliku p3_walk07
        elif klatka == 6:
            gracz.image = 'p3_walk07'

        # jeśli klatka jest równa 7
        # zmień kostium gracza na ten
        # z pliku p3_walk08
        elif klatka == 7:
            gracz.image = 'p3_walk08'

        # jeśli klatka jest równa 8
        # zmień kostium gracza na ten
        # z pliku p3_walk09
        elif klatka == 8:
            gracz.image = 'p3_walk09'

        # jeśli klatka jest równa 9
        # zmień kostium gracza na ten
        # z pliku p3_walk10
        elif klatka == 9:
            gracz.image = 'p3_walk10'

        # jeśli klatka jest równa 10
        # zmień kostium gracza na ten
        # z pliku p3_walk11
        elif klatka == 10:
            gracz.image = 'p3_walk11'

    klatka += 1  # zwiększ wartość 
    # zmiennej klatka o 1
    klatka %= 11  # obliczamy resztę z dzielenia
    # zmiennej klatka przez 11
    # wynik takiej operacji będzie liczba większa bądź
    # równa zero oraz mniejsza od 11


pgzrun.go()  # Linia ta jest konieczna
# aby okno nie zostało zamknięte
