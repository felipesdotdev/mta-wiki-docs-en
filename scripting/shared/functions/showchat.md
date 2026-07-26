---
doc_id: "mta-wiki:2691"
title: "ShowChat"
source_title: "ShowChat"
source_url: "https://wiki.multitheftauto.com/wiki/ShowChat"
revision_id: 72710
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:50.629682+00:00"
---

# ShowChat

This function is used to show or hide the player's chat.

## Syntax

Click to collapse [-]
Client

```
bool showChat ( bool show [, bool inputBlocked ] )
```

### Required Arguments

- **show:** A boolean value determining whether to show (*true*) or hide (*false*) the chat.

### Optional Arguments

- **inputBlocked:** A boolean value determining whether chat input is blocked/hidden, regardless of chat visibility. If unset, this will keep the default behaviour prior to r20898 (*true* when chat is hidden, *false* when chat is visible).

### Returns

Returns *true* if the player's chat was shown or hidden successfully, *false* otherwise.

Click to collapse [-]
Server

```
bool showChat ( player thePlayer, bool show [, bool inputBlocked ] )
```

### Required Arguments

- **thePlayer:** The [player](mta://reference/misc/player.md) whose chat is to be hidden or shown.

- **show:** A boolean value determining whether to show (*true*) or hide (*false*) the chat.

### Optional Arguments

- **inputBlocked:** A boolean value determining whether chat input is blocked/hidden, regardless of chat visibility. If unset, this will keep the default behaviour prior to r20898 (*true* when chat is hidden, *false* when chat is visible).

### Returns

Returns *true* if the player's chat was shown or hidden successfully, *false* otherwise.

## Example

Click to collapse [-]
Client

This example toggle's the player's chat when they press the "**i**" key.

```
--This example below is for all versions until 1.4:
local isChatVisible = true --Let's assume the chat is visible as soon as the resource starts.

function chat(key, keyState)
    if isChatVisible then --Check or the chat is visible.
        showChat(false) --If it is, hide it.
        isChatVisible = false
    else
        showChat(true) --If it is not, show it.
        isChatVisible = true
    end
end

bindKey("i", "down", chat) --Make a bind key to start the function as soon as a player presses the key 'i'

--This example below is for version 1.4 and up:
function chat(key, keyState)
    if isChatVisible() then --Check or the chat is visible.
        showChat(false) --If it is, hide it.
    else
        showChat(true) --If it is not, show it.
    end
end

bindKey("i", "down", chat) --Make a bind key to start the function as soon as a player presses the key 'i'
```

## See Also

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIpFromMasterServer](mta://scripting/server/functions/getserveripfrommasterserver.md)

- [getServerName](mta://scripting/server/functions/getservername.md)

- [getServerPassword](mta://scripting/server/functions/getserverpassword.md)

- [getServerPort](mta://scripting/server/functions/getserverport.md)

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)
