---
doc_id: "mta-wiki:14071"
title: "SetCameraDrunkLevel"
source_title: "SetCameraDrunkLevel"
source_url: "https://wiki.multitheftauto.com/wiki/SetCameraDrunkLevel"
revision_id: 80955
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:38.430387+00:00"
---

# SetCameraDrunkLevel

ADDED/UPDATED IN VERSION 1.6.0 [r21795](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21795):

This function sets the camera drunk level (as seen on the *Are you going to San Fierro?* singleplayer mission). This function was renamed from [setCameraShakeLevel](mta://scripting/client/functions/setcamerashakelevel.md). 

Drunk effect is a wavy motion of the camera depicting the player being drunk. This function used to be called [setCameraShakeLevel](mta://scripting/client/functions/setcamerashakelevel.md) which has since been deprecated.

## Syntax

```
bool setCameraDrunkLevel ( int shakeLevel )
```

### Required arguments

- **drunkLevel**: an integer between 0 and 255, which represents the camera drunk intensity level.

### Returns

Returns *true* if the camera drunk level was changed, *false* if the required argument is incorrect or missing.

## Example

This example adds a */camdrunk* command which allows any player to manually change its camera drunk level.

```
addCommandHandler( "camdrunk",
    function( _, level )
        local level = math.floor( level )
        if level and level >= 0 and level <= 255 then
            setCameraDrunkLevel( level )
            outputChatBox( "Camera drunk level updated to " .. level .. "." )
        else
            outputChatBox( "Camera drunk level must be between 0 and 255." )
        end
    end
)
```

## See also

- [getCamera](mta://scripting/client/functions/getcamera.md)

- [getCameraClip](mta://scripting/client/functions/getcameraclip.md)

- [getCameraFieldOfView](mta://scripting/client/functions/getcamerafieldofview.md)

- [getCameraGoggleEffect](mta://scripting/client/functions/getcameragoggleeffect.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21795](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21795):

- [getCameraDrunkLevel](mta://scripting/client/functions/getcameradrunklevel.md)

- [getCameraViewMode](mta://scripting/client/functions/getcameraviewmode.md)

- [setCameraClip](mta://scripting/client/functions/setcameraclip.md)

- [setCameraFieldOfView](mta://scripting/client/functions/setcamerafieldofview.md)

- [setCameraGoggleEffect](mta://scripting/client/functions/setcameragoggleeffect.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21795](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21795):

- setCameraDrunkLevel

- [setCameraViewMode](mta://scripting/client/functions/setcameraviewmode.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22631](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22631):

- [shakeCamera](mta://scripting/client/functions/shakecamera.md)

- [resetShakeCamera](mta://scripting/client/functions/resetshakecamera.md)

- **Shared**

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
