---
doc_id: "mta-wiki:4261"
title: "SetElementRotation"
source_title: "SetElementRotation"
source_url: "https://wiki.multitheftauto.com/wiki/SetElementRotation"
revision_id: 76250
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.3.2", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:40.377861+00:00"
---

# SetElementRotation

Sets the rotation of elements according to the world (does not work with players that are on the ground).

| [[{{{image}}}\|link=\|]] | Tip: New scripts should set conformPedRotation to true when using this function on peds . This will prevent quirky old behaviour. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This function does not work on colshape . |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This function does not work on dummy element . |
| --- | --- |
|  |  |

## Syntax

```
bool setElementRotation ( element theElement, float rotX, float rotY, float rotZ [, string rotOrder = "default", bool conformPedRotation = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):setRotation(...)*

**Variable**: *.rotation*

**Counterpart**: *[getElementRotation](mta://scripting/shared/functions/getelementrotation.md)*

### Required Arguments

- **theElement:** The element whose rotation will be set

- **rotX:** The element's rotation around the x axis in degrees

- **rotY:** The element's rotation around the y axis in degrees

- **rotZ:** The element's rotation around the z axis in degrees

### Optional Arguments

- **rotOrder:** A string representing the rotation order desired when interpreting the provided [euler angles](http://en.wikipedia.org/wiki/Euler_angles). If omitted, default value is *"default"*. Allowed values are:

- *"default":* default MTA behavior prior to 1.1, where rotation order depends on element type

- *"ZXY":* rotation about the Z axis (*up*), then about the resulting X axis (*right*), and finally about the resulting Y axis (*front*). This is the default rotation order for [objects](mta://reference/misc/object.md)

- *"ZYX":* rotation about the Z axis (*up*), then about the resulting Y axis (*front*), and finally about the resulting X axis (*right*). This is the default rotation order for [vehicles](mta://reference/misc/vehicle.md)

The default rotation order for peds/players is -Z-Y-X but this rotation order (set using *"default"* on peds) can not be set manually on other element types since it only exists due to historical and backward compatibility reasons.
Specifying a rotation order other than *"default"* allows the same angles to be uniformly used on several elements without having to consider their type.

- **conformPedRotation:** *Relevant only for peds and will be ignored for other element types.* A bool which should be set to *true* to ensure the ped rotation is correctly set in all circumstances. Failing to set this argument may result in the ped rotation being inverted whilst it is in the air and other inconsistencies. The default value of false is for backward compatibility with scripts which may depend upon the incorrect behaviour.

### Returns

Returns *true* if the element rotation was successfully set and *false* otherwise.

## Example

How to correctly set the rotation for a ped:

Click to collapse [-]
Client

```
function pedRotate ( )
    local rotX, rotY, rotZ = getElementRotation(localPlayer) -- get the local players's rotation
    setElementRotation(localPlayer,0,0,rotZ+10,"default",true) -- turn the player 10 degrees clockwise
end
addCommandHandler ( "turn", pedRotate )
```

When a player used the command "turn" and they are the driver of a vehicle the vehicle will rotate 10 degrees clockwise

Click to collapse [-]
Client

```
function carRotate( )
    if isPedInVehicle(localPlayer) then -- if the local client is in a vehicle
        localVehicle = getPedOccupiedVehicle(localPlayer)
        if getVehicleController(localVehicle) == localPlayer then -- if the local client is the controller (driver) of the vehicle
            local rotX, rotY, rotZ = getElementRotation(localVehicle) -- get the local client's vehicle rotation
            setElementRotation(localVehicle,rotX,rotY,rotZ+10) -- turn the vehicle 10 degrees clockwise
         end
    end
end
addCommandHandler ( "turn", carRotate )
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.1-9.04680 | Added conformPedRotation argument |
| --- | --- |

## See Also

- [getElementBoneMatrix](mta://scripting/client/functions/getelementbonematrix.md)

- [getElementBonePosition](mta://scripting/client/functions/getelementboneposition.md)

- [getElementBoneRotation](mta://scripting/client/functions/getelementbonerotation.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22741](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22741):

- [getElementBoneQuaternion](mta://scripting/client/functions/getelementbonequaternion.md) 

- [getElementBoundingBox](mta://scripting/client/functions/getelementboundingbox.md)

- [getElementDistanceFromCentreOfMassToBaseOfModel](mta://scripting/client/functions/getelementdistancefromcentreofmasstobaseofmodel.md)

- [getElementLighting](mta://scripting/client/functions/getelementlighting.md)

- [getElementRadius](mta://scripting/client/functions/getelementradius.md)

- [isElementCollidableWith](mta://scripting/client/functions/iselementcollidablewith.md)

- [isElementLocal](mta://scripting/client/functions/iselementlocal.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22862](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22862):

- [setElementLighting](mta://scripting/client/functions/setelementlighting.md)

- [isElementOnScreen](mta://scripting/client/functions/iselementonscreen.md)

- [isElementStreamable](mta://scripting/client/functions/iselementstreamable.md)

- [isElementStreamedIn](mta://scripting/client/functions/iselementstreamedin.md)

- [isElementSyncer](mta://scripting/client/functions/iselementsyncer.md)

- [isElementWaitingForGroundToLoad](mta://scripting/client/functions/iselementwaitingforgroundtoload.md)

- [setElementBoneMatrix](mta://scripting/client/functions/setelementbonematrix.md)

- [setElementBonePosition](mta://scripting/client/functions/setelementboneposition.md)

- [setElementBoneRotation](mta://scripting/client/functions/setelementbonerotation.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22741](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22741):

- [setElementBoneQuaternion](mta://scripting/client/functions/setelementbonequaternion.md) 

- [setElementCollidableWith](mta://scripting/client/functions/setelementcollidablewith.md)

- [setElementStreamable](mta://scripting/client/functions/setelementstreamable.md)

- [updateElementRpHAnim](mta://scripting/client/functions/updateelementrphanim.md)
  

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

- setElementRotation

- [setElementVelocity](mta://scripting/shared/functions/setelementvelocity.md)

- [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)
