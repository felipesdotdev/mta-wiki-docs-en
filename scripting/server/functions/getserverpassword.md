---
doc_id: "mta-wiki:3445"
title: "GetServerPassword"
source_title: "GetServerPassword"
source_url: "https://wiki.multitheftauto.com/wiki/GetServerPassword"
revision_id: 43307
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:24.715957+00:00"
---

# GetServerPassword

This function returns the current password required to join the server.

## Syntax

```
string getServerPassword ()
```

### Returns

Returns the current server password as a string if it has a password, if not it returns *nil*.

## Example

This example prints the serverpassword to the player

```
function viewPassword ( thePlayer, command )
  -- Put the password in a var
  local password = getServerPassword ()

  -- Check if the server has a password
  -- If the server has an password, echo it
  if password then
    outputChatBox ( "The server password is " .. password, thePlayer )
  
  -- Else print that there isnt any password
  else
    outputChatBox ( "The server doesn't have any password set", thePlayer )
  end
end

-- Add console command 'viewpassword'
addCommandHandler ( "viewpassword", viewPassword )
```

## See Also

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIpFromMasterServer](mta://scripting/server/functions/getserveripfrommasterserver.md)

- [getServerName](mta://scripting/server/functions/getservername.md)

- getServerPassword

- [getServerPort](mta://scripting/server/functions/getserverport.md)

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)
