import pgzrun  # importujemy bibliotekę
# Pygame Zero

# tworzymy pustą listę
# następnie dodajemy do niej cztery
# obiekty klasy Actor, każdy z tych
# obiektów różni się grafiką oraz pozycją
# obiektu na ekranie
chmury = [Actor('cloud1', (200, 200)),
          Actor('cloud2', (400, 300)),
          Actor('cloud3', (600, 200)),
          Actor('cloud1', (800, 300))]

# tworzymy obiekt klasy Actor gracza
# pierwszy argument – nazwa grafiki
# drugi argument – krotka, pozycja
gracz = Actor('p3_stand', (100, 484))

stan_gry = 0  # zmienna reprezentująca
# stan gry
# 0 – gra nie rozpoczęta
# 1 – rozpoczyna rozgrywkę
# 2 – ekran końcowy

klatka = 0  # zmienna globalna
# reprezentująca, która klatka
# animacji ma być aktualnie odtworzona

skok = 0  # zmienna globalna
# reprezentująca szybkość oraz kierunek
# przemieszczania się gracza

blokada_skoku = 0  # zmienna globalna
# będąca flagą
# 0 – skok jest możliwy
# 1 – skok nie jest możliwy

szybkosc_ruchu_chmur = 2
# zmienna globalna określająca
# z jaką szybkością mają się przesuwać
# chmury na ekranie

czas_gry = 0
# zmienna globalna przechowywująca
# czas gry


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
    for chmura in chmury:  # pętla przechodząca po liście
        chmura.draw()  # dla każdego obiektu wywołujemy
        # metodę rysującą dany element listy na ekranie
    screen.draw.text(
        wyrownaj_napis_czas(czas_gry),
        midright=(screen.width - 50, 50),
        fontname="roboto_mono_bold",
        color="orange",
        fontsize=45
    )
    # wyświetlanie licznika czasu
    # w prawym górnym rogu ekranu

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
    global stan_gry
    # ustawienie zmiennej stan_gry jako globalnej
    global skok
    # ustawienie zmiennej skok jako globalnej
    global blokada_skoku
    # ustawienie zmiennej blokada_skoku jako globalnej
    if keyboard.SPACE:  # sprawdza, czy został
        # wciśnięty klawisz spacji
        # jeśli tak
        if stan_gry == 0:
            # jeśli gra nie rozpoczęła się
            blokada_skoku = 1  # zablokuj skok
            clock.schedule_unique(zwolnienie_blokady, 0.3)
            # odblokowanie skoku nastąpi po 0.3 sekundy
        stan_gry = 1  # rozpocznij grę
        if blokada_skoku == 0:
            # jeśli skok możliwy do wykonania
            # wartość zero
            skok = -18
            # ustaw szybkość skoku na 18 pikseli
            blokada_skoku = 1
            # zablokuj możliwość ponownego skoku
            sounds.jingles_jump.play()
            # włączenie odtwarzania pliku
            # dźwiękowego jingles_jump
    animacja()
    # uruchom funkcję odpowiedzialną za animacje postaci
    skok_opadanie()
    # uruchom funkcję kontrolującą skok oraz opadanie
    ruch_chmur()
    # uruchom funkcję odpowiedzialną za ruch chmur


def odmierzaj_czas():  # funkcja ta wykonuje się
    # co 0.1sekudny,tymsamymzwiększaglobalnązmienną
    # przechowywującą liczbę sekund o 1
    # jeśli gra jeszcze się nie rozpoczęła, funkcja ta
    # ustawia globalna zmienna czas_gry na 0
    global czas_gry
    global stan_gry
    if stan_gry == 0:
        czas_gry = 0
    elif stan_gry == 1:
        czas_gry += 1


def wyrownaj_napis_czas(czas):
    # funkcja ta przyjmuje liczbę
    # funkcja ta zamienia liczbę na napis
    # o stałej szerokości wynoszącej zawsze 6 znaków
    napis = "0" * (5 - len(str(czas)))
    napis += str(czas)
    return napis


def ruch_chmur():  # funkcja odpowiedzialna za poruszanie
    # się chmur na ekranie oraz ich zawijanie
    # tak aby uzyskać efekt nieskończoności
    global szybkosc_ruchu_chmur
    # ustawienie zmiennej szybkosc_ruchu_chmur
    # jako globalnej
    global stan_gry
    # ustawienie zmiennej stan_gry jako globalnej

    # jeśli gra rozpoczęła się, to
    if stan_gry == 1:
        # przejdź listę obiektów chmur
        for chmura in chmury:
            # zmień każdemu z obiektów w liście chmury
            # wartość składowej x o wartość zmiennej
            # szybkosc_ruchu_chmur
            chmura.x -= szybkosc_ruchu_chmur
            # jeśli którykolwiek z obiektów
            # dotyka lewej krawędzi okna
            if chmura.x + 64 < 0:
                # to ustaw pozycję tej chmury
                # tak aby była z prawej strony
                chmura.x = screen.width + 32


def zwolnienie_blokady():  # funkcja odpowiedzialna
    # za zwalnaianie blokady skoku
    # zmienia wartość zmiennej blokada_skoku na zero
    global blokada_skoku
    # ustawienie zmiennej stan_gry jako globalnej
    blokada_skoku = 0
    # zwalnianie blokady skoku


def skok_opadanie():  # funkcja odpowiedzialna za
    # skok oraz opadanie
    global skok
    # ustawienie zmiennej skok jako globalnej
    global klatka  # zmienna globalna
    # decydująca, która klatka
    # animacji ma zostać aktualnie wyświetlona
    if skok != 0:  # jeśli skok aktywny
        klatka = 0  # zablokowanie animacji
        gracz.y += skok
        # gracz zmienia swoją pozycją o wartość
        # zmiennej skok
    if gracz.y >= 484:  # jeśli gracz dotknął podłoża
        zwolnienie_blokady()
        # następuje zwolnienie blokady skoku
        skok = 0
        # wartość zero gwarantuje, że nasz bohater
        # będzie stał w miejscu tuż nad podłożem
    if gracz.y <= 250:  # jeśli gracz znajduje się
        # wyżej niż wartość 250 na osi y
        # zacznij opadanie
        skok *= (-1)  # zmiana kierunku
        # poruszania się sprite


def animacja():  # funkcja odpowiedzialna za
    # animacje postaci gracza
    global klatka  # zmienna globalna
    # decydująca, która klatka
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
    # #zmiennej klatka przez 11
    # wynik takiej operacji to liczba większa bądź
    # równa zero oraz mniejsza od 11


clock.schedule_interval(odmierzaj_czas, 0.1)
# wywołujemy funkcję odmierzaj_czas() co 0.1 sekundy
pgzrun.go()  # Linia ta jest konieczna
# aby okno nie zostało zamknięte
