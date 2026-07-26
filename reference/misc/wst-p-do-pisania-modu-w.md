---
doc_id: "mta-wiki:13701"
title: "Wstęp do pisania modułów"
source_title: "Wstęp do pisania modułów"
source_url: "https://wiki.multitheftauto.com/wiki/Wst%C4%99p_do_pisania_modu%C5%82%C3%B3w"
revision_id: 74848
language: "en"
categories: []
generated_at: "2026-07-26T16:17:07.437945+00:00"
---

# Wstęp do pisania modułów

Moduły są rozszerzeniami rdzenia MTA Lua, które umożliwiają integrację i używanie niestandardowych funkcji Lua, które zostały napisane w C++ i skompilowane jako plik DLL lub SO. Moduły są powszechnie używane do tworzenia funkcji do takich celów, których brakuje w Multi Theft Auto, takich jak [gniazda](mta://reference/misc/modu-y-gniazda.md).

## Wprowadzenie

Żeby zacząć pisać nowe moduły trzeba mieć przynajmniej podstawową wiedzę z programowania w językach C/C++.  

Poradnik ten **nie uczy** o tym, jak zacząć przygodę z C++.  

Zacznijmy od pobrania szablonu przeznaczonego do stworzenia naszego własnego modułu.
Możemy zrobić to na 2 sposoby:

### Poprzez terminal

Upewnij się, że masz zainstalowany pakiet kontroli źródła [GIT](https://git-scm.com/downloads).
Otwórz wiersz poleceń (Win+R -> CMD) i wpisz tą komendę:

```
git clone https://github.com/TracerDS/mtasa-modules.git
```

### Poprzez stronę WWW

Wchodzimy na stronę [przykładowego modułu](https://github.com/TracerDS/mtasa-modules) i pobieramy go (Zielony przycisk "Code" -> "Download ZIP")
Rozpakuj archiwum

## Jak zacząć?

Wejdź do folderu

```
./mtasa-modules/ml_example
```

### Windows

Otwórz wiersz polecenia w tym folderze i uruchom skrypt `.\newModule.bat NazwaTwojegoModułu` np. `.\newModule.bat MojModul`

### Linux

Otwórz terminal w tym katalogu i uruchom skrypt `./newModule.sh NazwaTwojegoModułu` np. `./newModule.sh MojModul`

Po uruchomieniu skryptu powinien utworzyć się nowy folder o nazwie "**NazwaTwojegoModułu_module**".
W tym folderze został również utworzony automatycznie projekt Visual Studio **ORAZ plik README, który NALEŻY KONIECZNIE przeczytać.**

## Co się znajduje w tym szablonie?

### Struktura szablonowego modułu

- **include**
- **init**
- Common.h

- ILuaModuleManager.h

- lauxlib.h

- luaconf.h

- lua.h

- lua.hpp

- lualib.h

- CFunctions.h

- CLuaArgument.h

- CLuaArguments.h

- ml_nazwamodulu.hpp

- **lib**
- lua5.1.lib

- lua5.1_64.lib
- **src**
- CFunctions.cpp

- CLuaArgument.cpp

- CLuaArguments.cpp

- ml_example.cpp

- ml_nazwamodulu.sln

- ml_nazwamodulu.vcxproj

- ml_nazwamodulu.vcxproj.filters

- ml_nazwamodulu.vcxproj.user

- README

Zieloną czcionką oznaczono pliki  

**Pogrubioną niebieską czcionką** oznaczono katalogi  

Czerwonym tłem oznaczono pliki lub **foldery**, które **nie powinny** być modyfikowane.

## Do czego służy ___?

**P:** Folder **init**?  

**O:** Tego folderu nie ruszamy. Tam są przechowywane nagłówki potrzebne do wstępnego zainicjowania modułu.

**P:** Plik **CFunctions.h**?  

**O:** Tam są przechowywane deklaracje funkcji stworzonych przez użytkownika.
W pliku **CFunctions.cpp** przechowywane są definicje tychże funkcji.

**P:** Folder **lib**?  

**O:** Tego folderu **absolutnie** nie tykamy. W nim są przechowywane biblioteki potrzebne do połączenia między C++ a Lua.

**P:** Pliki **CLuaArgument/s.h/.cpp**?  

**O:** Te pliki służą do poprawnej obsługi parametrów z C++ do Lua

[Część 2](mta://reference/misc/wst-p-do-pisania-modu-w-2.md)
