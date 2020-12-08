import pgzrun  # importujemy bibliotekę
# Pygame Zero

def draw():  # funkcja rysująca
    screen.clear()  # metoda czyszcząca ekran
    screen.fill('#cff4f7')
    # metoda wypełniająca kolorem
    screen.blit('grass', (0, 0))
    # rysuje grafikę o nazwie grass w punkcie 0,0


def update():  # funkcja wykonuje się co klatkę
    pass  # pusta funkcja update


pgzrun.go()  # Linia ta jest konieczna
# aby okno nie zostało zamknięte
