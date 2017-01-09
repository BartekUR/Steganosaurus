# Dokumentacja wtyczki Claws-Mail „Steganosaurus”
### 1. Wymagania:
======
Steganosaurus jest wtyczką do Linuxowej wersji programu Claws Mail. Zanim będzie możliwe użycie programu, należy spełnić poniższe wymagania:
  1. Należy posiadać zainstalowany system Linux (Ubuntu, Arch, Debian, Solaris, itp.), gdyż wersja Claws Mail na systemy Microsoft Windows nie gwarantuje potrzebnej funkcjonalności.
  2. Zainstalować następujące paczki używając polecenia „sudo apt-get install”:
    1. python
    2. python-gtk2
    3. python-gobject-2
    4. claws-mail
    5. claws-mail-python-plugin
  3. Skonfigurować program Claws Mail by prawidłowo połączył się z kontem pocztowym (Pamiętać należy również, że niektóre konta pocztowe wymagają dodatkowej konfiguracji, np. Gmail)
  4. Pobrać Steganosaurusa z adresu <https://github.com/BartekUR/Steganosaurus>
  5. Rozpakować archiwum zip i skopiować zawartość folderu python-plugins do katalogu .claws-mail

### 2. Działanie wtyczki:
======
Wtyczka Steganosaurus służy do ukrywania wiadomości tekstowych w wychodzących wiadomościach e-mail poprzez wstawienie treści wiadomości ukrytej do nagłówka wiadomości e-mail, który nie jest wyświetlany w domyślnych programach pocztowych. Jako dodatkowe zabezpieczenie, treść wiadomości ukrytej zostaje zaszyfrowana. 

Drugą funkcjonalnością wtyczki jest odszyfrowanie i wyświetlenie ukrytej wiadomości z wiadomości przychodzącej.

### 3. Użytkowanie:
======
Aby ukryć wiadomość w wiadomości wychodzącej należy najpierw napisać treść wiadomości jawnej oraz treść wiadomości ukrytej (Kolejność nie jest istotna). Następnie, zaznaczyć tekst który ma zostać ukryty, otworzyć menu Tools w głównym oknie Claws Mail i wybrać opcję „EncodeToHeader” z podmenu „Python scripts”.

![alt text](https://s28.postimg.org/4222srzpp/image.jpg)
![alt text](https://s24.postimg.org/sc55rrfr9/image.jpg)

Aby wyświetlić wiadomość ukrytą, należy zaznaczyć wiadomość w skrzynce odbiorczej, a następnie otworzyć menu „Tools” i wybrać opcję „DecodeFromHeader” z podmenu „Python scripts”.

![alt text](https://s30.postimg.org/wwfkz21pd/image.jpg)

Jeżeli wiadomość nie zawierała ukrytych treści, pokaże się komunikat błędu. Jeżeli wiadomość zawierała ukrytą treść, zostanie wyświetlone okienko z tąż treścią.

![alt text](https://s30.postimg.org/6ids3bkfl/image.jpg)
