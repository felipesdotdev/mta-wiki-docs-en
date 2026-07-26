---
doc_id: "mta-wiki:8353"
title: "OnClientPlayerNetworkStatus"
source_title: "OnClientPlayerNetworkStatus"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPlayerNetworkStatus"
revision_id: 46525
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:19.683023+00:00"
---

# OnClientPlayerNetworkStatus

This event is triggered when the server network connection to a player is interrupted. See [onPlayerNetworkStatus](mta://scripting/server/events/onplayernetworkstatus.md) for detecting player to server interruptions.

## Parameters

```
int status, int ticks
```

- **status**: A number which is 0 if the interruption has begun, or 1 if the interruption is ending.

- **ticks**: Number of ticks since the interruption started.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [root element](mta://reference/misc/root-element.md).

## Example

This example shows a debug message when interruption starts and stops and also prevents the local player moving during the interruption.

```
frozen = false -- This variable stores whether or not the script is going to freeze them.
-- If they were already frozen then don't unfreeze them when the interruption ends to avoid conflicts with other scripts.
function handleInterrupt( status, ticks )
	if (status == 0) then
		outputDebugString( "(packets from server) interruption began " .. ticks .. " ticks ago" )
		if (not isElementFrozen(localPlayer)) then
			setElementFrozen(localPlayer, true) -- Freeze them to prevent them abusing the network interruption
			frozen = true
		end
	elseif (status == 1) then
		outputDebugString( "(packets from server) interruption began " .. ticks .. " ticks ago and has just ended" )
		if (frozen) then
			setElementFrozen(localPlayer, false) -- If we froze them, unfreeze them now.
			frozen = false
		end
	end
end
addEventHandler( "onClientPlayerNetworkStatus", root, handleInterrupt)
```

## See Also

### Other client events

- [onClientChatMessage](mta://scripting/client/events/onclientchatmessage.md)

- [onClientConsole](mta://scripting/client/events/onclientconsole.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22649](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22649):

- [onClientCoreCommand](mta://scripting/client/events/onclientcorecommand.md)

- [onClientDebugMessage](mta://scripting/client/events/onclientdebugmessage.md)

- [onClientExplosion](mta://scripting/client/events/onclientexplosion.md)

- [onClientFileDownloadComplete](mta://scripting/client/events/onclientfiledownloadcomplete.md)

- [onClientHUDRender](mta://scripting/client/events/onclienthudrender.md)

- [onClientMinimize](mta://scripting/client/events/onclientminimize.md)

- [onClientMTAFocusChange](mta://scripting/client/events/onclientmtafocuschange.md)

- [onClientPedsProcessed](mta://scripting/client/events/onclientpedsprocessed.md)

- onClientPlayerNetworkStatus

- [onClientPreRender](mta://scripting/client/events/onclientprerender.md)

- [onClientRender](mta://scripting/client/events/onclientrender.md)

- [onClientRestore](mta://scripting/client/events/onclientrestore.md)

- [onClientTransferBoxProgressChange](mta://scripting/client/events/onclienttransferboxprogresschange.md)

- [onClientTransferBoxVisibilityChange](mta://scripting/client/events/onclienttransferboxvisibilitychange.md)

- [onClientWorldSound](mta://scripting/client/events/onclientworldsound.md)
