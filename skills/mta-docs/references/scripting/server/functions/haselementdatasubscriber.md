---
doc_id: "mta-wiki:12426"
title: "HasElementDataSubscriber"
source_title: "HasElementDataSubscriber"
source_url: "https://wiki.multitheftauto.com/wiki/HasElementDataSubscriber"
revision_id: 81241
language: "en"
categories: ["Server_functions"]
---

# HasElementDataSubscriber

This function returns whether a [player](https://wiki.multitheftauto.com/index.php?search=player) is subscribed to specific [element data](mta://reference/misc/element-data--975d1ea3.md).
This function is used together with [setElementData](mta://scripting/shared/functions/setelementdata.md) in *"subscribe"* mode.

## Syntax

```
bool hasElementDataSubscriber ( element theElement, string key, player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):hasDataSubscriber(...)*

### Required Arguments

- **theElement:** The [element](mta://reference/misc/element.md) you wish to check whether the [player](https://wiki.multitheftauto.com/index.php?search=player) is subscribed to.

- **key:** The key you wish to check whether the player is subscribed to.

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) you wish to check.

### Returns

Returns *true* if the player is subscribed, *false* otherwise.

## Example

Click to collapse [-]
Server

```
local nameOfOurElementData = "random" --// name our element data

for i,v in ipairs(getElementsByType("player")) do --// loop through all the players on the server
    setElementData(v, nameOfOurElementData, true, "subscribe") --// set our element data to all players on server
end

function checkIsSubscribed(plr,cmd, key)

    if not key then return end --// check if you've typed element data key

    local randomPlayer = getRandomPlayer() --// getting random player from server

    local isSubscribed = hasElementDataSubscriber(randomPlayer, tostring(key), randomPlayer) --// use our function

    if not isSubscribed then --// if random player is not subscribed to given element data key then add him to subscription

        addElementDataSubscriber(randomPlayer, tostring(key), randomPlayer)
        outputChatBox("Element data key: "..tostring(key).." is now subscribed to: "..getPlayerName(randomPlayer), plr, 255, 255, 255, true)

    else --// if he is subscribed to given element data then remove him from subscription

        removeElementDataSubscriber(randomPlayer, tostring(key), randomPlayer)
        outputChatBox(getPlayerName(randomPlayer).." has been removed from subscription from element data key: "..tostring(key), plr, 255, 255, 255, true)

    end

end
addCommandHandler("checksub", checkIsSubscribed, false, false) --// creating command /checksub not restricted and not CASE sensitive

--// EXAMPLE: /checksub random
```

## See Also

- [addElementDataSubscriber](mta://scripting/server/functions/addelementdatasubscriber.md)

- [clearElementVisibleTo](mta://scripting/server/functions/clearelementvisibleto.md)

- [cloneElement](mta://scripting/server/functions/cloneelement.md)

- [getElementSyncer](mta://scripting/server/functions/getelementsyncer.md)

- [getElementZoneName](mta://scripting/server/functions/getelementzonename.md)

- hasElementDataSubscriber

- [isElementVisibleTo](mta://scripting/server/functions/iselementvisibleto.md)

- [removeElementData](mta://scripting/server/functions/removeelementdata.md)

- [removeElementDataSubscriber](mta://scripting/server/functions/removeelementdatasubscriber.md)

- [setElementSyncer](mta://scripting/server/functions/setelementsyncer.md)

- [setElementVisibleTo](mta://scripting/server/functions/setelementvisibleto.md)
  

- **Shared**

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

- [setElementHealth](mta://scripting/shared/functions/setelementhealth.md)

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
