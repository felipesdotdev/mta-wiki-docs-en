---
doc_id: "mta-wiki:3928"
title: "Shutdown"
source_title: "Shutdown"
source_url: "https://wiki.multitheftauto.com/wiki/Shutdown"
revision_id: 80041
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:50.785243+00:00"
---

# Shutdown

This function shuts down the server.

Make sure your server ACL setup has function.shutdown object protected.

## Syntax

```
bool shutdown ( [ string reason = "No reason specified", number exitCode = 0 ] )
```

### Optional Arguments

- **reason:** the reason why the server has been shutdown.

- **exitCode:** the server application exit code to be returned on shutdown.

### Returns

Returns *false* if it was not possible to shut down the server.

## Example

This command shuts down the server on request

```
addCommandHandler ( "shutdown", function ( player, command, reason )
  if ( hasObjectPermissionTo ( player, "function.shutdown" ) ) then
    shutdown ( reason or "" )
  end
end )
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

- shutdown
