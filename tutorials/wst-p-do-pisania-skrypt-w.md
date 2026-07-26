---
doc_id: "mta-wiki:5756"
title: "Wstęp do pisania skryptów"
source_title: "Wstęp do pisania skryptów"
source_url: "https://wiki.multitheftauto.com/wiki/Wst%C4%99p_do_pisania_skrypt%C3%B3w"
revision_id: 74689
language: "en"
categories: ["Tutorials"]
generated_at: "2026-07-26T16:17:07.492607+00:00"
---

# Wstęp do pisania skryptów

Zasoby są kluczową częścią MTA. Najprościej rzecz ujmując, zasób to folder lub plik .zip, który zawiera zbiór plików, oraz dodatkowo plik meta, który opisuje serwerowi jak zasób powinien być ładowany i jakie pliki zawiera. Zasób w MTA, w przełożeniu na bardziej znane środowisko systemu operacyjnego, odpowiada programowi lub usłudze działającego pod jego kontrolą - mogą być uruchamiane i zatrzymywane, przy czym wiele z nich może działać jednocześnie (multitasking).

Wszystko, co dzieje się wokół skryptów, dzieje się w zasobach, które to definiują, czy jest to gamemode, mapa, czy też cokolwiek innego. MTA jest dostępne do pobrania z wieloma zasobami, których to można opcjonalnie użyć w swoich gamemodach, np. takimi jak maplimits (zatrzymuje graczy w określonych granicach na mapie), weaponpickups (tworzy pickupy z brońmi), czy też admin panel (panel administratora).

| [[{{{image}}}\|link=\|]] | Wskazówka: Pierwszym krokiem na drodze pisania skryptów w Lua powinno być używanie odpowiedniego edytora skryptów. Ułatwi to znacznie pisanie skryptów. Polecamy Visual Studio Code . |
| --- | --- |
|  |  |

## Tworzymy działający skrypt

Najpierw nauczymy się, krok po kroku, jak stworzyć podstawowy, prosty skrypt, który pozwoli graczowi chodzić po mieście Los Santos.

### Ale gdzie zacząć?

Spójrzmy na strukturę skryptów. Wejdź do swojego folderu serwera MTA (MTA Server), a następnie w poniższą ścieżkę:

```
/MTA Server/mods/deathmatch/resources/
```

Powinieneś zobaczyć dużo plików .zip, które są przykładowymi skryptami, dostarczanymi wraz z MTA. Każdy plik jest "zasobem", oraz mogą być rozpakowane i załadowane przez serwer, kiedy jest uruchamiany. Aby stworzyć swój własny zasób, po prostu utwórz folder z preferowaną nazwą. Do celów tego samouczka, użyjemy nazwy "myserver".

Powinieneś być teraz w tym katalogu:

```
/MTA Server/mods/deathmatch/resources/myserver/
```

### Identyfikujemy swój zasób

Aby serwer wiedział, co znajduje się w zasobie, plik *meta.xml* musi zostać stworzony, aby wylistować wszystkie pliki zasobu serwerowi. Musi on znajdować się w głównym katalogu naszego zasobu (w tym przypadku, "myserver"). Tak więc, stwórz plik tekstowy i nazwij go "meta.xml", oraz otwórz go do edycji.

Wpisz do pliku *meta.xml* ponizszy kod:

```
<meta>
     <info author="TwojNick" version="0.1" type="gamemode" name="My Server" description="Moj pierwszy serwer MTA" />
     <script src="script.lua" type="server" />
</meta>
```

W znaczniku *<info />* znajduje się pole "type", które wskazuje na typ zasobu (może być to: gamemode, zwykły include lub mapa, która zostanie objaśniona w dalszej części). Gamemode to właśnie to, czego potrzebujesz, aby utworzyć działający serwer. Znacznik ten jest jedynie dla informacji i nie jest potrzebny by jakikolwiek skrypt działał, aczkolwiek ułatwi to potem identyfikowanie zasobów.

