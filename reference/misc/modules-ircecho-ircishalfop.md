---
doc_id: "mta-wiki:3623"
title: "Modules/IRCEcho/ircIsHalfop"
source_title: "Modules/IRCEcho/ircIsHalfop"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircIsHalfop"
revision_id: 14935
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.839429+00:00"
---

# Modules/IRCEcho/ircIsHalfop

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Can be used to check if the user has Halfop or higher

## Syntax

```
function ircIsHalfop ( IRCConnection irc, string channel, string nick )
```

### Required arguments

- **irc:** The IRCConnection

- **channel:** The channel that you want to check on

- **nick:** The person that you want to check on

## Example

**Example 1:** This script can be used from irc, so that people with Halfop or higher can use !asay

```
function irc_onPrivMsg( szChannel, szNick, szText )
  	if string.find( szText, "!asay" ) == 1 then
		if ( ircIsHalfop( pIRC, szChannel, szNick ) ) then
		  	local Message = string.sub(szText, 6)
		  	outputChatBox("The admin says: " .. Message, getRootResource(), 255, 0, 0)
		end
	end
end
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

- [ircRaw](mta://reference/misc/modules-ircecho-ircraw.md)

- [ircIsVoice](mta://reference/misc/modules-ircecho-ircisvoice.md)

- ircIsHalfop

- [ircIsOp](mta://reference/misc/modules-ircecho-ircisop.md)

- [ircIsSuper](mta://reference/misc/modules-ircecho-ircissuper.md)

- [ircIsOwner](mta://reference/misc/modules-ircecho-ircisowner.md)

- [ircGetStatus](mta://reference/misc/modules-ircecho-ircgetstatus.md)
