---
doc_id: "mta-wiki:3856"
title: "SetCameraInterior"
source_title: "SetCameraInterior"
source_url: "https://wiki.multitheftauto.com/wiki/SetCameraInterior"
revision_id: 67476
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:38.495420+00:00"
---

# SetCameraInterior

Sets the interior of the local camera. Only the interior of the camera is changed, the local player stays in the interior he was in.

## Syntax

Click to collapse [-]
Server

```
bool setCameraInterior ( player thePlayer, int interior )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):setCameraInterior(...)*

**Variable**: *.cameraInterior*

**Counterpart**: *[getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)*

### Required Arguments

- **thePlayer:** the player whose camera interior will be set.

- **interior:** the interior to place the camera in.

Click to collapse [-]
Client

```
bool setCameraInterior ( int interior )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Camera.setInterior(...)*

**Variable**: *.interior*

**Counterpart**: *[getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)*

### Required Arguments

- **interior:** the interior to place the camera in.

### Returns

Returns *true* if the camera's interior was changed successfully, *false* otherwise.

## Example

Click to collapse [-]
Server

**This example make a command to change your cam interior to a selected one.**

```
function setCamInt( thePlayer, commandName, intID )
        if( intID )then -- If there is an ID
		local seted = setCameraInterior( thePlayer, intID ) -- set the interior to the camera
                if( seted )then -- If it has been changed correctly
                        outputChatBox( "Your camera's interior has been set to "..intID, thePlayer ) -- Tell to the player his new camera's interior
                else -- otherwise
                        outputChatBox( "Can't change your camera's interior...", thePlayer, 255, 0, 0 ) -- Tell him the change failed
                end
	else -- otherwise 
		outputChatBox( "Syntax: /caminterior [interiorID] ", thePlayer, 255, 0, 0 ) -- Tell him the correct syntax
	end
end
addCommandHandler( "caminterior", setCamInt )
```

Click to collapse [-]
Client

**This example make a command to change your cam interior to a selected one.**

```
function setCam(command,int)
    if (int) then
		local setInt = setCameraInterior(int)
                if (setInt) then
                        outputChatBox("Your camera's interior has been set to "..int,255,255,0)
                else
                        outputChatBox("Can't change your camera's interior...",255,0,0)
                end
	else
		outputChatBox("Syntax: /camera [interiorID] ",255,0,0)
	end
end
addCommandHandler("camera",setCam)
```

## See Also

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

- setCameraInterior

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
