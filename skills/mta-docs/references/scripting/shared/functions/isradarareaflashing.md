---
doc_id: "mta-wiki:1614"
title: "IsRadarAreaFlashing"
source_title: "IsRadarAreaFlashing"
source_url: "https://wiki.multitheftauto.com/wiki/IsRadarAreaFlashing"
revision_id: 43076
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# IsRadarAreaFlashing

This function allows detection of whether a radar area is flashing or not.

## Syntax

```
bool isRadarAreaFlashing ( radararea theRadararea )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[radararea](https://wiki.multitheftauto.com/index.php?search=radararea):isFlashing(...)*

**Variable**: *.flashing*

**Counterpart**: *[setRadarAreaFlashing](mta://scripting/shared/functions/setradarareaflashing.md)*

### Required Arguments

- **theRadararea:** The radar area you wish to check the state of flashing

### Returns

Returns *true* if the radar area is flashing, *false* if it is not or if it doesn't exist.

## Example

This example checks whether the radar area in the variable *glenpark* is flashing, and announces it if it is.

```
function checkArea(sourcePlayer)
    if ( isRadarAreaFlashing ( glenpark ) ) then          -- if the radar area in the variable glenpark is flashing
        outputChatBox ( "Glen Park is under attack!!!" )  -- announce it
    end
end
addCommandHandler("checkArea", checkArea)
```

## See Also

- [createRadarArea](mta://scripting/shared/functions/createradararea.md)

- [getRadarAreaColor](mta://scripting/shared/functions/getradarareacolor.md)

- [getRadarAreaSize](mta://scripting/shared/functions/getradarareasize.md)

- [isInsideRadarArea](mta://scripting/shared/functions/isinsideradararea.md)

- isRadarAreaFlashing

- [setRadarAreaColor](mta://scripting/shared/functions/setradarareacolor.md)

- [setRadarAreaFlashing](mta://scripting/shared/functions/setradarareaflashing.md)

- [setRadarAreaSize](mta://scripting/shared/functions/setradarareasize.md)
