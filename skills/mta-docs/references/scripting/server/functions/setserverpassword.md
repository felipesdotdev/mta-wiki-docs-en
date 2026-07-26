---
doc_id: "mta-wiki:3444"
title: "SetServerPassword"
source_title: "SetServerPassword"
source_url: "https://wiki.multitheftauto.com/wiki/SetServerPassword"
revision_id: 66170
language: "en"
categories: ["Server_functions"]
---

# SetServerPassword

This function changes the password required to join the server to the given string.

## Syntax

```
bool setServerPassword ( string thePassword )
```

 

Lock icon indicating a password protected server.

### Required Arguments

- **thePassword:** The new server password you want. Pass *nil* or an empty string to remove the password.

### Returns

Returns *true* if the password was successfully changed or removed, *false* or *nil* otherwise.

## Example

This example adds two commands for you to use: setpassword and removepassword.

```
addCommandHandler( "setpassword", -- add a command handler for the command
   function( thePlayer, command, password )
      if #password < 3 then -- check if the password is shorter than 3 letters
         outputChatBox( "The password needs to be atleast 3 letters long!", thePlayer ) -- tell the player that password was too short
         return -- abort command
      end
      local success = setServerPassword( password ) -- check whether changing password worked
      if success then
         outputChatBox( "Server password change to: " .. password, thePlayer ) -- if it did, tell the player
      else
         outputChatBox( "Failed to change servers password.", thePlayer ) -- if it didn't, tell the player
      end
   end
)

addCommandHandler( "removepassword", -- add a command handler for the command
   function( thePlayer, command )
      local success = setServerPassword( nil ) -- check whether removing password worked
      if success then
         outputChatBox( "Server password removed successfully", thePlayer ) -- if it did, tell the player
      else
         outputChatBox( "Failed to remove servers password.", thePlayer ) -- if it didn't, tell the player
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

- setServerPassword

- [shutdown](mta://scripting/server/functions/shutdown.md)
