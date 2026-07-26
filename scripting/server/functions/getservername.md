---
doc_id: "mta-wiki:2770"
title: "GetServerName"
source_title: "GetServerName"
source_url: "https://wiki.multitheftauto.com/wiki/GetServerName"
revision_id: 49952
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:24.708129+00:00"
---

# GetServerName

This function retrieves the server's name.

## Syntax

```
string getServerName ( )
```

### Returns

A string containing the server's name.

## Example

This example creates a console command that outputs the server's name to the chatbox.

```
function outputServerName ( )
	outputChatBox ( getServerName( ) )
end

-- Add console command 'getServerName'
addCommandHandler ( "getServerName", outputServerName )
```

## See Also

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIpFromMasterServer](mta://scripting/server/functions/getserveripfrommasterserver.md)

- getServerName

- [getServerPassword](mta://scripting/server/functions/getserverpassword.md)

- [getServerPort](mta://scripting/server/functions/getserverport.md)

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)
