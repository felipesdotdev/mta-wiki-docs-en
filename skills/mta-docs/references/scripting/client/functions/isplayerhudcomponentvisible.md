---
doc_id: "mta-wiki:6815"
title: "IsPlayerHudComponentVisible"
source_title: "IsPlayerHudComponentVisible"
source_url: "https://wiki.multitheftauto.com/wiki/IsPlayerHudComponentVisible"
revision_id: 81150
language: "en"
categories: ["Client_functions", "Changes_in_1.1"]
---

# IsPlayerHudComponentVisible

This function can be used to check whether an hud component is visable or not.

## Syntax

```
bool isPlayerHudComponentVisible( string component )
```

### Required Arguments

- **component:** The component you wish to check. Valid values are:

- **ammo:** The display showing how much ammo the player has in their weapon

- **area_name:** The text that appears containing the name of the area a player has entered

- **armour:** The display showing the player's armor

- **breath:** The display showing the player's breath

- **clock:** The display showing the in-game time

- **health:** The display showing the player's health

- **money:** The display showing how much money the player has

- **radar:** The bottom-left corner miniradar

- **vehicle_name:** The text that appears containing the player's vehicle name when the player enters a vehicle

- **weapon:** The display showing the player's weapon

- **radio:** The display showing the radio label

- **wanted:** The display showing the player's wanted level

- **crosshair:** The weapon crosshair and sniper scope

### Returns

Returns *true* if the component is visable, *false* if not.

## Example

```
addEventHandler("onClientResourceStart",resourceRoot,function()
	local components = {"ammo","area_name","armour","breath","clock","health","money",
		"radar","vehicle_name","weapon","radio","wanted","crosshair"
	} --Table filled with all the available components to check
	for _,component in ipairs(components)do
		if isPlayerHudComponentVisible(component)then --check if the component is visible
			outputChatBox("Hud Component: "..component.." is visible!") --if it is then tell the client that
		else
			outputChatBox("Hud Component: "..component.." is not visible!") --if it is not then tell the client that it isn't
		end
	end
end)
```

## See Also

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
