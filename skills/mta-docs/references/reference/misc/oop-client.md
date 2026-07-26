---
doc_id: "mta-wiki:7764"
title: "OOP client"
source_title: "OOP client"
source_url: "https://wiki.multitheftauto.com/wiki/OOP_client"
revision_id: 82534
language: "en"
categories: ["Needs_Checking", "OOP"]
---

# OOP client

|  | This article needs checking. |
| --- | --- |
| Reason(s): This page is partially outdated. |  |

The new OOP in MTA allows for better code organization and readability. This is a list of [client-side functions](mta://scripting/concepts/client-scripting-functions.md).

*See also: [OOP](mta://tutorials/oop.md)*

## Element

```
areCollisionsEnabled (function: getElementCollisionsEnabled)
attach (function: attachElements)
clearVisibleTo (function: clearElementVisibleTo)
clone (function: cloneElement)
create (function: createElement)
destroy (function: destroyElement)
detach (function: detachElements)
getAllByType (function: getElementsByType)
getAlpha (function: getElementAlpha)
getAttachedElements (function: getAttachedElements)
getAttachedOffsets (function: getElementAttachedOffsets)
getAttachedTo (function: getElementAttachedTo)
getBoundingBox (function: getElementBoundingBox)
getByID (function: getElementByID)
getByType (function: getElementsByType)
getChild (function: getElementChild)
getChildren (function: getElementChildren)
getChildrenCount (function: getElementChildrenCount)
getColShape (function: getElementColShape)
getData (function: getElementData)
getDimension (function: getElementDimension)
getDistanceFromCentreOfMassToBaseOfModel (function: GetElementDistanceFromCentreOfMassToBaseOfModel)
getHealth (function: getElementHealth)
getID (function: getElementID)
getInterior (function: getElementInterior)
getLowLOD (function: getLowLODElement)
getModel (function: getElementModel)
getParent (function: getElementParent)
getPosition (function: getElementPosition, variable: position)
getRotation (function: getElementRotation, variable: rotation)
getSyncer (function: getElementSyncer)
getType (function: getElementType)
getVelocity (function: getElementVelocity)
getWithinColShape (function: getElementsWithinColShape)
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
setLowLOD (function: setLowLODElement)
setMatrix (function: setElementMatrix)
setModel (function: setElementModel)
setParent (function: setElementParent)
setPosition (function: setElementPosition)
setRotation (function: setElementRotation)
setVelocity (function: setElementVelocity)
setVisibleTo (function: setElementVisibleTo)
```

## Vehicle

*Inherited from [Element](#Element)*

```
addUpgrade (function: addVehicleUpgrade)
attachTrailer (function: attachTrailerToVehicle)
blow (function: blowVehicle)
create (function: createVehicle)
detachTrailer (function: detachTrailerFromVehicle)
fix (function: fixVehicle)
getAdjustableProperty (function: getVehicleAdjustableProperty)
getColor (function: getVehicleColor)
getCompatibleUpgrades (function: getVehicleCompatibleUpgrades)
getComponentPosition (function: getVehicleComponentPosition)
getComponentRotation (function: getVehicleComponentRotation)
getComponents (function: getVehicleComponents)
getComponentVisible (function: getVehicleComponentVisible)
getController (function: getVehicleController)
getDoorOpenRatio (function: getVehicleDoorOpenRatio)
getDoorState (function: getVehicleDoorState)
getEngineState (function: getVehicleEngineState)
getGear (function: getVehicleCurrentGear)
getGravity (function: getVehicleGravity)
getHandling (function: getVehicleHandling)
getHeadLightColor (function: getVehicleHeadLightColor)
getHelicopterRotorSpeed (function: getHelicopterRotorSpeed)
getLandingGearDown (function: getVehicleLandingGearDown)
getLightState (function: getVehicleLightState)
getMaxPassengers (function: getVehicleMaxPassengers)
getName (function: getVehicleName)
getNitroCount (function: getVehicleNitroCount)
getNitroLevel (function: getVehicleNitroLevel)
getOccupant (function: getVehicleOccupant)
getOccupants (function: getVehicleOccupants)
getOverrideLights (function: getVehicleOverrideLights)
getPaintjob (function: getVehiclePaintjob)
getPanelState (function: getVehiclePanelState)
getPlateText (function: getVehiclePlateText)
getSirens (function: getVehicleSirens)
getSirensOn (function: getVehicleSirensOn)
getTowedByVehicle (function: getVehicleTowedByVehicle)
getTowingVehicle (function: getVehicleTowingVehicle)
getTrainDirection (function: getTrainDirection)
getTrainSpeed (function: getTrainSpeed)
getTurnVelocity (function: getVehicleTurnVelocity)
getTurretPosition (function: getVehicleTurretPosition)
getUpgrades (function: getVehicleUpgrades)
getUpgradeSlotName (function: getVehicleUpgradeSlotName)
getVariant (function: getVehicleVariant)
getVehicleType (function: getVehicleType)
getWheelStates (function: getVehicleWheelStates)
isBlown (function: isVehicleBlown)
isDamageProof (function: isVehicleDamageProof)
isFuelTankExplodable (function: isVehicleFuelTankExplodable)
isLocked (function: isVehicleLocked)
isNitroActivated (function: isVehicleNitroActivated)
isNitroRecharging (function: isVehicleNitroRecharging)
isOnGround (function: isVehicleOnGround)
isTaxiLightOn (function: isVehicleTaxiLightOn)
isTrainDerailable (function: setTrainDerailable)
isTrainDerailed (function: isTrainDerailed)
isWheelCollided (function: isVehicleWheelCollided)
removeUpgrade (function: removeVehicleUpgrade)
resetComponentPosition (function: resetVehicleComponentPosition)
resetComponentRotation (function: resetVehicleComponentRotation)
setAdjustableProperty (function: setVehicleAdjustableProperty)
setColor (function: setVehicleColor)
setComponentPosition (function: setVehicleComponentPosition)
setComponentRotation (function: setVehicleComponentRotation)
setComponentVisible (function: setVehicleComponentVisible)
setDamageProof (function: setVehicleDamageProof)
setDirtLevel (function: setVehicleDirtLevel)
setDoorOpenRatio (function: setVehicleDoorOpenRatio)
setDoorState (function: setVehicleDoorState)
setDoorsUndamageable (function: setVehicleDoorsUndamageable)
setEngineState (function: setVehicleEngineState)
setFuelTankExplodable (function: setVehicleFuelTankExplodable)
setGravity (function: setVehicleGravity)
setHeadLightColor (function: setVehicleHeadLightColor)
setHelicopterRotorSpeed (function: setHelicopterRotorSpeed)
setLandingGearDown (function: setVehicleLandingGearDown)
setLightState (function: setVehicleLightState)
setLocked (function: setVehicleLocked)
setNitroActivated (function: setVehicleNitroActivated)
setNitroCount (function: setVehicleNitroCount)
setNitroLevel (function: setVehicleNitroLevel)
setOverrideLights (function: setVehicleOverrideLights)
setPaintjob (function: setVehiclePaintjob)
setPanelState (function: setVehiclePanelState)
setSirens (function: setVehicleSirens)
setSirensOn (function: setVehicleSirensOn)
setTaxiLightOn (function: setVehicleTaxiLightOn)
setTrainDerailable (function: setTrainDerailable)
setTrainDerailed (function: setTrainDerailed)
setTrainDirection (function: setTrainDirection)
setTrainSpeed (function: setTrainSpeed)
setTurnVelocity (function: setVehicleTurnVelocity)
setTurretPosition (function: setVehicleTurretPosition)
setVariant (function: setVehicleVariant)
setWheelStates (function: setVehicleWheelStates)
```

## Ped

*Inherited from [Element](#Element)*

```
addClothes (function: addPedClothes)
canBeKnockedOffBike (function: canPedBeKnockedOffBike)
create (function: createPed)
doesHaveJetPack (function: doesPedHaveJetPack)
getAmmoInClip (function: getPedAmmoInClip)
getAnalogControlState (function: getPedAnalogControlState)
getAnimation (function: getPedAnimation)
getAnimationData (function: getPedAnimationData)
getArmor (function: getPedArmor)
getBodyPartName (function: getBodyPartName)
getBonePosition (function: getPedBonePosition)
getCameraRotation (function: getPedCameraRotation)
getClothes (function: getPedClothes)
getClothesByTypeIndex (function: getClothesByTypeIndex)
getClothesTypeName (function: getClothesTypeName)
getContactElement (function: getPedContactElement)
getControlState (function: getPedControlState)
getMoveState (function: getPedMoveState)
getOccupiedVehicle (function: GetPedOccupiedVehicle)
getOxygenLevel (function: getPedOxygenLevel)
getSimplestTask (function: getPedSimplestTask)
getStat (function: getPedStat)
getTarget (function: getPedTarget)
getTargetCollision (function: getPedTargetCollision)
getTargetEnd (function: getPedTargetEnd)
getTargetStart (function: getPedTargetStart)
getTask (function: getPedTask)
getTotalAmmo (function: getPedTotalAmmo)
getTypeIndexFromClothes (function: getTypeIndexFromClothes)
getValidModels (function: getValidPedModels)
getVoice (function: getPedVoice)
getWalkingStyle (function: getPedWalkingStyle)
getWeapon (function: getPedWeapon)
getWeaponMuzzlePosition (function: getPedWeaponMuzzlePosition)
isChocking (function: isPedChoking)
isDoingGangDriveby (function: isPedDoingGangDriveby)
isDoingTask (function: isPedDoingTask)
isDucked (function: isPedDucked)
isHeadless (function: isPedHeadless)
isInVehicle (function: isPedInVehicle)
isOnFire (function: isPedOnFire)
isOnGround (function: isPedOnGround)
isReloadingWeapon (function: isPedReloadingWeapon)
isTargetingMarkerEnabled (function: isPedTargetingMarkerEnabled)
removeClothes (function: removePedClothes)
removeFromVehicle (function: removePedFromVehicle)
setAimTarget (function: setPedAimTarget)
setAnalogControlState (function: setPedAnalogControlState)
setAnimation (function: setPedAnimation)
setAnimationProgress (function: setPedAnimationProgress)
setCameraRotation (function: setPedCameraRotation)
setCanBeKnockedOffBike (function: setPedCanBeKnockedOffBike)
setControlState (function: setPedControlState)
setDoingGangDriveby (function: setPedDoingGangDriveby)
setFootBloodEnabled (function: setPedFootBloodEnabled)
setHeadless (function: setPedHeadless)
setLookAt (function: setPedLookAt)
setOnFire (function: setPedOnFire)
setOxygenLevel (function: setPedOxygenLevel)
setTargetingMarkerEnabled (function: setPedTargetingMarkerEnabled)
setVoice (function: setPedVoice)
setWalkingStyle (function: setPedWalkingStyle)
setWeaponSlot (function: setPedWeaponSlot)
warpIntoVehicle (function: warpPedIntoVehicle)
```

## Player

*Inherited from [Ped](#Ped)*

```
create (function: getPlayerFromName)
getBlurLevel (function: getPlayerBlurLevel)
getMapBoundingBox (function: getPlayerMapBoundingBox)
getMoney (function: getPlayerMoney)
getName (function: getPlayerName)
getNametagColor (function: getPlayerNametagColor)
getNametagText (function: getPlayerNametagText)
getPing (function: getPlayerPing)
getSerial (function: getPlayerSerial)
getTeam (function: getPlayerTeam)
getWantedLevel (function: getPlayerWantedLevel)
giveMoney (function: givePlayerMoney)
isHudComponentVisible (function: isPlayerHudComponentVisible)
isMapForced (function: isPlayerMapForced)
isMapVisible (function: isPlayerMapVisible)
isNametagShowing (function: isPlayerNametagShowing)
setBlurLevel (function: setPlayerBlurLevel)
setMoney (function: setPlayerMoney)
setNametagColor (function: setPlayerNametagColor)
setNametagShowing (function: setPlayerNametagShowing)
setNametagText (function: setPlayerNametagText)
showHudComponent (function: showPlayerHudComponent)
takeMoney (function: takePlayerMoney)
```

## Object

*Inherited from [Element](#Element)*

```
break (function: breakObject)
create (function: createObject)
getMass (function: getObjectMass)
getScale (function: getObjectScale)
isBreakable (function: isObjectBreakable)
move (function: moveObject)
respawn (function: respawnObject)
setBreakable (function: setObjectBreakable)
setMass (function: setObjectMass)
setScale (function: setObjectScale)
stop (function: stopObject)
toggleObjectRespawn (function: toggleObjectRespawn)
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

## Pickup

*Inherited from [Element](#Element)*

```
create (function: createPickup)
getAmmo (function: getPickupAmmo)
getAmount (function: getPickupAmount)
getType (function: getPickupType)
getWeapon (function: getPickupWeapon)
setType (function: setPickupType)
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

## Projectile

*Inherited from [Element](#Element)*

```
create (function: createProjectile)
getCounter (function: getProjectileCounter)
getCreator (function: getProjectileCreator)
getForce (function: getProjectileForce)
getTarget (function: getProjectileTarget)
getType (function: getProjectileType)
setCounter (function: setProjectileCounter)
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

## Team

*Inherited from [Element](#Element)*

```
countPlayers (function: countPlayersInTeam)
create (function: getTeamFromName)
getColor (function: getTeamColor)
getFriendlyFire (function: getTeamFriendlyFire)
getFromName (function: getTeamFromName)
getName (function: getTeamName)
```

## Water

*Inherited from [Element](#Element)*

```
create (function: createWater)
getColor (function: getWaterColor)
getLevel (function: getWaterLevel)
getVertexPosition (function: getWaterVertexPosition)
getWaveHeight (function: getWaveHeight)
isDrawnLast (function: isWaterDrawnLast)
resetColor (function: resetWaterColor)
resetLevel (function: resetWaterLevel)
setColor (function: setWaterColor)
setDrawnLast (function: setWaterDrawnLast)
setLevel (function: setWaterLevel)
setVertexPosition (function: setWaterVertexPosition)
setWaveHeight (function: setWaveHeight)
testLineAgainst (function: testLineAgainstWater)
```

## Sound

*Inherited from [Element](#Element)*

```
Sound (function: playSound)
getBPM (function: getSoundBPM)
getEffects (function: getSoundEffects)
getFFTData (function: getSoundFFTData)
getLength (function: getSoundLength)
getLevelData (function: getSoundLevelData)
getMetaTags (function: getSoundMetaTags)
getPan (function: getSoundPan)
getPlaybackPosition (function: getSoundPosition)
getProperties (function: getSoundProperties)
getSpeed (function: getSoundSpeed)
getVolume (function: getSoundVolume)
getWaveData (function: getSoundWaveData)
isPaused (function: isSoundPaused)
setEffectEnabled (function: setSoundEffectEnabled)
setPan (function: setSoundPan)
setPaused (function: setSoundPaused)
setPlaybackPosition (function: setSoundPosition)
setProperties (function: setSoundProperties)
setSpeed (function: setSoundSpeed)
setVolume (function: setSoundVolume)
stop (function: stopSound)
```

## Sound3D

*Inherited from [Sound](#Sound)*

```
create (function: playSound3D)
getMaxDistance (function: getSoundMaxDistance)
getMinDistance (function: getSoundMinDistance)
setMaxDistance (function: setSoundMaxDistance)
setMinDistance (function: setSoundMinDistance)
```

## Weapon

*Inherited from [Element](#Element)*

```
create (function: createWeapon)
fire (function: fireWeapon)
getAmmo (function: getWeaponAmmo)
getClipAmmo (function: getWeaponClipAmmo)
getFiringRate (function: getWeaponFiringRate)
getFlags (function: getWeaponFlags)
getOwner (function: getWeaponOwner)
getProperty (function: setWeaponProperty)
getState (function: getWeaponState)
getTarget (function: getWeaponTarget)
resetFiringRate (function: resetWeaponFiringRate)
setAmmo (function: setWeaponAmmo)
setClipAmmo (function: setWeaponClipAmmo)
setFiringRate (function: setWeaponFiringRate)
setFlags (function: setWeaponFlags)
setOwner (function: setWeaponOwner)
setProperty (function: setWeaponProperty)
setState (function: setWeaponState)
setTarget (function: setWeaponTarget)
```

## Effect

*Inherited from [Element](#Element)*

```
addBlood (function: fxAddBlood)
addBulletImpact (function: fxAddBulletImpact)
addBulletSplash (function: fxAddBulletSplash)
addDebris (function: fxAddDebris)
addFootSplash (function: fxAddFootSplash)
addGlass (function: fxAddGlass)
addGunshot (function: fxAddGunshot)
addPunchImpact (function: fxAddPunchImpact)
addSparks (function: fxAddSparks)
addTankFire (function: fxAddTankFire)
addTyreBurst (function: fxAddTyreBurst)
addWaterHydrant (function: fxAddWaterHydrant)
addWaterSplash (function: fxAddWaterSplash)
addWood (function: fxAddWood)
create (function: createEffect)
getDensity (function: getEffectDensity)
getSpeed (function: getEffectSpeed)
setDensity (function: setEffectDensity)
setSpeed (function: setEffectSpeed)
```

## GuiElement

*Inherited from [Element](#Element)*

```
bringToFront (function: guiBringToFront)
moveToBack (function: guiMoveToBack)
isChatBoxInputActive (function: isChatBoxInputActive)
isConsoleActive (function: isConsoleActive)
isDebugViewActive (function: isDebugViewActive)
isMainMenuActive (function: isMainMenuActive)
isMTAWindowActive (function: isMTAWindowActive)
isTransferBoxActive (function: isTransferBoxActive)
isInputEnabled (function: guiGetInputEnabled)
getInputMode (function: guiGetInputMode)
getScreenSize (function: guiGetScreenSize)
getProperties (function: guiGetProperties)
getAlpha (function: guiGetAlpha)
getFont (function: guiGetFont)
getEnabled (function: guiGetEnabled)
getVisible (function: guiGetVisible)
getText (function: guiGetText)
getPosition (function: guiGetPosition)
getSize (function: guiGetSize)
getProperty (function: guiGetProperty)
setInputEnabled (function: guiSetInputEnabled)
setAlpha (function: guiSetAlpha)
setEnabled (function: guiSetEnabled)
setFont (function: guiSetFont)
setVisible (function: guiSetVisible)
setText (function: guiSetText)
setInputMode (function: guiSetInputMode)
setProperty (function: guiSetProperty)
setPosition (function: guiSetPosition)
setSize (function: guiSetSize)
```

## GuiWindow

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateWindow)
setMovable (function: guiWindowSetMovable)
setSizable (function: guiWindowSetSizable)
```

## GuiButton

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateButton)
```

## GuiEdit

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateEdit)
getCaretIndex (function: guiEditGetCaretIndex)
setCaretIndex (function: guiEditSetCaretIndex)
setReadOnly (function: guiEditSetReadOnly)
setMasked (function: guiEditSetMasked)
setMaxLength (function: guiEditSetMaxLength)
```

## GuiLabel

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateLabel)
getFontHeight (function: guiLabelGetFontHeight)
getTextExtent (function: guiLabelGetTextExtent)
getColor (function: guiLabelGetColor)
setColor (function: guiLabelSetColor)
setHorizontalAlign (function: guiLabelSetHorizontalAlign)
setVerticalAlign (function: guiLabelSetVerticalAlign)
```

## GuiMemo

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateMemo)
getCaretIndex (function: guiMemoGetCaretIndex)
setCaretIndex (function: guiMemoSetCaretIndex)
setReadOnly (function: guiMemoSetReadOnly)
```

## GuiStaticImage

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateStaticImage)
loadImage (function: guiStaticImageLoadImage)
```

## GuiComboBox

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateComboBox)
addItem (function: guiComboBoxAddItem)
clear (function: guiComboBoxClear)
removeItem (function: guiComboBoxRemoveItem)
getSelected (function: guiComboBoxGetSelected)
getItemText (function: guiComboBoxGetItemText)
setItemText (function: guiComboBoxSetItemText)
setSelected (function: guiComboBoxSetSelected)
```

## GuiCheckBox

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateCheckBox)
getSelected (function: guiCheckBoxGetSelected)
setSelected (function: guiCheckBoxSetSelected)
```

## GuiRadioButton

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateRadioButton)
getSelected (function: guiRadioButtonGetSelected)
setSelected (function: guiRadioButtonSetSelected)
```

## GuiScrollPane

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateScrollPane)
getHorizontalScrollPosition (function: guiScrollPaneGetHorizontalScrollPosition)
getVerticalScrollPosition (function: guiScrollPaneGetVerticalScrollPosition)
setHorizontalScrollPosition (function: guiScrollPaneSetHorizontalScrollPosition)
setScrollBars (function: guiScrollPaneSetScrollBars)
setVerticalScrollPosition (function: guiScrollPaneSetVerticalScrollPosition)
```

## GuiScrollBar

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateScrollBar)
getScrollPosition (function: guiScrollBarGetScrollPosition)
setScrollPosition (function: guiScrollBarSetScrollPosition)
```

## GuiProgressBar

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateProgressBar)
getProgress (function: guiProgressBarGetProgress)
setProgress (function: guiProgressBarSetProgress)
```

## GuiGridList

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateGridList)
addColumn (function: guiGridListAddColumn)
addRow (function: guiGridListAddRow)
autoSizeColumn (function: guiGridListAutoSizeColumn)
clear (function: guiGridListClear)
insertRowAfter (function: guiGridListInsertRowAfter)
removeColumn (function: guiGridListRemoveColumn)
removeRow (function: guiGridListRemoveRow)
getItemData (function: guiGridListGetItemData)
getItemText (function: guiGridListGetItemText)
getRowCount (function: guiGridListGetRowCount)
getSelectedItem (function: guiGridListGetSelectedItem)
getItemColor (function: guiGridListGetItemColor)
getColumnTitle (function: guiGridListGetColumnTitle)
getHorizontalScrollPosition (function: guiGridListGetHorizontalScrollPosition)
getVerticalScrollPosition (function: guiGridListGetVerticalScrollPosition)
getSelectedCount (function: guiGridListGetSelectedCount)
getSelectedItems (function: guiGridListGetSelectedItems)
getColumnCount (function: guiGridListGetColumnCount)
setItemData (function: guiGridListSetItemData)
setItemText (function: guiGridListSetItemText)
setScrollBars (function: guiGridListSetScrollBars)
setSelectedItem (function: guiGridListSetSelectedItem)
setSelectionMode (function: guiGridListSetSelectionMode)
setSortingEnabled (function: guiGridListSetSortingEnabled)
setColumnWidth (function: guiGridListSetColumnWidth)
setItemColor (function: guiGridListSetItemColor)
setColumnTitle (function: guiGridListSetColumnTitle)
setHorizontalScrollPosition (function: guiGridListSetHorizontalScrollPosition)
setVerticalScrollPosition (function: guiGridListSetVerticalScrollPosition)
```

## GuiTabPanel

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateTabPanel)
getSelectedTab (function: guiGetSelectedTab)
setSelectedTab (function: guiSetSelectedTab)
```

## GuiTab

*Inherited from [GuiElement](#GuiElement)*

```
create (function: guiCreateTab)
delete (function: guiDeleteTab)
```

## GuiFont

*Inherited from [Element](#Element)*

```
create (function: guiCreateFont)
```

## Resource

```
create (function: getResourceFromName)
fromName (function: getResourceFromName)
getGuiElement (function: getResourceGUIElement)
getRootElement (function: getResourceRootElement)
getName (function: getResourceName)
getThis (function: getThisResource)
getConfig (function: getResourceConfig)
getConfig (function: getResourceConfig)
getDynamicElementRoot (function: getResourceDynamicElementRoot)
getExportedFunctions (function: getResourceExportedFunctions)
getState (function: getResourceState)
```

## Timer

```
create (function: setTimer)
destroy (function: killTimer)
reset (function: resetTimer)
isValid (function: isTimer)
getDetails (function: getTimerDetails)
```

## File

```
create (function: fileOpen)
destroy (function: fileClose)
close (function: fileClose)
new (function: fileCreate)
delete (function: fileDelete)
exists (function: fileExists)
flush (function: fileFlush)
getPos (function: fileGetPos)
getSize (function: fileGetSize)
isEOF (function: fileIsEOF)
read (function: fileRead)
rename (function: fileRename)
setPos (function: fileSetPos)
write (function: fileWrite)
copy (function: fileCopy)
```

## XML

```
load (function: xmlLoadFile)
unload (function: xmlUnloadFile)
copy (function: xmlCopyFile)
create (function: xmlCreateFile)
destroy (function: xmlDestroyNode)
getValue (function: xmlNodeGetValue)
setAttribute (function: xmlNodeSetAttribute)
setValue (function: xmlNodeSetValue)
saveFile (function: xmlSaveFile)
createChild (function: xmlCreateChild)
findChild (function: xmlFindChild)
getAttributes (function: xmlNodeGetAttributes)
getChildren (function: xmlNodeGetChildren)
getName (function: xmlNodeGetName)
getParent (function: xmlNodeGetParent)
getAttribute (function: xmlNodeGetAttribute)
setName (function: xmlNodeSetName)
```

## Camera

```
fade (function: fadeCamera)
getTarget (function: getCameraTarget)
getInterior (function: getCameraInterior)
getViewMode (function: getCameraViewMode)
getGoggleEffect (function: getCameraGoggleEffect)
setInterior (function: setCameraInterior)
setTarget (function: setCameraTarget)
setViewMode (function: setCameraViewMode)
setGoggleEffect (function: setCameraGoggleEffect)
setClip (function: setCameraClip)
```

## Engine

```
restoreCOL (function: engineRestoreCOL)
restoreModel (function: engineRestoreModel)
setAsynchronousLoading (function: engineSetAsynchronousLoading)
setModelLODDistance (function: engineSetModelLODDistance)
getVisibleTextureName (function: engineGetVisibleTextureNames)
getModelLODDistance (function: engineGetModelLODDistance)
getModelTextureNames (function: engineGetModelTextureNames)
getModelIDFromName (function: engineGetModelIDFromName)
getModelNameFromID (function: engineGetModelNameFromID)
```

## EngineCOL

*Inherited from [Element](#Element)*

```
create (function: engineLoadCOL)
replace (function: engineReplaceCOL)
```

## EngineTXD

*Inherited from [Element](#Element)*

```
create (function: engineLoadTXD)
import (function: engineImportTXD)
```

## EngineDFF

*Inherited from [Element](#Element)*

```
create (function: engineLoadDFF)
replace (function: engineReplaceModel)
```

## DxMaterial

*Inherited from [Element](#Element)*

```
getSize (function: dxGetMaterialSize)
```

## DxTexture

*Inherited from [DxMaterial](#DxMaterial)*

```
create (function: dxCreateTexture)
setEdge (function: dxSetTextureEdge)
setPixels (function: dxSetTexturePixels)
getPixels (function: dxGetTexturePixels)
```

## DxFont

```
DxFont (function: dxCreateFont)
getHeight (function: dxGetFontHeight)
getTextWidth (function: dxGetTextWidth)
```

## DxShader

*Inherited from [DxMaterial](#DxMaterial)*

```
create (function: dxCreateShader)
setValue (function: dxSetShaderValue)
setTessellation (function: dxSetShaderTessellation)
setTransform (function: dxSetShaderTransform)
value (function: dxGetFontHeight)
```

## DxScreenSource

```
create (function: dxCreateScreenSource)
update (function: dxUpdateScreenSource)
```

## DxRenderTarget

```
create (function: dxCreateRenderTarget)
setAsTarget (function: dxSetRenderTarget)
```
