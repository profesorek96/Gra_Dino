import pgzrun # importujemy bibliotekę
# Pygame Zero
import random # importujemy bibliotekę
# random

# tworzymy listę zawierającą cztery
# obiekty klasy Actor, każdy z tych
# obiektów różni się grafiką oraz pozycją
# obiektu na ekranie
chmury = [Actor('cloud1', (200, 200)),
          Actor('cloud2', (400, 300)),
          Actor('cloud3', (600, 200)),
          Actor('cloud1', (800, 300))]

# tworzymy listę zawierającą trzy obiekty
# klasy Actor, każdy z nich różni się pozycją
# wartość współrzędnej x dla każdego z obiektów
# jest losowa
przeszkody=[Actor('cactus', (random.randint(900,1000), 495)),
            Actor('cactus', (random.randint(1200,1500), 495)),
            Actor('cactus', (random.randint(1500,2000), 495))]

# tworzymy obiekt klasy Actor gracza
# pierwszy argument – nazwa grafiki
# drugi argument – krotka, pozycja
gracz = Actor('p3_stand', (100, 484))

stan_gry = 0 # zmienna reprezentująca
# stan gry
# 0 – gra nie rozpoczęta
# 1 – rozpoczyna rozgrywkę
# 2 – ekran końcowy

klatka = 0 # zmienna globalna
# reprezentująca, która klatka
# animacji ma być aktualnie odtworzona

skok = 0 # zmienna globalna
# reprezentująca szybkość oraz kierunek
# przemieszczania się gracza

blokada_skoku = 0 # zmienna globalna
# będąca flagą
# 0 – skok jest możliwy
# 1 – skok nie jest możliwy

szybkosc_ruchu_chmur = 2
# zmienna globalna określająca
# z jaką szybkością mają się przesuwać
# chmury na ekranie

czas_gry = 0
# zmienna globalna przechowująca
# czas gry

szybkosc_gry = 8
# zmienna globalna określająca
# z jaką szybkością mają się przesuwać
# kaktusy na ekranie

blokada_wznowienia_gry = 0
# zmienna globalna
# będąca flagą
# 0 – gra uruchomiona
# 1 – gra zablokowana


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
    for przeszkoda in przeszkody:
        przeszkoda.draw()  # dla każdego obiektu wywołujemy
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

    if stan_gry == 2:
        # jeśli gra się zakończyła
        screen.draw.text(
            "Koniec gry",
            center = (screen.width / 2, screen.height / 2),
            color = "red",
            fontsize = 60
        )
        screen.draw.text(
            "Wciśnij spację, aby zagrać jeszcze raz",
            center = (screen.width / 2, screen.height - 200),
            color = "orange",
            fontsize = 30
        )
        # wyświetla napis "Koniec Gry"
        # na środku ekranu oraz
        # napis "Wciśnij spację, aby zagrać jeszcze raz"


def update():  # funkcja wykonuje się co klatkę
    global stan_gry
    # ustawienie zmiennej stan_gry jako globalnej
    global skok
    # ustawienie zmiennej skok jako globalnej
    global blokada_skoku
    # ustawienie zmiennej blokada_skoku jako globalnej
    global blokada_wznowienia_gry
    # ustawienie zmiennej blokada_wznowienia_gry
    # jako globalnej
    if keyboard.SPACE and blokada_wznowienia_gry == 0:
        # sprawdza, czy został
        # wciśnięty klawisz spacji oraz czy można wznowić
        # grę, jeśli tak
        if stan_gry == 0 or stan_gry == 2:
            # jeśli gra nie rozpoczęła się ani nie zakończyła
            blokada_skoku = 1 # zablokuj skok
            clock.schedule_unique(zwolnienie_blokady, 0.3)
            # odblokowanie skoku nastąpi po 0.3 sekundy
            reset()
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
    ruch_przeszkody()
    # uruchom funkcję odpowiedzialną za ruch przeszkód
    sprawdz_kolizje()
    # uruchom funkcję odpowiedzialną
    # za sprawdzanie kolizji


def zmiania_trudnosci():
    # funkcja odpowiedzialna
    # za zmianę poziomu trudności gry
    # poprzez zwiększenie szybkości gry
    # oraz szybkości poruszania się chmur
    global szybkosc_gry
    # ustawienie zmiennej
    # szybkosc_gry jako globalnej
    global szybkosc_ruchu_chmur
    # ustawienie zmiennej szybkosc_ruchu_chmur
    # jako globalnej
    if szybkosc_gry < 16:
        # jeśli szybkosc_gry jest mniejsza
        # od 16, to zwiększ wartość o jeden
        # zmiennej szybkosc_gry oraz
        # zmiennej szybkosc_ruchu_chmur
        szybkosc_gry += 1
        szybkosc_ruchu_chmur += 1


