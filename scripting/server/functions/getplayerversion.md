---
doc_id: "mta-wiki:5264"
title: "GetPlayerVersion"
source_title: "GetPlayerVersion"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerVersion"
revision_id: 81418
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:20.847431+00:00"
---

# GetPlayerVersion

| [[{{{image}}}\|link=\|]] | Note: You can also compare if a version is higher than another using the < or > operators. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Current MTA version: mta -> 1.6 netcode -> 474 number -> 352 sortable -> 1.6.0-9.22279.0 tag -> 1.6-release-22279 type -> Release |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Alternatively, you can use getVersion on the server or client to obtain more information. |
| --- | --- |
|  |  |

This function gets the client version of the specified [player](mta://reference/misc/player.md) as a **sortable string**. The string is always 15 characters long and is formatted as follows:

- 1 character representing the major version

- 1 dot character

- 1 character representing the minor version

- 1 dot character

- 1 character representing the maintenance version

- 1 dash character

- 1 character representing the build type

- 1 dot character

- 5 characters representing the build number

- 1 dot character

- 1 character representing the build revision

An example of a version string would be: 1.0.4-9.01746.0

Where the first three numbers represent the major/minor/maintenance version, i.e. 1.0.4  

The fourth number is 9, which means it's a release build, (Development and beta builds have lower numbers here)  

And the fifth and sixth numbers represent the build number.

## Syntax

```
string getPlayerVersion ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):getVersion(...)*

**Variable**: *.version*

### Required Arguments

- **thePlayer:** The [player](mta://reference/misc/player.md) whose client version you wish to get.

### Returns

Returns a string containing the client version, or false if the [player](mta://reference/misc/player.md) is invalid.

## Example

Click to collapse [-]
Server

This example adds a command that allows players to see their own client version.

```
function showMeMyVersion( playerSource )
    local version = getPlayerVersion ( playerSource )
    outputChatBox ( "Your client version is: " .. version, playerSource )
end

addCommandHandler ( "myversion", showMeMyVersion )
```

## See Also

- [getAlivePlayers](mta://scripting/server/functions/getaliveplayers.md)

- [getDeadPlayers](mta://scripting/server/functions/getdeadplayers.md)

- [getPlayerAnnounceValue](mta://scripting/server/functions/getplayerannouncevalue.md)

- [getPlayerCount](mta://scripting/server/functions/getplayercount.md)

- [getPlayerIdleTime](mta://scripting/server/functions/getplayeridletime.md)

- [getPlayerIP](mta://scripting/server/functions/getplayerip.md)

- getPlayerVersion

- [getRandomPlayer](mta://scripting/server/functions/getrandomplayer.md)

- [isPlayerMuted](mta://scripting/server/functions/isplayermuted.md)

- [redirectPlayer](mta://scripting/server/functions/redirectplayer.md)

- [resendPlayerACInfo](mta://scripting/server/functions/resendplayeracinfo.md)

- [resendPlayerModInfo](mta://scripting/server/functions/resendplayermodinfo.md)

- [setPlayerAnnounceValue](mta://scripting/server/functions/setplayerannouncevalue.md)

- [setPlayerMuted](mta://scripting/server/functions/setplayermuted.md)

- [setPlayerScriptDebugLevel](mta://scripting/server/functions/setplayerscriptdebuglevel.md)

- [setPlayerTeam](mta://scripting/server/functions/setplayerteam.md)

- [setPlayerName](mta://scripting/server/functions/setplayername.md)

- [setPlayerVoiceBroadcastTo](mta://scripting/server/functions/setplayervoicebroadcastto.md)

- [setPlayerVoiceIgnoreFrom](mta://scripting/server/functions/setplayervoiceignorefrom.md)

- [setPlayerWantedLevel](mta://scripting/server/functions/setplayerwantedlevel.md)

- [spawnPlayer](mta://scripting/server/functions/spawnplayer.md)

- [takePlayerScreenShot](mta://scripting/server/functions/takeplayerscreenshot.md)
  

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
