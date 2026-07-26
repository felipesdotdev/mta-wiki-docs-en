---
doc_id: "mta-wiki:3790"
title: "Modules/IRCEcho/irc onConnecting"
source_title: "Modules/IRCEcho/irc onConnecting"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/irc_onConnecting"
revision_id: 15745
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.981897+00:00"
---

# Modules/IRCEcho/irc onConnecting

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

This is called when the IRC Module is attempting to connect to a server

## Syntax

```
function irc_onConnecting ( string IP, int Port )
```

### Required arguments

- **IP:** The IP/Hostname of the server you are trying to connect to

- **Port:** The Port of the IRC Server you are trying to connect to

## Example

**Example 1:** This script outputs to the server console that it is attempting a connection

```
function irc_onConnecting( IP, Port )
  	outputServerLog( "Connecting to IRC (" .. IP .. ":" .. tostring( Port ) .. ")" )
end
```

## See also

- irc_onConnecting

- [irc_onConnected](mta://reference/misc/modules-ircecho-irc-onconnected.md)

- [irc_onDisconnected](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onDisconnected&action=edit&redlink=1)

- [irc_onFailedConnection](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onFailedConnection&action=edit&redlink=1)

- [irc_onPrivMsg](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onPrivMsg&action=edit&redlink=1)

- [irc_onNotice](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onNotice&action=edit&redlink=1)

- [irc_onJoin](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onJoin&action=edit&redlink=1)

- [irc_onPart](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onPart&action=edit&redlink=1)

- [irc_onQuit](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onQuit&action=edit&redlink=1)

- [irc_onNickChange](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onNickChange&action=edit&redlink=1)

- [irc_onRaw](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onRaw&action=edit&redlink=1)
