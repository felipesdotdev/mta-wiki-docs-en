---
doc_id: "mta-wiki:6054"
title: "TakePlayerScreenShot"
source_title: "TakePlayerScreenShot"
source_url: "https://wiki.multitheftauto.com/wiki/TakePlayerScreenShot"
revision_id: 82148
language: "en"
categories: ["Server_functions"]
---

# TakePlayerScreenShot

This function forces a client to capture the current screen output and send it back to the server. The image will contain the GTA HUD and the output of any dxDraw functions that are not flagged as 'post GUI'. The image specifically excludes the chat box and all GUI (including the client console). The result is received with the event [onPlayerScreenShot](mta://scripting/server/events/onplayerscreenshot.md).

## Syntax

```
bool takePlayerScreenShot ( player thePlayer, int width, int height [, string tag = "", int quality = 30, int maxBandwidth = 5000, int maxPacketSize = 500 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):takeScreenShot(...)*

### Required Arguments

- **thePlayer:** the player to get the screen capture from.

- **width:** the width of the capture image.

- **height:** the height of the capture image.

### Optional Arguments

- **tag:** A string to help identify the screen capture. The string is passed to the matching [onPlayerScreenShot](mta://scripting/server/events/onplayerscreenshot.md) event for your personal convenience.

- **quality:** Quality of the final JPEG image from 0 to 100. A lower value can reduce the memory used by the image considerably which will result in faster and less intrusive uploads.

- **maxBandwidth:** The amount of client upload bandwidth to use (in bytes per second) when sending the image.

- **maxPacketSize:** The maximum size of one packet.

### Returns

Returns *true* if the function was successfully, *false* if invalid arguments are specified.

## Examples

This example will take a player screenshot whenever a player takes a picture with the camera weapon and then send the picture to all clients, which will render the latest screenshot in the bottom right corner of their screen.

Click to collapse [-]
Client

```
local screenSizeX,screenSizeY = guiGetScreenSize() -- save the current screen dimensions
local imgtexture
local takenBy

function wepFire(weapon)
	if weapon == 43 then -- if the weapon the player just fired is the camera
		triggerServerEvent("onPlayerTakesPhoto",localPlayer)
	end
end
addEventHandler("onClientPlayerWeaponFire",localPlayer,wepFire)

function updateLatestPhoto(img)
	if imgtexture then -- clean up the old dxTextrue if there is one
		destroyElement(imgtexture)
	end
	imgtexture = dxCreateTexture(img) -- create a new dxTexture from the image data so that we can render it using dxDrawImage
	takenBy = "taken by "..getPlayerName(source) -- let's also credit the photographer
end
addEvent("updatePhoto",true)
addEventHandler("updatePhoto",root,updateLatestPhoto)

function renderPhoto()
	if imgtexture then
		local sizeX, sizeY = 320, 240
		dxDrawImage(screenSizeX-sizeX,screenSizeY-sizeY,sizeX,sizeY,imgtexture) -- render the picture as well as the name of the photographer in the bottom right corner of the screen
		dxDrawText(takenBy,screenSizeX-sizeX,screenSizeY-sizeY,screenSizeX,screenSizeY,tocolor(0,0,0))
	end
end
addEventHandler("onClientRender",root,renderPhoto)
```

Click to collapse [-]
Server

```
function requestScreenshot()
	takePlayerScreenShot(client,320,240,"cameraphoto",50) -- the player just took a picture with the camera, let's request a screenshot to see what they took a photo of
end
addEvent("onPlayerTakesPhoto",true)
addEventHandler("onPlayerTakesPhoto",root,requestScreenshot)

function incomingPlayerScreenshot(res,status,img,timestamp,tag)
	if status == "ok" and tag == "cameraphoto" then -- make sure a picture was taken successfully and that we're the ones who requested this screenshot
		triggerClientEvent("updatePhoto",source,img)  -- trigger a client event to share the image with everyone on the server
	end
end
addEventHandler("onPlayerScreenShot",root,incomingPlayerScreenshot)
```

## See Also

- [getAlivePlayers](mta://scripting/server/functions/getaliveplayers.md)

- [getDeadPlayers](mta://scripting/server/functions/getdeadplayers.md)

- [getPlayerAnnounceValue](mta://scripting/server/functions/getplayerannouncevalue.md)

- [getPlayerCount](mta://scripting/server/functions/getplayercount.md)

- [getPlayerIdleTime](mta://scripting/server/functions/getplayeridletime.md)

- [getPlayerIP](mta://scripting/server/functions/getplayerip.md)

- [getPlayerVersion](mta://scripting/server/functions/getplayerversion.md)

- [getRandomPlayer](mta://scripting/server/functions/getrandomplayer.md)

- [isPlayerMuted](mta://scripting/server/functions/isplayermuted.md)

- [redirectPlayer](mta://scripting/server/functions/redirectplayer.md)

- [resendPlayerACInfo](mta://scripting/server/functions/resendplayeracinfo.md)

- [resendPlayerModInfo](mta://scripting/server/functions/resendplayermodinfo.md)

- [setPlayerAnnounceValue](mta://scripting/server/functions/setplayerannouncevalue.md)

- [setPlayerMuted](mta://scripting/server/functions/setplayermuted.md)

- [setPlayerScriptDebugLevel](mta://scripting/server/functions/setplayerscriptdebuglevel.md)

- [setPlayerTeam](mta://scripting/server/functions/setplayerteam.md)

- [setPlayerName](mta://scripting/server/functions/setplayername.md)

- [setPlayerVoiceBroadcastTo](mta://scripting/server/functions/setplayervoicebroadcastto.md)

- [setPlayerVoiceIgnoreFrom](mta://scripting/server/functions/setplayervoiceignorefrom.md)

- [setPlayerWantedLevel](mta://scripting/server/functions/setplayerwantedlevel.md)

- [spawnPlayer](mta://scripting/server/functions/spawnplayer.md)

- takePlayerScreenShot
  

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
