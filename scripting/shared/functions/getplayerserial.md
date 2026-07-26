---
doc_id: "mta-wiki:3667"
title: "GetPlayerSerial"
source_title: "GetPlayerSerial"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerSerial"
revision_id: 82127
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:20.435585+00:00"
---

# GetPlayerSerial

This function returns the [serial](mta://reference/misc/serial.md) for a specified [player](mta://reference/misc/player.md).

| [[{{{image}}}\|link=\|]] | Note: It's possible for a player to fake the value returned from getPlayerSerial when used on the clientside. For this reason you should only trust the value returned by this function when used serverside. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Important Note: You should use this function in conjunction with account system (e.g: login & password ) - especially for critical things, because serials could be invalid (as in, non-unique or faked ). See: Script security . |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
string getPlayerSerial ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):getSerial(...)*

**Variable**: *.serial*

### Required Arguments

- **thePlayer:** A [player](mta://reference/misc/player.md) object referencing the specified player.

## Returns

Returns the serial as a *string* if it was found, *false* otherwise.

## Syntax

Click to collapse [-]
Client

```
string getPlayerSerial ( )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[localPlayer](mta://scripting/client/functions/localplayer.md):getSerial(...)*

### Required Arguments

None

## Returns

Returns the serial as a *string* if it was found, *false* otherwise.

## Examples

Click to collapse [-]
Server

This example creates a command with which player can check their own serial.

```
function checkMySerial( thePlayer, command )
    local theSerial = getPlayerSerial( thePlayer )
    if theSerial then
        outputChatBox( "Your serial is: " .. theSerial, thePlayer )
    else
        outputChatBox( "Sorry, you have no serial. =(", thePlayer )
    end
end
addCommandHandler( "myserial", checkMySerial )
```

This example adds a command to ban a player's serial.

```
local function banSerialCommand ( source, command, playerName, reason )
   if playerName then
      local player, serial = getPlayerFromName ( playerName ), getPlayerSerial ( playerName )
      if player then
         addBan ( serial, source, reason )
      end
   end
end
addCommandHandler ( "banplayerserial", banSerialCommand )
```

This example only allows clients with a certain serial to log in into an account.

```
local allowedAccountSerials = 
{
    -- List of allowed serials to log in into an account. Format:
    -- [ Account name ] = { Allowed serial array }
    [ "3ash8" ] = { "9C9F3B55D9D7BB7135FF274D3BF444E4" },
    [ "test5" ] = { "1D6F76CF8D7193792D13789849498452" },
}
 
addEventHandler("onPlayerLogin", root,
    function(_, account)
        -- Get the player serial and the allowed serial list for that account
        -- (If no serial is allowed for the account, do not allow the player to log in as a safety measure)
        local playerSerial, allowedSerials = getPlayerSerial(source), allowedAccountSerials[getAccountName(account)] or {}
        -- Check whether the client has an allowed serial or not
        for i = 1, #allowedSerials do
            if allowedSerials[i] == playerSerial then
                -- The serial is allowed. Proceed with the normal log in proccess
                return
            end
        end
        -- If we reach this point the serial is not allowed. Do not let the player log in
        cancelEvent(true, "Client serial not allowed to log in into the account")
    end
)
```

## See Also

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- getPlayerSerial

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
