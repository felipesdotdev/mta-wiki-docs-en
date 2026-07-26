---
doc_id: "mta-wiki:2602"
title: "GetPlayerTargetEnd"
source_title: "GetPlayerTargetEnd"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerTargetEnd"
revision_id: 56781
language: "en"
categories: ["Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:20.572350+00:00"
---

# GetPlayerTargetEnd

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedTargetEnd instead. |  |

This function allows retrieval of the position where a players target range ends, when he is aiming with a weapon.

## Syntax

```
float, float, float getPlayerTargetEnd ( player targetingPlayer )
```

### Required Arguments

- **targetingPlayer:** The player who is targeting whose target end you wish to retrieve

### Returns

Returns three floats, *x*,*y*,*z*, representing the position where the player's target ends according to his range, or false if it was unsuccessful.

## Example

```
addEventHandler("onClientPlayerTarget", localPlayer,
    function()
        local endPosition = Vector3(getPlayerTargetEnd(source))
        outputChatBox("your target ends at point (" .. endPosition.x .. ", " .. endPosition.y .. ", " .. endPosition.z .. ")")
    end
)
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
