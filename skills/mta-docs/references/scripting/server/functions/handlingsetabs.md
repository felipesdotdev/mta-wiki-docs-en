---
doc_id: "mta-wiki:3894"
title: "HandlingSetABS"
source_title: "HandlingSetABS"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingSetABS"
revision_id: 82308
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
---

# HandlingSetABS

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setVehicleHandling instead. |  |

Turns ABS on or off for a handling element.

## Syntax

```
bool handlingSetABS ( handling theHandling, bool ABS )
```

### Required Arguments

- **theHandling:** the handling of which you want to toggle the ABS.

- **ABS:** *true* to turn ABS on, *false* to turn it off.

### Returns

Returns *true* on success, *false* in case of failure.

## Example

```
function turnABS(thePlayer)
	local theVehicle = getPedOccupiedVehicle(thePlayer) -- Get thePlayer vehicle
	if not theVehicle then return end -- if the player is not in the vehicle then cancel
		local ABS = getVehicleHandlingProperty(theVehicle,"ABS") -- We will use the additional function that you will find under this one. That will be more convenient.
		if ABS == true then -- Check, if ABS is turn on then turn its off.
			setVehicleHandling(theVehicle,"ABS",false)
			outputChatBox("You turn off ABS",thePlayer)
		else -- ABS is off. Turn on this.
	setVehicleHandling(theVehicle,"ABS",true)
	outputChatBox("You turn on ABS",thePlayer)
    end
end
	addCommandHandler("ABS",turnABS)
	
	function getVehicleHandlingProperty ( element, property )
    if isElement ( element ) and getElementType ( element ) == "vehicle" and type ( property ) == "string" then -- Make sure there's a valid vehicle and a property string
        local handlingTable = getVehicleHandling ( element ) -- Get the handling as table and save as handlingTable
        local value = handlingTable[property] -- Get the value from the table
        
        if value then -- If there's a value (valid property) 
			return value -- Return it
        end
    end
    
    return false -- Not an element, not a vehicle or no valid property string. Return failure
end
```

## See Also
