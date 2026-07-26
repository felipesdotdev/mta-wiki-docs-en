---
doc_id: "mta-wiki:1758"
title: "GivePlayerJetPack"
source_title: "GivePlayerJetPack"
source_url: "https://wiki.multitheftauto.com/wiki/GivePlayerJetPack"
revision_id: 81947
language: "en"
categories: ["Server_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:31.005064+00:00"
---

# GivePlayerJetPack

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setPedWearingJetpack instead. |  |

This function is used to give a player a jetpack.

This function is not guaranteed to succeed. There are some cases where the jetpack cannot be given, for example:

- If the player is in a vehicle

- If the player is falling

- Probably others too.

As such, you should either expect it to fail sometimes, or repeatedly try to give a jetpack every second or so until [doesPlayerHaveJetPack](mta://scripting/shared/functions/doesplayerhavejetpack.md) returns true. Alternatively, you can force the player into a 'safe' position (e.g. standing on the ground) before giving the jetpack, or user a pickup to handle it.

## Syntax

```
bool givePlayerJetPack ( player thePlayer )
```

### Required Arguments

- **thePlayer:** The [player](mta://reference/misc/player.md) you want to give a jetpack to.

### Returns

Returns *true* if a jetpack was successfully given to the player, *false* if it could not be given.

## Example

This examples adds a "jetpack" console command, which gives or removes a jetpack from the player.

```
[lua]
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
