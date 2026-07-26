---
doc_id: "mta-wiki:6477"
title: "Resource : CallingFunctions"
source_title: "Resource:CallingFunctions"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ACallingFunctions"
revision_id: 64163
language: "en"
categories: ["Resource"]
---

# Resource : CallingFunctions

| [[{{{image}}}\|link=\|]] | Note: It is strongly advised that you validate the functions being called or potentially a client can do anything they want with your server - banning players, adding themselves as admin (depending how well your ACL is set up) etc. This is why this function is not built into MTA. |
| --- | --- |
|  |  |

This resource was made off of the functions:
[CallClientFunction](mta://scripting/shared/functions/callclientfunction.md)
and
[CallServerFunction](mta://scripting/shared/functions/callserverfunction.md)

## Calling Functions

Click to collapse [-]
callSF

```
void exports.callingFunctions:callSF( string funcname, [ var arg1, ... ] )
```

# Required

- **funcname**: The name of the function that should be called serverside. May also be a function in a table, e.g. "math.round".

# Optional

- **agr1-argn**: The arguments that should be passed to the function.

# Example

This example removes the player from his team.

```
-- get the local player element
local _local = getLocalPlayer()
-- define the leaveTeam command handler function
function cmdLeaveTeam()
    -- set the player's team to nil
    callServerFunction("setPlayerTeam", _local)
end
-- add the command handler
addCommandHandler("leaveTeam", cmdLeaveTeam, false)
```

Click to collapse [-]
callCF

```
void exports.callingFunctions:callCF( client Client, string funcname, [ var arg1, ... ] )
```

# Required

- **Client**: The element of the player who should be affected.

- **funcname**: The name of the function that should be called serverside. May also be a function in a table, e.g. "math.round".

# Optional

- **agr1-argn**: The arguments that should be passed to the function.

# Example

This example sets the player's minute duration.

```
-- define the onPlayerJoin handler function
function onPlayerJoin()
    -- set the minute duration
    callClientFunction(source, "setMinuteDuration", 10000)
end
-- add the event handler
addEventHandler("onPlayerJoin", root, onPlayerJoin)
```

I give all thanks to Neon Black for making these functions.

## See Also

- [Download](http://community.mtasa.com/index.php?p=resources&s=details&id=4858)

- [callServerFunction](mta://scripting/shared/functions/callserverfunction.md)

- [callClientFunction](mta://scripting/shared/functions/callclientfunction.md)
