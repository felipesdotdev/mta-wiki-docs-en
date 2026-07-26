---
doc_id: "mta-wiki:3624"
title: "Modules/IRCEcho/ircIsOp"
source_title: "Modules/IRCEcho/ircIsOp"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircIsOp"
revision_id: 14934
language: "en"
categories: []
---

# Modules/IRCEcho/ircIsOp

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Can be used to check if the user has Op or higher

## Syntax

```
function ircIsOp ( IRCConnection irc, string channel, string nick )
```

### Required arguments

- **irc:** The IRCConnection

- **channel:** The channel that you want to check on

- **nick:** The person that you want to check on

## Example

**Example 1:** This script can be used from irc, so that people with op or higher can use !kick

```
function irc_onPrivMsg( szChannel, szNick, szText )
  	if string.find( szText, "!kick" ) == 1 then
		if ( ircIsOp( pIRC, szChannel, szNick ) ) then
		  	local thePlayer = getPlayerFromNick(string.sub(szText, 6))
		  	if (thePlayer) then
				kickPlayer( thePlayer )
			end
		end
	end
end
```
