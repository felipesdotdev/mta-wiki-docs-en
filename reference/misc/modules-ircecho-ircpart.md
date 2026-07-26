---
doc_id: "mta-wiki:3620"
title: "Modules/IRCEcho/ircPart"
source_title: "Modules/IRCEcho/ircPart"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircPart"
revision_id: 14916
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.942185+00:00"
---

# Modules/IRCEcho/ircPart

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Lets the IRCConnection leave a channel

## Syntax

```
function ircPart ( IRCConnection irc, string channel )
```

### Required arguments

- **irc:** The IRCConnection

- **channel:** The channel you want to leave

## Example

**Example 1:** This command makes the bot leave a channel

```
function ircLeaveChannel( thePlayer, command, channel )
	ircPart( pIRC, channel )
end

addCommandHandler( "ircpart", ircLeaveChannel )
```

## See also

- [ircInit](mta://reference/misc/modules-ircecho-ircinit.md)

- [ircOpen](mta://reference/misc/modules-ircecho-ircopen.md)

- [ircDisconnect](mta://reference/misc/modules-ircecho-ircdisconnect.md)

- [ircMessage](mta://reference/misc/modules-ircecho-ircmessage.md)

- [ircNotice](mta://reference/misc/modules-ircecho-ircnotice.md)

- [ircChangeNick](mta://reference/misc/modules-ircecho-ircchangenick.md)

- [ircJoin](mta://reference/misc/modules-ircecho-ircjoin.md)

- ircPart

- [ircRaw](mta://reference/misc/modules-ircecho-ircraw.md)

- [ircIsVoice](mta://reference/misc/modules-ircecho-ircisvoice.md)

- [ircIsHalfop](mta://reference/misc/modules-ircecho-ircishalfop.md)

- [ircIsOp](mta://reference/misc/modules-ircecho-ircisop.md)

- [ircIsSuper](mta://reference/misc/modules-ircecho-ircissuper.md)

- [ircIsOwner](mta://reference/misc/modules-ircecho-ircisowner.md)

- [ircGetStatus](mta://reference/misc/modules-ircecho-ircgetstatus.md)
