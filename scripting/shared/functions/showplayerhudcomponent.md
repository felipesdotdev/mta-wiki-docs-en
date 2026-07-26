---
doc_id: "mta-wiki:1799"
title: "ShowPlayerHudComponent"
source_title: "ShowPlayerHudComponent"
source_url: "https://wiki.multitheftauto.com/wiki/ShowPlayerHudComponent"
revision_id: 67717
language: "en"
categories: ["Changes_in_1.1", "Server_functions", "Client_functions", "Deprecated", "Changes_in_1.0"]
generated_at: "2026-07-26T16:16:50.737855+00:00"
---

# ShowPlayerHudComponent

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setPlayerHudComponentVisible instead. |  |

This function will show or hide a part of the player's HUD.

## Syntax

Click to collapse [-]
Server

```
bool showPlayerHudComponent ( player thePlayer, string component, bool show )
```

### Required Arguments

- **thePlayer:** The player element for which you wish to show/hide a HUD component

- **component:** The component you wish to show or hide. Valid values are:

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

- **all:** All of the above at the same time

- **show:** Specify if the component should be shown (*true*) or hidden (*false*)

Click to collapse [-]
Client

```
bool showPlayerHudComponent ( string component, bool show )
```

### Required Arguments

- **component:** The component you wish to show or hide. Valid values are:

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

- **all:** All of the above at the same time

- **show:** Specify if the component should be shown (*true*) or hidden (*false*)

### Returns

Returns *true* if the component was shown or hidden succesfully, *false* if an invalid argument was specified.

## Example

Click to collapse [-]
Server

This example hides the ammo and weapon displays for players when they join.

```
function hudChanger ()
    showPlayerHudComponent ( source, "ammo", false )    -- Hide the ammo displays for the newly joined player
    showPlayerHudComponent ( source, "weapon", false )  -- Hide the weapon displays for the newly joined player
end
-- Make our hudChanger function called when the player joins
addEventHandler ( "onPlayerJoin", root, hudChanger )
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
