---
doc_id: "mta-wiki:3791"
title: "Modules/IRCEcho/irc onConnected"
source_title: "Modules/IRCEcho/irc onConnected"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho/irc_onConnected"
revision_id: 15744
language: "en"
categories: []
---

# Modules/IRCEcho/irc onConnected

|  | This function is provided by the external module IRCEcho . You must install this module to use this function. |
| --- | --- |
|  |  |

This is called when the IRC Module has successfully connected to a server

## Syntax

```
function irc_onConnected (  )
```

## Example

**Example 1:** This script outputs that the server has connected to IRC

```
function irc_onConnected( )
  	outputServerLog( "IRC Connected!" )
end
```

## See also

- [irc_onConnecting](mta://reference/misc/modules-ircecho-irc-onconnecting.md)

- irc_onConnected

- [irc_onDisconnected](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onDisconnected&action=edit&redlink=1)

- [irc_onFailedConnection](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onFailedConnection&action=edit&redlink=1)

- [irc_onPrivMsg](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onPrivMsg&action=edit&redlink=1)

- [irc_onNotice](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onNotice&action=edit&redlink=1)

- [irc_onJoin](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onJoin&action=edit&redlink=1)

- [irc_onPart](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onPart&action=edit&redlink=1)

- [irc_onQuit](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onQuit&action=edit&redlink=1)

- [irc_onNickChange](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onNickChange&action=edit&redlink=1)

- [irc_onRaw](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onRaw&action=edit&redlink=1)
