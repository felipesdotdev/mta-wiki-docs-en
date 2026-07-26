---
doc_id: "mta-wiki:3589"
title: "Modules/IRCEcho/ircDisconnect"
source_title: "Modules/IRCEcho/ircDisconnect"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircDisconnect"
revision_id: 14870
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.801250+00:00"
---

# Modules/IRCEcho/ircDisconnect

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Disconnects an open IRC Connection

## Syntax

```
function ircDisconnect ( IRCConnection irc )
```

### Required arguments

- **irc:** The IRCConnection you wish to disconnect

## Example

**Example 1:** This example connects to a server on *ResourceStart* and disconnects on *ResourceStop*

```
szChans = {} --Init an array of channels for storage

function onResourceStart( res )
	if res == getThisResource() then -- If the starting resource is this one
		ircInit( ) -- Initialize the module for this resource
		pIRC = ircOpen( "irc.gtanet.com", 6667, "WikiTest", "#channel" ) -- Open the IRC connection
		if pIRC then -- If opening connection was successful
			szChans[ pIRC ] = "#channel" -- Add the channel to the table
		end
	end
end

function onResourceStop( res )
	if res == getThisResource () then -- If the stopping resource is this one
		if pIRC then -- If theres an IRC Connection
			ircDisconnect( pIRC ) -- Disconnect the connection
			szChans[ pIRC ] = nil -- Removes the channel from the array
			pIRC = nil -- Set the connection to nil
		end
	end
end

addEventHandler( "onResourceStart", getRootElement(), onResourceStart )
addEventHandler( "onResourceStop", getRootElement(), onResourceStop )
```

## See also

- [ircInit](mta://reference/misc/modules-ircecho-ircinit.md)

- [ircOpen](mta://reference/misc/modules-ircecho-ircopen.md)

- ircDisconnect

- [ircMessage](mta://reference/misc/modules-ircecho-ircmessage.md)

- [ircNotice](mta://reference/misc/modules-ircecho-ircnotice.md)

- [ircChangeNick](mta://reference/misc/modules-ircecho-ircchangenick.md)

- [ircJoin](mta://reference/misc/modules-ircecho-ircjoin.md)

- [ircPart](mta://reference/misc/modules-ircecho-ircpart.md)

- [ircRaw](mta://reference/misc/modules-ircecho-ircraw.md)

- [ircIsVoice](mta://reference/misc/modules-ircecho-ircisvoice.md)

- [ircIsHalfop](mta://reference/misc/modules-ircecho-ircishalfop.md)

- [ircIsOp](mta://reference/misc/modules-ircecho-ircisop.md)

- [ircIsSuper](mta://reference/misc/modules-ircecho-ircissuper.md)

- [ircIsOwner](mta://reference/misc/modules-ircecho-ircisowner.md)

- [ircGetStatus](mta://reference/misc/modules-ircecho-ircgetstatus.md)
