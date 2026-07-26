---
doc_id: "mta-wiki:3364"
title: "Vehicle default colors"
source_title: "Vehicle default colors"
source_url: "https://wiki.multitheftauto.com/wiki/Vehicle_default_colors"
revision_id: 19454
language: "en"
categories: []
generated_at: "2026-07-26T16:16:53.383206+00:00"
---

# Vehicle default colors

This file is copied from the MTA:DM Server.  

**File Name:** vehiclecolors.conf  

**File Location:** <MTAPath>\server\mods\deathmatch  

  

This file defines the color combinations a vehicle can have.

## File Syntax

[Vehicle ID] [Color 1] [Color 2] [Color 3] [Color 4]  

  

Note that most vehicles don't need more than two colors.   You can specify a vehicle ID more than once to specify more than one combination for a vehicle. The color combination used for a vehicle is randomly decided each time a player spawns in a vehicle.

If you mess this file up, just delete it and the server will generate a new file with GTA's default values in it.

## Example

In this example, vehicle ID 445 is being set colors for the server to use when the vehicle is created, you can add your own by adding new ones under it or anywhere inside this file as long as the syntax follows the example above.  

  

[Vehicle Color Pallete](mta://reference/misc/vehicle-colors.md)

| 445 34 34 445 35 35 445 37 37 445 39 39 445 41 41 445 43 43 445 45 45 |
| --- |
