---
doc_id: "mta-wiki:3617"
title: "Modules/IRCEcho/ircNotice"
source_title: "Modules/IRCEcho/ircNotice"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircNotice"
revision_id: 25673
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.915168+00:00"
---

# Modules/IRCEcho/ircNotice

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Notice somebody of an action

## Syntax

```
function ircNotice ( IRCConnection irc, string channel, string message )
```

### Required arguments

- **irc:** The IRCConnection

- **channel:** The channel or user you want to send to

- **message:** The message

## Example

**Example 1:** This example is warning IJs of an banned user

```
function ReportBan( ip )
	ircNotice( pIRC, "IJs", getPlayerName( source ) .. " banned " .. sz )
end

addEventHandler( "onBan", getRootElement(), ReportBan )
```

## See also

- [ircInit](mta://reference/misc/modules-ircecho-ircinit.md)

- [ircOpen](mta://reference/misc/modules-ircecho-ircopen.md)

- [ircDisconnect](mta://reference/misc/modules-ircecho-ircdisconnect.md)

- [ircMessage](mta://reference/misc/modules-ircecho-ircmessage.md)

- ircNotice

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
