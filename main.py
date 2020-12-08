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


pgzrun.go()  # Linia ta jest konieczna
# aby okno nie zostało zamknięte
