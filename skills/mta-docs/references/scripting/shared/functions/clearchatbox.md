---
doc_id: "mta-wiki:10754"
title: "ClearChatBox"
source_title: "ClearChatBox"
source_url: "https://wiki.multitheftauto.com/wiki/ClearChatBox"
revision_id: 72975
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.5"]
---

# ClearChatBox

This function clears the chatbox. It does not clear the console (F8)

## Syntax

Click to collapse [-]
Client

```
bool clearChatBox ()
```

### Returns

Returns *true* if the player's chat was cleared successfully, *false* otherwise.

Click to collapse [-]
Server

```
bool clearChatBox ( [ element clearFor = getRootElement() ])
```

### Required Arguments

- **clearFor :** The [player](https://wiki.multitheftauto.com/index.php?search=player) whose chat is to be cleared. By default, this is set to the root element, which will affect all players.

### Returns

Returns *true* if the player's chat was cleared successfully, *false* otherwise.

## Example

Click to collapse [-]
Server

This example adds an admin command to clear the chatbox for everyone

```
function cmdClearChat(p, cmd)
    if not isPlayerStaff(p) then return end
    clearChatBox()
end
addCommandHandler("clearchat", cmdClearChat)

-- Utility function
local staffACLs = {
    aclGetGroup("Admin"),
    aclGetGroup("Moderator")
}

function isPlayerStaff(p)
	if isElement(p) and getElementType(p) == "player" and not isGuestAccount(getPlayerAccount(p)) then
		local object = getAccountName(getPlayerAccount(p))

		for _, group in ipairs(staffACLs) do
			if isObjectInACLGroup("user." .. object, group) then
				return true
			end
		end
	end
	return false
end
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
