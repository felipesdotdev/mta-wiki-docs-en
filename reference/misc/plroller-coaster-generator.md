---
doc_id: "mta-wiki:14245"
title: "PL/Roller Coaster Generator"
source_title: "PLRoller Coaster Generator"
source_url: "https://wiki.multitheftauto.com/wiki/PLRoller_Coaster_Generator"
revision_id: 78929
language: "en"
categories: []
generated_at: "2026-07-26T16:16:27.653072+00:00"
---

# PL/Roller Coaster Generator

Logo

Roller Coaster Generator dla Multi Theft Auto: San Andreas

## Historia i koncepcja

### Historia

Pomysł na Roller Coaster Generator jest stary. Chciałem stworzyć mapę w stylu "Going Down", ale było to bardzo czasochłonne. To był czas kiedy pomyślałem o czymś, co będzie mogło wygenerować cały tor Rollercoaster'a. Powstało kilka algorytmów, nawet taki którego używają pętle. Algorytm generatora powstał na przełomie czerwca i lipca w 2007 roku. Konsolowy program tworzy plik .map po podaniu odpowiednich parametrów takich jak pozycje (musiałem szukać koordynatów ręcznie). Taki plik można potem uruchomić i wypróbować w grze. Roller Coaster Generator został wydany w lipcu 2009 roku. Nowe wydanie ukazało się w maju 2010 roku.

### Koncepcja

Roller Coaster Generator pomaga stworzyć i zarządzać seriami obiektów, tworząc zazwyczaj drogę, łuk lub pętlę. Głównym zamysłem jest wykorzystanie punktów kontrolnych (Control Points), jako punkty wyznaczające trasę. Roller Coaster Generator zawiera plik [edytowalnych definicji (EDF)](https://wiki.multitheftauto.com/wiki/PL/Resource:Editor/EDF) dla edytora, a także współpracuje z edytorem podczas jego działania.

## Przygotowanie

### Wymagania

- Multi Theft Auto 1.0.3

- Multi Theft Auto resources r596+ editor (Edytor map)

### Instalacja

- Pobierz Roller Coaster Generator i rozpakuj. (użyj Roller Coaster Generator Googlecode w linkach zewnętrznych na dole strony)

- Przenieś wypakowane foldery do katalogu *...\MTA San Andreas\server\mods\deathmatch\resources*.

### Ustawienie definicji

- Kliknij na ikonę *Definitions*.

- Dodaj definicję *rcg*.

- Naciśnij "Ok".

## Jak używać

### Podstawy

#### Definicja

- Najedź kursorem na te ikony.

- Kręć kółkiem myszy.

#### Punkt kontrolny

 

Ustawianie mocy klawiszami PageUp, PageDown

Punkt kontrolny określa położenie i kierunki toru oraz określa rotację elementów toru. Możesz wybrać 3 części punktu kontrolnego.

- Środek (Center)

Ten rodzaj zaznaczenia zapewnia możliwość poruszania, obracania i zmiany modelu punktu kontrolnego.

- Lewo, Prawo (Left, right)

Ten rodzaj zaznaczenia z kolei zapewnia możliwość zmiany "mocy", jak pokazano na obrazku. (PageUp, PageDown).

#### Trasa/Tor

Trasa łączy dwa punkty kontrolne, tworząc serię/ciąg obiektów.
Element trasy ma 3 główne właściwości:

- objectNumber

Właściwość ta określa jak wiele elementów ma zawierać trasa.

- controlPointLeft

Właściwość ta określa gdzie zaczyna się trasa.

- controlPointRight

Właściwość ta określa gdzie kończy się trasa.

### Zaawansowane

 

Edytowany model i względny obrót w punkcie kontrolnym.

#### Model

Istnieje więcej sposobów na edycję punktów kontrolnych lub zmianę modeli trasy.

- Jeśli ustawisz model punktu kontrolnego to także zmieni się model każdej trasy, która jest połączona z tym punktem kontrolnym.

- Jeśli zmodyfikujesz model trasy to także zmienią się modele wszystkich elementów trasy. Jednak nie zmieni się model punktu kontrolnego.

#### Względne pozycjonowanie i obracanie

Używaj względnych pozycji i rotacji jeśli element nie jest ustawiony we właściwym kierunku lub wymaga dodatkowej edycji.

**Użyj przycisku X, gdy masz zaznaczony punkt kontrolny, a następnie przesuń lub obróć go.**  

**Użyj przycisku V, podczas trzymania klawisza X, aby zresetować pozycję i rotację względną.**

- Pozycja względna

Nie ma wsparcia do wersji r9

- Rotacja względna

Pomaga obrócić element we właściwym kierunku.

## Użyte programy

- Notepad++

- Wolfram Mathematica

- Adobe Photoshop

## Zobacz także

- [PL/Resource:Editor](https://wiki.multitheftauto.com/wiki/PL/Resource:Editor)

- [PL/Resource:Editor/Plugins](https://wiki.multitheftauto.com/wiki/PL/Resource:Editor/Plugins)

## Linki zewnętrzne

- [Roller Coaster Generator Googlecode](https://code.google.com/p/mtasa-resources-rcg/)

- [Roller Coaster Generator Forum](http://forum.multitheftauto.com/viewtopic.php?f=108&t=27577)

- [Bézier curve Bézier Curve](http://en.wikipedia.org/wiki/B%C3%A9zier_curve)

- [Wolfram Research](http://www.wolfram.com/)
