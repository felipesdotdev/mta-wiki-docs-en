---
doc_id: "mta-wiki:3586"
title: "Modules/IRCEcho/ircInit"
source_title: "Modules/IRCEcho/ircInit"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircInit"
revision_id: 14871
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.825908+00:00"
---

# Modules/IRCEcho/ircInit

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Initializes the module for use in the script. Must be ran in the scripts you want to use with the echo

## Syntax

```
function ircInit()
```

## Example

**Example 1:** This example initializes the module on resource startup

```
function onResourceStart( res )
	if ( res == getThisResource () ) then
		ircInit()
		outputServerLog( "Initialized IRC for " .. getResourceName( res ) )
	end
end

addEventHandler( "onResourceStart", getRootElement(), onResourceStart )
```

## See also

- ircInit

- [ircOpen](mta://reference/misc/modules-ircecho-ircopen.md)

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
