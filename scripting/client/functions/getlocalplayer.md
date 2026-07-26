---
doc_id: "mta-wiki:2499"
title: "GetLocalPlayer"
source_title: "GetLocalPlayer"
source_url: "https://wiki.multitheftauto.com/wiki/GetLocalPlayer"
revision_id: 79025
language: "en"
categories: ["Client_functions", "Changes_in_1.1"]
generated_at: "2026-07-26T16:15:15.131848+00:00"
---

# GetLocalPlayer

This function gets the player element of the client running the current script.

You should use predefined variable **localPlayer** instead of typing getLocalPlayer() for better readability.

## Syntax

```
player getLocalPlayer ( )
```

### Returns

Returns the local [player](mta://reference/misc/player.md) element.

## Example

**Example 1:** This client side function outputs the player's current location to the console.

```
function outputLocalPlayerPosition()
	-- get the local player's position
	local px, py, pz = getElementPosition(localPlayer)
	-- output it to the console
	outputConsole("Your location: "..px.." "..py .." "..pz)
end
```

**Example 2:** This client side script makes the local player's camera flash red after being hit.

```
function flashRed()
	-- fade out the local player's camera to red during a second
	fadeCamera(false, 1.0, 255, 0, 0)
	-- set a 500 ms (0.5 sec) timer to fade it back in before it has completely faded out
	setTimer(fadeCamera, 500, 1, true, 1.0)
end
-- we attach our 'flashRed' function to be a handler of "onClientPlayerDamage" when its source (that is, the hit player) is the local player
addEventHandler("onClientPlayerDamage", localPlayer, flashRed)
```

## See Also

- getLocalPlayer

- [getPlayerMapBoundingBox](mta://scripting/client/functions/getplayermapboundingbox.md)

- [getPlayerMapOpacity](mta://scripting/client/functions/getplayermapopacity.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [getPlayerHudComponentProperty](mta://scripting/client/functions/getplayerhudcomponentproperty.md)

- [isPlayerMapVisible](mta://scripting/client/functions/isplayermapvisible.md)

- [isPlayerHudComponentVisible](mta://scripting/client/functions/isplayerhudcomponentvisible.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22751](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22751):

- [isPlayerCrosshairVisible](mta://scripting/client/functions/isplayercrosshairvisible.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [resetPlayerHudComponentProperty](mta://scripting/client/functions/resetplayerhudcomponentproperty.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [setPlayerHudComponentProperty](mta://scripting/client/functions/setplayerhudcomponentproperty.md)

- **Shared**

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- [forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)

- [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md)

- [getPlayerFromName](mta://scripting/shared/functions/getplayerfromname.md)

- [getPlayerMoney](mta://scripting/shared/functions/getplayermoney.md)

- [getPlayerName](mta://scripting/shared/functions/getplayername.md)

- [getPlayerNametagColor](mta://scripting/shared/functions/getplayernametagcolor.md)

- [getPlayerNametagText](mta://scripting/shared/functions/getplayernametagtext.md)

- [getPlayerPing](mta://scripting/shared/functions/getplayerping.md)

- [getPlayerWantedLevel](mta://scripting/shared/functions/getplayerwantedlevel.md)

- [givePlayerMoney](mta://scripting/shared/functions/giveplayermoney.md)

- [isPlayerMapForced](mta://scripting/shared/functions/isplayermapforced.md)

- [isPlayerNametagShowing](mta://scripting/shared/functions/isplayernametagshowing.md)

- [setPlayerHudComponentVisible](mta://scripting/shared/functions/setplayerhudcomponentvisible.md)

- [setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md)

- [setPlayerNametagColor](mta://scripting/shared/functions/setplayernametagcolor.md)

- [setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md)

- [setPlayerNametagText](mta://scripting/shared/functions/setplayernametagtext.md)

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)
