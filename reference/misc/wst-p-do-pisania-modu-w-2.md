---
doc_id: "mta-wiki:13723"
title: "Wstęp do pisania modułów 2"
source_title: "Wstęp do pisania modułów 2"
source_url: "https://wiki.multitheftauto.com/wiki/Wst%C4%99p_do_pisania_modu%C5%82%C3%B3w_2"
revision_id: 75167
language: "en"
categories: []
generated_at: "2026-07-26T16:17:07.459933+00:00"
---

# Wstęp do pisania modułów 2

W poprzedniej części wyjaśniliśmy sobie czym są moduły, jak pobrać szablon modułu oraz co on zawiera.  

W tej części omówimy sobie poszczególne części naszego modułu (co dana rzecz robi).
Nasz moduł w tym poradniku będzie się nazywał **PrzykladowyModul**

### ./src/ml_przykladowymodul.cpp

```
#include <include/ml_przykladowymodul.hpp>
#include <include/CFunctions.h>

ILuaModuleManager10* pModuleManager = NULL;
bool ms_bInitWorked = false;

// Initialisation function (module entrypoint)
MTAEXPORT bool InitModule(ILuaModuleManager10* pManager, char* szModuleName, char* szAuthor, float* fVersion) {
	pModuleManager = pManager;

	// Set the module info
	strncpy(szModuleName, MODULE_NAME, MAX_INFO_LENGTH); // set module name
	strncpy(szAuthor, MODULE_AUTHOR, MAX_INFO_LENGTH); // set module author

	*fVersion = MODULE_VERSION; // set module version

	ms_bInitWorked = true;
	return true;
}

MTAEXPORT void RegisterFunctions(lua_State* luaVM) {
	if (!ms_bInitWorked) return;

	if (pModuleManager && luaVM) {
		// Register functions
		pModuleManager->RegisterFunction(luaVM, "someFunction", CFunctions::someFunction);

		// Add events
		CFunctions::AddEvent(luaVM, "onSomeEvent");
	}
}

MTAEXPORT bool DoPulse() {

	return true;
}

MTAEXPORT bool ResourceStopped(lua_State* luaVM) {

	return true;
}

MTAEXPORT bool ShutdownModule() {

	return true;
}
```

Musimy sobie na początek zaimportować potrzebne dla nas nagłówki. W tym przypadku jest to nasz główny nagłówek (**ml_przykladowymodul.hpp**) oraz nagłówek do zarejestrowania naszych własnych funkcji w Lua (**CFunctions.h**). Zwróć uwagę na rozszerzenie pliku: **.hpp**. Pliki które będziemy tworzyć samodzielnie będziemy zapisywać z rozszerzeniem **.hpp**, by nie mieszać ich z predefiniowanymi plikami MTA.

```
ILuaModuleManager10* pModuleManager = NULL;
```

Tutaj predefiniujemy menedżer funkcji Lua, który przychodzi razem z plikami MTA. Tego nie ruszamy, jego wartość zmieni się przy inicjalizacji naszego modułu.

```
bool ms_bInitWorked = false;
```

Tutaj definiujemy zmienną, która posłuży nam jako "przełącznik". W momencie gdy moduł się załaduje, to wartość tej zmiennej się zmieni na **true**, dzięki czemu możliwe będzie załadowanie funkcji oraz zdarzeń (tak, by nie załadowały się przed inicjalizacją modułu).

```
MTAEXPORT bool InitModule(ILuaModuleManager10* pManager, char* szModuleName, char* szAuthor, float* fVersion) {
	// ...
}
```

W tym miejscu zaczyna się cała zabawa. Ta funkcja sprawia że nasz moduł się ładuje na serwer, ustawia jego nazwę, autora i wersję.

```
MTAEXPORT void RegisterFunctions(lua_State* luaVM) {
	// ...
}
```

