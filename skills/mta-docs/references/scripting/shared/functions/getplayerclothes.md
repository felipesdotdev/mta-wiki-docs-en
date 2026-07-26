---
doc_id: "mta-wiki:1733"
title: "GetPlayerClothes"
source_title: "GetPlayerClothes"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerClothes"
revision_id: 44560
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
---

# GetPlayerClothes

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedClothes instead. |  |

This function is used to get the current clothes texture and model of a certain type on a [player](https://wiki.multitheftauto.com/index.php?search=player).

## Syntax

```
string string getPlayerClothes ( player thePlayer, int clothesType )
```

### Required Arguments

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) whose clothes you want to retrieve.

- **clothesType:** The type/slot of clothing you want to get.

Clothing Types

- **0:** SHIRT

- **1:** HEAD

- **2:** TROUSERS

- **3:** SHOES

- **4:** TATTOOS_LEFT_UPPER_ARM

- **5:** TATTOOS_LEFT_LOWER_ARM

- **6:** TATTOOS_RIGHT_UPPER_ARM

- **7:** TATTOOS_RIGHT_LOWER_ARM

- **8:** TATTOOS_BACK

- **9:** TATTOOS_LEFT_CHEST

- **10:** TATTOOS_RIGHT_CHEST

- **11:** TATTOOS_STOMACH

- **12:** TATTOOS_LOWER_BACK

- **13:** NECKLACE

- **14:** WATCH

- **15:** GLASSES

- **16:** HAT

- **17:** EXTRA

### Returns

This function returns 2 *strings*, the clothes texture and model. The first return value will be *false* if this player's clothes type is empty or an invalid player was specified.

## Example

This example prints the model and texture of the current clothing on the player who calls the 'clothes' command. For example: 'clothes 3' for the shoes.

```
function getClothes ( source, key, clothesType )
    local texture, model = getPlayerClothes ( source, clothesType )
    if ( texture and model ) then
        outputChatBox ( getClientName(source) .. " is wearing " .. texture .. " " .. model ..
                        " on his " .. getClothesTypeName(clothesType), source )
    else
        outputChatBox ( "Invalid input.", source )
    end
end
addCommandHandler ( "clothes", getClothes )
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
