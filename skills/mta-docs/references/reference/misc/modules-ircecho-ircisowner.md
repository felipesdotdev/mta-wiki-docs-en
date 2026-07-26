---
doc_id: "mta-wiki:3626"
title: "Modules/IRCEcho/ircIsOwner"
source_title: "Modules/IRCEcho/ircIsOwner"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/ircIsOwner"
revision_id: 14932
language: "en"
categories: []
---

# Modules/IRCEcho/ircIsOwner

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

Can be used to check if the user has founderrights in an channel

## Syntax

```
function ircIsOwner ( IRCConnection irc, string channel, string nick )
```

### Required arguments

- **irc:** The IRCConnection

- **channel:** The channel that you want to check on

- **nick:** The person that you want to check on

## Example

**Example 1:** This script can be used from irc, so that people with founderrights or higher can use !unban

```
function irc_onPrivMsg( szChannel, szNick, szText )
  	if string.find( szText, "!unban" ) == 1 then
		if ( ircIsOwner( pIRC, szChannel, szNick ) ) then
		  	unbanIP(string.sub(szText, 7))
		end
	end
end
```
