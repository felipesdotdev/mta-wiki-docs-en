---
doc_id: "mta-wiki:8358"
title: "SetCameraShakeLevel"
source_title: "SetCameraShakeLevel"
source_url: "https://wiki.multitheftauto.com/wiki/SetCameraShakeLevel"
revision_id: 76932
language: "en"
categories: ["Client_functions", "Deprecated", "Changes_in_1.5", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:38.575391+00:00"
---

# SetCameraShakeLevel

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setCameraDrunkLevel instead. Deprecated as of 1.6.0 r21795. |  |

This function sets the camera shake level (as seen on the *Are you going to San Fierro?* singleplayer mission).

## Syntax

```
bool setCameraShakeLevel ( int shakeLevel )
```

### Required arguments

- **shakeLevel**: an integer between 0 and 255, which represents the camera shake intensity level.

### Returns

Returns *true* if the camera shake level was changed, *false* if the required argument is incorrect or missing.

## Example

This example adds a */camshake* command which allows any player to manually change its camera shake level.

```
addCommandHandler( "camshake",
    function( _, level )
        local level = math.floor( level )
        if level and level >=0 and level <= 255 then
            setCameraShakeLevel( level )
            outputChatBox( "Camera shake level updated to " .. level .. "." )
        else
            outputChatBox( "Camera shake level must be between 0 and 255." )
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

- [setCameraDrunkLevel](mta://scripting/client/functions/setcameradrunklevel.md)

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
