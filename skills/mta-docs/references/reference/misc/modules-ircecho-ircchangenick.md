---
doc_id: "mta-wiki:3618"
title: "Modules/IRCEcho/ircChangeNick"
source_title: "Modules/IRCEcho/ircChangeNick"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircChangeNick"
revision_id: 14918
language: "en"
categories: []
---

# Modules/IRCEcho/ircChangeNick

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Changes the name of the IRCConnection

## Syntax

```
function ircChangeNick ( IRCConnection irc, string newnick )
```

### Required arguments

- **irc:** The IRCConnection

- **newnick:** The new nickname

## Example

**Example 1:** This example adds the command "ircname". That command can change the IRCConnection's name

```
function changeIrcName( thePlayer, command, newname )
	ircChangeNick( pIRC, newname )
end

addCommandHandler( "ircname", changeIrcName )
```

## See also

- [ircInit](mta://reference/misc/modules-ircecho-ircinit.md)

- [ircOpen](mta://reference/misc/modules-ircecho-ircopen.md)

- [ircDisconnect](mta://reference/misc/modules-ircecho-ircdisconnect.md)

- [ircMessage](mta://reference/misc/modules-ircecho-ircmessage.md)

- [ircNotice](mta://reference/misc/modules-ircecho-ircnotice.md)

- ircChangeNick

- [ircJoin](mta://reference/misc/modules-ircecho-ircjoin.md)

- [ircPart](mta://reference/misc/modules-ircecho-ircpart.md)

- [ircRaw](mta://reference/misc/modules-ircecho-ircraw.md)

- [ircIsVoice](mta://reference/misc/modules-ircecho-ircisvoice.md)

- [ircIsHalfop](mta://reference/misc/modules-ircecho-ircishalfop.md)

- [ircIsOp](mta://reference/misc/modules-ircecho-ircisop.md)

- [ircIsSuper](mta://reference/misc/modules-ircecho-ircissuper.md)

- [ircIsOwner](mta://reference/misc/modules-ircecho-ircisowner.md)

- [ircGetStatus](mta://reference/misc/modules-ircecho-ircgetstatus.md)
