---
doc_id: "mta-wiki:5840"
title: "Resource : DE/Editor/Plugins"
source_title: "Resource:DE/Editor/Plugins"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ADE/Editor/Plugins"
revision_id: 27072
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:10:34.467279+00:00"
---

# Resource : DE/Editor/Plugins

Einführung

Der Editor bietet Funktionen und Kommandos um externe Resourcen als Schnittstelle zu nutzen. Gewöhnlicherweise sind Elemente die außerhalb des Editors erstellt wurden uneinsehbar und unveränderbar. Wenn man die Elemente importiert, sind diese kompatibel mit dem Editor. Somit können diese vom Editor verändert werden und in einer Map Resource gespeichert werden. In der Praxis erlaubt dies die grundlegende Entwicklung von Plugins oder eine manuelle Verbindung zu externen Resourcen.

## Commands

Ein "import" Command wird ausgeführt um dem Spieler zu erlauben die Elemente einer speziellen Resource zu importieren:

```
import <resourceName>
```

- **resourceName:** Der Name der Resource, dessen Objekte importiert werden sollen.

Die Elemente dieser Resource werden dann importiert. Dies ist eine praktische Möglichkeit um benutzerdefinierte Models zu importieren. Während der Editor selbst keine benutzerdefinierten Models laden kann, kann er die benutzerdefinierten Models einer Resource importieren, die diese laden kann. So können benutzerdefinierte Maps entstehen. Als Beispiel kann man den folgenden Schritten folgen um die Map sth-aztec in eine benutzerdefinierte Map umzuwandeln.

- Starte den Editor

- Starte (Nicht öffnen) sth-aztec manuell.  Dies sollte die Map starten und die benutzerdefinierten Models laden.

- Tippe "import sth-aztec" und die Objekte werden in den Editor importiert.

- Die Map wird nun geladen.

## Funktionen

Die **Editor** Resource besitzt auch eine *import* Funktion.  Diese spiegelt das Command wieder, aber erlaubt die Importierung von "element datatypes".  Im wesentlichen erlaubt dies anderen Resourcen die *import* Funktion zu nutzen, ohne eine Berechtigung vom Editor zu benötigen..

```
bool import ( element rootElement/resource resourceToImportFrom )
```

- **rootElement:**  Das Rootelement, dass du importieren möchtest (Dieses und alle children werden importiert)

**OR:**

- **resourceToImportFrom:**  Der resource pointer aus dem man importieren möchte.

## Editor Plugins

#### Editor Loop Generator

 

Loop generator working with the editor.

Ein Beispiel führ diese Benutzung ist [loop generator plugin](http://www.multiupload.com/ZSQLI9NM4L), adaptiert von Offroader23's Arbeit an *offedit*.

Diese Resource fügt ein benutzerdefiniertes gui hinzu, mit welchem man perfekte Loopings aus Standartobjekten erstellen kann. Nach der Berechnung und Erstellung der Objekte, nutzt diese Resource die exportierte *import* Funktion und erlaubt dem Editor die erstellen Objekte zu verändern/verschieben.

#### Editor racemap loader

Dieses Plugin lädt Objekte aus Race Maps ohne eine "conversion".

Du kannst sie [hier](http://www.multiupload.com/JPEDK14H0I) downloaden!

#### Roller Coaster Generator

Mit diesem Plugin kannst du Achterbahnen so leicht erstellen, wie man auch Maps erstellt.
[Learn more by clicking here.](mta://reference/misc/roller-coaster-generator.md)

#### Object Movement Generator

Ein Versuch das Erstellen und Bewegen von Objekten noch einfacher zu gestalten.

Downloadlink: [hier](http://community.mtasa.com/index.php?p=resources&s=details&id=1224)
