---
doc_id: "mta-wiki:3270"
title: "SetElementHealth"
source_title: "SetElementHealth"
source_url: "https://wiki.multitheftauto.com/wiki/SetElementHealth"
revision_id: 77189
language: "en"
categories: ["Server_functions", "Client_functions", "Functions_and_events_with_issues"]
---

# SetElementHealth

This function sets the health for the specified [element](mta://reference/misc/element.md). This can be a [ped](https://wiki.multitheftauto.com/index.php?search=ped), [object](https://wiki.multitheftauto.com/index.php?search=object) or a [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle).

| [[{{{image}}}\|link=\|]] | Note: In the case of the vehicle element, the following effects appear, depending on the health value: 650: white steam 0%, black smoke 0% 450: white steam 100%, black smoke 50% 250: white steam 0%, black smoke 100% 249: fire with big black smoke |
| --- | --- |
|  |  |

## Syntax

```
bool setElementHealth ( element theElement, float newHealth )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):setHealth(...)*

**Variable**: *.health*

**Counterpart**: *[getElementHealth](mta://scripting/shared/functions/getelementhealth.md)*

### Required Arguments

- **theElement:** The [ped](https://wiki.multitheftauto.com/index.php?search=ped), [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) or [object](https://wiki.multitheftauto.com/index.php?search=object) whose health you want to set.

- **newHealth:** A float indicating the new health to set for the element.

### Returns

Returns *true* if the new health was set successfully, or *false* if invalid arguments were passed.

## Example

Click to collapse [-]
Server

This example adds a 'hpslap' console command that lets players "slap" others (doing 20 damage).

```
function hpSlap ( sourcePlayer, command, targetPlayerName )
    -- check if the user has access to it first
    if not hasObjectPermissionTo(sourcePlayer, "command.slap", false) then
        outputChatBox ( "You cannot use this command.", sourcePlayer )
        return false
    end
    -- look up the player to be slapped
    local targetPlayer = getPlayerFromName ( targetPlayerName )
    -- if there's a player with such name,
    if targetPlayer then
        -- subtract 20 from his health
        setElementHealth ( targetPlayer, getElementHealth(targetPlayer) - 20 )
    else
        -- otherwise, output an error message
        outputChatBox ( "There is no player named " .. targetPlayerName .. "!", sourcePlayer )
    end
end
-- add our function as a handler for "hpslap"
addCommandHandler ( "hpslap", hpSlap )
```

Click to collapse [-]
Example 1

This example setting health by a command.

```
function Health(player, command, amount)
    setElementHealth(player, tonumber(amount))
end
addCommandHandler("set", Health)
```

## Issues

| Issue ID | Description |
| --- | --- |
| #414 | Using setElementHealth on a dead ped makes it invincible |

## See Also

- [attachElements](mta://scripting/shared/functions/attachelements.md)

- [createElement](mta://scripting/shared/functions/createelement.md)

- [destroyElement](mta://scripting/shared/functions/destroyelement.md)

- [detachElements](mta://scripting/shared/functions/detachelements.md)

- [getAttachedElements](mta://scripting/shared/functions/getattachedelements.md)

- [getElementAlpha](mta://scripting/shared/functions/getelementalpha.md)

- [getElementAttachedOffsets](mta://scripting/shared/functions/getelementattachedoffsets.md)

- [getElementAttachedTo](mta://scripting/shared/functions/getelementattachedto.md)

- [getElementByIndex](mta://scripting/shared/functions/getelementbyindex.md)

- [getElementByID](mta://scripting/shared/functions/getelementbyid.md)

- [getElementChild](mta://scripting/shared/functions/getelementchild.md)

- [getElementChildren](mta://scripting/shared/functions/getelementchildren.md)

- [getElementChildrenCount](mta://scripting/shared/functions/getelementchildrencount.md)

- [getElementCollisionsEnabled](mta://scripting/shared/functions/getelementcollisionsenabled.md)

- [getElementColShape](mta://scripting/shared/functions/getelementcolshape.md)

- [getElementData](mta://scripting/shared/functions/getelementdata.md)

- [getAllElementData](mta://scripting/shared/functions/getallelementdata.md)

- [hasElementData](mta://scripting/shared/functions/haselementdata.md)

- [getElementDimension](mta://scripting/shared/functions/getelementdimension.md)

- [getElementHealth](mta://scripting/shared/functions/getelementhealth.md)

- [getElementID](mta://scripting/shared/functions/getelementid.md)

- [getElementInterior](mta://scripting/shared/functions/getelementinterior.md)

- [getElementMatrix](mta://scripting/shared/functions/getelementmatrix.md)

- [getElementModel](mta://scripting/shared/functions/getelementmodel.md)

- [getElementParent](mta://scripting/shared/functions/getelementparent.md)

- [getElementPosition](mta://scripting/shared/functions/getelementposition.md)

- [getElementRotation](mta://scripting/shared/functions/getelementrotation.md)

- [getElementsByType](mta://scripting/shared/functions/getelementsbytype.md)

- [getElementsWithinColShape](mta://scripting/shared/functions/getelementswithincolshape.md)

- [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md)

- [getElementType](mta://scripting/shared/functions/getelementtype.md)

- [getElementVelocity](mta://scripting/shared/functions/getelementvelocity.md)

- [getLowLODElement](mta://scripting/shared/functions/getlowlodelement.md)

- [getRootElement](mta://scripting/shared/functions/getrootelement.md)

- [isElement](mta://scripting/shared/functions/iselement.md)

- [isElementAttached](mta://scripting/shared/functions/iselementattached.md)

- [isElementCallPropagationEnabled](mta://scripting/shared/functions/iselementcallpropagationenabled.md)

- [isElementDoubleSided](mta://scripting/shared/functions/iselementdoublesided.md)

- [isElementFrozen](mta://scripting/shared/functions/iselementfrozen.md)

- [isElementInWater](mta://scripting/shared/functions/iselementinwater.md)

- [isElementLowLOD](mta://scripting/shared/functions/iselementlowlod.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22864](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22864):

- [isElementOnFire](mta://scripting/shared/functions/iselementonfire.md)

- [isElementWithinColShape](mta://scripting/shared/functions/iselementwithincolshape.md)

- [isElementWithinMarker](mta://scripting/shared/functions/iselementwithinmarker.md)

- [setElementAlpha](mta://scripting/shared/functions/setelementalpha.md)

- [setElementAngularVelocity](mta://scripting/shared/functions/setelementangularvelocity.md)

- [getElementAngularVelocity](mta://scripting/shared/functions/getelementangularvelocity.md)

- [setElementAttachedOffsets](mta://scripting/shared/functions/setelementattachedoffsets.md)

- [setElementCallPropagationEnabled](mta://scripting/shared/functions/setelementcallpropagationenabled.md)

- [setElementCollisionsEnabled](mta://scripting/shared/functions/setelementcollisionsenabled.md)

- [setElementData](mta://scripting/shared/functions/setelementdata.md)

- [setElementDimension](mta://scripting/shared/functions/setelementdimension.md)

- [setElementDoubleSided](mta://scripting/shared/functions/setelementdoublesided.md)

- [setElementFrozen](mta://scripting/shared/functions/setelementfrozen.md)

- setElementHealth

- [setElementID](mta://scripting/shared/functions/setelementid.md)

- [setElementInterior](mta://scripting/shared/functions/setelementinterior.md)

- [setElementModel](mta://scripting/shared/functions/setelementmodel.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22864](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22864):

- [setElementOnFire](mta://scripting/shared/functions/setelementonfire.md)

- [setElementParent](mta://scripting/shared/functions/setelementparent.md)

- [setElementPosition](mta://scripting/shared/functions/setelementposition.md)

- [setElementRotation](mta://scripting/shared/functions/setelementrotation.md)

- [setElementVelocity](mta://scripting/shared/functions/setelementvelocity.md)

- [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)
