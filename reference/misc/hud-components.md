---
doc_id: "mta-wiki:14513"
title: "HUD Components"
source_title: "HUD Components"
source_url: "https://wiki.multitheftauto.com/wiki/HUD_Components"
revision_id: 81596
language: "en"
categories: ["Scripting_Concepts"]
generated_at: "2026-07-26T16:15:42.357099+00:00"
---

# HUD Components

This page contains a list of HUD components and their properties.

### Components

- **all:** All of the following at the same time

- **ammo:** The display showing how much ammo the player has in their weapon

- **area_name:** The text that appears containing the name of the area a player has entered

- **armour:** The display showing the player's armor

- **breath:** The display showing the player's breath

- **clock:** The display showing the in-game time

- **health:** The display showing the player's health

- **money:** The display showing how much money the player has

- **radar:** The bottom-left corner miniradar

- **vehicle_name:** The text that appears containing the player's vehicle name when the player enters a vehicle

- **weapon:** The display showing the player's weapon

- **radio:** The display showing the radio label

- **wanted:** The display showing the player's wanted level

- **crosshair:** The weapon crosshair and sniper scope

## Properties

Properties used in functions [setPlayerHudComponentProperty](mta://scripting/client/functions/setplayerhudcomponentproperty.md), [getPlayerHudComponentProperty](mta://scripting/client/functions/getplayerhudcomponentproperty.md) and [resetPlayerHudComponentProperty](mta://scripting/client/functions/resetplayerhudcomponentproperty.md). Components like **crosshair**, **radar** remain unchanged and are not supported by these functions.

### General

- **position (x, y):** The position of the component.

- **size (w, h):** The size of the component. For text components, this corresponds to font scale.

- **fillColor (number tocolor):** The primary color of the component, e.g., bar fill color, weapon icon color or text color.

- **FillColorSecondary (number tocolor):** A secondary color, used for components like

- **money** Color when the value is negative.

- **wanted** Color of "empty" stars.

- **weapon** Specific color for the fist icon.

- **radio** Text color when a station is "loading" (this seems to be skipped in MTA).

- **useCustomAlpha (bool):** By default, settings like **fillColor** and **dropColor** ignore the provided alpha value to preserve original fade-in/fade-out animations. Use this parameter to override that behavior.

- **all:** Used for resetting all properties of a component in [resetPlayerHudComponentProperty](mta://scripting/client/functions/resetplayerhudcomponentproperty.md).

### Bars

- **drawBlackBorder (bool):** Adds a black border around the bar.

- **drawPercentage (bool):** Displays the percentage value as text on the bar.

- **blinkingValue (number):** Specific to the health bar, determines the HP threshold below which the bar will start blinking.

### Texts

- **dropColor (number tocolor):** The color of the text's shadow or outline.

- **fontOutline (number):** The size of the text's outline.

- **fontShadow (number):** The shadow offset for the text.

- **fontStyle (string):** - The font style, selected from GTA's default fonts:

- **menu**

- **subtitles**

- **pricedown**

- **gothic**

- **fontAlignment (string):** Specifies the text alignment, useful for custom positioning

- **left**

- **right**

- **center**

- **proportional (bool):** Adjusts uneven character spacing when changing fonts.

- **textSize (w, h):** Read-only, returns the width and height of the text for the specified component.
