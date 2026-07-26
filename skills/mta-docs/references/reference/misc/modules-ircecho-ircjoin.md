---
doc_id: "mta-wiki:3619"
title: "Modules/IRCEcho/ircJoin"
source_title: "Modules/IRCEcho/ircJoin"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircJoin"
revision_id: 14917
language: "en"
categories: []
---

# Modules/IRCEcho/ircJoin

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Lets the IRCConnection join an channel

## Syntax

```
function ircJoin ( IRCConnection irc, string channel )
```

### Required arguments

- **irc:** The IRCConnection

- **channel:** The channel you want to join

## Example

**Example 1:** This command makes the bot join another channel

```
function ircJoinChannel( thePlayer, command, channel )
	ircJoinChannel( pIRC, channel )
end

addCommandHandler( "ircjoin", ircJoinChannel )
```

## See also

- [ircInit](mta://reference/misc/modules-ircecho-ircinit.md)

- [ircOpen](mta://reference/misc/modules-ircecho-ircopen.md)

- [ircDisconnect](mta://reference/misc/modules-ircecho-ircdisconnect.md)

- [ircMessage](mta://reference/misc/modules-ircecho-ircmessage.md)

- [ircNotice](mta://reference/misc/modules-ircecho-ircnotice.md)

- [ircChangeNick](mta://reference/misc/modules-ircecho-ircchangenick.md)

- ircJoin

- [ircPart](mta://reference/misc/modules-ircecho-ircpart.md)

- [ircRaw](mta://reference/misc/modules-ircecho-ircraw.md)

- [ircIsVoice](mta://reference/misc/modules-ircecho-ircisvoice.md)

- [ircIsHalfop](mta://reference/misc/modules-ircecho-ircishalfop.md)

- [ircIsOp](mta://reference/misc/modules-ircecho-ircisop.md)

- [ircIsSuper](mta://reference/misc/modules-ircecho-ircissuper.md)

- [ircIsOwner](mta://reference/misc/modules-ircecho-ircisowner.md)

- [ircGetStatus](mta://reference/misc/modules-ircecho-ircgetstatus.md)
