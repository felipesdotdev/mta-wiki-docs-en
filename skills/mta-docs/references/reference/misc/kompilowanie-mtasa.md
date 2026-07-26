---
doc_id: "mta-wiki:11260"
title: "Kompilowanie MTASA"
source_title: "Kompilowanie MTASA"
source_url: "https://wiki.multitheftauto.com/wiki/Kompilowanie_MTASA"
revision_id: 79880
language: "en"
categories: ["PL/Development", "Translated/Development"]
---

# Kompilowanie MTASA

Aby pomyślnie skompilować Multi Theft Auto z kodu źródłowego, niezbędne jest wykonanie kilku kroków, które przedstawimy poniżej.

Przeczytaj uważnie poniższe instrukcje i nie pomijaj żadnej z nich, jeśli nie masz doświadczenia.

## Podstawowe Wymagania

Kompilacja klienta Multi Theft Auto jest oficjalnie wspierana tylko na systemie Windows 10.

Upewnij się czy masz zainstalowane następujące programy i zestawy SDK:

### Visual Studio 2022

- **[Microsoft Visual Studio 2022](https://visualstudio.microsoft.com/vs/)** (Edycja Community jest darmowa).

- Na liście podczas instalacji, [zaznacz te dwa pola](https://wiki.multitheftauto.com/wiki/File:VSFoundationClasses_PL.png)

- *Programowanie aplikacji klasycznych w języku C++*

- Opcjonalny komponent (po prawej stronie na liście) *C++ MFC dla najnowszych narzędzi kompilacji w wersji 143 (x86 & x64)*

Jeśli nie zaznaczysz komponentu MFC to otrzymasz błąd `cannot open include file 'afxres.h'`
Jeśli popełnisz błąd, możesz ponownie uruchomić instalator, aby zmodyfikować aktualna instalację bez konieczności odinstalowywania i instalowania.

### Microsoft DirectX SDK

**Pobierz Microsoft DirectX SDK (August 2009)**

- [Link 1](https://archive.org/download/dxsdk_aug09/DXSDK_Aug09.exe)

- [Link 2](https://mega.nz/file/pQJCiAJY#jBcYT6ZP4DMBpnm12BLRto9EQ-RjjpP3BWkSPanpvLI)

| Algorytm i wariant | Hash |  |
| --- | --- | --- |
| SHA-3 | SHA3-224 | 8bfcdc03518d7edd34689534fd4d21291469ff2f2eb10437ad648c58 |
| SHA3-256 | 45bf3e08da3b3636ddb4f4a74243430f8d65759c074c0d79756ef810c4701c5a |  |
| SHA3-384 | b358e529963d6f5fd7f8bd4b530fb18f6a2e6a442009a54e981b2f9967589ed48150af310f283640d56f9b60d41100c9 |  |
| SHA3-512 | 43522187053af744250059ef69c0f3083cecd1157fe56daac16b9497ebc6fb5b525875144e42898367c55f757cffd3526f37074d544470578602a5a944a45a75 |  |
| SHAKE128 | 2a7c81bde9e867cbb5ef00b72ad8de66a3ee64c1d59f16465fa712479b6a84d28a02cc5ed08afa1d51e72011657453dbd4656cc9340d32e18179c39d03982dfc35c8f0c2a5c99e11dc74d0e23ed21b1e55f19c809a5a152bde39a2d46fcd12421f373f2d691ade1b57faf6c2ab7aded5a7d174f1f1c77127c0d6a1523b4775c569c5e1b4efa2da4bf2f708a96707a709e245a7f507382e69a81777919c90e95a091c0b699ce7f517 |  |
| SHAKE256 | 9c100dac5245a61774f3a2752bf9e941bdcd5654b18035155161c63b20936dfc9bd7334feb9a6fe9a99a65491161083b39ac3bd578e2cf4f90cba3c786e9924fa0611f65a725331b77b63e7c8b552e1637bc77531ba0f2c9cac72115b28e523929ede4e5b246a0755e8d5c4089d94bf16627fb08672cfffa523bba3d976489a0eec60d3c6a96ca2b |  |
| SHA-2 | SHA-224 | a3a74b89cccfe314b79418d5598aac5e94800221e5d945c74f15c004 |
| SHA-256 | 4ab1de69312f10f6b41310a5218d80c478bbd823bc0f86627318d690b128fb9f |  |
| SHA-384 | 254ed29c6ad2cadc6f013d2d51c0ac78a6bbe236a2c94ca99610eba8b2c1200d1a62c445ca9ee51bb09354875d5eca8a |  |
| SHA-512 | 736393c0dfa32221e229890f87eb330174d70dd2a02fa0cace303816d3e7a10a332a44129748de39665d1b339e627d6028c2080268f7afdd5240c447fec8ff0b |  |
| SHA-512/224 | 7e23d9ba916000782a17e23abf48e25237f45590cfe767aed9d79f10 |  |
| SHA-512/256 | 0c833a56046fe7e4213fcb1862c730acf313d1b8f60b51eebf64dc3e79730c1c |  |
| MD5 | 66e5379ecf46b014688779621bcc677c |  |
| SHA-1 | 5b9b969ed7b6cf5534bb7350e44c09b3573b0e71 |  |
| CRC32 | e9f5c61d |  |

**UWAGA:** Po zainstalowaniu *Microsoft DirectX SDK* należy uruchomić ponownie komputer, ponieważ zmienna środowiskowa **DXSDK_DIR** nie będzie jeszcze dostępna. Po ponownym uruchomieniu otwórz ponownie plik **create-projects.bat**

**Nie można odnaleźć d3dx9.h**

Dodaj **$(DXSDK_DIR)Include;** do katalogów VC++ w projektach DirectX9GuiRenderer, GUI i Client Core. 
Listę katalogów VC++ znajdziesz wybierając projekt, a następnie używając skrótu klawiszowego ALT + ENTER (bez +). Wybierz właściwości konfiguracji i znajdziesz tam katalogi VC++, kliknij tam "Dołącz katalogi" i dodaj **;$(DXSDK_DIR)Include;** na końcu.
**Uwaga: Musisz zrobić to samo także dla kompilacji w trybie RELEASE**

**Nie można odnaleźć d3dx9.lib**

Wykonaj takie same czynności jak opisano powyżej w przypadku błędu z plikiem **d3dx9.h**. Jednak zamiast **;$(DXSDK_DIR)Include;** musisz dodać **;$(DXSDK_DIR)Lib/x86;** w katalogach bibliotek.
**Uwaga: Musisz zrobić to samo także dla kompilacji w trybie RELEASE**

**Błąd S1023**

["S1023" błąd podczas instalacji DirectX SDK (June 2010)](https://support.microsoft.com/en-us/kb/2728613)

**Nie można otworzyć pliku źródłowego "xxx.h" po aktualizacji do Visual Studio 2022**

Jeśli zaktualizowałeś Visual Studio do wersji 2022 i pracowałeś z MTA na wcześniejszej wersji to podczas kompilacji projektu możesz otrzymać błędy związane z plikami nagłówków. Głównie są to błędy, że nie udało się znaleźć lub otworzyć jakiegoś pliku np. stdio.h, stddef.h itd.

Upewnij się, że masz zainstalowaną najnowszą wersję zestawu Windows 10 SDK (w instalatorze Visual Studio na liście komponentów) i uruchom ponownie komputer.
Jeśli masz zainstalowany najnowszy zestaw i po ponownym uruchomieniu problem wciąż występuje to zamknij Visual Studio, przejdź do folderu "Build" (tam gdzie znajduje się folder mtasa-blue) i usuń folder o nazwie ".vs".

### Klient Git

Jeśli chcesz współpracować przy MTA, powinieneś zainstalować GIT. Pozwoli Ci to współpracować z nami poprzez tworzenie nowych gałęzi i przesyłanie zmian do nich we własnym repozytorium (fork). 
Jeśli korzystanie z konsoli jest dla Ciebie niekomfortowe, zalecamy korzystanie z [Github Desktop](https://desktop.github.com/)

Jeśli chcesz tylko skompilować kod źródłowy i nie zamierzasz współpracować razem z nami, możesz pobrać kod źródłowy bezpośrednio z linku poniżej, bez konieczności instalowania GIT.

## Zdobycie najświeższego kodu źródłowego

Aby zdobyć najświeższy kod źródłowy, będziesz musiał pobrać ostatnią kopie naszego repozytorium Git.  

Zalecamy sklonować nasze repozytorium w twoim kliencie Git, ponieważ możesz łatwo pobierać z niego dowolne aktualizacje.

- **Repozytorium:** [multitheftauto/mtasa-blue](https://github.com/multitheftauto/mtasa-blue)

- **.zip:** [master.zip](https://github.com/multitheftauto/mtasa-blue/archive/master.zip)

- **.tar.gz:** [master.tar.gz](https://github.com/multitheftauto/mtasa-blue/archive/master.tar.gz)

## Kompilacja kodu

- Uruchom skrypt (otwórz plik) **win-create-projects.bat**

- Otwórz plik rozwiązania **MTASA.sln** w folderze **Build**

- Jeśli zostaniesz zapytany o aktualizacje projektu, kliknij **Anuluj**

- W Visual Studio wybierz konfigurację **DEBUG**, a następnie wybierz **"Kompiluj"** -> **"Kompiluj rozwiązanie"** (Może to potrwać kilka minut)

- Uruchom skrypt (otwórz plik) **win-install-data.bat**

# Uruchamianie programu

## Uruchamianie klienta MTA

Możesz uruchomić swojego klienta w folderze **Bin**. Możesz znaleźć tutaj pliki *Mutli Theft Auto.exe* i/lub *Multi Theft Auto_d.exe*. Przyrostek *_d* oznacza kompilacje developerską (konfiguracja debug) programu.
Ponadto, możesz także uruchomić swojego klienta w debuggerze z Visual Studio jeśli chcesz przeanalizować układ stosu lub ustawić punkty przerwania w interesujących regionach kodu (przeczytaj więcej poniżej w sekcji Debugowanie).

## Uruchamianie dedykowanego serwera

Jeśli już wykonałeś krok 5 (*Instalacja zasobów*) w sekcji *Kompilacja kodu* aby zainstalować zasoby, możesz przejść do sekcji *Uruchamianie serwera lokalnego*.

### Instalacja najświeższych zasobów

Jeśli chcesz uruchomić dedykowany serwer Multi Theft Auto, musisz zainstalować wymagane zasoby. Są one niezbędne, ponieważ dodają podstawowe funkcje (np. odradzanie graczy) aby móc grać.

Nasze oficjalne repozytorium zasobów: [znajdujące się w serwisie GitHub](https://github.com/multitheftauto/mtasa-resources). Możesz pobrać najświeższe zasoby z tego repozytorium lub [pobierz archiwum .zip](http://mirror.mtasa.com/mtasa/resources/). Upewnij się, że masz najnowszą paczkę zasobów.

### Uruchamianie serwera

Aby uruchomić serwer, otwórz plik *MTA Server.exe* w folderze **Bin/server**. Przyrostek *_d* oznacza kompilację developerską (konfigurację debug) programu.  

Możesz także uruchomić serwer w wersji developerskiej (debug); *MTA Server_d.exe* przy pomocy debuggera Visual Studio (jak przy pisaniu, możesz zrobić to poprzez kliknięcie prawego przycisku myszki na projekcie *Launcher*, po stronie serwera (Rozwiń projekt Server) i wybranie *Uruchom lokalną instancję* w zakładce *Debugger*), ale możesz także dołączyć do działającego debuggera serwera MTA (zobacz więcej niżej, w sekcji *Debuggowanie*).

## Debuggowanie

Jeśli skompilowałeś już kod w konfiguracji **DEBUG** to możesz przejść dalej - Jeśli nie, to wróć wyżej do sekcji **Kompilacja kodu** i wykonaj opisane tam kroki.

Możesz uruchomić MTA i dołączyć dowolny debbuger (dotyczy to także debbugera Visual Studio) lub zacząć lokalną sesję debbugowania w Visual Studio.

### Jak włączyć punkty przerwania

Jeśli zdecydowałeś się uruchomić MTA z Visual Studio, powinieneś również dołączyć debbuger do pliku wykonywalnego **gta_sa.exe** (naciśnij *CTRL + ALT + P* w Visual Studio) - W przeciwnym razie punkty przerwania nie będą działać dla niczego poza Launcherem MTA.

### Przedłużenie limitu czasowego

Jeśli używasz punktów przerwania podczas debbugowania, możesz zostać wyrzucony z serwera z powodu upływu czasu, gdyż klient jest zamrożony. Aby tego uniknąć stwórz plik **timeout.longtime** w katalogu *Bin/server*.
W pliku wprowadź limit czasowy w sekundach, więc pamiętaj, aby wpisać tutaj bardzo duże liczby. Jeśli pozostawisz plik pusty to limit czasowy zostanie ustawiony na domyślny (120 sekund).

### Ponowne dołączenie debbugera w Visual Studio

Możesz skorzystać z narzędzia [ReAttach](https://marketplace.visualstudio.com/items?itemName=ErlandR.ReAttach) do ponowneggo dołączenia debbugera do pliku wykonywalnego **gta_sa.exe** zawsze gdy rozpoczynasz lokalną sesję debbugowania w Visual Studio.

# Chęci współpracy

Prosimy, sprawdź nasze [Wytyczne na temat kodowania](mta://scripting/concepts/coding-guidelines.md) po więcej informacji o praktykach kodowania.

# Dodatkowe informacje

Jeśli potrzebujesz więcej informacji, sprawdź nasz [bug tracker](https://github.com/multitheftauto/mtasa-blue/issues) lub [Discord](https://discord.com/invite/mtasa).

# Błędy

## CL38 error. [nie znaleziono netc_d.dll]

Rozwiązanie: Usuń **Mutli Theft Auto_d.exe** i naciśnij 'Kompiluj ponownie' w Visual Studio.

## Po sklonowaniu repozytorium, nie można skompilować projektu

Rozwiązanie: Otwórz plik **win-create-projects.bat** w głównym katalogu.

## CL17 Load field. Prosimy, upewnij się, że najnowsze pliki danych zostały zainstalowane poprawnie

Rozwiązanie: Otwórz plik **win-install-data.bat** w głównym katalogu.

## ERROR: Ładowanie biblioteki net_d.dll nie powiodło się!

Rozwiązanie: Otwórz plik **win-install-data.bat** w głównym katalogu.
