---
doc_id: "mta-wiki:2315"
title: "FadeCamera"
source_title: "FadeCamera"
source_url: "https://wiki.multitheftauto.com/wiki/FadeCamera"
revision_id: 68491
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# FadeCamera

This function will fade a player's camera to a color or back to normal over a specified time period. This will also affect the sound volume for the player (50% faded = 50% volume, full fade = no sound). For clientside scripts you can perform 2 fade ins or fade outs in a row, but for serverside scripts you must use one then the other.

| [[{{{image}}}\|link=\|]] | Note: The speed of the effect depends directly on the current gamespeed. |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
bool fadeCamera ( player thePlayer, bool fadeIn, [ float timeToFade = 1.0, int red = 0, int green = 0, int blue = 0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):fadeCamera(...)*

### Required Arguments

- **thePlayer:** The player whose camera you wish to fade.

- **fadeIn:** Should the camera be faded in or out? Pass *true* to fade the camera in, *false* to fade it out to a color.

### Optional Arguments

- **timeToFade:** The number of seconds it should take to fade.

- **red:** The amount of red in the color that the camera fades out to (0 - 255). Not required for fading in.

- **green:** The amount of green in the color that the camera fades out to (0 - 255). Not required for fading in.

- **blue:** The amount of blue in the color that the camera fades out to (0 - 255). Not required for fading in.

Click to collapse [-]
Client

```
bool fadeCamera ( bool fadeIn, [ float timeToFade = 1.0, int red = 0, int green = 0, int blue = 0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Camera.fade(...)*

### Required Arguments

- **fadeIn:** Should the camera be faded in our out? Pass *true* to fade the camera in, *false* to fade it out to a color.

### Optional Arguments

- **timeToFade:** The number of seconds it should take to fade.

- **red:** The amount of red in the color that the camera fades out to (0 - 255). Not required for fading in.

- **green:** The amount of green in the color that the camera fades out to (0 - 255). Not required for fading in.

- **blue:** The amount of blue in the color that the camera fades out to (0 - 255). Not required for fading in.

### Returns

Returns *true* if the camera was faded successfully, *false* if invalid arguments were passed to the function.

## Example

Click to collapse [-]
Server example

When a player gets damaged, place a quick fade-to-red effect on his screen.

```
function addRednessOnDamage ( )
      fadeCamera ( source, false, 1.0, 255, 0, 0 )         -- fade the player's camera to red over a period of 1 second
      setTimer ( fadeCameraDelayed, 500, 1, source )   -- don't let it go to opaque red, interrupt it after half a second and fade back to normal
end
addEventHandler ( "onPlayerDamage", root, addRednessOnDamage )

function fadeCameraDelayed(player) -- This function prevents debug warnings when the player disconnects while the timer is running.
      if (isElement(player)) then
            fadeCamera(player, true, 0.5)
      end
end
```

## See Also

- fadeCamera

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
