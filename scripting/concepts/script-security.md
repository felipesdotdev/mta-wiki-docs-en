---
doc_id: "mta-wiki:9399"
title: "Script security"
source_title: "Script security"
source_url: "https://wiki.multitheftauto.com/wiki/Script_security"
revision_id: 82697
language: "en"
categories: []
generated_at: "2026-07-26T16:16:35.722219+00:00"
---

# Script security

Awareness of client memory

Starting from very basics:

- You should be aware that everything you store on client-side is at risk, this includes .lua files as well. Any confidential (and/or) important data which is stored, or travels through client-side (player PC) could be accessed by malicious clients.

- To keep sensitive data (and/or) Lua logic safe - use server-side.

- Do note that scripts marked as **shared** act also as **client code**, which means that everything above applies to them. For example defining:

```
<script src="script.lua" type="shared"/> <!-- this script will run separately both on client and server -->
```

Is same as doing:

```
<script src="script.lua" type="client"/> <!-- define it separately on client -->
<script src="script.lua" type="server"/> <!-- do the same, but on server -->
```

## Additional protection layer

In order to make things *slightly harder** for those having bad intentions towards your server, you can make use of cache attribute (and/or [Lua compile (also known as Luac) with extra obfuscation set to level **3**](https://luac.mtasa.com/) - [API](https://wiki.multitheftauto.com/wiki/Lua_compilation_API)) available in [meta.xml](https://wiki.multitheftauto.com/wiki/Meta.xml), along with configuring MTA's built-in AC by toggling SD (Special detections), see: [Anti-cheat guide](https://wiki.multitheftauto.com/wiki/Anti-cheat_guide).

```
<script src="shared.lua" type="shared" cache="false"/> <!-- cache="false" indicates that this Lua file won't be saved on player's PC -->
<script src="client.lua" type="client" cache="false"/> <!-- cache="false" indicates that this Lua file won't be saved on player's PC -->
```

- *Slightly harder* **but not impossible** for some to obtain client code, yet does good job at keeping **most** people away from inspecting your .lua files - those looking for possible logic flaws (bugs) or missing/incorrect security based checks.

- Can be used on both **client** and **shared** script type (has no effect on server-sided Lua).

- It doesn't remove Lua files which were previously downloaded.

## Detecting and dealing with backdoors and cheats

**To ensure minimum (or no) damage resulting from Lua scripts:**

- Keep your server up-to-date, you can [download latest server builds from MTA:SA nightly site.](https://nightly.multitheftauto.com/) Information on specific builds can be [found here.](https://buildinfo.multitheftauto.com/)

- Keep your resources up-to-date, you can [download latest (default) resources from GitHub repository.](https://github.com/multitheftauto/mtasa-resources) Those often contain latest security fixes, which could mean difference between having your server resist from attack or not.

- Make sure to properly configure [ACL (Access Control List)](https://wiki.multitheftauto.com/wiki/Access%20Control%20List) - which will block resources from using certain, potentially dangerous functions.

- Zero-trust with giving away admin rights for resources (including maps) coming from unknown sources.

- Before running any resource you don't trust, analyze:

- [meta.xml](https://wiki.multitheftauto.com/wiki/Meta.xml) of it, for possible hidden scripts lurking beneath other file extensions.

- It's source code, for malicious logic.

- Do not run/keep using compiled resources (scripts) of which legitimacy you aren't sure.

**To ensure minimum damage when a cheater connects to your server:**

- When making scripts, remember to never trust data coming from a client.

- While reviewing scripts for possible security holes. Look at any data coming from the client that is being trusted.

- Any kind of data could be sent, hence server scripts which communicate with client by receiving data sent by players should validate it, before further use in latter parts of code. Mostly, it will be done either by [setElementData](mta://scripting/shared/functions/setelementdata.md) or [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md).

- You shouldn't rely only on player [serial](https://wiki.multitheftauto.com/wiki/Serial), when it comes to processing crucial operations (auto-login/admin actions). **Serials aren't guaranted to be unique or non-fakable**. This is why you should **put it behind** account system, as **important authentication factor** (e.g: **login & password**).

- Server-side logic **can not be bypassed** or **tampered** with (unless server is breached or when there is a bug in code, but that's whole different scenario) - **use it to your advantage**. In majority of cases, you will be able to perform security validations with no participation of client-side.

- Using concept of ***“All parameters including source can be faked and should not be trusted. Global variable client can be trusted.”*** - gives you reliable assurance that player to which you refer (via **client**) **is** in fact, **the one which really called event**. This approach will protect you from situations where cheater can call & process for instance: admin events (e.g kick/ban player) by passing the actual admin (**2nd** argument in **[triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md)**), or trigger events for other players (as if they were the ones who called them, but in reality it was forcefully done by cheater) - as a consequence of using wrong variable. To make sure you fully understood it, take a look at examples below:

```
--[[
	DON'T EVER DO THAT - THAT IS COMPLETELY WRONG AND INSECURE
	THE ISSUE: BY USING 'source' IN hasObjectPermissionTo YOU ARE LEAVING DOOR STRAIGHT OPEN FOR CHEATERS
]]

function onServerWrongAdminEvent(playerToBan)
	if (not client) then -- 'client' points to the player who triggered the event, and should be used as security measure (in order to prevent player faking)
		return false -- if this variable doesn't exists at the moment (for unknown reason, or it was the server who triggered this event), stop code execution
	end

	local defaultPermission = false -- do not allow action by default, see (defaultPermission): https://wiki.multitheftauto.com/wiki/HasObjectPermissionTo
	local canAdminBanPlayer = hasObjectPermissionTo(source, "function.banPlayer", defaultPermission) -- the vulnerability lies here...

	if (not canAdminBanPlayer) then -- if player doesn't have permissions
		return false -- don't do it
	end

	local validElement = isElement(playerToBan) -- check whether argument passed from client is an element

	if (not validElement) then -- it is not
		return false -- stop code processing
	end

	local elementType = getElementType(playerToBan) -- it's an element, so get it's type
	local playerType = (elementType == "player") -- make sure that it's a player

	if (not playerType) then -- it's not a player
		return false -- stop here
	end

	-- banPlayer(...) -- do what needs to be done
end
addEvent("onServerWrongAdminEvent", true)
addEventHandler("onServerWrongAdminEvent", root, onServerWrongAdminEvent)

--[[
	onServerCorrectAdminEvent IS PERFECTLY SECURED, AS IT SHOULD BE
	NO ISSUE HERE: WE'VE USED 'client' IN hasObjectPermissionTo WHICH MAKES IT SAFE FROM FAKING PLAYER WHO CALLED EVENT
]]

function onServerCorrectAdminEvent(playerToBan)
	if (not client) then -- 'client' points to the player who triggered the event, and should be used as security measure (in order to prevent player faking)
		return false -- if this variable doesn't exists at the moment (for unknown reason, or it was the server who triggered this event), stop code execution
	end

	local defaultPermission = false -- do not allow action by default, see (defaultPermission): https://wiki.multitheftauto.com/wiki/HasObjectPermissionTo
	local canAdminBanPlayer = hasObjectPermissionTo(client, "function.banPlayer", defaultPermission) -- is player allowed to do that?

	if (not canAdminBanPlayer) then -- if player doesn't have permissions
		return false -- don't do it
	end

	local validElement = isElement(playerToBan) -- check whether argument passed from client is an element

	if (not validElement) then -- it is not
		return false -- stop code processing
	end

	local elementType = getElementType(playerToBan) -- it's an element, so get it's type
	local playerType = (elementType == "player") -- make sure that it's a player

	if (not playerType) then -- it's not a player
		return false -- stop here
	end

	-- banPlayer(...) -- do what needs to be done
end
addEvent("onServerCorrectAdminEvent", true)
addEventHandler("onServerCorrectAdminEvent", root, onServerCorrectAdminEvent)
```

## Securing setElementData

- You should refrain from using [element data](mta://reference/misc/element-data--975d1ea3.md) everywhere, it should be only used when really necessary. It is advised to replace it with [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md) instead.

- If you still insist on using it, it is recommended to set **4th** argument in [setElementData](mta://scripting/shared/functions/setelementdata.md) to **false** (disabling sync for this, certain data) and use subscriber mode - [addElementDataSubscriber](mta://scripting/server/functions/addelementdatasubscriber.md), for both security & performance reasons described in [event section.](https://wiki.multitheftauto.com/wiki/Script_security#Securing_triggerServerEvent)

| [[{{{image}}}\|link=\|]] | Important Note: Disabling sync however, doesn't fully protect data key. It would be still vulnerable by default, but in this case you are not leaving it in plain sight. Using getAllElementData or digging in RAM wouldn't expose it, since it won't be synced to client in first place. Therefore, it needs to be added to anti-cheat as well. |
| --- | --- |
|  |  |

- All parameters including **source** can be faked and should not be trusted.

- Global variable **client** can be trusted.

Click to collapse [-]
Server

Example of basic element data anti-cheat.

```
local function reportAndRevertDataChange(clientElement, sourceElement, dataKey, oldValue, newValue) -- helper function to log and revert changes
	local logClient = inspect(clientElement) -- in-depth view of player which forced element data sync
	local logSerial = getPlayerSerial(clientElement) or "N/A" -- client serial, or "N/A" if not possible, for some reason
	local logSource = tostring(sourceElement) -- element which received data
	local logOldValue = tostring(oldValue) -- old value
	local logNewValue = tostring(newValue) -- new value
	local logText = -- fill our report with data
		"=======================================\n"..
		"Detected element data abnormality:\n"..
		"Client: "..logClient.."\n"..
		"Client serial: "..logSerial.."\n"..
		"Source: "..logSource.."\n"..
		"Data key: "..dataKey.."\n"..
		"Old data value: "..logOldValue.."\n"..
		"New data value: "..logNewValue.."\n"..
		"======================================="

	local logVisibleTo = root -- specify who will see this log in console, in this case each player connected to server
	local hadData = (oldValue ~= nil) -- check if element had such data before

	if (hadData) then -- if element had such data before
		setElementData(sourceElement, dataKey, oldValue, true) -- revert changes, it will call onElementDataChange event, but will fail (stop) on first condition - because server (not client) forced change
	else
		removeElementData(sourceElement, dataKey) -- remove it completely
	end

	outputConsole(logText, logVisibleTo) -- print it to console

	return true -- all success
end

function onElementDataChangeBasicAC(dataKey, oldValue, newValue) -- the heart of our anti-cheat, which does all the magic security measurements
	if (not client) then -- check if data is coming from client
		return false -- if it's not, do not go further
	end

	local checkSpecialThing = (dataKey == "special_thing") -- compare whether dataKey matches "special_thing"
	local checkFlagWaving = (dataKey == "flag_waving") -- compare whether dataKey matches "flag_waving"

	if (checkSpecialThing) then -- if it does, do our security checks
		local invalidElement = (client ~= source) -- verify whether source element is different from player which changed data

		if (invalidElement) then -- if it's so
			reportAndRevertDataChange(client, source, dataKey, oldValue, newValue) -- revert data change, because "special_thing" can only be set for player himself
		end
	end

	if (checkFlagWaving) then -- if it does, do our security checks
		local playerVehicle = getPedOccupiedVehicle(client) -- get player's current vehicle
		local invalidVehicle = (playerVehicle ~= source) -- verify whether source element is different from player's vehicle

		if (invalidVehicle) then -- if it's so
			reportAndRevertDataChange(client, source, dataKey, oldValue, newValue) -- revert data change, because "flag_waving" can only be set for player's own vehicle
		end
	end
end
addEventHandler("onElementDataChange", root, onElementDataChangeBasicAC)
```

Click to collapse [-]
Server

Example of advanced element data anti-cheat.

```
--[[
	For maximum security set punishPlayerOnDetect, punishmentBan, allowOnlyProtectedKeys to true (as per default configuration)
	If allowOnlyProtectedKeys is enabled, do not forget to add every client-side element data key to protectedKeys table - otherwise you will face false-positives

	Anti-cheat (handleDataChange) table structure and it's options:

	["keyName"] = { -- name of key which would be protected
		onlyForPlayerHimself = true, -- enabling this (true) will make sure that this element data key can only be set on player who synced it (ignores onlyForOwnPlayerVeh and allowForElements), use false/nil to disable this
		onlyForOwnPlayerVeh = false, -- enabling this (true) will make sure that this element data key can only be set on player's current vehicle who synced it (ignores allowForElements), use false/nil to disable this
		allowForElements = { -- restrict this key for certain element type(s), set to false/nil or leave it empty to not check this (full list of element types: https://wiki.multitheftauto.com/wiki/GetElementsByType)
			["player"] = true,
			["ped"] = true,
			["vehicle"] = true,
			["object"] = true,
		},
		allowedDataTypes = { -- restrict this key for certain value type(s), set to false/nil or leave it empty to not check this
			["string"] = true,
			["number"] = true,
			["table"] = true,
			["boolean"] = true,
			["nil"] = true,
		},
		allowedStringLength = {1, 32}, -- if value is a string, then it's length must be in between (min-max), set it to false/nil to not check string length - do note that allowedDataTypes must contain ["string"] = true
		allowedTableLength = {1, 64}, -- if value is a table, then it's length must be in between (min-max), set it to false/nil to not check table length - do note that allowedDataTypes must contain ["table"] = true
		allowedNumberRange = {1, 128}, -- if value is a number, then it must be in between (min-max), set it to false/nil to not check number range - do note that allowedDataTypes must contain ["number"] = true
	}
]]

local punishPlayerOnDetect = true -- should player be punished upon detection (make sure that resource which runs this code has admin rights)
local punishmentBan = true -- only relevant if punishPlayerOnDetect is set to true; use true for ban or false for kick
local punishmentReason = "Altering element data" -- only relevant if punishPlayerOnDetect is set to true; reason which would be shown to punished player
local punishedBy = "Console" -- only relevant if punishPlayerOnDetect is set to true; who was responsible for punishing, as well shown to punished player
local banByIP = false -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; banning by IP nowadays is not recommended (...)
local banByUsername = false -- community username - legacy thing, hence is set to false and should stay like that
local banBySerial = true -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; (...) if there is a player serial to use instead
local banTime = 0 -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; time in seconds, 0 for permanent
local allowOnlyProtectedKeys = true -- disallow (remove by using removeElementData) every element data besides those given in protectedKeys table; in case someone wanted to flood server with garbage keys, which would be kept in memory until server restart or manual remove - setElementData(source, key, nil) won't remove it; it has to be removeElementData
local debugLevel = 4 -- this debug level allows to hide INFO: prefix, and use custom colors
local debugR = 255 -- debug message - red color
local debugG = 127 -- debug message - green color
local debugB = 0 -- debug message - blue color
local protectedKeys = {
	["vehicleNumber"] = { -- we want vehicleNumber to be set only on vehicles, with stricte numbers in range of 1-100
		allowForElements = {
			["vehicle"] = true,
		},
		allowedDataTypes = {
			["number"] = true,
		},
		allowedNumberRange = {1, 100},
	},
	["personalVehData"] = { -- we want be able to set personalVehData only on current vehicle, also it should be a string with length between 1-24
		onlyForOwnPlayerVeh = true,
		allowedDataTypes = {
			["string"] = true,
		},
		allowedStringLength = {1, 24},
	},
	-- perform security checks on keys stored in this table, in a convenient way
}

local function reportAndRevertDataChange(clientElement, sourceElement, dataKey, oldValue, newValue, failReason, forceRemove) -- helper function to log and revert changes
	local logClient = inspect(clientElement) -- in-depth view of player which forced element data sync
	local logSerial = getPlayerSerial(clientElement) or "N/A" -- client serial, or "N/A" if not possible, for some reason
	local logSource = inspect(sourceElement) -- in-depth view of element which received data
	local logOldValue = inspect(oldValue) -- in-depth view of old value
	local logNewValue = inspect(newValue) -- in-depth view of new value
	local logText = -- fill our report with data
		"*\n"..
		"Detected element data abnormality:\n"..
		"Client: "..logClient.."\n"..
		"Client serial: "..logSerial.."\n"..
		"Source: "..logSource.."\n"..
		"Data key: "..dataKey.."\n"..
		"Old data value: "..logOldValue.."\n"..
		"New data value: "..logNewValue.."\n"..
		"Fail reason: "..failReason.."\n"..
		"*"

	outputDebugString(logText, debugLevel, debugR, debugG, debugB) -- print it to debug

	if (forceRemove) then -- we don't want this element data key to exist at all
		removeElementData(sourceElement, dataKey) -- remove it

		return true -- return success and stop here, we don't need further checks
	end

	setElementData(sourceElement, dataKey, oldValue, true) -- revert changes, it will call onElementDataChange event, but will fail (stop) on first condition - because server (not client) forced change

	return true -- return success
end

local function handleDataChange(clientElement, sourceElement, dataKey, oldValue, newValue) -- the heart of our anti-cheat, which does all the magic security measurements, returns true if there was no altering from client (based on data from protectedKeys), false otherwise
	local protectedKey = protectedKeys[dataKey] -- look up whether key changed is stored in protectedKeys table

	if (not protectedKey) then -- if it's not

		if (allowOnlyProtectedKeys) then -- if we don't want garbage keys
			local failReason = "Key isn't present in protectedKeys" -- reason shown in report
			local forceRemove = true -- should key be completely removed

			reportAndRevertDataChange(clientElement, sourceElement, dataKey, oldValue, newValue, failReason, forceRemove) -- report accident, and handle (or not) this player

			return false -- return failure
		end

		return true -- this key isn't protected, let it through
	end

	local onlyForPlayerHimself = protectedKey.onlyForPlayerHimself -- if key has "self-set" lock
	local onlyForOwnPlayerVeh = protectedKey.onlyForOwnPlayerVeh -- if key has "self-vehicle" lock
	local allowForElements = protectedKey.allowForElements -- if key has element type check
	local allowedDataTypes = protectedKey.allowedDataTypes -- if key has allowed data type check

	if (onlyForPlayerHimself) then -- if "self-set" lock is active
		local matchingElement = (clientElement == sourceElement) -- verify whether player who set data is equal to element which received data

		if (not matchingElement) then -- if it's not matching
			local failReason = "Can only set on player himself" -- reason shown in report
			local forceRemove = false -- should key be completely removed

			reportAndRevertDataChange(clientElement, sourceElement, dataKey, oldValue, newValue, failReason, forceRemove) -- report accident, and handle (or not) this player

			return false -- return failure
		end
	end

	if (onlyForOwnPlayerVeh) then -- if "self-vehicle" lock is active
		local playerVehicle = getPedOccupiedVehicle(clientElement) -- get current vehicle of player which set data
		local matchingVehicle = (playerVehicle == sourceElement) -- check whether it matches the one which received data

		if (not matchingVehicle) then -- if it doesn't match
			local failReason = "Can only set on player's own vehicle" -- reason shown in report
			local forceRemove = false -- should key be completely removed

			reportAndRevertDataChange(clientElement, sourceElement, dataKey, oldValue, newValue, failReason, forceRemove) -- report accident, and handle (or not) this player

			return false -- return failure
		end
	end

	if (allowForElements) then -- check if it's one of them
		local elementType = getElementType(sourceElement) -- get type of element whose data changed
		local matchingElementType = allowForElements[elementType] -- verify whether it's allowed

		if (not matchingElementType) then -- this isn't matching
			local failReason = "Invalid element type" -- reason shown in report
			local forceRemove = false -- should key be completely removed

			reportAndRevertDataChange(clientElement, sourceElement, dataKey, oldValue, newValue, failReason, forceRemove) -- report accident, and handle (or not) this player

			return false -- return failure
		end
	end

	if (allowedDataTypes) then -- if there's allowed data types
		local valueType = type(newValue) -- get data type of value
		local matchingType = allowedDataTypes[valueType] -- check if it's one of allowed

		if (not matchingType) then -- if it's not then
			local failReason = "Invalid data type" -- reason shown in report
			local forceRemove = false -- should key be completely removed

			reportAndRevertDataChange(clientElement, sourceElement, dataKey, oldValue, newValue, failReason, forceRemove) -- report accident, and handle (or not) this player

			return false -- return failure
		end

		local allowedStringLength = protectedKey.allowedStringLength -- if key has specified string length check
		local dataString = (valueType == "string") -- make sure it's a string

		if (allowedStringLength and dataString) then -- if we should check string length
			local minLength = allowedStringLength[1] -- retrieve min length
			local maxLength = allowedStringLength[2] -- retrieve max length
			local stringLength = utf8.len(newValue) -- get length of data string
			local matchingLength = (stringLength >= minLength) and (stringLength <= maxLength) -- compare whether value fits in between

			if (not matchingLength) then -- if it doesn't
				local failReason = "Invalid string length (must be between "..minLength.."-"..maxLength..")" -- reason shown in report
				local forceRemove = false -- should key be completely removed

				reportAndRevertDataChange(clientElement, sourceElement, dataKey, oldValue, newValue, failReason, forceRemove) -- report accident, and handle (or not) this player

				return false -- return failure
			end
		end

		local allowedTableLength = protectedKey.allowedTableLength -- if key has table length check
		local dataTable = (valueType == "table") -- make sure it's a table

		if (allowedTableLength and dataTable) then -- if we should check table length
			local minLength = allowedTableLength[1] -- retrieve min length
			local maxLength = allowedTableLength[2] -- retrieve max length
			local minLengthAchieved = false -- variable which checks 'does minimum length was achieved'
			local maxLengthExceeded = false -- variable which checks 'does length has exceeds more than allowed maximum'
			local tableLength = 0 -- store initial table length

			for _, _ in pairs(newValue) do -- loop through whole table
				tableLength = (tableLength + 1) -- add + 1 on each table entry
				minLengthAchieved = (tableLength >= minLength) -- is length bigger or at very minimum we require
				maxLengthExceeded = (tableLength > maxLength) -- does table exceeded more than max length?

				if (maxLengthExceeded) then -- it is bigger than it should be
					break -- break the loop (due of condition above being worthy, it makes no point to count further and waste CPU, on a table which potentially could have huge amount of entries)
				end
			end

			local matchingLength = (minLengthAchieved and not maxLengthExceeded) -- check if min length has been achieved, and make sure that it doesn't go beyond max length

			if (not matchingLength) then -- this table doesn't match requirements
				local failReason = "Invalid table length (must be between "..minLength.."-"..maxLength..")" -- reason shown in report
				local forceRemove = false -- should key be completely removed

				reportAndRevertDataChange(clientElement, sourceElement, dataKey, oldValue, newValue, failReason, forceRemove) -- report accident, and handle (or not) this player

				return false -- return failure
			end
		end

		local allowedNumberRange = protectedKey.allowedNumberRange -- if key has allowed number range check
		local dataNumber = (valueType == "number") -- make sure it's a number

		if (allowedNumberRange and dataNumber) then -- if we should check number range
			local minRange = allowedNumberRange[1] -- retrieve min number range
			local maxRange = allowedNumberRange[2] -- retrieve max number range
			local matchingRange = (newValue >= minRange) and (newValue <= maxRange) -- compare whether value fits in between

			if (not matchingRange) then -- if it doesn't
				local failReason = "Invalid number range (must be between "..minRange.."-"..maxRange..")" -- reason shown in report
				local forceRemove = false -- should key be completely removed

				reportAndRevertDataChange(clientElement, sourceElement, dataKey, oldValue, newValue, failReason, forceRemove) -- report accident, and handle (or not) this player

				return false -- return failure
			end
		end
	end

	return true -- security checks passed, we are all clear with this data key
end

function onElementDataChangeAdvancedAC(dataKey, oldValue, newValue) -- this event makes use of handleDataChange, the code was split for better readability
	if (not client) then -- check if data is coming from client
		return false -- if it's not, do not continue
	end

	local approvedChange = handleDataChange(client, source, dataKey, oldValue, newValue) -- run our security checks

	if (approvedChange) then -- it's all cool and good
		return false -- we don't need further action
	end

	if (not punishPlayerOnDetect) then -- we don't want to punish player for some reason
		return false -- so stop here
	end
		
	if (punishmentBan) then -- if it's ban
		banPlayer(client, banByIP, banByUsername, banBySerial, punishedBy, punishmentReason, banTime) -- remove his presence from server
	else -- otherwise
		kickPlayer(client, punishedBy, punishmentReason) -- simply kick player out of server
	end
end
addEventHandler("onElementDataChange", root, onElementDataChangeAdvancedAC)
```

## Securing triggerServerEvent

- All parameters including **source** can be faked and should not be trusted.

- Global variable **client** can be trusted.

- **Admin** styled **events** should be verifying player (client) **ACL rights**, either by [isObjectInACLGroup](https://wiki.multitheftauto.com/wiki/IsObjectInACLGroup) or [hasObjectPermissionTo](https://wiki.multitheftauto.com/wiki/HasObjectPermissionTo).

- Do **not** use the same name for your custom event as MTA native server events (which aren't remotely triggerable by default), e.g: **onPlayerLogin**; doing so would open door for cheaters manipulations.

- Be aware to which players event is sent via [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md). For both security & performance reasons, admin like events should be received by admins only (to prevent confidential data being accessed), in the same time you shouldn't send each event to everyone on server (e.g: login success event which hides login panel for certain player). [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md) allows you to specify the event receiver as first (optional) argument. It defaults to [root](mta://reference/misc/root.md), meaning if you don't specify it, it will be sent to everyone connected to server - even those who are still downloading server cache (which results in *Server triggered clientside event eventName, but event is not added clientside.*). You can either pass player element or table with receivers:

```
local playersToReceiveEvent = {player1, player2, player3} -- each playerX is player element

triggerClientEvent(playersToReceiveEvent, ...) -- do not forget to fill the latter part of arguments
```

Click to collapse [-]
Server

Example of anti-cheat function designed for events, used for data validation for both normal, and admin events which are called from client-side.

```
--[[
	For maximum security set punishPlayerOnDetect, punishmentBan to true (as per default configuration)

	Anti-cheat (processServerEventData) table structure and it's options:

	checkACLGroup = { -- check whether player who called event belongs to at least one group below, set to false/nil to not check this
		"Admin",
	},
	checkPermissions = { -- check whether player who called event has permission to at least one thing below, set to false/nil to not check this
		"function.kickPlayer",
	},
	checkEventData = {
		{
			debugData = "source", -- optional details for report shown in debug message
			eventData = source, -- data we want to verify
			equalTo = client, -- compare whether eventData == equalTo
			allowedElements = { -- restrict eventData to be certain element type(s), set to false/nil or leave it empty to not check this (full list of element types: https://wiki.multitheftauto.com/wiki/GetElementsByType)
				["player"] = true,
				["ped"] = true,
				["vehicle"] = true,
				["object"] = true,
			},
			allowedDataTypes = { -- restrict eventData to be certain value type(s), set to false/nil or leave it empty to not check this
				["string"] = true,
				["number"] = true,
				["table"] = true,
				["boolean"] = true,
				["nil"] = true,
			},
			allowedStringLength = {1, 32}, -- if eventData is a string, then it's length must be in between (min-max), set it to false/nil to not check string length - do note that allowedDataTypes must contain ["string"] = true
			allowedTableLength = {1, 64}, -- if eventData is a table, then it's length must be in between (min-max), set it to false/nil to not check table length - do note that allowedDataTypes must contain ["table"] = true
			allowedNumberRange = {1, 128}, -- if eventData is a number, then it must be in between (min-max), set it to false/nil to not check number range - do note that allowedDataTypes must contain ["number"] = true
		},
	},
]]

local punishPlayerOnDetect = true -- should player be punished upon detection (make sure that resource which runs this code has admin rights)
local punishmentBan = true -- only relevant if punishPlayerOnDetect is set to true; use true for ban or false for kick
local punishmentReason = "Altering server event data" -- only relevant if punishPlayerOnDetect is set to true; reason which would be shown to punished player
local punishedBy = "Console" -- only relevant if punishPlayerOnDetect is set to true; who was responsible for punishing, as well shown to punished player
local banByIP = false -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; banning by IP nowadays is not recommended (...)
local banByUsername = false -- community username - legacy thing, hence is set to false and should stay like that
local banBySerial = true -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; (...) if there is a player serial to use instead
local banTime = 0 -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; time in seconds, 0 for permanent
local debugLevel = 4 -- this debug level allows to hide INFO: prefix, and use custom colors
local debugR = 255 -- debug message - red color
local debugG = 127 -- debug message - green color
local debugB = 0 -- debug message - blue color

function processServerEventData(clientElement, sourceElement, serverEvent, securityChecks) -- the heart of our anti-cheat, which does all the magic security measurements, returns true if there was no altering from client (based on data from securityChecks), false otherwise
	if (not securityChecks) then -- if we haven't passed any security checks
		return true -- nothing to check, let code go further
	end
	
	if (not clientElement) then -- if client variable isn't available for some reason (although it should never happen)
		local failReason = "Client variable not present" -- reason shown in report
		local skipPunishment = true -- should server skip punishment

		reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

		return false -- return failure
	end

	local checkACLGroup = securityChecks.checkACLGroup -- if there's any ACL groups to check
	local checkPermissions = securityChecks.checkPermissions -- if there's any permissions to check
	local checkEventData = securityChecks.checkEventData -- if there's any data checks

	if (checkACLGroup) then -- let's check player ACL groups
		local playerAccount = getPlayerAccount(clientElement) -- get current account of player
		local guestAccount = isGuestAccount(playerAccount) -- if account is guest (meaning player is not logged in)

		if (guestAccount) then -- it's the case
			local failReason = "Can't retrieve player login - guest account" -- reason shown in report
			local skipPunishment = true -- should server skip punishment

			reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

			return false -- return failure
		end

		local accountName = getAccountName(playerAccount) -- get name of player's current account
		local aclString = "user."..accountName -- format it for further use in isObjectInACLGroup function

		for groupID = 1, #checkACLGroup do -- iterate over table of given groups
			local groupName = checkACLGroup[groupID] -- get each group name
			local aclGroup = aclGetGroup(groupName) -- check if such group exists

			if (not aclGroup) then -- it doesn't
				local failReason = "ACL group '"..groupName.."' is missing" -- reason shown in report
				local skipPunishment = true -- should server skip punishment

				reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

				return false -- return failure
			end

			local playerInACLGroup = isObjectInACLGroup(aclString, aclGroup) -- check if player belong to the group

			if (playerInACLGroup) then -- yep, it's the case
				return true -- so it's a success
			end
		end

		local failReason = "Player doesn't belong to any given ACL group" -- reason shown in report
		local skipPunishment = true -- should server skip punishment

		reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

		return false -- return failure
	end

	if (checkPermissions) then -- check if player has at least one desired permission
		local allowedByDefault = false -- does he have access by default

		for permissionID = 1, #checkPermissions do -- iterate over all permissions
			local permissionName = checkPermissions[permissionID] -- get permission name
			local hasPermission = hasObjectPermissionTo(clientElement, permissionName, allowedByDefault) -- check whether player is allowed to perform certain action

			if (hasPermission) then -- if player has access
				return true -- one is available (and enough), server won't bother to check others (as return keywords also breaks loop)
			end
		end

		local failReason = "Not enough permissions" -- reason shown in report
		local skipPunishment = true -- should server skip punishment

		reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

		return false -- return failure
	end

	if (checkEventData) then -- if there is some data to verify

		for dataID = 1, #checkEventData do -- iterate over each of data
			local dataToCheck = checkEventData[dataID] -- get each data set
			local eventData = dataToCheck.eventData -- this is the one we'll be verifying
			local equalTo = dataToCheck.equalTo -- we want to compare whether eventData == equalTo
			local allowedElements = dataToCheck.allowedElements -- check whether is element, and whether belongs to certain element types
			local allowedDataTypes = dataToCheck.allowedDataTypes -- do we restrict data to be certain type?
			local debugData = dataToCheck.debugData -- additional helper data
			local debugText = debugData and " ("..debugData..")" or "" -- if it's present, format it nicely

			if (equalTo) then -- equal check exists
				local matchingData = (eventData == equalTo) -- compare whether those two values are equal

				if (not matchingData) then -- they aren't
					local failReason = "Data isn't equal @ argument "..dataID..debugText -- reason shown in report
					local skipPunishment = false -- should server skip punishment

					reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

					return false -- return failure
				end
			end

			if (allowedElements) then -- we do check whether is an element, and belongs to at least one given in the list
				local validElement = isElement(eventData) -- check if it's actual element

				if (not validElement) then -- it's not
					local failReason = "Data isn't element @ argument "..dataID..debugText -- reason shown in report
					local skipPunishment = false -- should server skip punishment

					reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

					return false -- return failure
				end

				local elementType = getElementType(eventData) -- it's element, so we want to know it's type
				local matchingElementType = allowedElements[elementType] -- verify whether it's allowed

				if (not matchingElementType) then -- it's not allowed
					local failReason = "Invalid element type @ argument "..dataID..debugText -- reason shown in report
					local skipPunishment = false -- should server skip punishment

					reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

					return false -- return failure
				end
			end

			if (allowedDataTypes) then -- let's check allowed data types
				local dataType = type(eventData) -- get data type
				local matchingType = allowedDataTypes[dataType] -- verify whether it's allowed

				if (not matchingType) then -- it isn't
					local failReason = "Invalid data type @ argument "..dataID..debugText -- reason shown in report
					local skipPunishment = false -- should server skip punishment

					reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

					return false -- return failure
				end

				local allowedStringLength = dataToCheck.allowedStringLength -- if data has string length check
				local dataString = (dataType == "string") -- make sure it's a string

				if (allowedStringLength and dataString) then -- if we should check string length
					local minLength = allowedStringLength[1] -- retrieve min length
					local maxLength = allowedStringLength[2] -- retrieve max length
					local stringLength = utf8.len(eventData) -- get length of data string
					local matchingLength = (stringLength >= minLength) and (stringLength <= maxLength) -- compare whether value fits in between

					if (not matchingLength) then -- if it doesn't
						local failReason = "Invalid string length (must be between "..minLength.."-"..maxLength..") @ argument "..dataID..debugText -- reason shown in report
						local skipPunishment = false -- should server skip punishment

						reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

						return false -- return failure
					end
				end

				local allowedTableLength = dataToCheck.allowedTableLength -- if data has table length check
				local dataTable = (dataType == "table") -- make sure it's a table

				if (allowedTableLength and dataTable) then -- if we should check table length
					local minLength = allowedTableLength[1] -- retrieve min length
					local maxLength = allowedTableLength[2] -- retrieve max length
					local minLengthAchieved = false -- variable which checks 'does minimum length was achieved'
					local maxLengthExceeded = false -- variable which checks 'does length has exceeds more than allowed maximum'
					local tableLength = 0 -- store initial table length

					for _, _ in pairs(eventData) do -- loop through whole table
						tableLength = (tableLength + 1) -- add + 1 on each table entry
						minLengthAchieved = (tableLength >= minLength) -- is length bigger or at very minimum we require
						maxLengthExceeded = (tableLength > maxLength) -- does table exceeded more than max length?

						if (maxLengthExceeded) then -- it is bigger than it should be
							break -- break the loop (due of condition above being worthy, it makes no point to count further and waste CPU, on a table which potentially could have huge amount of entries)
						end
					end

					local matchingLength = (minLengthAchieved and not maxLengthExceeded) -- check if min length has been achieved, and make sure that it doesn't go beyond max length

					if (not matchingLength) then -- this table doesn't match requirements
						local failReason = "Invalid table length (must be between "..minLength.."-"..maxLength..") @ argument "..dataID..debugText -- reason shown in report
						local skipPunishment = false -- should server skip punishment

						reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

						return false -- return failure
					end
				end

				local allowedNumberRange = dataToCheck.allowedNumberRange -- if data has number range check
				local dataNumber = (dataType == "number") -- make sure it's a number

				if (allowedNumberRange and dataNumber) then -- if we should check number range
					local minRange = allowedNumberRange[1] -- retrieve min number range
					local maxRange = allowedNumberRange[2] -- retrieve max number range
					local matchingRange = (eventData >= minRange) and (eventData <= maxRange) -- compare whether value fits in between

					if (not matchingRange) then -- if it doesn't
						local failReason = "Invalid number range (must be between "..minRange.."-"..maxRange..") @ argument "..dataID..debugText -- reason shown in report
						local skipPunishment = false -- should server skip punishment

						reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- report accident, and handle (or not) this player

						return false -- return failure
					end
				end
			end
		end
	end

	return true -- security checks passed, we are all clear with this event call
end

function reportAndHandleEventAbnormality(clientElement, sourceElement, serverEvent, failReason, skipPunishment) -- helper function to log and handle accidents
	local logClient = inspect(clientElement) -- in-depth view player which called event
	local logSerial = getPlayerSerial(clientElement) or "N/A" -- client serial, or "N/A" if not possible, for some reason
	local logSource = inspect(sourceElement) -- in-depth view of source element
	local logText = -- fill our report with data
		"*\n"..
		"Detected event abnormality:\n"..
		"Client: "..logClient.."\n"..
		"Client serial: "..logSerial.."\n"..
		"Source: "..logSource.."\n"..
		"Event: "..serverEvent.."\n"..
		"Reason: "..failReason.."\n"..
		"*"

	outputDebugString(logText, debugLevel, debugR, debugG, debugB) -- print it to debug

	if (not punishPlayerOnDetect or skipPunishment) then -- we don't want to punish player for some reason
		return true -- stop here
	end
		
	if (punishmentBan) then -- if it's ban
		banPlayer(clientElement, banByIP, banByUsername, banBySerial, punishedBy, punishmentReason, banTime) -- remove his presence from server
	else -- otherwise
		kickPlayer(clientElement, punishedBy, punishmentReason) -- simply kick player out of server
	end

	return true -- all done, report success
end

function onServerEvent(clientData)
	--[[
		Assume this server event (function) is called in such way:

		local dataToPass = 10

		triggerServerEvent("onServerEvent", localPlayer, dataToPass)
	]]

	local shouldProcessServerCode = processServerEventData(
		client, -- client element - responsible for calling event
		source, -- source element - passed in triggerServerEvent (as 2nd argument)
		eventName, -- name of event - in this case 'onServerEvent'
		{
			checkEventData = { -- we want to verify everything what comes from client
				{
					eventData = source, -- first to check, source variable
					equalTo = client, -- we want to check whether it matches player who called event
					debugData = "source", -- helper details which would be shown in report
				},
				{
					eventData = clientData, -- let's check the data which client sent to us
					allowedDataTypes = {
						["number"] = true, -- we want it to be only number
					},
					allowedNumberRange = {1, 100}, -- in range of 1 to 100
					debugData = "clientData", -- if something goes wrong, let server know where (it will appear in debug report)
				},
			},
		}
	)

	if (not shouldProcessServerCode) then -- something isn't right, no green light for processing code behind this scope
		return false -- stop code execution
	end

	-- do code as usual
end
addEvent("onServerEvent", true)
addEventHandler("onServerEvent", root, onServerEvent)

function onServerAdminEvent(playerToBan)
	--[[
		Assume this server admin event (function) is called in such way:

		local playerToBan = getPlayerFromName("playerToBan")

		triggerServerEvent("onServerAdminEvent", localPlayer, playerToBan)
	]]

	local shouldProcessServerCode = processServerEventData(
		client, -- client element - responsible for calling event
		source, -- source element - passed in triggerServerEvent (as 2nd argument)
		eventName, -- name of event - in this case 'onServerAdminEvent'
		{
			checkACLGroup = { -- we need to check whether player who called event belongs to ACL groups
				"Admin", -- in this case admin group
			},
			checkEventData = { -- we want to verify everything what comes from client
				{
					eventData = source, -- first to check, source variable
					equalTo = client, -- we want to check whether it matches player who called event
					debugData = "source", -- helper details which would be shown in report
				},
				{
					eventData = playerToBan, -- let's check the data which client sent to us
					allowedDataTypes = {
						["player"] = true, -- we want it to be player
					},
					debugData = "playerToBan", -- if something goes wrong, let server know where (it will appear in debug report)
				},
			},
		}
	)

	if (not shouldProcessServerCode) then -- something isn't right, no green light for processing code behind this scope
		return false -- stop code execution
	end

	-- do code as usual
end
addEvent("onServerAdminEvent", true)
addEventHandler("onServerAdminEvent", root, onServerAdminEvent)
```

## Securing server-only events

- It is very important to **disable remote triggering** ability in [addEvent](https://wiki.multitheftauto.com/wiki/AddEvent), to prevent calling server-side only events from client-side.

- **Admin** styled **events** should be verifying player **ACL rights**, either by [isObjectInACLGroup](https://wiki.multitheftauto.com/wiki/IsObjectInACLGroup) or [hasObjectPermissionTo](https://wiki.multitheftauto.com/wiki/HasObjectPermissionTo).

Click to collapse [-]
Server

This example shows how you should make event server-side only.

```
function onServerSideOnlyEvent()
	-- do some server-side stuff
end
addEvent("onServerSideOnlyEvent", false) -- set second argument (allowRemoteTriger) to false, so it can't be called from client
addEventHandler("onServerSideOnlyEvent", root, onServerSideOnlyEvent) -- associate our event with function onServerSideOnlyEvent
```

## Securing projectiles & explosions

This section (and **code** is **work in progress**) - **use at your own risk**.

Click to expand [+]
Server

Projectile ammo tracker:

```
local playerProjectileAmmo = {} -- store player-held weapons ammo here
local playerWeaponsToTrack = { -- keep track of ammo for certain player-held weapon types, basically those which create projectile; [weaponID] = weaponSlot
	[16] = 8, -- grenade
	[17] = 8, -- teargas
	[18] = 8, -- molotov
	[35] = 7, -- rocket launcher
	[36] = 7, -- rocket launcher (heat-seeking)
	[39] = 8, -- satchel charge
}

local function updateProjectileAmmoForPlayer(playerElement)
	local validElement = isElement(playerElement)

	if (not validElement) then
		return false
	end

	local playerDead = isPedDead(playerElement)

	if (playerDead) then
		return false
	end

	for weaponID, weaponSlot in pairs(playerWeaponsToTrack) do
		local weaponInSlot = getPedWeapon(playerElement, weaponSlot)
		local weaponTotalAmmo = getPedTotalAmmo(playerElement, weaponSlot)
		local weaponHasAmmo = (weaponTotalAmmo > 0)
		local weaponMatching = (weaponInSlot == weaponID)
		local updateWeaponAmmo = (weaponMatching and weaponHasAmmo)

		if (updateWeaponAmmo) then
			local storedProjectileAmmo = playerProjectileAmmo[playerElement]
			local newWeaponAmmo = (updateWeaponAmmo and weaponTotalAmmo or nil)

			if (not storedProjectileAmmo) then
				playerProjectileAmmo[playerElement] = {}
				storedProjectileAmmo = playerProjectileAmmo[playerElement]
			end

			storedProjectileAmmo[weaponID] = newWeaponAmmo
		end
	end

	return true
end

function hasPlayerProjectileAmmo(playerElement, projectileWeapon)
	local validElement = isElement(playerElement)

	if (not validElement) then
		return false
	end

	local playerDead = isPedDead(playerElement)

	if (playerDead) then
		return false
	end
	
	local projectileData = playerProjectileAmmo[playerElement]
	local projectileAmmo = (projectileData and projectileData[projectileWeapon])

	return projectileAmmo
end

function decreasePlayerProjectileAmmo(playerElement, projectileWeapon)
	local validElement = isElement(playerElement)

	if (not validElement) then
		return false
	end

	local playerDead = isPedDead(playerElement)

	if (playerDead) then
		return false
	end

	local playerProjectileData = playerProjectileAmmo[playerElement]

	if (not playerProjectileData) then
		return false
	end
	
	local projectileWeaponAmmo = playerProjectileData[projectileWeapon]
	local tempProjectileAmmo = (projectileWeaponAmmo - 1)
	local newProjectileAmmo = (tempProjectileAmmo > 0 and tempProjectileAmmo or nil)

	playerProjectileData[projectileWeapon] = newProjectileAmmo

	return true
end

function onPlayerWeaponSwitchAntiCheat(previousWeaponID, currentWeaponID)
	setTimer(updateProjectileAmmoForPlayer, 50, 1, source)
end
addEventHandler("onPlayerWeaponSwitch", root, onPlayerWeaponSwitchAntiCheat)

function onResourceStartAntiCheat()
	local playersTable = getElementsByType("player")

	for playerID = 1, #playersTable do
		local playerElement = playersTable[playerID]

		updateProjectileAmmoForPlayer(playerElement)
	end
end
addEventHandler("onResourceStart", resourceRoot, onResourceStartAntiCheat)

function onPlayerWastedQuitAntiCheat()
	playerProjectileAmmo[source] = nil
end
addEventHandler("onPlayerWasted", root, onPlayerWastedQuitAntiCheat)
addEventHandler("onPlayerQuit", root, onPlayerWastedQuitAntiCheat)
```

Click to expand [+]
Server

Projectile handler:

```
local playerCreatedProjectiles = {} -- store count of legitimately created player projectiles; [playerElement] = {[projectileType] = activeProjectiles}
local projectileTypes = {
	[16] = { -- Grenade
		projectileAllowed = true,
		projectileMaxDistanceFromCreator = 2,
		projectileAllowedWeapons = {
			[16] = true, -- grenade
		},
	},
	[17] = { -- Teargas
		projectileAllowed = true,
		projectileMaxDistanceFromCreator = 2,
		projectileAllowedWeapons = {
			[17] = true, -- teargas
		},
	},
	[18] = { -- Molotov
		projectileAllowed = true,
		projectileMaxDistanceFromCreator = 2,
		projectileAllowedWeapons = {
			[18] = true, -- molotov
		},
	},
	[19] = { -- Rocket
		projectileAllowed = true,
		projectileMaxDistanceFromCreator = 5,
		projectileMaxVelocity = 2,
		projectileAllowedWeapons = {
			[35] = true, -- rocket launcher
		},
		projectileAllowedVehicles = {
			[425] = true, -- hunter
			[520] = true, -- hydra
		},
	},
	[20] = { -- Rocket (heat-seeking)
		projectileAllowed = true,
		projectileMaxDistanceFromCreator = 5,
		projectileMaxVelocity = 2,
		projectileAllowedWeapons = {
			[36] = true, -- rocket launcher (heat-seeking)
		},
		projectileAllowedVehicles = {
			[520] = true, -- hydra
		},
	},
	[21] = { -- Airbomb
		projectileAllowed = true,
		projectileAllowedVehicles = {
			[520] = true, -- hydra
		},
	},
	[39] = { -- Satchel charge
		projectileAllowed = true,
		projectileMaxDistanceFromCreator = 2,
		projectileAllowedWeapons = {
			[39] = true, -- satchel charge
		},
	},
	[58] = { -- Hydra flare
		projectileAllowed = true,
		projectileMaxDistanceFromCreator = 5,
		projectileAllowedVehicles = {
			[520] = true, -- hydra
		},
	},
}

local reportAbnormality = true -- whether to report about abnormality in debug script - by default
local punishPlayerOnDetect = false -- should player be punished upon detection; true - yes, or false to not do anything (make sure that resource which runs this code has admin rights)
local punishmentBan = true -- only relevant if punishPlayerOnDetect is set to true; use true for ban or false for kick
local punishmentReason = "Projectile/explosion anti-cheat" -- only relevant if punishPlayerOnDetect is set to true; reason which would be shown to punished player
local punishedBy = "Console" -- only relevant if punishPlayerOnDetect is set to true; who was responsible for punishing, as well shown to punished player
local banByIP = false -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; banning by IP nowadays is not recommended (...)
local banByUsername = false -- community username - legacy thing, hence is set to false and should stay like that
local banBySerial = true -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; (...) if there is a player serial to use instead
local banTime = 0 -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; time in seconds, 0 for permanent
local debugMsgLevel = 4 -- this debug level allows to hide INFO: prefix, and use custom colors
local debugMsgR = 255 -- debug message - red color
local debugMsgG = 127 -- debug message - green color
local debugMsgB = 0 -- debug message - blue color

local function reportProjectileAbnormality(playerElement, projectileType, projectileX, projectileY, projectileZ, projectileForce, projectileTarget, projectileRX, projectileRY, projectileRZ, projectileVX, projectileVY, projectileVZ, detectionCode)
	local projectileSyncer = inspect(playerElement)
	local projectilePosition = projectileX..", "..projectileY..", "..projectileZ
	local projectileZoneName = getZoneName(projectileX, projectileY, projectileZ, false)
	local projectileCityName = getZoneName(projectileX, projectileY, projectileZ, true)
	local projectileLog =
		"* Detected projectile abnormality - "..detectionCode.." *\n"..
		"Projectile syncer: "..projectileSyncer.."\n"..
		"Projectile type: "..projectileType.."\n"..
		"Projectile position: "..projectilePosition.. " ("..projectileZoneName..", "..projectileCityName..")\n"

	outputDebugString(projectileLog, debugMsgLevel, debugMsgR, debugMsgG, debugMsgB)

	return true
end

local function processProjectileChecks(playerElement, projectileType, projectileX, projectileY, projectileZ, projectileForce, projectileTarget, projectileRX, projectileRY, projectileRZ, projectileVX, projectileVY, projectileVZ)
	local projectileData = projectileTypes[projectileType]
	local projectileAllowed = projectileData.projectileAllowed

	if (not projectileAllowed) then
		return false, "Projectile not allowed"
	end

	local projectileAllowedWeapons = projectileData.projectileAllowedWeapons

	if (projectileAllowedWeapons) then
		local playerWeapon = getPedWeapon(playerElement)
		local allowedWeapon = projectileAllowedWeapons[playerWeapon]

		if (not allowedWeapon) then
			return false, "Player is not holding correct weapon"
		end

		local weaponAmmo = hasPlayerProjectileAmmo(playerElement, playerWeapon)
		local playerHasAmmo = (weaponAmmo > 0)

		if (not playerHasAmmo) then
			return false, "Player doesn't have ammo for weapon"
		end

		decreasePlayerProjectileAmmo(playerElement, playerWeapon)
	end

	local playerVehicle = getPedOccupiedVehicle(playerElement)

	if (playerVehicle) then
		local projectileAllowedVehicles = projectileData.projectileAllowedVehicles

		if (projectileAllowedVehicles) then
			local vehicleModel = getElementModel(playerVehicle)
			local allowedVehicle = projectileAllowedVehicles[vehicleModel]

			if (not allowedVehicle) then
				return false, "Player is not inside allowed vehicles"
			end

			local vehicleDriver = getVehicleController(playerVehicle)
			local playerDriver = (playerElement == vehicleDriver)

			if (not playerDriver) then
				return false, "Player is not vehicle driver"
			end

			return true
		end

		return false, "Player in vehicle"
	end

	local projectileMaxDistanceFromCreator = projectileData.projectileMaxDistanceFromCreator

	if (projectileMaxDistanceFromCreator) then
		local playerX, playerY, playerZ = getElementPosition(playerElement)
		local distanceToProjectile = getDistanceBetweenPoints3D(playerX, playerY, playerZ, projectileX, projectileY, projectileZ)
		local matchingProjectileDistance = (distanceToProjectile <= projectileMaxDistanceFromCreator)

		if (not matchingProjectileDistance) then
			return false, "Projectile distance mismatch"
		end
	end

	local projectileMaxVelocity = projectileData.projectileMaxVelocity

	if (projectileMaxVelocity) then
		local projectileVelocity = (projectileVX ^ 2 + projectileVY ^ 2 + projectileVZ ^ 2)
		local projectileSpeed = math.sqrt(projectileVelocity)
		local matchingProjectileVelocity = (projectileSpeed <= projectileMaxVelocity)

		if (not matchingProjectileVelocity) then
			return false, "Projectile velocity mismatch"
		end
	end

	return true
end

local function trackPlayerProjectile(playerElement, projectileID)
	local validElement = isElement(playerElement)

	if (not validElement) then
		return false
	end

	local playerProjectiles = playerCreatedProjectiles[playerElement]

	if (not playerProjectiles) then
		playerCreatedProjectiles[playerElement] = {}
		playerProjectiles = playerCreatedProjectiles[playerElement]
	end

	local projectilesByType = playerProjectiles[projectileID] or 0
	local newProjectilesCount = (projectilesByType + 1)

	playerProjectiles[projectileID] = newProjectilesCount

	return true
end

local function getProjectileDetectionOverwrittenBehavior(projectileType)
	local projectileData = projectileTypes[projectileType]

	if (not projectileData) then
		return reportAbnormality, punishPlayerOnDetect, punishmentBan
	end

	local projectileBehaviour = projectileData.projectileOverwriteBehaviour

	if (not projectileBehaviour) then
		return reportAbnormality, punishPlayerOnDetect, punishmentBan
	end

	local overwriteReport = projectileBehaviour.reportAbnormality
	local overwritePunish = projectileBehaviour.punishPlayerOnDetect
	local overwriteBan = projectileBehaviour.punishmentBan

	return overwriteReport, overwritePunish, overwriteBan
end

function decreasePlayerProjectiles(playerElement, projectileID)
	local validElement = isElement(playerElement)

	if (not validElement) then
		return false
	end

	local playerProjectiles = playerCreatedProjectiles[playerElement]

	if (not playerProjectiles) then
		return false, true
	end

	local projectilesByType = playerProjectiles[projectileID]

	if (not projectilesByType) then
		return false, true
	end

	local tempProjectilesCount = (projectilesByType - 1)
	local newProjectilesCount = (tempProjectilesCount > 0 and tempProjectilesCount or nil)

	playerProjectiles[projectileID] = newProjectilesCount

	return true
end

function onPlayerProjectileCreationAntiCheat(projectileType, projectileX, projectileY, projectileZ, projectileForce, projectileTarget, projectileRX, projectileRY, projectileRZ, projectileVX, projectileVY, projectileVZ)
	local approvedProjectile, detectionCode = processProjectileChecks(source, projectileType, projectileX, projectileY, projectileZ, projectileForce, projectileTarget, projectileRX, projectileRY, projectileRZ, projectileVX, projectileVY, projectileVZ)

	if (approvedProjectile) then
		trackPlayerProjectile(source, projectileType)

		return true
	end

	local reportAbnormality, punishPlayerOnDetect, punishmentBan = getProjectileDetectionOverwrittenBehavior(projectileType)

	if (reportAbnormality) then
		reportProjectileAbnormality(source, projectileType, projectileX, projectileY, projectileZ, projectileForce, projectileTarget, projectileRX, projectileRY, projectileRZ, projectileVX, projectileVY, projectileVZ, detectionCode)
	end

	cancelEvent()

	if (not punishPlayerOnDetect) then -- we don't want to punish player for some reason
		return false -- so stop here
	end
		
	if (punishmentBan) then -- if it's ban
		banPlayer(source, banByIP, banByUsername, banBySerial, punishedBy, punishmentReason, banTime) -- remove his presence from server
	else -- otherwise
		kickPlayer(source, punishedBy, punishmentReason) -- simply kick player out of server
	end
end
addEventHandler("onPlayerProjectileCreation", root, onPlayerProjectileCreationAntiCheat)

function onPlayerQuitAntiCheat()
	playerCreatedProjectiles[source] = nil
end
addEventHandler("onPlayerQuit", root, onPlayerQuitAntiCheat)
```

Click to expand [+]
Server

Explosions handler:

```
local rocketInstantExplosionDistanceThreshold = 1.55 -- distance below which only explosion will be created (and not rocket projectile, hence not calling onPlayerProjectileCreation); do not change it
local explosionTypes = { -- more specific info on explosion, and whether it is allowed
	[0] = { -- Grenade
		explosionAllowed = true,
		explosionAllowedProjectiles = {
			[16] = true, -- grenade
		},
	},
	[1] = { -- Molotov
		explosionAllowed = true,
		explosionAllowedProjectiles = {
			[18] = true, -- molotov
		},
	},
	[2] = { -- Rocket
		explosionAllowed = true,
		explosionAllowedWeapons = {
			[35] = true, -- rocket launcher
			[36] = true, -- rocket launcher (heat-seeking)
		},
		explosionAllowedProjectiles = {
			[19] = true, -- rocket
			[20] = true, -- rocket (heat-seeking)
		},
	},
	[3] = { -- Rocket weak
		explosionAllowed = true,
		explosionAllowedProjectiles = {
			[19] = true, -- rocket
			[20] = true, -- rocket (heat-seeking)
		},
	},
	[4] = { -- Car
		explosionAllowed = true,
	},
	[5] = { -- Car quick
		explosionAllowed = true,
	},
	[6] = { -- Boat
		explosionAllowed = true,
	},
	[7] = { -- Heli
		explosionAllowed = true,
	},
	[8] = { -- Mine
		explosionAllowed = true,
	},
	[9] = { -- Object
		explosionAllowed = true,
	},
	[10] = { -- Tank grenade
		explosionAllowed = true,
		explosionMaxDistanceFromCreator = 80,
		explosionAllowedVehicles = {
			[432] = true,
		}
	},
	[11] = { -- Small
		explosionAllowed = true,
	},
	[12] = { -- Tiny
		explosionAllowed = true,
	},
}

local reportAbnormality = true -- whether to report about abnormality in debug script - by default
local punishPlayerOnDetect = false -- should player be punished upon detection; true - yes, or false to not do anything (make sure that resource which runs this code has admin rights)
local punishmentBan = true -- only relevant if punishPlayerOnDetect is set to true; use true for ban or false for kick
local punishmentReason = "Projectile/explosion anti-cheat" -- only relevant if punishPlayerOnDetect is set to true; reason which would be shown to punished player
local punishedBy = "Console" -- only relevant if punishPlayerOnDetect is set to true; who was responsible for punishing, as well shown to punished player
local banByIP = false -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; banning by IP nowadays is not recommended (...)
local banByUsername = false -- community username - legacy thing, hence is set to false and should stay like that
local banBySerial = true -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; (...) if there is a player serial to use instead
local banTime = 0 -- only relevant if punishPlayerOnDetect and punishmentBan is set to true; time in seconds, 0 for permanent
local debugMsgLevel = 4 -- this debug level allows to hide INFO: prefix, and use custom colors
local debugMsgR = 255 -- debug message - red color
local debugMsgG = 127 -- debug message - green color
local debugMsgB = 0 -- debug message - blue color

local function reportExplosionAbnormality(playerElement, explosionType, explosionX, explosionY, explosionZ, detectionCode)
	local explosionSyncer = inspect(playerElement)
	local explosionType = explosionType
	local explosionPosition = explosionX..", "..explosionY..", "..explosionZ
	local explosionZoneName = getZoneName(explosionX, explosionY, explosionZ, false)
	local explosionCityName = getZoneName(explosionX, explosionY, explosionZ, true)
	local explosionLog =
		"* Detected explosion abnormality - "..detectionCode.." *\n"..
		"Explosion syncer: "..explosionSyncer.."\n"..
		"Explosion type: "..explosionType.."\n"..
		"Explosion position: "..explosionPosition.. " ("..explosionZoneName..", "..explosionCityName..")\n"

	outputDebugString(explosionLog, debugMsgLevel, debugMsgR, debugMsgG, debugMsgB)

	return true
end

local function processExplosionChecks(playerElement, explosionType, explosionX, explosionY, explosionZ)
	local explosionData = explosionTypes[explosionType]
	local explosionAllowed = explosionData.explosionAllowed

	if (not explosionAllowed) then
		return false, "Explosion type not allowed"
	end

	local rocketExplosion = (explosionType == 2)

	if (rocketExplosion) then
		local playerX, playerY, playerZ = getElementPosition(playerElement)
		local distanceToExplosion = getDistanceBetweenPoints3D(playerX, playerY, playerZ, explosionX, explosionY, explosionZ)
		local instantExplosion = (distanceToExplosion < rocketInstantExplosionDistanceThreshold)

		if (instantExplosion) then
			local explosionAllowedWeapons = explosionData.explosionAllowedWeapons
			local playerWeapon = getPedWeapon(playerElement)
			local allowedWeapon = explosionAllowedWeapons[playerWeapon]

			if (not allowedWeapon) then
				return false, "Player is not holding rocket launcher"
			end

			local weaponAmmo = hasPlayerProjectileAmmo(playerElement, playerWeapon)
			local playerHasAmmo = (weaponAmmo > 0)

			if (not playerHasAmmo) then
				return false, "Player doesn't have ammo for rocket launcher"
			end

			decreasePlayerProjectileAmmo(playerElement, playerWeapon)

			return true
		end
	end

	local explosionAllowedProjectiles = explosionData.explosionAllowedProjectiles

	if (explosionAllowedProjectiles) then

		for projectileID, _ in pairs(explosionAllowedProjectiles) do
			local atleastOneProjectile = decreasePlayerProjectiles(playerElement, projectileID)

			if (atleastOneProjectile) then
				return true
			end
		end

		return false, "Explosion created without respective projectile"
	end

	local explosionAllowedVehicles = explosionData.explosionAllowedVehicles

	if (explosionAllowedVehicles) then
		local playerVehicle = getPedOccupiedVehicle(playerElement)

		if (not playerVehicle) then
			return false, "Player is not in vehicle"
		end

		local vehicleModel = getElementModel(playerVehicle)
		local allowedVehicle = explosionAllowedVehicles[vehicleModel]

		if (not allowedVehicle) then
			return false, "Player is inside not allowed vehicles"
		end

		local vehicleDriver = getVehicleController(playerVehicle)
		local playerDriver = (playerElement == vehicleDriver)

		if (not playerDriver) then
			return false, "Player is not vehicle driver"
		end
	end

	local explosionMaxDistanceFromCreator = explosionData.explosionMaxDistanceFromCreator

	if (explosionMaxDistanceFromCreator) then
		local playerX, playerY, playerZ = getElementPosition(playerElement)
		local distanceToExplosion = getDistanceBetweenPoints3D(playerX, playerY, playerZ, explosionX, explosionY, explosionZ)
		local matchingExplosionDistance = (distanceToExplosion < explosionMaxDistanceFromCreator)

		if (not matchingExplosionDistance) then
			return false, "Explosion distance mismatch"
		end
	end

	return true
end

local function getExplosionDetectionOverwrittenBehavior(explosionType)
	local explosionData = explosionTypes[explosionType]

	if (not explosionData) then
		return reportAbnormality, punishPlayerOnDetect, punishmentBan
	end

	local explosionBehaviour = explosionData.explosionOverwriteBehaviour

	if (not explosionBehaviour) then
		return reportAbnormality, punishPlayerOnDetect, punishmentBan
	end

	local overwriteReport = explosionBehaviour.reportAbnormality
	local overwritePunish = explosionBehaviour.punishPlayerOnDetect
	local overwriteBan = explosionBehaviour.punishmentBan

	return overwriteReport, overwritePunish, overwriteBan
end

function onExplosionAntiCheat(explosionX, explosionY, explosionZ, explosionType)
	local serverSyncExplosion = (source == root)

	if (serverSyncExplosion) then
		return true
	end

	local approvedExplosion, detectionCode = processExplosionChecks(source, explosionType, explosionX, explosionY, explosionZ)

	if (approvedExplosion) then
		return true
	end

	local reportAbnormality, punishPlayerOnDetect, punishmentBan = getExplosionDetectionOverwrittenBehavior(explosionType)

	if (reportAbnormality) then
		reportExplosionAbnormality(source, explosionType, explosionX, explosionY, explosionZ, detectionCode)
	end

	cancelEvent()

	if (not punishPlayerOnDetect) then -- we don't want to punish player for some reason
		return false -- so stop here
	end
		
	if (punishmentBan) then -- if it's ban
		banPlayer(source, banByIP, banByUsername, banBySerial, punishedBy, punishmentReason, banTime) -- remove his presence from server
	else -- otherwise
		kickPlayer(source, punishedBy, punishmentReason) -- simply kick player out of server
	end
end
addEventHandler("onExplosion", root, onExplosionAntiCheat)
```

## Handling non-registered events

See: [onPlayerTriggerInvalidEvent](mta://scripting/server/events/onplayertriggerinvalidevent.md)

## Handling events spam

See: [onPlayerTriggerEventThreshold](mta://scripting/server/events/onplayertriggereventthreshold.md)
