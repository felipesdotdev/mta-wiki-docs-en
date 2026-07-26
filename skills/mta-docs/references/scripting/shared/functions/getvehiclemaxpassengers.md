---
doc_id: "mta-wiki:1381"
title: "GetVehicleMaxPassengers"
source_title: "GetVehicleMaxPassengers"
source_url: "https://wiki.multitheftauto.com/wiki/GetVehicleMaxPassengers"
revision_id: 76278
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetVehicleMaxPassengers

This function returns the maximum number of passengers that a specified vehicle can hold. Only passenger seats are counted, the driver seat is excluded.

| [[{{{image}}}\|link=\|]] | Important Note: Only passenger seats are counted, the driver seat is excluded. |
| --- | --- |
|  |  |

## Syntax

```
int getVehicleMaxPassengers ( vehicle theVehicle / int modelID )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle):getMaxPassengers(...)*

**Variable**: *.maxPassengers*

### Required Arguments

- **theVehicle:** the [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) that you wish to know the maximum capacity of.

OR

- **modelID:** the model id that you wish to know the maximum capacity of.

### Returns

Returns an [int](mta://reference/misc/int.md) indicating the maximum number of passengers that can enter a vehicle. Returns **false** if vehicle (or its ID) is a trailer

## Example

This example creates a vehicle then gets the number of passenger seats and outputs it in the chat box.

```
newcar = createVehicle ( 520, 1024, 1024, 1024 ) -- create a vehicle
numseats = getVehicleMaxPassengers ( newcar ) -- get the passenger seat count
outputChatBox ( "This vehicle supports " .. numseats .. " passengers." ) -- show it in the chat
```

## See Also
