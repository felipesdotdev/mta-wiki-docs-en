---
doc_id: "mta-wiki:3621"
title: "Modules/IRCEcho/ircRaw"
source_title: "Modules/IRCEcho/ircRaw"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircRaw"
revision_id: 14921
language: "en"
categories: []
---

# Modules/IRCEcho/ircRaw

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Sends an raw message to the IRCConnection

## Syntax

```
function ircRaw ( IRCConnection irc, string command )
```

### Required arguments

- **irc:** The IRCConnection

- **command:** The command that you want to send to the IRC server

## Example

**Example 1:** This makes the IRCConnection ban Fedor!*@*

```
function ircBanHost( thePlayer, command, channel )
	ircRaw("MODE #mta +B Fedor!*@*")
end

addCommandHandler( "disgrace", ircBanHost )
```

## See also

- [ircInit](mta://reference/misc/modules-ircecho-ircinit.md)

- [ircOpen](mta://reference/misc/modules-ircecho-ircopen.md)

- [ircDisconnect](mta://reference/misc/modules-ircecho-ircdisconnect.md)

- [ircMessage](mta://reference/misc/modules-ircecho-ircmessage.md)

- [ircNotice](mta://reference/misc/modules-ircecho-ircnotice.md)

- [ircChangeNick](mta://reference/misc/modules-ircecho-ircchangenick.md)

- [ircJoin](mta://reference/misc/modules-ircecho-ircjoin.md)

- [ircPart](mta://reference/misc/modules-ircecho-ircpart.md)

- ircRaw

- [ircIsVoice](mta://reference/misc/modules-ircecho-ircisvoice.md)

- [ircIsHalfop](mta://reference/misc/modules-ircecho-ircishalfop.md)

- [ircIsOp](mta://reference/misc/modules-ircecho-ircisop.md)

- [ircIsSuper](mta://reference/misc/modules-ircecho-ircissuper.md)

- [ircIsOwner](mta://reference/misc/modules-ircecho-ircisowner.md)

- [ircGetStatus](mta://reference/misc/modules-ircecho-ircgetstatus.md)
