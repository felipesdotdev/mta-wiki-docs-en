---
doc_id: "mta-wiki:1689"
title: "ExecuteCommandHandler"
source_title: "ExecuteCommandHandler"
source_url: "https://wiki.multitheftauto.com/wiki/ExecuteCommandHandler"
revision_id: 62787
language: "en"
categories: ["Utility_templates", "Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:14:59.820499+00:00"
---

# ExecuteCommandHandler

This function will call all the attached functions of an existing console command, for a specified player.

| [[{{{image}}}\|link=\|]] | Note: You can only execute commands created with addCommandHandler. You cannot execute MTA harcoded commands due to security reasons. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Serverside commands can only be executed by the server. The same applies to the client side |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
bool executeCommandHandler ( string commandName, player thePlayer, [ string args ] )
```

## Required Arguments

- **commandName:** The name of the command you wish to execute. This is what must be typed into the console to trigger the function.

- **thePlayer:** The player that will be presented as executer of the command to the handler function(s) of the command.

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **args:** Additional parameters that will be passed to the handler function(s) of the command that is called, separated by spaces.

Click to collapse [-]
Client

```
bool executeCommandHandler ( string commandName, [ string args ] )
```

## Required Arguments

- **commandName:** The name of the command you wish to execute. This is what must be typed into the console to trigger the function.

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **args:** Additional parameters that will be passed to the handler function(s) of the command that is called, separated by spaces.

### Returns

Returns *true* if the command handler was called successfully, *false* otherwise.

## Example

Click to collapse [-]
Server

This example defines a command handler for the command *createmarker* (which creates a red marker at the caller's position). It then creates a second command handler *createmarker2* which will call the first one.

```
-- Define the function that will handle the 'createmarker' command
function consoleCreateMarker ( playerSource, commandName )
	-- If a player triggered it (rather than the admin) then
	if ( playerSource ) then
		-- Get that player's position
		x, y, z = getElementPosition ( playerSource )
		-- Create a marker at their position
		createMarker ( x, y, z, 0, "checkpoint", 255, 0, 0, 255 )
		-- Output it in the chat box
		outputChatBox ( "You got a red marker", playerSource )
	end
end
-- Add the function as a handler for the command
addCommandHandler ( "createmarker", consoleCreateMarker )

-- Define a second console command that will just call the first.
-- First define the function
function consoleCreateMarker2 ( playerSource, commandName )
	-- re-route back to the original
	executeCommandHandler ( "createmarker", playerSource )
end
-- Then add it as a handler for the new console command
addCommandHandler ( "createmarker2", consoleCreateMarker2 )
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
