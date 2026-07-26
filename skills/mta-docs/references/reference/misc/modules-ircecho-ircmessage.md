---
doc_id: "mta-wiki:3616"
title: "Modules/IRCEcho/ircMessage"
source_title: "Modules/IRCEcho/ircMessage"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircMessage"
revision_id: 14920
language: "en"
categories: []
---

# Modules/IRCEcho/ircMessage

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Displays an message to an IRC Channel

## Syntax

```
function ircMessage ( IRCConnection irc, string channel, string message )
```

### Required arguments

- **irc:** The IRCConnection

- **channel:** The channel or person you want to send the message to

- **message:** The message

## Example

**Example 1:** This echo is displaying all the ingame chat to #mta with the IRCConnection stored in pIRC

```
function ChatToIRC( message, type )
	if (type == 0) then -- Its an normal chatmessage
		ircMessage( pIRC, "#mta", "CHAT:�� " .. getClientName( source ) .. ": " .. message )
	elseif (type == 1) then -- Its an action
		ircMessage( pIRC, "#mta", "ACTION: " .. getClientName( source ) .. ": " .. message )
	elseif (type == 2) then -- Teamchat message
		ircMessage( pIRC, "#mta", "TEAMCHAT: " .. getClientName( source ) .. ": " .. message )
	end
end

addEventHandler( "onPlayerChat", getRootElement(), ChatToIRC )
```

## See also

- [ircInit](mta://reference/misc/modules-ircecho-ircinit.md)

- [ircOpen](mta://reference/misc/modules-ircecho-ircopen.md)

- [ircDisconnect](mta://reference/misc/modules-ircecho-ircdisconnect.md)

- ircMessage

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
