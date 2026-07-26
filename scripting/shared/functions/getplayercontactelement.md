---
doc_id: "mta-wiki:2778"
title: "GetPlayerContactElement"
source_title: "GetPlayerContactElement"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerContactElement"
revision_id: 44600
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:19.233919+00:00"
---

# GetPlayerContactElement

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedContactElement instead. |  |

This function detects the element a player is standing on. This can be a vehicle or an object.  Note that the server is unable to retrieve contact elements that are created clientside.

## Syntax

```
element getPlayerContactElement ( player thePlayer )
```

### Required Arguments

- **thePlayer:** The [player](mta://reference/misc/player.md) you want to get the [element](mta://reference/misc/element.md) he is touching from.

### Returns

Returns an [object](mta://reference/misc/object.md) or a [vehicle](mta://reference/misc/vehicle.md) if the player is standing on one, *false* if he is touching none or is a invalid player.

## Example

This clientside function outputs the name of the vehicle the specified player is standing on, or a message saying he isn't on one.

```
function outputContactVehicleMessage ( thePlayer )
  local elementStandingOn = getPlayerContactElement( thePlayer )
  if getElementType( elementStandingOn ) == "vehicle" then
    local vehicleName = getVehicleName( elementStandingOn )
    outputChatBox( "The player is standing on a " .. vehicleName .. "." )
  else
    outputChatBox( "The player isn't standing on any vehicle." )
  end
end
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
