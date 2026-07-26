---
doc_id: "mta-wiki:1493"
title: "AddCommandHandler"
source_title: "AddCommandHandler"
source_url: "https://wiki.multitheftauto.com/wiki/AddCommandHandler"
revision_id: 78787
language: "en"
categories: ["Utility_templates", "Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:10:20.100162+00:00"
---

# AddCommandHandler

| [[{{{image}}}\|link=\|]] | Important Note: Do NOT use the same name for your handler function as the command name, as this can lead to confusion if multiple handler functions are used. Use a name that describes your handler's purpose more specifically. |
| --- | --- |
|  |  |

This function will attach a scripting function (handler) to a console command, so that whenever a player or administrator uses the command the function is called.

Multiple command handlers can be attached to a single command, and they will be called in the order that the handlers were attached. Equally, multiple commands can be handled by a single function, and the *commandName* parameter used to decide the course of action.

For users, a command is in the format:

*commandName* *argument1* *argument2*

This can be triggered from the player's console or directly from the chat box by prefixing the message with a forward slash (*/*). For server side handlers, the server admin is also able to trigger these directly from the server's console in the same way as they are triggered from a player's console.

| [[{{{image}}}\|link=\|]] | Note: You can't use "check", "list", "test" and "help" as a command name. |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
bool addCommandHandler ( string commandName, function handlerFunction [, bool restricted = false, bool caseSensitive = true ] )
```

### Required Arguments

- **commandName:** This is the name of the command you wish to attach a handler to. This is what must be typed into the console to trigger the function.

- **handlerFunction:** This is the function that you want the command to trigger, which has to be defined before you add the handler. This function can take two parameters, playerSource and commandName, followed by as many parameters as you expect after your command (see below). These are all optional.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **restricted:** Specify whether or not this command should be restricted by default. Use this on commands that should be inaccessible to everyone as default except special users specified in the ACL (Access Control List). This is to make sure admin commands such as ie. 'punish' won't be available to everyone if a server administrator forgets masking it in ACL. Make sure to add the command to your ACL under the proper group for it to be usefull (i.e <right name="command.killEveryone" access="true"></right>). This argument defaults to false if nothing is specified.

- **caseSensitive:** Specifies if the command handler will ignore the case for this command name.

Click to collapse [-]
Client

```
bool addCommandHandler ( string commandName, function handlerFunction [, bool caseSensitive = true ] )
```

### Required Arguments

- **commandName:** This is the name of the command you wish to attach a handler to. This is what must be typed into the console to trigger the function.

- **handlerFunction:** This is the function that you want the command to trigger, which has to be defined before you add the handler. This function can take commandName parameter, followed by as many parameters as you expect after your command (see below). These are all optional.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **caseSensitive:** Specifies if the command handler will ignore the case for this command name.

#### Handler function parameters

These are the parameters for the handler function that is called when the command is used.

Click to collapse [-]
Server

```
player playerSource, string commandName [, string arg1, string arg2, ... ]
```

- **playerSource:** The player who triggered the command or the [server console](mta://reference/misc/element-console.md). If not triggered by a player (e.g. by admin) or server console, this will be *false*.

- **commandName:** The name of the command triggered. This is useful if multiple commands go through one function.

- **arg1, arg2, ...:** Each word after command name in the original command is passed here in a seperate variable. If there is no value for an argument, its variable will contain [nil](mta://reference/misc/nil.md). You can deal with a variable number of arguments using the vararg expression, as shown in **Server Example 2** below.

Click to collapse [-]
Client

```
string commandName [, string arg1, string arg2, ... ]
```

- **commandName:** The name of the command triggered. This is useful if multiple commands go through one function.

- **arg1, arg2, ...:** Each word after command name in the original command is passed here in a seperate variable. If there is no value for an argument, its variable will contain [nil](mta://reference/misc/nil.md). You can deal with a variable number of arguments using the vararg expression, as shown in **Server Example 2** below.

### Returns

Returns *true* if the command handler was added successfully, *false* otherwise.

## Examples

Click to collapse [-]
Server

**Example 1:** This example defines a command handler for the command *createmarker*. This will create a red marker at the position of the player player who uses it.

```
-- Define our function that will handle this command
function consoleCreateMarker ( playerSource, commandName )
	-- If a player triggered it (rather than the admin) then
	if ( playerSource ) then
		-- Get that player's position
		local x, y, z = getElementPosition ( playerSource )
		-- Create a size 2, red checkpoint marker at their position
		createMarker ( x, y, z, "checkpoint", 2, 255, 0, 0, 255 )
		-- Output it in his chat box
		outputChatBox ( "You got a red marker", playerSource )
	end
end
-- Attach the 'consoleCreateMarker' function to the "createmarker" command
addCommandHandler ( "createmarker", consoleCreateMarker )
```

Click to expand [+]
Server

**Example 2:** This example makes use of Lua's vararg expression to implement a *check_parameters* command to count the number of parameters passed, merge them all into a single string and output it. This is also shows you how you can use table.concat to merge all the passed arguments. This is particularly useful when you want to read in a sentence of text passed from the user.

```
-- Define our function that will handle this command (which can accept a variable number of arguments after commandName)
function consoleCheckParameters ( playerSource, commandName, ... )
	-- If a player, not an admin, triggered it,
	if playerSource then
		local arg = {...}
		-- Get the number of arguments in the arg table (arg table is the same as: {...})
		local parameterCount = #arg
		-- Output it to the player's chatbox
		outputChatBox ( "Number of parameters: " .. parameterCount, playerSource )
		-- Join them together in a single comma-separated string
		local stringWithAllParameters = table.concat( arg, ", " )
		-- Output this parameter list to the player's chatbox
		outputChatBox ( "Parameters passed: " .. stringWithAllParameters, playerSource )
	end
end
-- Attach the 'consoleCheckParameters' function to the "check_parameters" command
addCommandHandler ( "check_parameters", consoleCheckParameters )
```

Click to expand [+]
Server

**Example 3:** This example shows using a single function to handle multiple command handlers. This isn't advised for general usage, as it makes code harder to understand, but where multiple command handlers share some logic, it can be a useful way of reducing duplicated code. Generally, it would be preferable to put this shared logic in a separate function instead, as this gives you more control over the flow.

```
-- make the function
function moneyCmd(player, commandName, amount)
    if getElementData(player, "canUseMoneyFunctions") then -- the shared logic
        if commandName == "givemoney" then
            amount  = tonumber(amount)
            if amount then
                givePlayerMoney(player, amount)
            else
                outputChatBox("[usage] /givemoney [amount]", player)
            end
        else if commandName == "takemoney" then
            amount = tonumber(amount)
            if amount then
                takePlayerMoney(player, amount)
            else
                outputChatBox("[usage] /takemoney [amount]", player)
            end
        end
    else
        outputChatBox("You aren't able to use this command", player)
    end
end
 
addCommandHandler("givemoney", moneyCmd);
addCommandHandler("takemoney", moneyCmd);
```

Click to expand [+]
Client

**Example 1:** This example warps the local player to a random nearby location (useful for when a player gets stuck somewhere).

```
function escapeMe ( commandName )
	local x, y, z = getElementPosition ( localPlayer ) --Get player's position
	setElementPosition ( localPlayer, x+(math.random(-10,10)), y+(math.random(-10,10)), z+(math.random(1,15)) ) --Move a player randomly to a nearby location. X is current x + a number between -10, 10 and so on.
end    
addCommandHandler ( "escape", escapeMe ) --When player types "/escape" in chatbox or "escape" in console
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
