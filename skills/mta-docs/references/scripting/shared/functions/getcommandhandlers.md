---
doc_id: "mta-wiki:9143"
title: "GetCommandHandlers"
source_title: "GetCommandHandlers"
source_url: "https://wiki.multitheftauto.com/wiki/GetCommandHandlers"
revision_id: 61861
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.6", "Utility_templates"]
---

# GetCommandHandlers

This function is used to retrieve a list of all the registered command handlers of a given resource (or of all resources).
Function also added client-side.

## Syntax

```
table getCommandHandlers ( [ resource theResource ] )
```

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **theResource:** The resource from which you wish to retrieve all command handlers. Or leave it empty to retrieve command handlers of all resources.

### Returns

Returns a *table* containing all the commands of the given resource or a table with subtables containing the command and theResource pointer ( { "command", theResource } ). See examples below if you don't understand it.

## Example

This example add a command to output list of all commands in the chat.

```
addCommandHandler( "commands", 
   function(player)
      local commandsList = {} --table to store commands
		
      --store/sort commands in the table where key is resource and value is table with commands
      for _, subtable in pairs( getCommandHandlers() ) do
	 local commandName = subtable[1]
	 local theResource = subtable[2]
			
         if not commandsList[theResource] then
	    commandsList[theResource] = {}
	 end
			
	 table.insert( commandsList[theResource], commandName )
      end
		
      --output sorted information in the chat
      for theResource, commands in pairs( commandsList ) do
	  local resourceName = getResourceInfo( theResource, "name" ) or getResourceName( theResource ) --try to get full name, if no full name - use short name
	  outputChatBox( "== "..resourceName.. " ==", player, 0, 255, 0 )
			
	  --output list of commands
	  for _, command in pairs( commands ) do
	     outputChatBox( "/"..command, player, 255, 255, 255 )
	  end
      end
  end
)
```

This example add a command to output list of all commands for the resource in the chat. Syntax: /commands [resource-name]

```
addCommandHandler("commands", 
  function( player, _, resourceName)
     local theResource = (resourceName and getResourceFromName(resourceName)) or resource 
     outputChatBox( "* Commands from "..getResourceName(theResource).." resource", player, 0, 255, 0 )
		
     local commands = getCommandHandlers( theResource )
     for _, command in pairs( commands ) do
        outputChatBox( "/"..command, player, 255, 255, 255 )
     end
  end
)
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
