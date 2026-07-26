---
doc_id: "mta-wiki:3622"
title: "Modules/IRCEcho/ircIsVoice"
source_title: "Modules/IRCEcho/ircIsVoice"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircIsVoice"
revision_id: 14936
language: "en"
categories: []
---

# Modules/IRCEcho/ircIsVoice

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Can be used to check if the user has Voice or higher

## Syntax

```
function ircIsVoice ( IRCConnection irc, string channel, string nick )
```

### Required arguments

- **irc:** The IRCConnection

- **channel:** The channel that you want to check on

- **nick:** The person that you want to check on

## Example

**Example 1:** This script can be used from irc, so that people with voice or higher can use !say

```
function irc_onPrivMsg( szChannel, szNick, szText )
  	if string.find( szText, "!say" ) == 1 then
		if ( ircIsVoice( pIRC, szChannel, szNick ) ) then
		  	local Message = string.sub(szText, 5)
		  	outputChatBox("* " .. szNick .. " [IRC]: " .. Message)
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

- ircIsVoice

- [ircIsHalfop](mta://reference/misc/modules-ircecho-ircishalfop.md)

- [ircIsOp](mta://reference/misc/modules-ircecho-ircisop.md)

- [ircIsSuper](mta://reference/misc/modules-ircecho-ircissuper.md)

- [ircIsOwner](mta://reference/misc/modules-ircecho-ircisowner.md)

- [ircGetStatus](mta://reference/misc/modules-ircecho-ircgetstatus.md)
