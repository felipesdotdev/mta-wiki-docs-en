---
doc_id: "mta-wiki:12835"
title: "HU/CreateBlip"
source_title: "Hu/CreateBlip"
source_url: "https://wiki.multitheftauto.com/wiki/Hu/CreateBlip"
revision_id: 71301
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates", "Mudanças_em_1.0"]
generated_at: "2026-07-26T16:15:43.749152+00:00"
---

# HU/CreateBlip

Ez a funkció létrehoz egy [blip](mta://reference/misc/blip.md) [elemet](mta://reference/misc/element.md), amely egy ikonként jelenik meg a játékos radarán.

## Szintaxis

Click to collapse [-]
Server

```
blip createBlip ( float x, float y, float z [, int icon = 0, int size = 2, int r = 255, int g = 0, int b = 0, int a = 255, int ordering = 0, float visibleDistance = 16383.0, visibleTo = getRootElement( ) ] )
```

Click to collapse [-]
Client

```
blip createBlip ( float x, float y, float z [, int icon = 0, int size = 2, int r = 255, int g = 0, int b = 0, int a = 255, int ordering = 0, float visibleDistance = 16383.0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Blip](mta://reference/misc/blip.md)(...)*

### Kötelező argumentumok

- **x:** A blip x kordinátája, in world coordinates.

- **y:** A blip y kordinátája, in world coordinates.

- **z:** A blip z kordinátája, in world coordinates.

### Tetszőleges argumentumok

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).   

*NOTE*: Amikor tetszőleges argumentumokat használ, előfordulhat, hogy az összes argumentumokat meg kell adnia, mielőtt egyet is használna.

- **icon:** Az icon, mely a radar blipnek lennie kell. Az érvényes értékeket megtekintheti a [Radar Blips](mta://reference/misc/radar-blips.md) oldalon.

- **size:** A radar blip mérete. Csak a "Marker" ikonra érvényes. Az alapértelmezett érték a 2, maximum a 25.

- **r:** A piros mennyisége a blip színében (0 - 255). Csak a "Marker" ikonra érvényes. Az alapértelmezett érték 255.

- **g:** A zöld mennyisége a blip színében (0 - 255). Csak a "Marker" ikonra érvényes. Az alapértelmezett érték 0.

- **b:** A kék mennyisége a blip színében (0 - 255). Csak a "Marker" ikonra érvényes. Az alapértelmezett érték 0.

- **a:** Az telítettség mennyisége a blip színében (0 - 255). Csak a "Marker" ikonra érvényes. Az alapértelmezett érték 255.

- **ordering:** Leírja a blip, Z-tengelyen való helyét (-32768 - 32767). Az alapértelmezett érték a 0.

- **visibleDistance:** A maximális távolság a kamerától, ahol a blip még mindig látható (0-65535).

Click to collapse [-]
Server

- **visibleTo:** Ez határozza meg, hogy mely elemek láthassák a blip-et. Alapértelmezetten mindenkinek látható. Lásd [visibility](mta://reference/misc/visibility.md).

## Visszaadott érték

Visszaadja a [blip](mta://reference/misc/blip.md) egy [elemét](mta://reference/misc/element.md), ha sikeresen létre lett hozva, egyébként *false*.

## Példa

Click to collapse [-]
Server

**Example 1:** Ez a példa létrehoz egy radar blipet egy random játékos pozíciójában, ami csak annak a játékosnak látható.

```
-- Pick a random player
local myPlayer = getRandomPlayer( )
-- Retrieve the player's position and store it in the variables x, y and z
local x, y, z = getElementPosition( myPlayer )
-- Create a radar blip at the player's position, with a 'cash' icon and only visible to the player
local myBlip = createBlip( x, y, z, 51, 0, 0, 0, 255, myPlayer )
```

**Példa 2:** Ez a pálda egy blipet rögzít egy játékosnak. You can attach a blip to an element by just setting the blip's parent to that element.

```
-- Pick a random player
local myPlayer = getRandomPlayer( )
-- Create a radar blip in the middle of the map
local myBlip = createBlip( 0, 0, 0 )
-- Make the player the parent of the blip, so that the blip follows the player around
setElementParent( myBlip, myPlayer )
```

## Lásd még

- [createBlip](mta://scripting/shared/functions/createblip.md)

- [createBlipAttachedTo](mta://scripting/shared/functions/createblipattachedto.md)

- [getBlipColor](mta://scripting/shared/functions/getblipcolor.md)

- [getBlipIcon](mta://scripting/shared/functions/getblipicon.md)

- [getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)

## Fordította

- Surge
