---
doc_id: "mta-wiki:3625"
title: "Modules/IRCEcho/ircIsSuper"
source_title: "Modules/IRCEcho/ircIsSuper"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircIsSuper"
revision_id: 14933
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.864163+00:00"
---

# Modules/IRCEcho/ircIsSuper

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Can be used to check if the user has superops (aka Protection) or higher

## Syntax

```
function ircIsSuper ( IRCConnection irc, string channel, string nick )
```

### Required arguments

- **irc:** The IRCConnection

- **channel:** The channel that you want to check on

- **nick:** The person that you want to check on

## Example

**Example 1:** This script can be used from irc, so that people with superops or higher can use !ban

```
function irc_onPrivMsg( szChannel, szNick, szText )
  	if string.find( szText, "!ban" ) == 1 then
		if ( ircIsSuper( pIRC, szChannel, szNick ) ) then
		  	local thePlayer = getPlayerFromNick(string.sub(szText, 5))
		  	if (thePlayer) then
				banPlayer( thePlayer )
			end
		end
	end
end
```