W tej funkcji rejestrujemy nasze funkcje i zdarzenia, które będzie można użyć w skrypcie Lua. Jedynym parametrem tutaj jest tzw. status wirtualnej maszyny Lua. Zasadniczo serwer dzieli każdy zasób na oddzielne wirtualne maszyny, które podłączone są do jednego statusu globalnego. Parametrem w tej funkcji jest stan zasobu, który uruchomił moduł (wszystkie funkcje, zdarzenia dzieją się osobno na każdym zasobie). Do tego przejdziemy w późniejszej części poradnika.

```
MTAEXPORT bool DoPulse() {
	return true;
}

MTAEXPORT bool ResourceStopped(lua_State* luaVM) {
	return true;
}

MTAEXPORT bool ShutdownModule() {
	return true;
}
```

1 funkcja wysyła informację o tym, że moduł jest aktywny. Podobny wynik możemy zyskać wpisując w wiersz poleceń `ping google.com`  

2 funkcja wywoła się jak zdarzenie. Jeżeli moduł zostanie z jakiegokolwiek powodu zatrzymany, to ta funkcja się wykona razem ze stanem tegoż modułu.  

3 funkcja wywoła się kiedy cały moduł zostanie zatrzymany (poprzez konsolowe komendy **unloadmodule**, **reloadmodule** i **loadmodule**).

### ./include/ml_przykladowymodul.hpp

Tutaj interesują nas właściwie tylko 3 linie:

```
#define MODULE_NAME "Example module" // Module name
#define	MODULE_AUTHOR "Tracer" // Author of the module
#define MODULE_VERSION 1.0f // Module version (1.00)
```

W pierwszej definiujemy nazwę naszego modułu, w drugiej autorów, a w trzeciej wersję naszego modułu

### ./include/CFunctions.h

Tutaj dzieje się nieco więcej.

```
extern ILuaModuleManager10* pModuleManager;

class CFunctions {
public:
    static int someFunction(lua_State* luaVM);

    static void AddEvent(lua_State* luaVM, const std::string& strEventName);
    static void TriggerEvent(lua_State* luaVM, const std::string& strEventName,
        void* baseElem, const std::initializer_list<VarTypes>& arg = {});
};
```

W pierwszej kolejności mamy odniesienie do wcześniej zdefiniowanej zmiennej odpowiedzialnej za zarządzanie modułami.
Dalej mamy klasę, w której definiujemy nasze własne funkcje oraz zdarzenia.  

Zauważ, że każda funkcja jest definiowana statycznie a jako parametr przyjmuje status danego zasobu, który uruchomił nasz moduł.  

`AddEvent` pozwala nam na zarejestrowanie niestandardowego zdarzenia. `TriggerEvent` jak nazwa mówi wywołuje zdarzenie, którego nazwę podamy jako parametr. Warto zaznaczyć, że do wywołania zdarzenia potrzebny jest też element, do którego podłączona jest funkcja obsługi zdarzeń (event handler), oraz argumenty. Są one przedstawione jako lista `VarType`'ów, czyli typów zmiennych poza tablicą.

Żeby zarejestrować naszą funkcję używamy metody

```
pModuleManager->RegisterFunction(luaVM, "naszaFunkcja", CFunctions::naszaFunkcja);
```

Natomiast żeby zarejestrować zdarzenie używamy metody

```
CFunctions::AddEvent(luaVM, "naszePierwszeZdarzenie");
```

Po kompilacji, jeżeli wywołamy naszą funkcję w skrypcie Lua:

```
naszaFunkcja("Parametr")
```

to powinna się ona wykonać po stronie modułu.

## Rozpiska

```
lua_State* luaVM
```

Status zasobu, w którym został uruchomiony moduł

```
ILuaModuleManager10* pModuleManager
```

Menedżer modułu oraz zasobów

```
void* getRootElement(lua_State*)
```

Funkcja zwracająca [root](https://wiki.multitheftauto.com/wiki/PL/Element_tree#Elementy_drzewa)'a

```
void* getResourceRootElement(lua_State*)
```

Funkcja zwracająca [root](https://wiki.multitheftauto.com/wiki/PL/Element_tree#Elementy_drzewa)'a zasobu,
w którym został uruchomiony dany moduł
