---
doc_id: "mta-wiki:1576"
title: "OutputServerLog"
source_title: "OutputServerLog"
source_url: "https://wiki.multitheftauto.com/wiki/OutputServerLog"
revision_id: 80372
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:27.463106+00:00"
---

# OutputServerLog

This outputs a line of text to the server's log. This could be useful for debugging.

## Syntax

```
bool outputServerLog ( string text )
```

### Required Arguments

- **text:** The text to be output to the log.

### Returns

Returns *true* if successful, *false* otherwise.

## Example

Click to collapse [-]
Server

**Example 1:** This example outputs client logins to the server log.

```
function logClientLogin ( previous_account, current_account )
	outputServerLog ( "Client " .. getPlayerName ( source ) .. " logged in as " .. getAccountName ( current_account ) )
end
addEventHandler ( "onPlayerLogin", root, logClientLogin )
```

**Example 2:** This example outputs the clients position to the server

```
function outputPosition(source)
   outputServerLog( table.concat({getElementPosition(source)}, ", ") )
end
addCommandHandler("op", outputPosition)
```

**Example 3:** This is an debugging example, to identify which resource/source is responsible for vehicles that get spawned/exist but aren't supposed to be (like forbidden, where they can still spawn it through creation vulnerability, or identify which resource is hooked into (that has spawnvehicle server event) by a LUA code injector/hacked client so you know which resource/calls you have to secure

```
local triggeredByModels = { [432]=true } 

function detectVehicleCreation() 
    if getElementType(source) == "vehicle" and triggeredByModels[getElementModel(source)] then 
        outputServerLog ("** ILLEGAL VEHICLE DETECTED ** "..getVehicleName(source).." was found at "..toJSON({getElementPosition(source)}).. " dim: "..getElementDimension(source).. " & int: "..getElementInterior(source)) 
        local x,y,z = getElementPosition(source) 
        local sphere = createColSphere(x,y,z,40) 
        setElementInterior(sphere, getElementInterior(source)) 
        setElementDimension(sphere, getElementDimension(source)) 
        attachElements(sphere, source) 
        local players = {} 
        local pc = getElementsWithinColShape(sphere, "player") 
        for _,p in pairs (pc) do 
            if p then 
                table.insert (players, getPlayerName(p)) 
            end 
        end 
        if players and #players ~= 0 then 
            outputServerLog ("** Nearby players: (possibly driver/spawner) "..toJSON(players)) 
        end 
        outputServerLog ("** Responsible resource: "..tostring(getElementID(getElementParent(getElementParent(source))))) 
        destroyElement(sphere) 
    end 
end 
addEventHandler ("onElementStartSync", root, detectVehicleCreation)
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
