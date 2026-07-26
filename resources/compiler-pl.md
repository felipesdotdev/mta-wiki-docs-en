---
doc_id: "mta-wiki:13404"
title: "Resource : Compiler/PL"
source_title: "Resource:Compiler/PL"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ACompiler/PL"
revision_id: 72991
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:16:58.896879+00:00"
---

# Resource : Compiler/PL

**Nazwa**: Compiler

**Deweloper**: [User:GalAnonim](https://wiki.multitheftauto.com/index.php?title=User:GalAnonim&action=edit&redlink=1) (Rick)

**Stan**: OpenSource

**Źródło Github**: [https://github.com/httpRick/Compiler/tree/master](https://github.com/httpRick/Compiler/tree/master)

**Serwer Discord**: [https://discord.gg/gJszaFjDQA](https://discord.gg/gJszaFjDQA)

**Aktualna wersja**: 1.0.0

## Omówienie

Prosty w użyciu zasób, którym można eksportować zarówno po stronie klienta jak i po stronie serwera. polegająca na szyfrowaniu/odszyfrowywaniu plików.

## Wyeksportowane funkcje

### fileCompile

Click to collapse [-]
Shared

Ta funkcja szyfruje dane pliku.

```
string exports.Compiler:fileCompile(string filePath, var key, [int maxBytes = 1024])
```

### Wymagane Argumenty

- **string filePath:** [filepath](mta://reference/misc/filepath.md) ścieżka do pliku w następującym formacie: **":nazwazasobu/ścieżka"**. 'nazwazasobu' to nazwa zasobu, w którym znajduje się plik, oraz 'path' to ścieżka do katalogu głównego zasobu z plikiem.

Na przykład, jeśli w zasobie „objectSearch” znajduje się plik o nazwie „coolObjects.txt”, można go w ten sposób otworzyć z innego zasobu: *fileOpen(":objectSearch/coolObjects.txt")*.

Jeżeli plik znajduje się w bieżącym zasobie, wystarczy ścieżka do pliku np. *fileOpen("coolObjects.txt")*.

- **var key:** Klucz, którego chcesz użyć jako klucza kodowania pliku (używanych jest pierwsze 16 znaków wyniku)

### Opcjonalne Argumenty

- **int maxBytes:** Maksymalna liczba całkowita bajtów do zakodowania, domyślnie 1024 bajty. (nie zaleca się używania mniej niż 1024 bajtów)

### Zwroty

Zwraca zaszyfrowane bajty, które zostały odczytane w pliku, jeśli coś się nie powiedzie zwraca false.

### fileDecompile

Click to collapse [-]
Shared

Ta funkcja odszyfrowuje dane pliku.

```
string exports.Compiler:fileDecompile(string filePath, var key)
```

### Wymagane Argumenty

- **string filePath:** [filepath](mta://reference/misc/filepath.md) ścieżka do pliku w następującym formacie: **":nazwazasobu/ścieżka"**. 'nazwazasobu' to nazwa zasobu, w którym znajduje się plik, oraz 'path' to ścieżka do katalogu głównego zasobu z plikiem.

Na przykład, jeśli w zasobie „objectSearch” znajduje się plik o nazwie „coolObjects.txt”, można go w ten sposób otworzyć z innego zasobu: *fileOpen(":objectSearch/coolObjects.txt")*.

Jeżeli plik znajduje się w bieżącym zasobie, wystarczy ścieżka do pliku np. *fileOpen("coolObjects.txt")*.

- **var key:** Klucz, którego chcesz użyć jako klucza kodowania pliku (używanych jest pierwsze 16 znaków wyniku)

### Zwroty

Zwraca odszyfrowane bajty, które zostały odczytane w pliku, jeśli coś się nie powiedzie zwraca false.

### replaceCompileFile

Click to collapse [-]
Shared

Funkcja szyfruje i nadpisuje plik lub tworzy nowy w określonej nowej ścieżce.

```
boolean exports.Compiler:replaceCompileFile(string filePath, var key, [string newFilePath, int maxBytes])
```

### Wymagane Argumenty

- **string filePath:** [filepath](mta://reference/misc/filepath.md) ścieżka do pliku w następującym formacie: **":nazwazasobu/ścieżka"**. 'nazwazasobu' to nazwa zasobu, w którym znajduje się plik, oraz 'path' to ścieżka do katalogu głównego zasobu z plikiem.

Na przykład, jeśli w zasobie „objectSearch” znajduje się plik o nazwie „coolObjects.txt”, można go w ten sposób otworzyć z innego zasobu: *fileOpen(":objectSearch/coolObjects.txt")*.

Jeżeli plik znajduje się w bieżącym zasobie, wystarczy ścieżka do pliku np. *fileOpen("coolObjects.txt")*.

- **var key:** Klucz, którego chcesz użyć jako klucza kodowania pliku (używanych jest pierwsze 16 znaków wyniku)

### Opcjonalne Argumenty

- **string newFilePath:** Docelowa nowa ścieżka utworzenia nowego pliku.

- **int maxBytes:** Maksymalna liczba całkowita bajtów do zakodowania, domyślnie 1024 bajty. (nie zaleca się używania mniej niż 1024 bajtów)

### Zwroty

Zwraca true przy prawidłowym szyfrowaniu, jeśli coś się nie powiedzie zwraca false.

### replaceDecompileFile

Click to collapse [-]
Shared

Funkcja odszyfrowuje i nadpisuje plik lub tworzy nowy w określonej nowej ścieżce.

```
boolean exports.Compiler:replaceDecompileFile(string filePath, var key, [string newFilePath])
```

### Wymagane Argumenty

- **string filePath:** [filepath](mta://reference/misc/filepath.md) ścieżka do pliku w następującym formacie: **":nazwazasobu/ścieżka"**. 'nazwazasobu' to nazwa zasobu, w którym znajduje się plik, oraz 'path' to ścieżka do katalogu głównego zasobu z plikiem.

Na przykład, jeśli w zasobie „objectSearch” znajduje się plik o nazwie „coolObjects.txt”, można go w ten sposób otworzyć z innego zasobu: *fileOpen(":objectSearch/coolObjects.txt")*.

Jeżeli plik znajduje się w bieżącym zasobie, wystarczy ścieżka do pliku np. *fileOpen("coolObjects.txt")*.

- **var key:** Klucz, którego chcesz użyć jako klucza kodowania pliku (używanych jest pierwsze 16 znaków wyniku)

### Opcjonalne Argumenty

- **string newFilePath:** Docelowa nowa ścieżka utworzenia nowego pliku.

### Zwroty

Zwraca true przy prawidłowym odszyfrowaniu, jeśli coś się nie powiedzie zwraca false.

## Przykłady

### fileCompile

Click to collapse [-]
Server

```
function onResourceStart()
	local encryptedData = exports.Compiler:fileCompile("twojPlik.txt", "TwojeHaslo")
	if encryptedData then
		local fileHandler = fileCreate("twojPlik.txtc")
		fileWrite(fileHandler, encryptedData)
		fileClose(fileHandler)
        outputChatBox(encryptedData)
		outputChatBox("Pomyślnie zaszyfrowano twojPlik.txt")
	else
		outputChatBox("Nie udało się zaszyfrować twojPlik.txt")
	end
end
addEventHandler( "onResourceStart", resourceRoot, onResourceStart)
```

Click to collapse [-]
Client

```
function onClientResourceStart()
	local txd = exports.Compiler:fileCompile("banshee.txd", "TwojeHaslo")
	local dff = exports.Compiler:fileCompile("banshee.dff", "TwojeHaslo")
	if txd and dff then
		local fileHandlerTxd = fileCreate("banshee.txdc")
		fileWrite(fileHandlerTxd, txd)
		fileClose(fileHandlerTxd)

		local fileHandlerDff = fileCreate("banshee.dffc")
		fileWrite(fileHandlerDff, dff)
		fileClose(fileHandlerDff)
		outputChatBox("Pomyślnie zaszyfrowany model banshee")
	else
		outputChatBox("Nie udało się zaszyfrować modelu banshee")
	end
end
addEventHandler( "onClientResourceStart", resourceRoot, onClientResourceStart)
```

### fileDecompile

Click to collapse [-]
Server

```
function onResourceStart()
	local decryptedData = exports.Compiler:fileDecompile("twojPlik.txtc", "TwojeHaslo")
    if decryptedData then
    	outputChatBox(decryptedData)
    	outputChatBox("Pomyślnie odszyfrowano twojPlik.txtc")
    else
    	outputChatBox("Nie udało się odszyfrować twojPlik.txtc")
    end
end
addEventHandler( "onResourceStart", resourceRoot, onResourceStart)
```

Click to collapse [-]
Client

```
function onClientResourceStart()
	local txd = exports.Compiler:fileDecompile("banshee.txdc", "TwojeHaslo")
	local dff = exports.Compiler:fileDecompile("banshee.dffc", "TwojeHaslo")
	if txd and dff then
		local loadTXD = engineLoadTXD(txd)
		engineImportTXD(loadTXD, 429)
		local loadDFF = engineLoadDFF(dff)
		engineReplaceModel(loadDFF, 429)
		outputChatBox("Pomyślnie odszyfrowano i wczytano model banshee")
	else
		outputChatBox("Nie udało się odszyfrować modelu banshee")
	end
end
addEventHandler( "onClientResourceStart", resourceRoot, onClientResourceStart)
```

### replaceCompileFile

Click to collapse [-]
Server

```
function onResourceStart()
	local isEncrypted = exports.Compiler:replaceCompileFile("twojPlik.txt", "TwojeHaslo", "twojPlik.txtc")
	if isEncrypted then
		outputChatBox("Pomyślnie zaszyfrowano i utworzono twojPlik.txtc")
	else
		outputChatBox("Nie udało się zaszyfrować twojPlik.txt")
	end
end
addEventHandler( "onResourceStart", resourceRoot, onResourceStart)
```

Click to collapse [-]
Client

```
function onClientResourceStart()
	local isEncryptedTxd = exports.Compiler:replaceCompileFile("banshee.txd", "TwojeHaslo")
	local isEncryptedDff = exports.Compiler:replaceCompileFile("banshee.dff", "TwojeHaslo")
	if isEncryptedTxd and isEncryptedDff then
		outputChatBox("Pomyślnie zaszyfrowane i nadpisano pliki modelu banshee")
	else
		outputChatBox("Nie udało się zaszyfrować modelu banshee")
	end
end
addEventHandler( "onClientResourceStart", resourceRoot, onClientResourceStart)
```

### replaceDecompileFile

Click to collapse [-]
Server

```
function onResourceStart()
	local isDecrypted = exports.Compiler:replaceDecompileFile("twojPlik.txtc", "TwojeHaslo", "twojPlik.decrypted")
	if isEncrypted then
		outputChatBox("Pomyślnie odszyfrowano i utworzono twojPlik.decrypted")
	else
		outputChatBox("Nie udało się odszyfrować twojPlik.txtc")
	end
end
addEventHandler( "onResourceStart", resourceRoot, onResourceStart)
```

Click to collapse [-]
Client

```
function onClientResourceStart()
	local isDecryptedTxd = exports.Compiler:replaceDecompileFile("banshee.txd", "TwojeHaslo")
	local isDecryptedDff = exports.Compiler:replaceDecompileFile("banshee.dff", "TwojeHaslo")
	if isDecryptedTxd and isDecryptedDff then
		outputChatBox("Pomyślnie odszyfrowano i nadpisano pliki modelu banshee")
	else
		outputChatBox("Nie udało się odszyfrować modelu banshee")
	end
end
addEventHandler( "onClientResourceStart", resourceRoot, onClientResourceStart)
```