Znacznik *<script />* wskazuje na pliki skryptów (.lua), które znajdują się w zasobie, większość z nich utworzysz samodzielnie później.

### Piszemy prosty skrypt

Zauważ, że w znaczniku *<script />* plik skryptu .lua umieściliśmy w bieżącym katalogu (gdybyśmy chcieli inaczej, zawsze jest taka możliwości, działa to dokładnie tak, jak w HTML'u). Teraz utwórzmy ten plik.
Możesz teraz skopiować i wkleić poniższy kod do pliku script.lua:

```
local x = 1959.55
local y = -1714.46
local z = 15

function joinHandler()
	spawnPlayer(source, x, y, z)
	fadeCamera(source, true)
	setCameraTarget(source, source)
	outputChatBox('Witaj na moim serwerze!', source)
end
addEventHandler('onPlayerJoin', root, joinHandler)
```

Skrypt ten odrodzi cię w powyższych koordynatach (x, y, z), kiedy tylko dołączysz do gry. Zauważ, że funkcja *fadeCamera* musi zostać tutaj użyta, inaczej ekran byłby cały czas czarny. Musisz również ustawić cel kamery (inaczej gracz zobaczy tylko niebo).

Zmienna **source** wskazuje, kto wywołał event (zdarzenie). Gdy gracz dołączy, kiedy kod jest wykonywany, zmiennej tej używa się, aby zobaczyć, kto dołączył. Dzięki niej, odrodzi docelowego gracza, zamiast każdego, lub losowej osoby.

Jeżeli bliżej przyjrzymy się funkcji [addEventHandler](mta://scripting/shared/functions/addeventhandler.md), możemy zauważyć 3 rzeczy: zdarzenie **onPlayerJoin**, który wskazuje, kiedy event jest wywoływany; zmienna **root**, które pokazuje kto/co może go wywołać (root oznacza "najwyższego rodzica" w hierarchii), oraz **joinHandler**, które wskazuje na funkcję, która ma być wywołana po tym, kiedy event się zaczął. Wszelakie inne detale zostaną wyjaśnione w dalszej części. Teraz można już uruchomić serwer, oraz wytestować skrypt!

### Uruchamianie skryptu

Żeby wystartować serwer pod kontrolą systemu Windows, po prostu uruchom plik wykonywalny w katalogu twojego serwera MTA. Na początku wyświetlą się dane twojego serwera. Zanotuj numer portu, którego będziesz potem potrzebował, przy dołączaniu do gry. Następnie serwer załaduje wszystkie zasoby (załaduje, ale nie uruchomi), które znajdują się w katalogu /resources/, i finalnie, stanie się dostępny dla graczy ("ready to accept connections!").

Zanim podłączysz się do serwera, musisz wpierw uruchomić swój zasób. To logiczne, po to, aby można było mieć na "czymś" grać. Wpisz "start myserver", oraz wciśnij Enter. Serwer uruchomi twój świeżo utworzony gamemode, a także wyświetli tutaj listę wszystkich błędów/ostrzeżeń. Wreszcie, możesz uruchomić klienta MTA, wybrać opcję "Quick Connect" i używając swojego adresu IP, oraz portu (który zdobyliśmy wcześniej) połączyć się. Jeżeli wszystko pójdzie dobrze, za kilka chwil twoja postać będzie wędrowała po ulicach Los Santos.

Następnie, utworzymy prostą komendę do wcześniejszego skryptu, którą gracze będą mogli używać, aby przywoływać sobie pojazdy, blisko ich pozycji. Możesz pominąć tą część, i przejść do bardziej zaawansowanego skryptowania z [Map Managerem](mta://mapping/map-manager.md), który kontynuuje ten samouczek. Inną drogą jest przejście do samouczka [Wstęp do pisania skryptów z GUI](mta://scripting/concepts/introduction-to-scripting-the-gui.md), gdzie wyjaśnione jest, jak interfejs graficzny jest rysowany oraz oskryptowany w MTA.

## Tworzymy prostą komendę

Wróćmy więc do zawartości pliku *script.lua*. Jak zostało wspomniane wyżej, stworzymy komendę, po której wywołaniu obok bieżącej pozycji gracza pojawi się wybrany pojazd. Po pierwsze, musimy utworzyć funkcję, którą będziemy wzywali wywołaniem komendy, oraz tzw. *command handlera*, który tworzy i sprawia, że komenda może być wprowadzona przez gracza w konsoli.

```
-- tworzymy funkcję, którą będzie wzywał command handler, z argumentami thePlayer (gracz), command (komenda), vehicleModel (model pojazdu)
function createVehicleForPlayer(thePlayer, command, vehicleModel)
   -- Tutaj stworzymy i zespawnujemy pojazd
end

-- tworzymy command handler
addCommandHandler('stworzpojazd', createVehicleForPlayer)
```

*Notka: kliknięcie nazwy funkcji powoduje przejście do strony z informacjami na jej temat.*

### O command handlerach

Pierwszym argumentem funkcji [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md) jest nazwa komendy, którą gracz może wprowadzić, drugim argumentem jest nazwa funkcji, którą chcielibyśmy wywołać, w tym przypadku *createVehicleForPlayer*.

Jeżeli masz już doświadczenie w programowaniu, zapewne wiesz, jak wygląda typowa postać funkcji:

```
nazwaFunkcji(argument1, argument2, argument3, ...)

nazwaFunkcji(thePlayer, commandName, argument3, ...)
```

Jeżeli bliżej przypatrzymy się powyższemu przykładowi, zobaczymy, że argumentem1 jest thePlayer, a argumentem2 jest commandName. thePlayer jest po prostu zmienną oznaczającą kto wprowadził komendę, więc jakkolwiek byś jej nie nazwał, będzie zawierała gracza, który aktywował komendę. commandName jest komendą, którą gracz wprowadził. Także, jeżeli gracz wpisałby np. "/alarm", ten argument zawierałby wartość typu string (tekst) "alarm". Argument3 jest czymś dodatkowym, co tylko wpisze gracz za komendą, będzie to później omawiane. Nigdy nie zapomnij, że pierwsze 2 argumenty są obowiązkowe, lecz możesz je nazwać dowolnie.

Dlatego też najpierw stworzyliśmy funkcję, do której [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md) się odwołuje, a potem dopiero dodaliśmy command handler. W innym przypadku komenda nie zostałaby poprawnie przypisana do funkcji. Zalecany jest taki porządek.

Dla przykładu: ktoś wpisze w konsoli "/stworzpojazd 468", aby stworzyć obok siebie Sancheza, command handler wywoła funkcję createVehicleForPlayer, która będzie wyglądała tak, kiedy argumenty zostaną do niej przekazane:

```
-- thePlayer to zmienna typu element (gracz), która wskazuje na tego gracza, który wprowadził komendę
createVehicleForPlayer(thePlayer,'stworzpojazd',468)
```

Jak możemy zobaczyć, dostarczane jest kilka parametrów: gracz, który wywołał komendę, treść komendy, oraz wartość, która została wprowadzona po niej, w tym przypadku "**486**" (ID Sancheza). Pierwsze dwa parametry będą takie same we wszystkich command handlerach, można to doczytać na stronie funkcji [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md). W wyniku tego, zawsze będziesz musiał definiować przynajmniej dwa pierwsze argumenty, aby potem dodać ich dowolną ilość (dla przykładu, jakieś wartości, które funkcja ma przetwarzać)

#### Piszemy funkcję

Aby prawidłowo "zapełnić" naszą funkcję, powinniśmy pomyśleć o rzeczach, które ma zrobić:

- Pobrać pozycję gracza, skąd będziemy wiedzieli, gdzie respawnować pojazd (chcemy, aby pojawił się po lewej stronie)

- Obliczyć dokładną pozycję spawnu auta (nie chcemy, aby spadło na gracza)

- Zespawnować podany pojazd

- Sprawdzić, czy się udało, w innym wypadku wypisać komunikat

Aby dokonać tego celu, będziemy potrzebować kilku funkcji. Aby znaleźć funkcje, których będziemy potrzebować, powinniśmy odwiedzić [Listę funkcji serwerowych](mta://scripting/concepts/scripting-functions.md). Po pierwsze, potrzebujemy funkcji, która pobierze i zwróci pozycję gracza. Odkąd gracze są Elementami, przejdziemy najpierw do **Element functions**, gdzie znajdziemy funkcję [getElementPosition](mta://scripting/shared/functions/getelementposition.md). Klikając nazwę funkcji na liście, pokaże się jej opis. Możemy tam zobaczyć jej składnię, co zwraca, oraz przykłady użycia. Składnia pokazuje nam, jakich argumentów trzeba użyć:

Dla [getElementPosition](mta://scripting/shared/functions/getelementposition.md), składnia wygląda tak:

```
float, float, float getElementPosition ( element theElement )
```

Trzy zmienne typu *float* na początku oznaczają wartości, które funkcja zwraca. W tym wypadku są to 3 wartości typu zmiennoprzecinkowego (floating point) (x, y i z). W nawiasach możesz dostrzec argumenty, które musisz dostarczyć funkcji, aby została prawidłowo wykonana. W tym przypadku będzie to jedynie element (gracz), którego pozycję chcesz znać.

```
function createVehicleForPlayer(thePlayer, command, vehicleModel)
	-- pobierz pozycję i zapisz ją w zmiennych x,y,z
	-- (local znaczy, że zmienna będzie istniała tylko w obrębie tej funkcji, przeciwieństwo globalnej zmiennej)
	local x,y,z = getElementPosition(thePlayer)
end
```

Następnie chcemy mieć pewność, że pojazd nie zespawnuje się przygniatając gracza, toteż dodamy kilka jednostek do zmiennej x, aby go przesunąć na wschód:

```
function createVehicleForPlayer(thePlayer, command, vehicleModel)
	local x,y,z = getElementPosition(thePlayer) -- pobierz pozycję gracza
	x = x + 5 -- dodaj 5 jednostek do pozycji
end
```

Teraz potrzebujemy następnej, innej funkcji, która będzie spawnować podane auto. Raz jeszcze poszukamy jej w [Server Functions List](mta://scripting/concepts/scripting-functions.md), tym razem powinna być w kategorii **Vehicle functions**, gdzie wybierzemy właściwą: [createVehicle](mta://scripting/shared/functions/createvehicle.md). W składnie tej funkcji mamy tylko jedną rzecz, którą zwraca (jest to często spotykane), element typu vehicle, który wskazuje na spawnowany pojazd. Także, możemy zauważyć argumenty objęte nawiasem kwadratowym, które są opcjonalne.

Mamy już wszystkie argumenty, których potrzebujemy dla [createVehicle](mta://scripting/shared/functions/createvehicle.md) w naszej funkcji: Pozycję, którą obliczyliśmy w zmiennych *x,y,z*, oraz model pojazdu, który dostarczymy przez komendę ("stworzpojazd 486"), oraz możliwość dostępu do funkcji przez zmienną *vehicleModel* (model pojazdu)

```
function createVehicleForPlayer(thePlayer, command, vehicleModel)
	local x,y,z = getElementPosition(thePlayer) -- pobierz pozycję gracza
	x = x + 5 -- dodaj 5 jednostek do pozycji
	-- Stwórz pojazd i przechowaj element typu vehicle w zmiennej ''createdVehicle''
	local createdVehicle = createVehicle(tonumber(vehicleModel),x,y,z)
end
```
