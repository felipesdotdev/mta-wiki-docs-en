---
doc_id: "mta-wiki:3588"
title: "Modules/IRCEcho/ircOpen"
source_title: "Modules/IRCEcho/ircOpen"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircOpen"
revision_id: 14872
language: "en"
categories: ["Utility_templates"]
generated_at: "2026-07-26T16:16:12.930562+00:00"
---

# Modules/IRCEcho/ircOpen

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Opens a connection to the specified IRC Server

## Syntax

```
IRCConnection ircOpen ( string hostname, int port, string nick, string channel, [ string password = ""] )
```

### Required arguments

- **hostname:** The IRC server to connect to

- **port:** The IRC server port

- **nick:** The nickname you want your bot to connect as

- **channel:** The channel you want the bot to join on connect

### Optional arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **password**: The password to enter the IRC server

### Returns

Returns a pointer to the IRC connection if successful, otherwise it returns *nil*

## Example

**Example 1:** This example connects to *irc.gtanet.com* on port *6667* as *WikiTest* and joins *#Channel*

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

addEventHandler( "onResourceStart", getRootElement(), onResourceStart )
```

## See also

- [ircInit](mta://reference/misc/modules-ircecho-ircinit.md)

- ircOpen

- [ircDisconnect](mta://reference/misc/modules-ircecho-ircdisconnect.md)

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
