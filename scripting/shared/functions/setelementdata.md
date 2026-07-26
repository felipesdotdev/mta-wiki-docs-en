---
doc_id: "mta-wiki:1537"
title: "SetElementData"
source_title: "SetElementData"
source_url: "https://wiki.multitheftauto.com/wiki/SetElementData"
revision_id: 82583
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:39.933721+00:00"
---

# SetElementData

This function stores [element data](mta://reference/misc/element-data--975d1ea3.md) under a certain key, attached to an element. Element data set using this is then synced with all clients and the server. The data can contain server-created elements, but you should avoid passing data that is not able to be synced such as xmlnodes, acls, aclgroups etc.

As element data is synced to all clients, it can generate a lot of network traffic and be heavy on performance. Events are much more efficient for sending data from a client to the server only, or from the server to a specific client.   

Usage of element data should be discouraged where your goal can be achieved with events like above, and [tables](mta://reference/misc/table.md) for storing and retrieving data.

| [[{{{image}}}\|link=\|]] | Tip: A simple and efficient way to make a variable known to the server and clients is to use setElementData on the root element. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: See Script security for tips on preventing cheaters when using events and element data. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: For performance reasons, never use setElementData in events that fire often (like onClientRender ) without further optimization or conditions. In fact, using element data in general, can take such a toll on performance that not using it unless strictly necessary (e.g use alternatives such as storing data in tables) is recommended. |
| --- | --- |
|  |  |

A subscription mode has been introduced for setElementData serverside. When setting data in subscription mode, only clients that are added through [addElementDataSubscriber](mta://scripting/server/functions/addelementdatasubscriber.md) will receive the data, which is good for performance.
Note this mode only works when setting element data serverside. Setting data clientside still sends the update to all clients if 'synchronize' is set to true.

## Syntax

Click to collapse [-]
Server

```
bool setElementData ( element theElement, string key, var value [, string syncMode = "broadcast", string clientChangesPolicy = "default" ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):setData(...)*

**Counterpart**: *[getElementData](mta://scripting/shared/functions/getelementdata.md)*

### Required Arguments

- **theElement:** The [element](mta://reference/misc/element.md) you wish to attach the data to.

- **key:** The key you wish to store the data under. (Maximum 128 characters.)

- **value:** The value you wish to store. See [element data](mta://reference/misc/element-data--975d1ea3.md) for a list of acceptable datatypes.

### Optional Arguments

- **syncMode:** Synchronization mode.

- *"broadcast"* - Synchronize to all clients (default behavior). You can also parse *true* for this option.

- *"local"* - Don't synchronize. You can also parse *false* for this option.

- *"subscribe"* - Only synchronize to specific clients. See [addElementDataSubscriber](mta://scripting/server/functions/addelementdatasubscriber.md) and [removeElementDataSubscriber](mta://scripting/server/functions/removeelementdatasubscriber.md).

ADDED/UPDATED IN VERSION 1.6.0 [r22815](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22815):

- **clientChangesPolicy:** Client changes policy.

- *"default"* - Use **elementdata_whitelisted** setting from [mtaserver.conf](https://wiki.multitheftauto.com/wiki/Server_mtaserver.conf#elementdata_whitelisted)

- *"allow"* - Trust changes from clients.

- *"deny"* - Deny client changes. The server will trigger the [onPlayerChangesProtectedData](mta://scripting/server/events/onplayerchangesprotecteddata.md) event when the client attempts to change the value.

Click to collapse [-]
Client

```
bool setElementData ( element theElement, string key, var value [, bool synchronize = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[element](mta://reference/misc/element.md):setData(...)*

**Counterpart**: *[getElementData](mta://scripting/shared/functions/getelementdata.md)*

### Required Arguments

- **theElement:** The [element](mta://reference/misc/element.md) you wish to attach the data to.

- **key:** The key you wish to store the data under. (Maximum 128 characters.)

- **value:** The value you wish to store. See [element data](mta://reference/misc/element-data--975d1ea3.md) for a list of acceptable datatypes.

### Optional Arguments

- **synchronize:** Determines whether or not the data will be synchronized with the server.

### Returns

Returns *true* if the data was set successfully, *false* otherwise.

## Example

Example 1

Click to collapse [-]
Server

This example allows a player to add a custom tag onto their nickname, and also reverts it back to normal if they wish.

```
function addPlayerCustomTag ( thePlayer, command, newTag )
	--Let's make sure the newTag param has been entered...
	if ( newTag ) then
		--Grab their current playername for saving.
		local sPlayerNickname = getPlayerName ( thePlayer )
		--Create their new nickname with their tag
		local sNewPlayerNickname = newTag .. " " .. sPlayerNickname
		
		--Let's first load the element data, see if it's there already
		--The reason for this is that if a player were to do /addtag twice,
		--the tag would be prepended a second time
		local sOldNick = getElementData( thePlayer, "tempdata.originalnick" )
		if ( sOldNick == false ) then
			--Save their orignal nickname in their element data
			setElementData ( thePlayer, "tempdata.originalnick", sPlayerNickname )
		end
		
		--Set their new nickname globally
		setPlayerName ( thePlayer, sNewPlayerNickname )
		
		--Tell them it's done
		outputChatBox ( "Your new nickname has been set, to put it back to its original state you can use /deltag", thePlayer )
	else
		--The newTag param was not entered, give an error message
		outputChatBox ( "/addtag - Incorrect syntax, Correct: /addtag <newtag>", thePlayer )
	end
end
addCommandHandler ( "addtag", addPlayerCustomTag )

function removePlayerCustomTag ( thePlayer, command )
	--We first need to check that they have already used /addtag, let's do that now
	local sOldNick = getElementData( thePlayer, "tempdata.originalnick" )
	if ( sOldNick ) then
		--Great, they have a tag added, let's reset them
		
		--First we will want to reset the element data back to its default (that being false)
		setElementData ( thePlayer, "tempdata.originalnick", false )
		
		--Now set the client name back
		setPlayerName( thePlayer, sOldNick )
		
		--Notify them
		outputChatBox ( "Your old nickname has been set", thePlayer )
	end
end
addCommandHandler ( "deltag", removePlayerCustomTag )
```

## Changelog

| Version | Description |
| --- | --- |

| 1.6.0-9.22815 | Added clientChangesPolicy argument |
| --- | --- |

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

- setElementData

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
