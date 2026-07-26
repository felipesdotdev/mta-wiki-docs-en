---
doc_id: "mta-wiki:1375"
title: "Element/Marker"
source_title: "Marker"
source_url: "https://wiki.multitheftauto.com/wiki/Marker"
revision_id: 70575
language: "en"
categories: ["Element_Types"]
generated_at: "2026-07-26T16:16:08.043671+00:00"
---

# Element/Marker

The marker class represents colored, 3D shapes in the GTA world. There are several types of markers, including cylinders and checkpoints. In scripts, markers are often used to mark spots and trigger some sort of action when a player goes into them.

The element type of this class is **"marker"**.

The size of the marker cannot be specified from XML and defaults to 4.0.

## XML syntax

```
<marker posX="" posY="" posZ="" type="" .../>
```

### Required Attributes

- **posX**: A float representing the X position of the marker.

- **posY**: A float representing the Y position of the marker.

- **posZ**: A float representing the Z position of the marker.

### Optional Attributes

- **type:** The visual type of the marker to be created. Possible values:

- **"checkpoint"**: A race checkpoint. These are very tall, but not infinite, light pillars. Checkpoints snap to ground and become invisible after going over a certain Z height.

- **"ring"**: Doughnut shaped ring, normally used for aircraft.

- **"cylinder"**: Small glowing ground ring. These are the glow markers you walk into to activate missions or events in single player.

- **"arrow"**: Arrow pointing down. These are the arrows on the doors you can enter in single player, except MTA's are not animated by default.

- **"corona"**: A glowing ball of light.

- **color:** The color of the marker in HTML style format #RRGGBB, defaults to red if not specified.

## Related scripting functions

- [createMarker](mta://scripting/shared/functions/createmarker.md)

- [getMarkerColor](mta://scripting/shared/functions/getmarkercolor.md)

- [getMarkerCount](mta://scripting/shared/functions/getmarkercount.md)

- [getMarkerIcon](mta://scripting/shared/functions/getmarkericon.md)

- [getMarkerSize](mta://scripting/shared/functions/getmarkersize.md)

- [getMarkerTarget](mta://scripting/shared/functions/getmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [getMarkerTargetArrowProperties](mta://scripting/shared/functions/getmarkertargetarrowproperties.md)

- [getMarkerType](mta://scripting/shared/functions/getmarkertype.md)

- [setMarkerColor](mta://scripting/shared/functions/setmarkercolor.md)

- [setMarkerIcon](mta://scripting/shared/functions/setmarkericon.md)

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)
