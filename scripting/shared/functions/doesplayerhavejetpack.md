---
doc_id: "mta-wiki:1757"
title: "DoesPlayerHaveJetPack"
source_title: "DoesPlayerHaveJetPack"
source_url: "https://wiki.multitheftauto.com/wiki/DoesPlayerHaveJetPack"
revision_id: 44576
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:14:42.971395+00:00"
---

# DoesPlayerHaveJetPack

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use doesPedHaveJetPack instead. |  |

This function is used to determine whether or not a player has a jetpack. Jetpacks can be given to players using the [givePlayerJetPack](mta://scripting/server/functions/giveplayerjetpack.md) function and removed with the [removePlayerJetPack](mta://scripting/server/functions/removeplayerjetpack.md) function.

## Syntax

```
bool doesPlayerHaveJetPack ( player thePlayer )
```

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) you are checking.

### Returns

Returns *true* if a player has a jetpack, *false* otherwise.

## Example

Click to collapse [-]
Server

**Example 1:** This examples adds a "jetpack" console command, which gives or removes a jetpack from the player.

```
-- Checks whether or not the player has a jetpack, and gives or removes it from the player
function consoleJetPack ( thePlayer, commandName )
   if ( not doesPlayerHaveJetPack ( thePlayer ) ) then            -- if the player doesn't have a jetpack
      local status = givePlayerJetPack ( thePlayer )              -- give him one
      if ( not status ) then
         outputConsole ( "Failed to give jetpack.", thePlayer )   -- tell him if it failed
      end
   else
      local status = removePlayerJetPack ( thePlayer )            -- remove his jetpack
      if ( not status ) then
         outputConsole ( "Failed to remove jetpack.", thePlayer ) -- tell him if it failed
      end
   end
end

-- add the function above to handle the "jetpack" command
addCommandHandler ( "jetpack", consoleJetPack )
```

Click to collapse [-]
Server and client

**Example 2:** This example provides a check to see if players have a jetpack when they enter a particular marker.

```
function onWarpMarkerHit(thePlayer, matchingDimension)
   -- check whether the player has a jetpack and store it in the hasJetPack flag
   local hasJetPack = doesPlayerHaveJetPack(thePlayer)
   if (not hasJetPack) then
      -- warp the player to their destination
      setElementPosition(thePlayer, 1337, 1337, 50)
   else
      -- tell the player to remove their jetpack
      outputChatBox("You must remove your jetpack to use this marker!", thePlayer)
   end
end

-- create a marker and add the function above to its onMarkerHit event
addEventHandler("onMarkerHit", createMarker(3180, 200, 27), onWarpMarkerHit)
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
