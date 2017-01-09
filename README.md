# Dokumentacja wtyczki Claws-Mail „Steganosaurus”
### 1. Wymagania:
======
Steganosaurus jest wtyczką do Linuxowej wersji programu Claws Mail. Zanim będzie możliwe użycie programu, należy spełnić poniższe wymagania:
  1. Należy posiadać zainstalowany system Linux (Ubuntu, Arch, Debian, Solaris, itp.), gdyż wersja Claws Mail na systemy Microsoft Windows nie gwarantuje potrzebnej funkcjonalności.
  2. Zainstalować następujące paczki używając polecenia „sudo apt-get install”:
    1. python
    2. python-gtk2
    3. python-gobject-2
    4. python-imaging
    5. claws-mail
    6. claws-mail-python-plugin
  3. Skonfigurować program Claws Mail by prawidłowo połączył się z kontem pocztowym (Pamiętać należy również, że niektóre konta pocztowe wymagają dodatkowej konfiguracji, np. Gmail)
  4.	Użyć następujących poleceń w Terminalu:
      rm -rf ~/.claws-mail/python-scripts
      git clone https://github.com/BartekUR/Steganosaurus.git
      ln -s ~/Steganosaurus/python-scripts ~/.claws-mail

(Należy zwrócić uwagę na to, że wszystkie skrypty wcześniej dodane zostaną usunięte. Polecane utworzenie backupu)
  
### 2. Działanie wtyczki:
======
Wtyczka Steganosaurus służy do ukrywania wiadomości tekstowych w wychodzących wiadomościach e-mail poprzez wstawienie treści wiadomości ukrytej do nagłówka wiadomości e-mail, który nie jest wyświetlany w domyślnych programach pocztowych. Program jest również w zdolny do odczytania ukrytej treści z wiadomości przychodzącej.

Drugą funkcjonalnością wtyczki jest kodowanie wiadomości i zapisanie jej w pliku .png. (W wersji demonstracyjnej użyty zostaje obrazek z kotem). Dołączony jest również skrypt pythona do odczytywania wiadomości z dowolnego obrazka. Zaletą zapisywania wiadomości w obrazku jest możliwość zapisania długich wiadomości bez większego wpływu na rozmiar załącznika.


### 3. Użytkowanie:
======
Aby ukryć wiadomość w wiadomości wychodzącej należy najpierw napisać treść wiadomości jawnej oraz treść wiadomości ukrytej (Kolejność nie jest istotna). Następnie, zaznaczyć tekst który ma zostać ukryty, otworzyć menu Tools w głównym oknie Claws Mail i wybrać opcję „EncodeToHeader” z podmenu „Python scripts”.

![przed](https://s28.postimg.org/4222srzpp/image.jpg)
![po](https://s24.postimg.org/sc55rrfr9/image.jpg)

Aby wyświetlić wiadomość ukrytą, należy zaznaczyć wiadomość w skrzynce odbiorczej, a następnie otworzyć menu „Tools” i wybrać opcję „DecodeFromHeader” z podmenu „Python scripts”.

![przed](https://s30.postimg.org/wwfkz21pd/image.jpg)

Jeżeli wiadomość nie zawierała ukrytych treści, pokaże się komunikat błędu. Jeżeli wiadomość zawierała ukrytą treść, zostanie wyświetlone okienko z tąż treścią.

![po](https://s30.postimg.org/6ids3bkfl/image.jpg)

Aby zapisać ukrytą wiadomość w załączniku, należy postępować tak samo jak przy ukrywaniu wiadomości w nagłówku, z tą różnicą, że należy wybrać „EncodeToAttach”

![przed](https://s29.postimg.org/4mrdot2gn/Kodowanie_kocie.png)

Natomiast, żeby zobaczyć wiadomość ukrytą w obrazku musimy najpierw zapisać obrazek (najprościej do katalogu domowego) a następnie wejść przez terminal do ~/.claws-mail/python-scripts/tools, zmienić uprawnienia do pliku imgdec.py (Tylko za pierwszym razem) przy pomocy komendy chmod +x imgdec.py i uruchomić skrypt komendą ./imgdec.py <ścieżka do obrazka>. Wiadomość ukryta zostanie wypisana na konsolę

![po](https://s29.postimg.org/5z4hcyaif/dekotowanie.png)
