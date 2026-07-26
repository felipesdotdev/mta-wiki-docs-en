---
doc_id: "mta-wiki:1497"
title: "OutputConsole"
source_title: "OutputConsole"
source_url: "https://wiki.multitheftauto.com/wiki/OutputConsole"
revision_id: 64912
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# OutputConsole

This outputs the specified text string to the console window (accessed with F8 or ~ key). It can be specified as a message to certain player(s) or all players.

## Syntax

Click to collapse [-]
Client

```
bool outputConsole ( string text )
```

### Required Arguments

- **text:** The text string that you wish to send to the console window

Click to collapse [-]
Server

```
bool outputConsole ( string text, [ element visibleTo=getRootElement() ] )
```

### Required Arguments

- **text:** The text string that you wish to send to the console window

### Optional Arguments

- **visibleTo:** This specifies who the chat is visible to. Any players in this element will see the chat message. See [visibility](mta://reference/misc/visibility.md).

| [[{{{image}}}\|link=\|]] | Note: visibleTo can also be a Team object, in this case, the text will be visible to all the players of that team. |
| --- | --- |
|  |  |

## Remarks

The serverside function has a limitation of 1000 characters for the text parameter. Anything beyond 1000 characters is trimmed away. This limitation does not apply to the clientside version.

## Example

Click to collapse [-]
Server

This code creates two console commands. One, 'public', will post a message in the consoles of all players, and the other, 'private', will post a message in only the console of the player that executed the command.

```
function message(player,command)
	if command == "public" then
		outputConsole("Public console message")
	else
		outputConsole("Private console message",player)
	end
end
addCommandHandler("public",message)
addCommandHandler("private",message)
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
