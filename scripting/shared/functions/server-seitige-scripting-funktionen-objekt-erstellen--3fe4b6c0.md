---
doc_id: "mta-wiki:6327"
title: "DE/createObject"
source_title: "Server seitige Scripting Funktionen/Objekt erstellen"
source_url: "https://wiki.multitheftauto.com/wiki/Server_seitige_Scripting_Funktionen/Objekt_erstellen"
revision_id: 30505
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:10:41.918218+00:00"
---

# DE/createObject

Diese Funktion erstellt ein Objekt in der GTA-Welt.

## Syntax

```
object createObject ( int modelid, float x, float y, float z, [ float rx, float ry, float rz, bool isLowLOD = false ] )
```

### Benötigte Parameter

- **modelid:** Eine ganze Zahl, dass die Modelid bestimmt.

- **x:** Eine Fließkommadarstellungen, welche die X Koordinate in der Karte darstellt.

- **y:** Eine Fließkommadarstellungen, welche die Y Koordinate in der Karte darstellt.

- **z:** Eine Fließkommadarstellungen, welche die Z Koordinate in der Karte darstellt.

### Optionale Parameter

Notiz: Wenn optionale Parameter benutzt werden, müssen erst alle benötigten Parameter erfüllt sein! Für mehr Informationen siehe: [Optionale Parameter](http://wiki.multitheftauto.com/wiki/Optional_Arguments)

- **rx:** Eine Fließkommadarstellungen, welche die Rotation and der X Axe darstellt.

- **ry:** Eine Fließkommadarstellungen, welche die Rotation and der Y Axe darstellt.

- **rz:** Eine Fließkommadarstellungen, welche die Rotation and der Z Axe darstellt.

- **isLowLOD:** Ein Boolean, welches bestimmt, ob das Objekt ein low LOD Objekt ist. Ein low LOD Objekt hat keine Kollision und wird auf längere Distanz dargestellt.

### Returns

Gibt das Objekt Element zurück, falls es erfolgreich erstellt wurde, ansonsten den Boolean *false*

## Beispiel

Click to collapse [-]
Server

Dieses Beispiel erstellt beim Start einer Resource ein Objekt:

```
function mapLoad ( name )
   -- erstellt ein Objekt mit den angegebenen Koordinaten und Rotationen
   createObject ( 1337, 5540.6654, 1020.55122, 1240.545, 90, 0, 0 )
end
addEventHandler ( "onResourceStart", getRootElement(), mapLoad )
```

## Siehe Auch

- DE/createObject

- [DE/moveObject](https://wiki.multitheftauto.com/wiki/DE/moveObject)

- [DE/stopObject](https://wiki.multitheftauto.com/index.php?title=DE/stopObject&action=edit&redlink=1)

- [DE/getObjectScale](https://wiki.multitheftauto.com/index.php?title=DE/getObjectScale&action=edit&redlink=1)

- [DE/setObjectScale](https://wiki.multitheftauto.com/index.php?title=DE/setObjectScale&action=edit&redlink=1)
