---
doc_id: "mta-wiki:14199"
title: "SCamera"
source_title: "SCamera"
source_url: "https://wiki.multitheftauto.com/wiki/SCamera"
revision_id: 81857
language: "en"
categories: ["Useful_Functions"]
---

# SCamera

This function creates a speed camera in-game, fines speeding vehicles, and notifies the driver and take money from player based on vehicle speed.

## Syntax

```
function sCamera(modelId, x, y, z, speed, between)
```

## Parameters

- modelId: The model ID of the camera object to be created.

- x, y, z: The coordinates where the camera object will be placed in the game world.

- speed: The speed limit that vehicles should not exceed.

- between: The maximum distance from the camera at which a vehicle can be detected.

## Description

The sCamera function creates a camera object at a specified location in the game world. It then sets up a timer to check the speed of all vehicles in the game every second. If a vehicle is found to be exceeding the defined speed limit and is within a certain distance from the camera, the driver of the vehicle is fined. The fine is calculated based on the vehicle’s speed, and a message is displayed to the driver informing them of the fine.

## Code

Click to collapse [-]
Server

The function creates a speed camera in-game, fines speeding vehicles, and notifies the driver and take money from player based on vehicle speed.

```
function sCamera(modelId, x, y, z, speed, between)
    local camera = createObject(modelId, x, y, z)

    local speedLimit = speed

    local speedCheckTimer = setTimer(
        function()
            local vehicles = getElementsByType("vehicle")
            for i, vehicle in ipairs(vehicles) do
                local vx, vy, vz = getElementVelocity(vehicle)
                local vehicleSpeed = (vx^2 + vy^2 + vz^2)^(0.5) * 180
                local x1, y1, z1 = getElementPosition(vehicle)
                local x2, y2, z2 = getElementPosition(camera)
                local distance = getDistanceBetweenPoints3D(x1, y1, z1, x2, y2, z2)
                if vehicleSpeed > speedLimit and distance < between then
                    local driver = getVehicleOccupant(vehicle, 0)
                    if driver then
                        local fine = 0
                        local speedFines = {
                            {maxSpeed = 10, fine = 150},
                            {maxSpeed = 20, fine = 350},
                            {maxSpeed = 50, fine = 1250},
                            {maxSpeed = math.huge, fine = 2250},
                        }
                        for _, value in ipairs(speedFines) do
                            if vehicleSpeed <= value.maxSpeed then
                                fine = value.fine
                            end
                        end
                        takePlayerMoney(driver, fine)
                        fadeCamera(driver, false, 0.4 , 255,255,255)
                        setTimer(fadeCamera, 250, 1, driver, true, 1.0)
                        outputChatBox("You were caught speeding by a traffic enforcement camera! You've been fined $" .. fine .. ".", driver, 255, 0, 0)
                    end
                end
            end
        end,
        1000, 0 
    )
end
```

## Example Code

Click to collapse [-]
Server

The function creates a speed camera in-game, fines speeding vehicles, and notifies the driver and take money from player based on vehicle speed.

```
-- Create a speed camera at coordinates (-710.23791503906, 688.37194824219, 17.034782409668) with a speed limit of 70 and a detection range of 15 units
sCamera(1286, -710.23791503906, 688.37194824219, 17.034782409668, 70, 15)
```

By : [KhaledX](https://forum.multitheftauto.com/profile/52553-khaledx/)
