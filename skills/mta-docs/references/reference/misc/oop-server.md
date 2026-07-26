---
doc_id: "mta-wiki:7765"
title: "OOP server"
source_title: "OOP server"
source_url: "https://wiki.multitheftauto.com/wiki/OOP_server"
revision_id: 82275
language: "en"
categories: ["Needs_Checking", "OOP"]
---

# OOP server

|  | This article needs checking. |
| --- | --- |
| Reason(s): This page is partially outdated. |  |

The new OOP in MTA allows for better code organization and readability. This is a list of [server-side functions](mta://scripting/concepts/server-scripting-functions.md).

*See also: [OOP](mta://tutorials/oop.md)*

## Element

```
areCollisionsEnabled (function: getElementCollisionsEnabled)
attach (function: attachElements)
clearVisibility (function: clearElementVisibleTo)
clone (function: cloneElement)
create (function: createElement)
destroy (function: destroyElement)
detach (function: detachElements)
getAllByType (function: getElementsByType)
getAllData (function: getAllElementData)
getAlpha (function: getElementAlpha)
getAttachedElements (function: getAttachedElements)
getAttachedOffsets (function: getElementAttachedOffsets)
getAttachedTo (function: getElementAttachedTo)
getByID (function: getElementByID)
getByIndex (function: getElementByIndex)
getChild (function: getElementChild)
getChildren (function: getElementChildren)
getChildrenCount (function: getElementChildrenCount)
getColShape (function: getElementColShape)
getData (function: getElementData)
getDimension (function: getElementDimension)
getHealth (function: getElementHealth)
getID (function: getElementID)
getInterior (function: getElementInterior)
getLowLOD (function: getLowLODElement)
getModel (function: getElementModel)
getParent (function: getElementParent)
getPosition (function: getElementPosition)
getRotation (function: getElementRotation)
getSyncer (function: getElementSyncer)
getType (function: getElementType)
getVelocity (function: getElementVelocity)
getZoneName (function: getElementZoneName)
isAttached (function: isElementAttached)
isCallPropagationEnabled (function: isElementCallPropagationEnabled)
isDoubleSided (function: isElementDoubleSided)
isFrozen (function: isElementFrozen)
isInWater (function: isElementInWater)
isLowLOD (function: isElementLowLOD)
isVisibleTo (function: isElementVisibleTo)
isWithinColShape (function: isElementWithinColShape)
isWithinMarker (function: isElementWithinMarker)
removeData (function: removeElementData)
setAlpha (function: setElementAlpha)
setAttachedOffsets (function: setElementAttachedOffsets)
setCallPropagationEnabled (function: setElementCallPropagationEnabled)
setCollisionsEnabled (function: setElementCollisionsEnabled)
setData (function: setElementData)
setDimension (function: setElementDimension)
setDoubleSided (function: setElementDoubleSided)
setFrozen (function: setElementFrozen)
setHealth (function: setElementHealth)
setID (function: setElementID)
setInterior (function: setElementInterior)
setMatrix (function: setElementMatrix)
setModel (function: setElementModel)
setParent (function: setElementParent)
setPosition (function: setElementPosition)
setRotation (function: setElementRotation)
setSyncer (function: setElementSyncer)
setVelocity (function: setElementVelocity)
```

## ACL

```
create (function: aclCreate)
destroy (function: aclDestroy)
get (function: aclGet)
getName (function: aclGetName)
getRight (function: aclGetRight)
hasObjectPermissionTo (function: hasObjectPermissionTo)
list (function: aclList)
listRights (function: aclListRights)
reload (function: aclReload)
removeRight (function: aclRemoveRight)
save (function: aclSave)
setRight (function: aclSetRight)
```

## ACLGroup

```
addACL (function: aclGroupAddACL)
addObject (function: aclGroupAddObject)
addToGroup (function: aclGroupAddACL)
create (function: aclCreateGroup)
destroy (function: aclDestroyGroup)
doesContainObject (function: isObjectInACLGroup)
get (function: aclGetGroup)
getName (function: aclGroupGetName)
list (function: aclGroupList)
listACL (function: aclGroupListACL)
listObjects (function: aclGroupListObjects)
removeACL (function: aclGroupRemoveACL)
removeFromGroup (function: aclGroupRemoveACL)
removeObject (function: aclGroupRemoveObject)
```

## Account

```
add (function: addAccount)
copyDataTo (function: copyAccountData)
getData (function: getAccountData)
getID (function: getAccountID)
getIP (function: getAccountIP)
getName (function: getAccountName)
getPlayer (function: getAccountPlayer)
getAllByData (function: getAccountsByData)
getAllByIP (function: getAccountsByIP)
getAllBySerial (function: getAccountsBySerial)
getSerial (function: getAccountSerial)
getAll (function: getAccounts)
create (function: getAccount)
getAllData (function: getAllAccountData)
getAccount (function: getPlayerAccount)
isGuest (function: isGuestAccount)
logIn (function: logIn)
logOut (function: logOut)
remove (function: removeAccount)
setData (function: setAccountData)
setName (function: setAccountName)
setPassword (function: setAccountPassword)
```

## Ban

```
create (function: addBan)
getAdmin (function: getBanAdmin)
getIP (function: getBanIP)
getList (function: getBans)
getNick (function: getBanNick)
getReason (function: getBanReason)
getSerial (function: getBanSerial)
getTime (function: getBanTime)
getUnbanTime (function: getUnbanTime)
remove (function: removeBan)
```

## Blip

*Inherited from [Element](#Element)*

```
create (function: createBlip)
createAttachedTo (function: createBlipAttachedTo)
getColor (function: getBlipColor)
getIcon (function: getBlipIcon)
getOrdering (function: getBlipOrdering)
getSize (function: getBlipSize)
getVisibleDistance (function: getBlipVisibleDistance)
setColor (function: setBlipColor)
setIcon (function: setBlipIcon)
setOrdering (function: setBlipOrdering)
setSize (function: setBlipSize)
setVisibleDistance (function: setBlipVisibleDistance)
```

## ColShape

*Inherited from [Element](#Element)*

```
Circle (function: createColCircle)
Cuboid (function: createColCuboid)
getElementsWithin (function: getElementsWithinColShape)
getShapeType (function: getColShapeType)
isElementWithin (function: isElementWithinColShape)
Polygon (function: createColPolygon)
Rectangle (function: createColRectangle)
Sphere (function: createColSphere)
Tube (function: createColTube)
```

## File

```
close (function: fileClose)
copy (function: fileCopy)
create (function: fileOpen)
delete (function: fileDelete)
destroy (function: fileClose)
exists (function: fileExists)
flush (function: fileFlush)
getPos (function: fileGetPos)
getSize (function: fileGetSize)
isEOF (function: fileIsEOF)
new (function: fileCreate)
read (function: fileRead)
rename (function: fileRename)
setPos (function: fileSetPos)
write (function: fileWrite)
```

## Marker

*Inherited from [Element](#Element)*

```
create (function: createMarker)
getColor (function: getMarkerColor)
getCount (function: getMarkerCount)
getIcon (function: getMarkerIcon)
getSize (function: getMarkerSize)
getTarget (function: getMarkerTarget)
getType (function: getMarkerType)
setColor (function: setMarkerColor)
setIcon (function: setMarkerIcon)
setSize (function: setMarkerSize)
setTarget (function: setMarkerTarget)
setType (function: setMarkerType)
```

## Object

*Inherited from [Element](#Element)*

```
create (function: createObject)
getScale (function: getObjectScale)
move (function: moveObject)
setScale (function: setObjectScale)
stop (function: stopObject)
```

## Ped

*Inherited from [Element](#Element)*

```
addClothes (function: addPedClothes)
create (function: createPed)
doesHaveJetpack (function: doesPedHaveJetPack)
getAmmoInClip (function: getPedAmmoInClip)
getAnalogControlState (function: getPedAnalogControlState)
getArmor (function: getPedArmor)
getClothes (function: getPedClothes)
getContactElement (function: getPedContactElement)
getFightingStyle (function: getPedFightingStyle)
getGravity (function: getPedGravity)
getOccupiedVehicle (function: getPedOccupiedVehicle)
getOccupiedVehicleSeat (function: getPedOccupiedVehicleSeat)
getStat (function: getPedStat)
getTarget (function: getPedTarget)
getTotalAmmo (function: getPedTotalAmmo)
getValidModels (function: getValidPedModels)
getWalkingStyle (function: getPedWalkingStyle)
getWeapon (function: getPedWeapon)
getWeaponSlot (function: getPedWeaponSlot)
giveJetPack (function: givePedJetPack)
isChoking (function: isPedChoking)
isDead (function: isPedDead)
isDoingGangDriveby (function: isPedDoingGangDriveby)
isDucked (function: isPedDucked)
isFrozen (function: isPedFrozen)
isHeadless (function: isPedHeadless)
isInVehicle (function: isPedInVehicle)
isInWater (function: isPedInWater)
isOnFire (function: isPedOnFire)
isOnGround (function: isPedOnGround)
kill (function: killPed)
reloadWeapon (function: reloadPedWeapon)
removeClothes (function: removePedClothes)
removeFromVehicle (function: removePedFromVehicle)
removeJetPack (function: removePedJetPack)
setAnalogControlState (function: setPedAnalogControlState)
setAnimation (function: setPedAnimation)
setAnimationProgress (function: setPedAnimationProgress)
setArmor (function: setPedArmor)
setChoking (function: setPedChoking)
setDoingGangDriveBy (function: setPedDoingGangDriveby)
setFightingStyle (function: setPedFightingStyle)
setFrozen (function: setPedFrozen)
setGravity (function: setPedGravity)
setHeadless (function: setPedHeadless)
setOnFire (function: setPedOnFire)
setStat (function: setPedStat)
setWalkingStyle (function: setPedWalkingStyle)
setWeaponSlot (function: setPedWeaponSlot)
warpIntoVehicle (function: warpPedIntoVehicle)
```

## Pickup

*Inherited from [Element](#Element)*

```
create (function: createPickup)
getAmmo (function: getPickupAmmo)
getAmount (function: getPickupAmount)
getRespawnInterval (function: getPickupRespawnInterval)
getType (function: getPickupType)
getWeapon (function: getPickupWeapon)
setRespawnInterval (function: setPickupRespawnInterval)
setType (function: setPickupType)
use (function: usePickup)
```

## Player

*Inherited from [Ped](#Ped)*

```
ban (function: banPlayer)
create (function: getPlayerFromName)
forceMap (function: forcePlayerMap)
getAccount (function: getPlayerAccount)
getACInfo (function: getPlayerACInfo)
getAllAlive (function: getAlivePlayers)
getAllDead (function: getDeadPlayers)
getAnnounceValue (function: getPlayerAnnounceValue)
getBlurLevel (function: getPlayerBlurLevel)
getCount (function: getPlayerCount)
getIdleTime (function: getPlayerIdleTime)
getIP (function: getPlayerIP)
getMoney (function: getPlayerMoney)
getName (function: getPlayerName)
getNametagColor (function: getPlayerNametagColor)
getNametagText (function: getPlayerNametagText)
getPing (function: getPlayerPing)
getRandom (function: getRandomPlayer)
getSerial (function: getPlayerSerial)
getTeam (function: getPlayerTeam)
getVersion (function: getPlayerVersion)
getWantedLevel (function: getPlayerWantedLevel)
giveMoney (function: givePlayerMoney)
isMapForced (function: isPlayerMapForced)
isMuted (function: isPlayerMuted)
isNametagShowing (function: isPlayerNametagShowing)
isObservingDisplay (function: textDisplayIsObserver)
isVoiceEnabled (function: isVoiceEnabled)
kick (function: kickPlayer)
logOut (function: logOut)
observeDisplay (function: textDisplayAddObserver)
redirect (function: redirectPlayer)
resendModInfo (function: resendPlayerModInfo)
setAnnounceValue (function: setPlayerAnnounceValue)
setBlurLevel (function: setPlayerBlurLevel)
setHudComponentVisible (function: setPlayerHudComponentVisible)
setMoney (function: setPlayerMoney)
setMuted (function: setPlayerMuted)
setName (function: setPlayerName)
setNametagColor (function: setPlayerNametagColor)
setNametagShowing (function: setPlayerNametagShowing)
setNametagText (function: setPlayerNametagText)
setTeam (function: setPlayerTeam)
setVoiceBroadcastTo (function: setPlayerVoiceBroadcastTo)
setVoiceIgnoreFrom (function: setPlayerVoiceIgnoreFrom)
setWantedLevel (function: setPlayerWantedLevel)
showHudComponent (function: showPlayerHudComponent)
spawn (function: spawnPlayer)
stopObservingDisplay (function: textDisplayRemoveObserver)
takeMoney (function: takePlayerMoney)
takeScreenshot (function: takePlayerScreenShot)
```

## RadarArea

*Inherited from [Element](#Element)*

```
create (function: createRadarArea)
getColor (function: getRadarAreaColor)
getSize (function: getRadarAreaSize)
isFlashing (function: isRadarAreaFlashing)
isInside (function: isInsideRadarArea)
setColor (function: setRadarAreaColor)
setFlashing (function: setRadarAreaFlashing)
setSize (function: setRadarAreaSize)
```

## Resource

```
call (function: call)
copy (function: copyResource)
create (function: createResource)
getDynamicElementRoot (function: getResourceDynamicElementRoot)
getAll (function: getResources)
getFromName (function: getResourceFromName)
getInfo (function: getResourceInfo)
getMapRootElement (function: getResourceMapRootElement)
getName (function: getResourceName)
getRootElement (function: getResourceRootElement)
getState (function: getResourceState)
removeFile (function: removeResourceFile)
restart (function: restartResource)
start (function: startResource)
stop (function: stopResource)
setInfo (function: setResourceInfo)
rename (function: renameResource)
delete (function: deleteResource)
```

## Connection

*Inherited from [Element](#Element)*

```
create (function: dbConnect)
exec (function: dbExec)
query (function: dbQuery)
prepareString (function: dbPrepareString)
```

## QueryHandle

```
free (function: dbFree)
poll (function: dbPoll)
```

## Team

*Inherited from [Element](#Element)*

```
countPlayers (function: countPlayersInTeam)
create (function: createTeam)
getColor (function: getTeamColor)
getFriendlyFire (function: getTeamFriendlyFire)
getFromName (function: getTeamFromName)
getName (function: getTeamName)
getPlayers (function: getPlayersInTeam)
setColor (function: setTeamColor)
setFriendlyFire (function: setTeamFriendlyFire)
setName (function: setTeamName)
```

## TextDisplay

```
addObserver (function: textDisplayAddObserver)
addText (function: textDisplayAddText)
create (function: textCreateDisplay)
destroy (function: textDestroyDisplay)
getObservers (function: textDisplayGetObservers)
isObserver (function: textDisplayIsObserver)
removeObserver (function: textDisplayRemoveObserver)
removeText (function: textDisplayRemoveText)
```

## TextItem

```
create (function: textCreateTextItem)
destroy (function: textDestroyTextItem)
getColor (function: textItemGetColor)
getPosition (function: textItemGetPosition)
getPriority (function: textItemGetPriority)
getScale (function: textItemGetScale)
getText (function: textItemGetText)
setColor (function: textItemSetColor)
setPosition (function: textItemSetPosition)
setPriority (function: textItemSetPriority)
setScale (function: textItemSetScale)
setText (function: textItemSetText)
```

## Vehicle

*Inherited from [Element](#Element)*

```
addSirens (function: addVehicleSirens)
addUpgrade (function: addVehicleUpgrade)
areSirensOn (function: getVehicleSirensOn)
attachTrailer (function: attachTrailerToVehicle)
blow (function: blowVehicle)
create (function: createVehicle)
detachTrailer (function: detachTrailerFromVehicle)
fix (function: fixVehicle)
getAllOfType (function: getVehiclesOfType)
getColor (function: getVehicleColor)
getCompatibleUpgrades (function: getVehicleCompatibleUpgrades)
getController (function: getVehicleController)
getDirection (function: getTrainDirection)
getDoorOpenRatio (function: getVehicleDoorOpenRatio)
getDoorState (function: getVehicleDoorState)
getEngineState (function: getVehicleEngineState)
getHandling (function: getVehicleHandling)
getHeadLightColor (function: getVehicleHeadLightColor)
getLandingGearDown (function: getVehicleLandingGearDown)
getLightState (function: getVehicleLightState)
getMaxPassengers (function: getVehicleMaxPassengers)
getModelFromName (function: getVehicleModelFromName)
getModelHandling (function: getModelHandling)
getName (function: getVehicleName)
getNameFromModel (function: getVehicleNameFromModel)
getOccupant (function: getVehicleOccupant)
getOccupants (function: getVehicleOccupants)
getOriginalHandling (function: getOriginalHandling)
getOverrideLights (function: getVehicleOverrideLights)
getPaintjob (function: getVehiclePaintjob)
getPanelState (function: getVehiclePanelState)
getPlateText (function: getVehiclePlateText)
getSirenParams (function: getVehicleSirenParams)
getSirens (function: getVehicleSirens)
getSpeed (function: getTrainSpeed)
getTowedByVehicle (function: getVehicleTowedByVehicle)
getTowingVehicle (function: getVehicleTowingVehicle)
getTurnVelocity (function: getVehicleTurnVelocity)
getTurretPosition (function: getVehicleTurretPosition)
getUpgradeOnSlot (function: getVehicleUpgradeOnSlot)
getUpgrades (function: getVehicleUpgrades)
getUpgradeSlotName (function: getVehicleUpgradeSlotName)
getVariant (function: getVehicleVariant)
getVehicleType (function: getVehicleType)
getWheelStates (function: getVehicleWheelStates)
isBlown (function: isVehicleBlown)
isDamageProof (function: isVehicleDamageProof)
isDerailable (function: isTrainDerailable)
isDerailed (function: isTrainDerailed)
isFuelTankExplodable (function: isVehicleFuelTankExplodable)
isLocked (function: isVehicleLocked)
isOnGround (function: isVehicleOnGround)
isTaxiLightOn (function: isVehicleTaxiLightOn)
removeSirens (function: removeVehicleSirens)
removeUpgrade (function: removeVehicleUpgrade)
resetExplosionTime (function: resetVehicleExplosionTime)
resetIdleTime (function: resetVehicleIdleTime)
respawn (function: respawnVehicle)
setColor (function: setVehicleColor)
setDamageProof (function: setVehicleDamageProof)
setDerailable (function: setTrainDerailable)
setDerailed (function: setTrainDerailed)
setDirection (function: setTrainDirection)
setDoorOpenRatio (function: setVehicleDoorOpenRatio)
setDoorState (function: setVehicleDoorState)
setDoorsUndamageable (function: setVehicleDoorsUndamageable)
setEngineState (function: setVehicleEngineState)
setFuelTankExplodable (function: setVehicleFuelTankExplodable)
setHandling (function: setVehicleHandling)
setHeadLightColor (function: setVehicleHeadLightColor)
setIdleRespawnDelay (function: setVehicleIdleRespawnDelay)
setLandingGearDown (function: setVehicleLandingGearDown)
setLightState (function: setVehicleLightState)
setLocked (function: setVehicleLocked)
setModelHandling (function: setModelHandling)
setOverrideLights (function: setVehicleOverrideLights)
setPaintJob (function: setVehiclePaintjob)
setPanelState (function: setVehiclePanelState)
setPlateText (function: setVehiclePlateText)
setRespawnDelay (function: setVehicleRespawnDelay)
setRespawnPosition (function: setVehicleRespawnPosition)
setSirens (function: setVehicleSirens)
setSirensOn (function: setVehicleSirensOn)
setSpeed (function: setTrainSpeed)
setTaxiLightOn (function: setVehicleTaxiLightOn)
setTurnVelocity (function: setVehicleTurnVelocity)
setTurretPosition (function: setVehicleTurretPosition)
setVariant (function: setVehicleVariant)
setWheelStates (function: setVehicleWheelStates)
spawn (function: spawnVehicle)
toggleRespawn (function: toggleVehicleRespawn)
```

## Water

*Inherited from [Element](#Element)*

```
create (function: createWater)
getColor (function: getWaterColor)
getVertexPosition (function: getWaterVertexPosition)
getWaveHeight (function: getWaveHeight)
resetColor (function: resetWaterColor)
resetLevel (function: resetWaterLevel)
setColor (function: setWaterColor)
setLevel (function: setWaterLevel)
setVertexPosition (function: setWaterVertexPosition)
setWaveHeight (function: setWaveHeight)
```

## XML

```
copy (function: xmlCopyFile)
create (function: xmlCreateFile)
createChild (function: xmlCreateChild)
destroy (function: xmlDestroyNode)
findChild (function: xmlFindChild)
getAttribute (function: xmlNodeGetAttribute)
getAttributes (function: xmlNodeGetAttributes)
getChildren (function: xmlNodeGetChildren)
getName (function: xmlNodeGetName)
getParent (function: xmlNodeGetParent)
load (function: xmlLoadFile)
loadMapData (function: loadMapData)
saveFile (function: xmlSaveFile)
saveMapData (function: saveMapData)
setAttribute (function: xmlNodeSetAttribute)
setName (function: xmlNodeSetName)
setValue (function: xmlNodeGetValue)
setValue (function: xmlNodeSetValue)
unload (function: xmlUnloadFile)
```

## Timer

```
create (function: setTimer)
destroy (function: killTimer)
getDetails (function: getTimerDetails)
isValid (function: isTimer)
reset (function: resetTimer)
```
