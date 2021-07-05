# Gra Dino
## Spis treści
* [__O projekcie__](#o-projekcie)
* [__Uruchomienie__](#uruchomienie)
* [__Gameplay__](#gameplay)
* [__Technologie__](#technologie)
* [__Assety__](#assety)
* [__Status__](#status)
* [__Licencja__](#licencja)


## O projekcie
Projekt powstał na potrzeby serii artykułów publikowanych na łamach magazynu Programista Junior. 
Gra powstała z wykorzystaniem freamworka Pygame Zero oraz języka Python 3.
Projekt podobny jest pod względem mechaniki do gry Dino znanej z przeglądarki Google Chrome. 
 

Artykuły prezentujące budowę krok po kroku gry ukazały się w magazynie Programista Junior:
* Programista Junior 5/2020 - Gra Dino w Pygame Zero. Część 1
* Programista Junior 6/2020 - Gra Dino w Pygame Zero. Część 2
* Programista Junior 1/2021 - Gra Dino w Pygame Zero. Część 3
* Programista Junior 2/2021 - Gra Dino w Pygame Zero: finał

![Animacja](https://github.com/profesorek96/Gra_Dino/blob/master/screenshot/animacja.gif)

## Uruchomienie
### Uruchomienie Linux/macOS
Do wybranej przez siebie lokalizacji pobierz repozytorium, w tym celu w terminalu wprowadź poniższą komendę.
```sh
git clone https://github.com/profesorek96/Gra_Dino.git
```
Następnie przejdź do pobranego katalogu.
```sh
cd Gra_Dino
```
Kolejny krok to stworzenie wirtualne środowisko, w tym celu w terminalu wprowadź następujące polecenie.
```sh
python3 -m venv venv
```
Jeśli wszystko przebiegło pomyślnie, czas zarejestrować nasz terminal. W terminalu wprowadź poniższe polecenie.
```sh
source venv/bin/activate
```
Jeśli wszystko przebiegło pomyślnie, widzimy napis `(venv)` na początku znaku zachęty naszego terminala. 
Możemy teraz za pomocą menadżera pakietów PIP zainstalować bibliotekę Pygame Zero
W tym celu w terminalu wprowadzamy poniższe polecenie.
```sh
pip install pgzero
```
Jeśli instalacja się powiodła, poniższe polecenie spowoduje uruchomienie gry.
```sh
python main.py
```

### Uruchomienie Windows
Do wybranej przez siebie lokalizacji pobierz repozytorium, w tym celu w terminalu (CMD) wprowadź poniższą komendę.
```sh
git clone https://github.com/profesorek96/Gra_Dino.git
```
Następnie przejdź do pobranego katalogu.
```sh
cd Gra_Dino
```
Kolejny krok to stworzenie wirtualne środowisko, w tym celu w terminalu wprowadź następujące polecenie.
```sh
python -m venv venv
```
Jeśli wszystko przebiegło pomyślnie, czas zarejestrować nasz terminal. W terminalu wprowadź poniższe polecenie.
```sh
venv\Scripts\activate.bat
```
Jeśli wszystko przebiegło pomyślnie, widzimy napis `(venv)` na początku znaku zachęty naszego terminala. 
Możemy teraz za pomocą menadżera pakietów PIP zainstalować bibliotekę Pygame Zero
W tym celu w terminalu wprowadzamy poniższe polecenie.
```sh
pip install pgzero
```
Jeśli instalacja się powiodła, poniższe polecenie spowoduje uruchomienie gry.
```sh
python main.py
```

## Gameplay
Film prezentujący gameplay dostępny jest pod tym [linkiem](https://www.youtube.com/watch?v=PsPaJSwrnbc)

## Technologie
* __Python 3__
* __Pygame Zero__

## Assety
Projekt korzysta z następujących paczek assetów:
* https://kenney.nl/assets/platformer-art-deluxe
* https://kenney.nl/assets/music-jingles

## Status
Niniejszy projekt został: __ukończony__

## Licencja
Apache 2.0
Więcej informacji znajdziesz w pliku: `LICENSE.md`.
