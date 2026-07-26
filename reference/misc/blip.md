---
doc_id: "mta-wiki:1447"
title: "Element/Blip"
source_title: "Blip"
source_url: "https://wiki.multitheftauto.com/wiki/Blip"
revision_id: 70596
language: "en"
categories: ["Element_Types"]
generated_at: "2026-07-26T16:10:25.910364+00:00"
---

# Element/Blip

The blip class represents small icons or blips that can be shown on a player's radar.

The element type of this class is **"blip"**. The list of blip icons are available on the [Radar Blips](mta://reference/misc/radar-blips.md) page.

## XML syntax

```
<blip posX="" posY="" posZ="" icon="" color="" dimension="" ordering=""/>
```

### Required Attributes

- **posX**: A float representing the X position of the blip.

- **posY**: A float representing the Y position of the blip.

- **posZ**: A float representing the Z position of the blip.

### Optional Attributes

- **color:** The color of the icon in HTML-style format (i.e. #RRGGBB). Defaults to blue if not specified.

- **icon:** The icon of the blip. Defaults to 0 if not specified.

- **dimension:** The dimension of the blip. Defaults to 0 if not specified.

- **ordering:** The Z-level ordering of the blip. Defaults to 0 if not specified.

## Related scripting functions

### Client

**Shared**

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

### Server

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
