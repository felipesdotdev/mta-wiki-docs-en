---
doc_id: "mta-wiki:14512"
title: "SetPlayerHudComponentProperty"
source_title: "SetPlayerHudComponentProperty"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerHudComponentProperty"
revision_id: 81669
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:43.765870+00:00"
---

# SetPlayerHudComponentProperty

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

This function allows for modifying HUD properties, such as text or bar color, position, size, and more. 

| [[{{{image}}}\|link=\|]] | Note: Due to a rendering bug in GTA, setting transparency for text with outline or shadow causes a visual glitch, resulting in blurred/smudged text. Transparency only works correctly on text without outline and shadow. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: If the characters are uneven after changing the font, you should set the proportional property to true |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: The health bar is positioned relative to its width, so after changing its width, its position on the X-axis will also change. If you want to maintain the bar's position, you also need to calculate its position based on its width. Additionally, the width is calculated depending on the MAX_HEALTH stat. |
| --- | --- |
|  |  |

 

Example of a modified HUD.

## Syntax

```
bool setPlayerHudComponentProperty (string component, string property, mixed value)
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):setHudComponentProperty(...)*

**Counterpart**: *[getPlayerHudComponentProperty](mta://scripting/client/functions/getplayerhudcomponentproperty.md)*

### Required Arguments

- **component:** The component you wish to modify. See [HUD Components](mta://reference/misc/hud-components.md).

- **property:** The name of the property you want to modify. See [HUD Properties](mta://reference/misc/hud-components.md).

- **value:** The value you want to set.

### Returns

Returns **true** if the property was successfully modified, **false** otherwise.

## Example

This example makes the HUD look like it does in the picture on the side.

```
addEventHandler('onClientResourceStart', resourceRoot, function()
    setPlayerHudComponentProperty('clock', 'fillColor', tocolor(50, 168, 82, 255))
    setPlayerHudComponentProperty('clock', 'dropColor', tocolor(94, 14, 7, 255))
    setPlayerHudComponentProperty('clock', 'fontOutline', 1)
    setPlayerHudComponentProperty('clock', 'fontStyle', 'subtitles')
    setPlayerHudComponentProperty('clock', 'proportional', true)

    setPlayerHudComponentProperty('money', 'fillColor', tocolor(11, 102, 158, 255))
    setPlayerHudComponentProperty('money', 'fillColorSecondary', tocolor(176, 23, 130, 255))
    setPlayerHudComponentProperty('money', 'fontOutline', 1)
    setPlayerHudComponentProperty('money', 'fontStyle', 'subtitles')

    setPlayerHudComponentProperty('health', 'fillColor', tocolor(50, 168, 82, 255))

    setPlayerHudComponentProperty('ammo', 'fillColor', tocolor(245, 66, 126, 255))
    setPlayerHudComponentProperty('weapon', 'fillColor', tocolor(235, 76, 52, 255))

    setPlayerHudComponentProperty('wanted', 'fillColorSecondary', tocolor(140, 138, 137, 255))
    setPlayerHudComponentProperty('wanted', 'fillColor', tocolor(66, 33, 252, 255))
end)
```

## See Also

- [getLocalPlayer](mta://scripting/client/functions/getlocalplayer.md)

- [getPlayerMapBoundingBox](mta://scripting/client/functions/getplayermapboundingbox.md)

- [getPlayerMapOpacity](mta://scripting/client/functions/getplayermapopacity.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [getPlayerHudComponentProperty](mta://scripting/client/functions/getplayerhudcomponentproperty.md)

- [isPlayerMapVisible](mta://scripting/client/functions/isplayermapvisible.md)

- [isPlayerHudComponentVisible](mta://scripting/client/functions/isplayerhudcomponentvisible.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22751](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22751):

- [isPlayerCrosshairVisible](mta://scripting/client/functions/isplayercrosshairvisible.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [resetPlayerHudComponentProperty](mta://scripting/client/functions/resetplayerhudcomponentproperty.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- setPlayerHudComponentProperty

- **Shared**

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- [forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)

- [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md)

- [getPlayerFromName](mta://scripting/shared/functions/getplayerfromname.md)

- [getPlayerMoney](mta://scripting/shared/functions/getplayermoney.md)

- [getPlayerName](mta://scripting/shared/functions/getplayername.md)

- [getPlayerNametagColor](mta://scripting/shared/functions/getplayernametagcolor.md)

- [getPlayerNametagText](mta://scripting/shared/functions/getplayernametagtext.md)

- [getPlayerPing](mta://scripting/shared/functions/getplayerping.md)

- [getPlayerWantedLevel](mta://scripting/shared/functions/getplayerwantedlevel.md)

- [givePlayerMoney](mta://scripting/shared/functions/giveplayermoney.md)

- [isPlayerMapForced](mta://scripting/shared/functions/isplayermapforced.md)

- [isPlayerNametagShowing](mta://scripting/shared/functions/isplayernametagshowing.md)

- [setPlayerHudComponentVisible](mta://scripting/shared/functions/setplayerhudcomponentvisible.md)

- [setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md)

- [setPlayerNametagColor](mta://scripting/shared/functions/setplayernametagcolor.md)

- [setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md)

- [setPlayerNametagText](mta://scripting/shared/functions/setplayernametagtext.md)

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)
