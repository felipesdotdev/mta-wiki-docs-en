---
doc_id: "mta-wiki:4022"
title: "GetMTAVersion"
source_title: "GetMTAVersion"
source_url: "https://wiki.multitheftauto.com/wiki/GetMTAVersion"
revision_id: 44614
language: "en"
categories: ["Client_functions", "Deprecated"]
---

# GetMTAVersion

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getVersion instead. |  |

This function returns a string which tell you which MTA version player uses. From DP2.1 onwards.

## Syntax

```
string getMTAVersion( )
```

### Required Arguments

None

### Returns

A *string* - currently: "1.0 dp2.1"

## Example

```
function checkVersion( )
    if getMTAVersion( ) ~= "1.0 dp2.1" then
        outputChatBox( "Download the latest MTA:SA DM and come back!" )
    end
end
addEventHandler( "onClientResourceStart", getResourceRootElement(), checkVersion )
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