def reset():
    # funkcja odpowiedzialna za resetowanie
    # wartości zmiennych do tych znanych
    # z początku rozgrywki
    global klatka
    # ustawienie zmiennej klatka jako globalnej
    global stan_gry
    # ustawienie zmiennej stan_gry jako globalnej
    global skok
    # ustawienie zmiennej skok jako globalnej
    global blokada_skoku
    # ustawienie zmiennej blokada_skoku jako globalnej
    global szybkosc_ruchu_chmur
    # ustawienie zmiennej szybkosc_ruchu_chmur
    # jako globalnej
    global szybkosc_gry
    # ustawienie zmiennej
    # szybkosc_gry jako globalnej
    global czas_gry
    # ustawienie zmiennej
    # czas_gry jako globalnej
    if stan_gry == 2:
        # jeśli stan_gry równa się zero
        # przywróć domyślne wartości zmiennym
        klatka = 0
        stan_gry = 0
        skok = 0
        blokada_skoku = 1
        szybkosc_ruchu_chmur = 2
        szybkosc_gry = 8
        czas_gry = 0
        gracz.pos = (100, 484)
        chmury[0].pos = (200, 200)
        chmury[1].pos = (400, 300)
        chmury[2].pos = (600, 200)
        chmury[3].pos = (800, 300)
        przeszkody[0].pos = (random.randint(900, 1000), 495)
        przeszkody[1].pos = (random.randint(1200, 1500), 495)
        przeszkody[2].pos = (random.randint(1500, 2000), 495)
        clock.unschedule(zmiania_trudnosci)
        # odwołanie działania metody schedule_interval
        # dla funkcji zmiana_trudnosci
        clock.schedule_interval(zmiania_trudnosci, 20)
        # wywołujemy funkcję zmiana_trudnosci()
        # co 20 sekund


def zwolnienie_blokady_wznowienia_gry():
    # funkcja odpowiedzialna
    # za zwalnianie blokady wznowienia gry
    # zmienia wartość zmiennej
    # blokada_wznowienia_gry na zero
    global blokada_wznowienia_gry
    # ustawienie zmiennej blokada_wznowienia_gry
    # jako globalnej
    blokada_wznowienia_gry = 0


def sprawdz_kolizje():
    # funkcja odpowiedzialna za sprawdzanie
    # czy nastąpiła kolizja któregoś z kaktusów
    # z graczem
    global stan_gry
    # ustawienie zmiennej stan_gry jako globalnej
    global blokada_wznowienia_gry
    # ustawienie zmiennej blokada_wznowienia_gry
    # jako globalnej
    if stan_gry == 1:
        # jeśli gra się rozpoczęła
        for i in przeszkody:
            # iterujemy po liście przeszkody
            if gracz.collidepoint(i.x, i.y):
                # jeśli gracz ma kolizję z którąś
                # z przeszkód, to
                stan_gry = 2  # zmieniamy stan_gry
                # na 2, co oznacza wyświetlenie
                # ekranu końcowego
                sounds.jingles_end.play()
                # odtwarzamy dźwięk porażki
                blokada_wznowienia_gry = 1
                # blokujemy możliwość wznowienia gry
                clock.schedule_unique(
                    zwolnienie_blokady_wznowienia_gry,
                    2.0
                )
                # ustawiamy zwolnienie blokady
                # wznowienia gry za 2 sekundy


def ruch_przeszkody():
    global szybkosc_gry
    # ustawienie zmiennej
    # szybkosc_gry jako globalnej
    global stan_gry
    # ustawienie zmiennej stan_gry jako globalnej
    if stan_gry == 1:
        # jeśli gra się rozpoczęła
        for i in range(len(przeszkody)):
            # iterujmy po liście przeszkody
            przeszkody[i].x -= szybkosc_gry
            # zmniejszamy wartość x dla każdej
            # przeszkody o aktualną wartość zmiennej
            # szybkosc_gry
            if przeszkody[i].x + 35 < 0:
                # jeśli przeszkoda wyszła poza
                # ekran z lewej strony
                przeszkody[i].x = random.randint(900, 1500)
                # losujemy nową pozycję dla tej
                # przeszkody z zakresu 900 do 1500
                for j in range(0, len(przeszkody)):
                    # iterujemy po liście przeszkód
                    # sprawdzając, czy wylosowana pozycja nie
                    # pokrywa się z pozycją innej przeszkody
                    # oraz czy nie są zbyt blisko siebie
                    if j!=i \
                    and \
                    abs(przeszkody[i].x - przeszkody[j].x) < 300:
                        przeszkody[i].x += 400
                        # jeśli tak, dodajemy do aktualnej
                        # pozycji 400 dla wylosowanej
                        # przeszkody


def odmierzaj_czas(): # funkcja ta wykonuje się
    # co 0.1 sekundy, tym samym zwiększa globalną zmienną
    # przechowującą liczbę sekund o 1
    # jeśli gra jeszcze się nie rozpoczęła, funkcja ta
    # ustawia globalną zmienną czas_gry na 0
    global czas_gry
    global stan_gry
    if stan_gry == 0:
        czas_gry = 0
    elif stan_gry == 1:
        czas_gry += 1


def wyrownaj_napis_czas(czas):  # funkcja ta przyjmuje liczbę
    # funkcja ta zamienia liczbę na napis o stałej szerokości
    # wynoszącej zawsze 6 znaków
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
        # przechodzimy listę obiektów
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
    # za zwalnianie blokady skoku
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
        # gracz zmienia swoją pozycję o wartość
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
    # zmiennej klatka przez 11
    # wynik takiej operacji to liczba większa bądź
    # równa zero oraz mniejsza od 11


clock.schedule_interval(odmierzaj_czas, 0.1)
# wywołujemey funkcję odmierzaj_czas() co 0.1 sekundy
clock.schedule_interval(zmiania_trudnosci, 20)
# wywołujemy funkcję zmiana_trudnosci() co 20 sekundy
pgzrun.go()  # linia ta jest konieczna
# aby okno nie zostało zamknięte
