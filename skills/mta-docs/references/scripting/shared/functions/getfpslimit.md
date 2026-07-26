---
doc_id: "mta-wiki:4019"
title: "GetFPSLimit"
source_title: "GetFPSLimit"
source_url: "https://wiki.multitheftauto.com/wiki/GetFPSLimit"
revision_id: 76827
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetFPSLimit

This function retrieves the maximum [FPS (Frames per second)](http://en.wikipedia.org/wiki/Frame_rate) that players on the server can run their game at.

| [[{{{image}}}\|link=\|]] | Note: Starting from version [ r21313 ] and above fpsLimit range is 25-32767 . In older MTA releases it was 25-100 . |
| --- | --- |
|  |  |

## Syntax

```
int getFPSLimit ()
```

### Returns

Returns an integer between **25** and **32767** (refer to the note above) of the maximum FPS that players can run their game at.

## Example

This example displays a message in the chatbox showing the current FPS limit.

```
function checkFPSLimit()
	local fpsLimit = getFPSLimit()

	outputChatBox("The FPS limit is: "..fpsLimit)
end
addCommandHandler("checkfpslimit", checkFPSLimit) -- Add command "checkfpslimit" which calls the function checkFPSLimit
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
