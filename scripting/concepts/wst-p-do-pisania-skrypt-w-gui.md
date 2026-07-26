---
doc_id: "mta-wiki:12602"
title: "Wstęp do pisania skryptów GUI"
source_title: "Wstęp do pisania skryptów GUI"
source_url: "https://wiki.multitheftauto.com/wiki/Wst%C4%99p_do_pisania_skrypt%C3%B3w_GUI"
revision_id: 73424
language: "en"
categories: []
generated_at: "2026-07-26T16:17:07.500950+00:00"
---

# Wstęp do pisania skryptów GUI

Jedną z ważnych funkcji MTA:SA jest możliwość stworzenia elementów GUI (graficznego interfejsu użytkownika). GUI składa się z okien, przycisków, pól edycji, pól wyboru i wiele innych. Mogą być wyświetlane, gdy użytkownik jest w grze, i używane jako punkty wejścia i wyjścia zamiast tradycyjnych poleceń.

 

Graficzny interfejs administracyjny

## Tworzenie okna logowania

W tym samouczku utworzymy proste okno logowania z dwoma polami wprowadzania danych i przyciskiem. Okno pojawia się, gdy gracz dołącza do gry, a po kliknięciu przycisku gracz zostaje zrespawnowany (odrodzony). Ten tutorial będzie kontynuacją trybu gry, który stworzyliśmy w [Wstępie do pisania skryptów](mta://tutorials/wst-p-do-pisania-skrypt-w.md) *(Jeśli korzystałeś/aś z naszego [Wstępu do pisania skryptów](mta://tutorials/wst-p-do-pisania-skrypt-w.md), będziesz musiał usunąć lub skomentować wiersz [spawnPlayer](https://wiki.multitheftauto.com/wiki/PL/spawnPlayer) w funkcji "joinHandler" w swoim kodzie, ponieważ zastąpimy go alternatywnym rozwiązaniem poprzez interfejs graficzny)*. Weźmiemy także pod uwagę skrypty po stronie klienta.

### Rysowanie

Cały interfejs musi być utworzony po stronie klienta. Dobrą praktyką jest również przechowywanie wszystkich skryptów klienta w oddzielnym folderze.

Przejdź do katalogu /TwójSerwerMTA/mods/deathmatch/resources/MójZasób/, i stwórz folder o nazwie "klient". W folderze /klient/, stwórz plik tekstowy i nazwij go: **gui.lua**.

W tym pliku napiszemy funkcję rysującą okno. Aby utworzyć okno, użyjemy funkcji [guiCreateWindow](mta://scripting/client/functions/guicreatewindow.md):

```
function stworzPanelLogowania()
	-- zdefiniuj pozycje X i Y naszego okna
	local X = 0.375
	local Y = 0.375
	-- zdefiniuj szerokość i wysokość naszego okna
	local szerokosc = 0.25
	local wysokosc = 0.25
	-- utwórz okno i zapisz jego wartość w zmiennej o nazwie 'oknoLogin'
	-- możesz kliknąć nazwę funkcji, aby przeczytać jej dokumentację
	oknoLogin = guiCreateWindow(X, Y, szerokosc, wysokosc, "Zaloguj sie", true)
end
```

### Wartości względne i absolutne

Zauważ, że ostatni argument przekazany do funkcji [guiCreateWindow](mta://scripting/client/functions/guicreatewindow.md) w powyższym przykładzie to *true* (prawda). Oznacza to, że współrzędne i wymiary okna są **względne**, co oznacza, że stanowią *procent* całkowitego rozmiaru ekranu. Oznacza to, że jeśli najdalsza pozycja lewej strony ekranu to 0, a skrajna prawa pozycja prawej strony - 1 to pozycja X o wartości 0,5 oznaczałaby środek ekranu. Podobnie, jeśli górna część ekranu to 0, a dolna to 1, pozycja Y o wartości 0,2 odpowiadałaby 20% długości ekranu. Te same zasady dotyczą zarówno szerokości, jak i wysokości (przy wartości szerokości wynoszącej 0,5, co oznacza, że okno będzie o połowę mniejsze niż szerokość ekranu).

Alternatywą dla używania wartości względnych jest użycie wartości **bezwzględnej** (przekazanie wartości *false* (fałsz) zamiast *true* do guiCreateWindow). Wartości bezwzględne są obliczane jako całkowita liczba pikseli z lewego górnego rogu elementu nadrzędnego (jeśli nie określono elementu nadrzędnego elementu GUI, nadrzędnym jest sam ekran). Jeśli przyjmiemy rozdzielczość ekranu 1920x1200, najdalsza lewa strona ekranu to 0 pikseli, a skrajna prawa to 1920 pikseli, pozycja X równa 960 będzie reprezentować środek ekranu. Podobnie, jeśli górna część ekranu ma 0 pikseli, a dolna 1200, pozycja Y o wartości 20 będzie równa 20 pikseli w dół od góry ekranu. Te same zasady dotyczą zarówno szerokości, jak i wysokości (przy wartości szerokość równej 50, co oznacza, że okno będzie miało szerokość 50 pikseli). *Możesz użyć [guiGetScreenSize](mta://scripting/client/functions/guigetscreensize.md) i trochę matematyki, aby obliczyć pewne pozycje bezwzględne.*

Różnice między stosowaniem wartości względnych i bezwzględnych są dość proste; Graficzny interfejs użytkownika utworzony przy użyciu wartości bezwzględnych zawsze będzie posiadał dokładnie taki sam rozmiar i położenie pikseli, podczas gdy interfejs GUI utworzony przy użyciu wartości względnych będzie zawsze stanowić procent rozmiaru ekranu.

Wartości bezwzględne są ogólnie łatwiejsze do utrzymania podczas ręcznej edycji kodu, jednak wybór typu zależy od sytuacji, w której go używasz.

Na potrzeby tego wprowadzenia będziemy używać wartości względnych.
