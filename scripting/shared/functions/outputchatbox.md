---
doc_id: "mta-wiki:1473"
title: "OutputChatBox"
source_title: "OutputChatBox"
source_url: "https://wiki.multitheftauto.com/wiki/OutputChatBox"
revision_id: 80829
language: "en"
categories: ["Utility_templates", "Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:27.119919+00:00"
---

# OutputChatBox

| [[{{{image}}}\|link=\|]] | Note: Avoid outputting text to the chatbox that isn't actually chat, as this can be annoying for players. Output information and status messages to the HUD. |
| --- | --- |
|  |  |

This outputs the specified text string to the chatbox. It can be specified as a message to certain player(s) or all players.

It can optionally allow you to embed color changes into the string by setting the colorCoded boolean to true. This allows:

```
outputChatBox ( "#FF0000Hello #00FF00World", root, 255, 255, 255, true )
```

This will display as: **Hello World**

## Syntax

Click to collapse [-]
Server

```
bool outputChatBox ( string text [, table/element visibleTo = root, int r = 231, int g = 217, int b = 176, bool colorCoded = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):outputChat(...)*

## Required Arguments

- **text:** The text string that you wish to send to the chat window. If more than 256 characters it will not be showed in chat.

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **visibleTo:** This specifies who the chat is visible to. Any players in this element will see the chat message. See [visibility](mta://reference/misc/visibility.md).

ADDED/UPDATED IN VERSION 1.5.7-9.20391 :

- **visibleTo:** Can also be a table of players or team.

- **r:** The amount of red in the color of the text. Default value is 231.

- **g:** The amount of green in the color of the text. Default value is 217.

- **b:** The amount of blue in the color of the text. Default value is 176.

- **colorCoded:** A boolean value determining whether or not '#RRGGBB' tags should be used.

Note: The #RRGGBB format must contain capital letters a-f is not acceptable but A-F is. Default RGB values in this format are: '#E7D9B0'.

Click to collapse [-]
Client

```
bool outputChatBox ( string text [, int r = 231, int g = 217, int b = 176, bool colorCoded = false ] )
```

## Required Arguments

- **text:** The text string that you wish to send to the chat window. If more than 256 characters it will not be showed in chat.

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **r:** The amount of red in the color of the text. Default value is 231.

- **g:** The amount of green in the color of the text. Default value is 217.

- **b:** The amount of blue in the color of the text. Default value is 176.

- **colorCoded:** A boolean value determining whether or not '#RRGGBB' tags should be used.

Note: The #RRGGBB format must contain capital letters a-f is not acceptable but A-F is. Default RGB values in this format are: '#E7D9B0'.

## Returns

Returns *true* if the message was displayed successfully. Returns *false* if invalid arguments are specified.

## Example

Click to collapse [-]
Server

**Example 1:** This example displays a chat message to all users.

```
x = 5
y = 10  
-- Displays the message
outputChatBox ( "I have " .. x .. " apples and " .. y .. " oranges." )
```

**Example 2:** This example outputs a simple colour coded message, "Red White", where the 'White' is in white colour, and 'Red' is in a red colour.

```
outputChatBox ( "Red #FFFFFFWhite", root, 255, 0, 0, true )
```

**Example 3:** This example allows for coloured chat, according to a player's nametag.  This makes use of colour coded outputs.

```
function colouredChat ( message, theType )
    if theType == 0 then --if its normal chat (not /me or teamchat) then
        cancelEvent() --prevent MTA from outputting chat
        local message = string.gsub(message, "#%x%x%x%x%x%x", "") --remove any hex tags in a player's chat to prevent custom colours by using lua's string.gsub
        local r, g, b = getPlayerNametagColor ( source ) --get the player's nametag colour
        local chatterName = getPlayerName ( source ) --get his name
        --output a message with the name as his nametag colour, and the rest in white.
        outputChatBox ( chatterName..":#FFFFFF "..message, root, r, g, b, true )
    end
end
addEventHandler("onPlayerChat", root, colouredChat)
```

**Example 4:** This example displays a chat message to a single user called *someguy*.

```
-- Find the player element for the player called 'someguy'
local myPlayer = getPlayerFromName ( "someguy" )
-- If a player was found called 'someguy' then...
if ( myPlayer ~= false ) then
    x = 5
    y = 10
    -- Display the message
    outputChatBox ( "I have " .. x .. " apples and " .. y .. " oranges.", myPlayer )
end
```

**Example 5:** These two functions can speed up typing, and display a message when a player Joins.

```
local msg_red,msg_green,msg_blue = 255,255,0

function servertalkprivate(message, sendto)
        --Talk to one client only
	outputChatBox(tostring(message), sendto, msg_red, msg_green, msg_blue, true)
end

function servertalk(message)
    --Talk to everyone
    servertalkprivate(message, root)
end

function onJoin()
    servertalkprivate("Welcome to My Server", source)
end

addEventHandler("onPlayerJoin", root, onJoin)
```

**Example 6:** This can be used to display a message when the player joins and sets its armor to 100.

```
function onJoin()
    setPedArmor(source, 100)
    outputChatBox("Welcome ".. getPlayerName(source) .." To The Server", source, 0, 154, 255)
end
addEventHandler("onPlayerJoin", root, onJoin)
```

**Example 7:** This code will output an message to nearby players.

```
function displayLocalMessage(player, cmd)
    if player then -- Check if command was triggered by player
        local x, y, z = getElementPosition(player) -- Get player position
        local nearbyPlayers = getElementsWithinRange(x, y, z, 10, "player") -- Retrieve nearby players in range of 10

        outputChatBox("Local message :)!", nearbyPlayers) -- Output our message
    end
end
addCommandHandler("localmessage", displayLocalMessage)
```

**Example 8:** This example displays your nickname and the amount of money.

```
function player_info(player, cmd)
    outputChatBox("Name: #FFFFFF"..getPlayerName(player), player, 255, 0, 0, true)
    outputChatBox("Money: #FFFFFF"..getPlayerMoney(player).."#00FF00$", player, 255, 0, 0, true)
end
addCommandHandler("info", player_info)
```

## See Also

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIpFromMasterServer](mta://scripting/server/functions/getserveripfrommasterserver.md)

- [getServerName](mta://scripting/server/functions/getservername.md)

- [getServerPassword](mta://scripting/server/functions/getserverpassword.md)

- [getServerPort](mta://scripting/server/functions/getserverport.md)

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)
