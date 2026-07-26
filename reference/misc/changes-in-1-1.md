---
doc_id: "mta-wiki:5789"
title: "Changes in 1.1"
source_title: "Changes in 1.1"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.1"
revision_id: 42209
language: "en"
categories: ["Changelog", "Changes_in_1.1"]
generated_at: "2026-07-26T16:11:30.172738+00:00"
---

# Changes in 1.1

| MTA:SA Releases | Changelog Pages |
| --- | --- |
| 1.0 | 1.0.0 • 1.0.1 • 1.0.2 • 1.0.3 • 1.0.4 |
| 1.1 | 1.1.0 • 1.1.1 |
| 1.2 | 1.2.0 |
| 1.3 | 1.3.0 • 1.3.1 • 1.3.2 • 1.3.3 • 1.3.4 • 1.3.5 |
| 1.4 | 1.4.0 • 1.4.1 |
| 1.5 | 1.5.0 • 1.5.1 • 1.5.2 • 1.5.3 • 1.5.4 • 1.5.5 • 1.5.6 • 1.5.7 • 1.5.8 • 1.5.9 |
| 1.6 | 1.6.0 |
| 1.7 | 1.7.0 |

This page lists all changes which may be relevant to scripters and end users. Any changes which were back ported to 1.0.x have not been listed here. If you know of any changes that need mentioning feel free to update the list as the original author of this page does not understand every commit made (he isn't a developer)

## End-user features

**Very incomplete list**

- Vehicle handling can be modified by servers

- Custom fonts

- Special skins

- Improved server browser

- Voice chat (on servers that support it)

- Improved sound support, including streaming audio

- Increased maximum player count

- Custom shaders

- Cars can now have any color you want, not just the ones GTA has normally

- GUI Skin switching

## Client

### New Functions

- Added [guiCreateComboBox](mta://scripting/client/functions/guicreatecombobox.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1815](http://code.google.com/p/mtasa-blue/source/detail?r=1815)

- Added [guiComboBoxAddItem](mta://scripting/client/functions/guicomboboxadditem.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1815](http://code.google.com/p/mtasa-blue/source/detail?r=1815)

- Added [guiComboBoxGetItemText](mta://scripting/client/functions/guicomboboxgetitemtext.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1815](http://code.google.com/p/mtasa-blue/source/detail?r=1815)

- Added [guiComboBoxSetItemText](mta://scripting/client/functions/guicomboboxsetitemtext.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1815](http://code.google.com/p/mtasa-blue/source/detail?r=1815)

- Added [guiComboBoxRemoveItem](mta://scripting/client/functions/guicomboboxremoveitem.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1815](http://code.google.com/p/mtasa-blue/source/detail?r=1815)

- Added [guiComboBoxGetSelected](mta://scripting/client/functions/guicomboboxgetselected.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1815](http://code.google.com/p/mtasa-blue/source/detail?r=1815)

- Added [guiComboBoxSetSelected](mta://scripting/client/functions/guicomboboxsetselected.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1815](http://code.google.com/p/mtasa-blue/source/detail?r=1815)

- Added [getPedMoveState](mta://scripting/client/functions/getpedmovestate.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1842](http://code.google.com/p/mtasa-blue/source/detail?r=1842)

- Added [getCameraViewMode](mta://scripting/client/functions/getcameraviewmode.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1861](http://code.google.com/p/mtasa-blue/source/detail?r=1861)

- Added [setCameraViewMode](mta://scripting/client/functions/setcameraviewmode.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1861](http://code.google.com/p/mtasa-blue/source/detail?r=1861)

- Added [resetTimer](mta://scripting/shared/functions/resettimer.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1876](http://code.google.com/p/mtasa-blue/source/detail?r=1876)

- Added [getSoundMetaTags](mta://scripting/client/functions/getsoundmetatags.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1755](http://code.google.com/p/mtasa-blue/source/detail?r=1755)

- Added [getSoundEffects](mta://scripting/client/functions/getsoundeffects.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1755](http://code.google.com/p/mtasa-blue/source/detail?r=1755)

- Added [setSoundEffectEnabled](mta://scripting/client/functions/setsoundeffectenabled.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1755](http://code.google.com/p/mtasa-blue/source/detail?r=1755)

- Added [getElementAttachedOffsets](mta://scripting/shared/functions/getelementattachedoffsets.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1899](http://code.google.com/p/mtasa-blue/source/detail?r=1899)

- Added [setTrafficLightState](mta://scripting/shared/functions/settrafficlightstate.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1836](http://code.google.com/p/mtasa-blue/source/detail?r=1836)

- Added [getTrafficLightState](mta://scripting/shared/functions/gettrafficlightstate.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1836](http://code.google.com/p/mtasa-blue/source/detail?r=1836)

- Added [utfChar](mta://scripting/shared/functions/utfchar.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1944](http://code.google.com/p/mtasa-blue/source/detail?r=1944)

- Added [utfCode](mta://scripting/shared/functions/utfcode.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1944](http://code.google.com/p/mtasa-blue/source/detail?r=1944)

- Added [utfLen](mta://scripting/shared/functions/utflen.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1944](http://code.google.com/p/mtasa-blue/source/detail?r=1944)

- Added [utfSeek](mta://scripting/shared/functions/utfseek.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1944](http://code.google.com/p/mtasa-blue/source/detail?r=1944)

- Added [utfSub](mta://scripting/shared/functions/utfsub.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1944](http://code.google.com/p/mtasa-blue/source/detail?r=1944)

- Added [fileClose](mta://scripting/shared/functions/fileclose.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileCreate](mta://scripting/shared/functions/filecreate.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileDelete](mta://scripting/shared/functions/filedelete.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileExists](mta://scripting/shared/functions/fileexists.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileFlush](mta://scripting/shared/functions/fileflush.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileGetPos](mta://scripting/shared/functions/filegetpos.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileGetSize](mta://scripting/shared/functions/filegetsize.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileIsEOF](mta://scripting/shared/functions/fileiseof.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileOpen](mta://scripting/shared/functions/fileopen.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileRead](mta://scripting/shared/functions/fileread.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileRename](mta://scripting/shared/functions/filerename.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileSetPos](mta://scripting/shared/functions/filesetpos.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileWrite](mta://scripting/shared/functions/filewrite.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1975](http://code.google.com/p/mtasa-blue/source/detail?r=1975)

- Added [fileRename](mta://scripting/shared/functions/filerename.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2611](http://code.google.com/p/mtasa-blue/source/detail?r=2611)

- Added [setVehicleTurretPosition](mta://scripting/shared/functions/setvehicleturretposition.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1996](http://code.google.com/p/mtasa-blue/source/detail?r=1996)

- Added [getResourceExportedFunctions](mta://scripting/shared/functions/getresourceexportedfunctions.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1998](http://code.google.com/p/mtasa-blue/source/detail?r=1998)

- Added [getCameraGoggleEffect](mta://scripting/client/functions/getcameragoggleeffect.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2032](http://code.google.com/p/mtasa-blue/source/detail?r=2032)

- Added [setCameraGoggleEffect](mta://scripting/client/functions/setcameragoggleeffect.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2032](http://code.google.com/p/mtasa-blue/source/detail?r=2032)

- Added [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2052](http://code.google.com/p/mtasa-blue/source/detail?r=2052)

- Added [getWindVelocity](mta://scripting/shared/functions/getwindvelocity.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2072](http://code.google.com/p/mtasa-blue/source/detail?r=2072)

- Added [setWindVelocity](mta://scripting/shared/functions/setwindvelocity.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2072](http://code.google.com/p/mtasa-blue/source/detail?r=2072)

- Added [resetWindVelocity](mta://scripting/shared/functions/resetwindvelocity.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2072](http://code.google.com/p/mtasa-blue/source/detail?r=2072)

- Added [guiSetInputMode](mta://scripting/client/functions/guisetinputmode.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2075](http://code.google.com/p/mtasa-blue/source/detail?r=2075)

- Added [guiGetInputMode](mta://scripting/client/functions/guigetinputmode.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2075](http://code.google.com/p/mtasa-blue/source/detail?r=2075)

- Added [getWaterColor](mta://scripting/shared/functions/getwatercolor.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2092](http://code.google.com/p/mtasa-blue/source/detail?r=2092)

- Added [getSkyGradient](mta://scripting/shared/functions/getskygradient.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2093](http://code.google.com/p/mtasa-blue/source/detail?r=2093)

- Added [setElementFrozen](mta://scripting/shared/functions/setelementfrozen.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2096](http://code.google.com/p/mtasa-blue/source/detail?r=2096)

- Added [isElementFrozen](mta://scripting/shared/functions/iselementfrozen.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2096](http://code.google.com/p/mtasa-blue/source/detail?r=2096)

- Added [getInteriorSoundsEnabled](mta://scripting/shared/functions/getinteriorsoundsenabled.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2100](http://code.google.com/p/mtasa-blue/source/detail?r=2100)

- Added [setInteriorSoundsEnabled](mta://scripting/shared/functions/setinteriorsoundsenabled.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2100](http://code.google.com/p/mtasa-blue/source/detail?r=2100)

- Added [getRainLevel](mta://scripting/shared/functions/getrainlevel.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2103](http://code.google.com/p/mtasa-blue/source/detail?r=2103)

- Added [setRainLevel](mta://scripting/shared/functions/setrainlevel.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2103](http://code.google.com/p/mtasa-blue/source/detail?r=2103)

- Added [resetRainLevel](mta://scripting/shared/functions/resetrainlevel.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2103](http://code.google.com/p/mtasa-blue/source/detail?r=2103)

- Added [getFogDistance](mta://scripting/shared/functions/getfogdistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2104](http://code.google.com/p/mtasa-blue/source/detail?r=2104)

- Added [setFogDistance](mta://scripting/shared/functions/setfogdistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2104](http://code.google.com/p/mtasa-blue/source/detail?r=2104)

- Added [resetFogDistance](mta://scripting/shared/functions/resetfogdistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2104](http://code.google.com/p/mtasa-blue/source/detail?r=2104)

- Added [getEasingValue](mta://scripting/shared/functions/geteasingvalue.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2122](http://code.google.com/p/mtasa-blue/source/detail?r=2122)

- Added [interpolateBetween](mta://scripting/shared/functions/interpolatebetween.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2122](http://code.google.com/p/mtasa-blue/source/detail?r=2122)

- Added [getSunColor](mta://scripting/shared/functions/getsuncolor.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2134](http://code.google.com/p/mtasa-blue/source/detail?r=2134)

- Added [setSunColor](mta://scripting/shared/functions/setsuncolor.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2134](http://code.google.com/p/mtasa-blue/source/detail?r=2134)

- Added [resetSunColor](mta://scripting/shared/functions/resetsuncolor.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2134](http://code.google.com/p/mtasa-blue/source/detail?r=2134)

- Added [getSunSize](mta://scripting/shared/functions/getsunsize.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2135](http://code.google.com/p/mtasa-blue/source/detail?r=2135)

- Added [setSunSize](mta://scripting/shared/functions/setsunsize.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2135](http://code.google.com/p/mtasa-blue/source/detail?r=2135)

- Added [resetSunSize](mta://scripting/shared/functions/resetsunsize.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2135](http://code.google.com/p/mtasa-blue/source/detail?r=2135)

- Added [setElementID](mta://scripting/shared/functions/setelementid.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2154](http://code.google.com/p/mtasa-blue/source/detail?r=2154)

- Added [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2248](http://code.google.com/p/mtasa-blue/source/detail?r=2248)

- Added [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2248](http://code.google.com/p/mtasa-blue/source/detail?r=2248)

- Added [setVehicleDoorOpenRatio](mta://scripting/shared/functions/setvehicledooropenratio.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2329](http://code.google.com/p/mtasa-blue/source/detail?r=2329)

- Added [getVehicleDoorOpenRatio](mta://scripting/shared/functions/getvehicledooropenratio.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2329](http://code.google.com/p/mtasa-blue/source/detail?r=2329)

- Added [getHeatHaze](mta://scripting/shared/functions/getheathaze.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2349](http://code.google.com/p/mtasa-blue/source/detail?r=2349)

- Added [setHeatHaze](mta://scripting/shared/functions/setheathaze.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2349](http://code.google.com/p/mtasa-blue/source/detail?r=2349)

- Added [resetHeatHaze](mta://scripting/shared/functions/resetheathaze.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2349](http://code.google.com/p/mtasa-blue/source/detail?r=2349)

- Added [setClipBoard](mta://scripting/client/functions/setclipboard--ec01ade9.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2517](http://code.google.com/p/mtasa-blue/source/detail?r=2517)

- Added [dxCreateTexture](mta://scripting/client/functions/dxcreatetexture.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2796](http://code.google.com/p/mtasa-blue/source/detail?r=2796)

- Added [dxCreateShader](mta://scripting/client/functions/dxcreateshader.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2796](http://code.google.com/p/mtasa-blue/source/detail?r=2796)

- Added [dxSetShaderValue](mta://scripting/client/functions/dxsetshadervalue.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2796](http://code.google.com/p/mtasa-blue/source/detail?r=2796)

- Added [dxCreateRenderTarget](mta://scripting/client/functions/dxcreaterendertarget.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2797](http://code.google.com/p/mtasa-blue/source/detail?r=2797)

- Added [dxSetRenderTarget](mta://scripting/client/functions/dxsetrendertarget.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2797](http://code.google.com/p/mtasa-blue/source/detail?r=2797)

- Added [dxCreateScreenSource](mta://scripting/client/functions/dxcreatescreensource.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2797](http://code.google.com/p/mtasa-blue/source/detail?r=2797)

- Added [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2797](http://code.google.com/p/mtasa-blue/source/detail?r=2797)

- Added [dxGetMaterialSize](mta://scripting/client/functions/dxgetmaterialsize.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2797](http://code.google.com/p/mtasa-blue/source/detail?r=2797)

- Added [dxCreateFont](mta://scripting/client/functions/dxcreatefont.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2814](http://code.google.com/p/mtasa-blue/source/detail?r=2814)

- Added [guiCreateFont](mta://scripting/client/functions/guicreatefont.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2814](http://code.google.com/p/mtasa-blue/source/detail?r=2814)

- Added [engineApplyShaderToModel](mta://scripting/client/functions/engineapplyshadertomodel.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2828](http://code.google.com/p/mtasa-blue/source/detail?r=2828)

- Added [engineRemoveShaderFromModel](mta://scripting/client/functions/engineremoveshaderfrommodel.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2828](http://code.google.com/p/mtasa-blue/source/detail?r=2828)

- Added [engineGetModelNameFromID](mta://scripting/client/functions/enginegetmodelnamefromid.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2843](http://code.google.com/p/mtasa-blue/source/detail?r=2843)

- Added [engineGetModelIDFromName](mta://scripting/client/functions/enginegetmodelidfromname.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2843](http://code.google.com/p/mtasa-blue/source/detail?r=2843)

- Added [setAircraftMaxHeight](mta://scripting/shared/functions/setaircraftmaxheight.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2848](http://code.google.com/p/mtasa-blue/source/detail?r=2848)

- Added [detonateSatchels](mta://scripting/shared/functions/detonatesatchels.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2857](http://code.google.com/p/mtasa-blue/source/detail?r=2857)

- Added [engineApplyShaderToWorldTexture](mta://scripting/client/functions/engineapplyshadertoworldtexture.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2888](http://code.google.com/p/mtasa-blue/source/detail?r=2888)

- Added [engineGetModelTextureNames](mta://scripting/client/functions/enginegetmodeltexturenames.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2892](http://code.google.com/p/mtasa-blue/source/detail?r=2892)

- Added [setAmbientSoundEnabled](mta://scripting/client/functions/setambientsoundenabled.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2905](http://code.google.com/p/mtasa-blue/source/detail?r=2905)

- Added [isAmbientSoundEnabled](mta://scripting/client/functions/isambientsoundenabled.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2905](http://code.google.com/p/mtasa-blue/source/detail?r=2905)

- Added [resetAmbientSounds](mta://scripting/client/functions/resetambientsounds.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2905](http://code.google.com/p/mtasa-blue/source/detail?r=2905)

- Added [getJetpackMaxHeight](mta://scripting/shared/functions/getjetpackmaxheight.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2084](http://code.google.com/p/mtasa-blue/source/detail?r=2084)

- Added [setJetpackMaxHeight](mta://scripting/shared/functions/setjetpackmaxheight.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2084](http://code.google.com/p/mtasa-blue/source/detail?r=2084)

- Added [getNetworkStats](mta://scripting/shared/functions/getnetworkstats.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2979](http://code.google.com/p/mtasa-blue/source/detail?r=2979)

- Added [setPedAnimationProgress](mta://scripting/shared/functions/setpedanimationprogress.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=3002](http://code.google.com/p/mtasa-blue/source/detail?r=3002)

- Added [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=3041](http://code.google.com/p/mtasa-blue/source/detail?r=3041)

- Added [dxSetTestMode](mta://scripting/client/functions/dxsettestmode.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=3041](http://code.google.com/p/mtasa-blue/source/detail?r=3041)

### New Events

- Added [onClientDoubleClick](mta://scripting/client/events/onclientdoubleclick.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1808](http://code.google.com/p/mtasa-blue/source/detail?r=1808)

- Added [onClientGUIComboBoxAccepted](mta://scripting/client/events/onclientguicomboboxaccepted.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1846](http://code.google.com/p/mtasa-blue/source/detail?r=1846)

- Added [onClientSoundStream](mta://scripting/client/events/onclientsoundstream.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1755](http://code.google.com/p/mtasa-blue/source/detail?r=1755)

- Added [onClientSoundChangedMeta](mta://scripting/client/events/onclientsoundchangedmeta.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1898](http://code.google.com/p/mtasa-blue/source/detail?r=1898)

- Added [onClientSoundFinishedDownload](mta://scripting/client/events/onclientsoundfinisheddownload.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1755](http://code.google.com/p/mtasa-blue/source/detail?r=1755)

- Added [onClientVehicleExplode](mta://scripting/client/events/onclientvehicleexplode.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1906](http://code.google.com/p/mtasa-blue/source/detail?r=1906)

- Added [onClientGUIFocus](mta://scripting/client/events/onclientguifocus.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2075](http://code.google.com/p/mtasa-blue/source/detail?r=2075)

- Added [onClientGUIBlur](mta://scripting/client/events/onclientguiblur.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2075](http://code.google.com/p/mtasa-blue/source/detail?r=2075)

- Added [onClientDebugMessage](mta://scripting/client/events/onclientdebugmessage.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2091](http://code.google.com/p/mtasa-blue/source/detail?r=2091)

- Added [onClientKey](mta://scripting/client/events/onclientkey.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2480](http://code.google.com/p/mtasa-blue/source/detail?r=2480)

- Added [onClientCharacter](mta://scripting/client/events/onclientcharacter.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2480](http://code.google.com/p/mtasa-blue/source/detail?r=2480)

- Added [onClientHUDRender](mta://scripting/client/events/onclienthudrender.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2855](http://code.google.com/p/mtasa-blue/source/detail?r=2855)

- Added [onClientMinimize](mta://scripting/client/events/onclientminimize.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2945](http://code.google.com/p/mtasa-blue/source/detail?r=2945)

- Added [onClientRestore](mta://scripting/client/events/onclientrestore.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2945](http://code.google.com/p/mtasa-blue/source/detail?r=2945)

### Changes

- Improved [setPedAnimation](mta://scripting/shared/functions/setpedanimation.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1763](http://code.google.com/p/mtasa-blue/source/detail?r=1763)

- Added server join que Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1828](http://code.google.com/p/mtasa-blue/source/detail?r=1828)

- Made knife kills more balanced Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1839](http://code.google.com/p/mtasa-blue/source/detail?r=1839)

- Fixed water elements being affected by [resetMapInfo](mta://scripting/server/functions/resetmapinfo.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1863](http://code.google.com/p/mtasa-blue/source/detail?r=1863)

- Made [onClientPlayerVehicleExit](mta://scripting/client/events/onclientplayervehicleexit.md) more reliable Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1877](http://code.google.com/p/mtasa-blue/source/detail?r=1877)

- Added BASS (allows stream files to be played) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1755](http://code.google.com/p/mtasa-blue/source/detail?r=1755)

- Added synchronized traffic lights Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1836](http://code.google.com/p/mtasa-blue/source/detail?r=1836)

- Added "all" to [showPlayerHudComponent](mta://scripting/shared/functions/showplayerhudcomponent.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1912](http://code.google.com/p/mtasa-blue/source/detail?r=1912)

- Added "crosshair" to [showPlayerHudComponent](mta://scripting/shared/functions/showplayerhudcomponent.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2974](http://code.google.com/p/mtasa-blue/source/detail?r=2974)

- Added "radio" and "wanted" to [showPlayerHudComponent](mta://scripting/shared/functions/showplayerhudcomponent.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2027](http://code.google.com/p/mtasa-blue/source/detail?r=2027)

- Added support for unicode text Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1944](http://code.google.com/p/mtasa-blue/source/detail?r=1944)

- Added RGB vehicle colors Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2090](http://code.google.com/p/mtasa-blue/source/detail?r=2090)

- Synchronized vehicle doors Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2110](http://code.google.com/p/mtasa-blue/source/detail?r=2110)

- Added localPlayer predefined variable Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2140](http://code.google.com/p/mtasa-blue/source/detail?r=2140)

- Made [onClientPlayerWasted](mta://scripting/client/events/onclientplayerwasted.md) work for the local player Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2180](http://code.google.com/p/mtasa-blue/source/detail?r=2180)

- Added special skins to the game Details: [http://wiki.multitheftauto.com/wiki/Special_Skins_Page](http://wiki.multitheftauto.com/wiki/Special_Skins_Page)

- Added new main menu starting at: [http://code.google.com/p/mtasa-blue/source/detail?r=2280](http://code.google.com/p/mtasa-blue/source/detail?r=2280)

- Added GUI skin changer Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2308](http://code.google.com/p/mtasa-blue/source/detail?r=2308)

- Added basic sync for objects Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2312](http://code.google.com/p/mtasa-blue/source/detail?r=2312)

- Made game loading when joining a server much quicker Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2325](http://code.google.com/p/mtasa-blue/source/detail?r=2325)

- Added new server browser starting at: [http://code.google.com/p/mtasa-blue/source/detail?r=2441](http://code.google.com/p/mtasa-blue/source/detail?r=2441)

- Renamed hud command to showhud Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2566](http://code.google.com/p/mtasa-blue/source/detail?r=2566)

- Added random name generator Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2582](http://code.google.com/p/mtasa-blue/source/detail?r=2582)

- Added custom handling to vehicles Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2678](http://code.google.com/p/mtasa-blue/source/detail?r=2678)

- Increased the available streamer memory Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2740](http://code.google.com/p/mtasa-blue/source/detail?r=2740)

- Added shader element for [dxDrawImage](mta://scripting/client/functions/dxdrawimage.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2790](http://code.google.com/p/mtasa-blue/source/detail?r=2790)

- New message box images Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2793](http://code.google.com/p/mtasa-blue/source/detail?r=2793)

- split and gettok no longer require string.byte Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2808](http://code.google.com/p/mtasa-blue/source/detail?r=2808)

- Added world model info to [processLineOfSight](mta://scripting/client/functions/processlineofsight.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2845](http://code.google.com/p/mtasa-blue/source/detail?r=2845)

- Added default buttons in settings Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2864](http://code.google.com/p/mtasa-blue/source/detail?r=2864)

- Disabled brown streak trailer Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2880](http://code.google.com/p/mtasa-blue/source/detail?r=2880)

- Large amount of crash fixes, bug fixes and optimizations

- Added ability to add shaders to the game

- Changed [guiGridListSetItemData](mta://scripting/client/functions/guigridlistsetitemdata.md) to support any datatype [http://code.google.com/p/mtasa-blue/source/detail?r=2005](http://code.google.com/p/mtasa-blue/source/detail?r=2005)

- Added voice (microphone support) to the game [http://code.google.com/p/mtasa-blue/source/detail?r=3000](http://code.google.com/p/mtasa-blue/source/detail?r=3000)

## Server

### New Functions

- Added [getElementAttachedOffsets](mta://scripting/shared/functions/getelementattachedoffsets.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1899](http://code.google.com/p/mtasa-blue/source/detail?r=1899)

- Added [setTrafficLightsLocked](mta://scripting/shared/functions/settrafficlightslocked.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1836](http://code.google.com/p/mtasa-blue/source/detail?r=1836)

- Added [areTrafficLightsLocked](mta://scripting/shared/functions/aretrafficlightslocked.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1836](http://code.google.com/p/mtasa-blue/source/detail?r=1836)

- Added [utfChar](mta://scripting/shared/functions/utfchar.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1944](http://code.google.com/p/mtasa-blue/source/detail?r=1944)

- Added [utfCode](mta://scripting/shared/functions/utfcode.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1944](http://code.google.com/p/mtasa-blue/source/detail?r=1944)

- Added [utfLen](mta://scripting/shared/functions/utflen.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1944](http://code.google.com/p/mtasa-blue/source/detail?r=1944)

- Added [utfSeek](mta://scripting/shared/functions/utfseek.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1944](http://code.google.com/p/mtasa-blue/source/detail?r=1944)

- Added [utfSub](mta://scripting/shared/functions/utfsub.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1944](http://code.google.com/p/mtasa-blue/source/detail?r=1944)

- Added [refreshResources](mta://scripting/server/functions/refreshresources.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1994](http://code.google.com/p/mtasa-blue/source/detail?r=1994)

- Added [setVehicleTurretPosition](mta://scripting/shared/functions/setvehicleturretposition.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1996](http://code.google.com/p/mtasa-blue/source/detail?r=1996)

- Added [getObjectScale](mta://scripting/shared/functions/getobjectscale.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2029](http://code.google.com/p/mtasa-blue/source/detail?r=2029)

- Added [setObjectScale](mta://scripting/shared/functions/setobjectscale.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2029](http://code.google.com/p/mtasa-blue/source/detail?r=2029)

- Added [setElementCollisionsEnabled](mta://scripting/shared/functions/setelementcollisionsenabled.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2030](http://code.google.com/p/mtasa-blue/source/detail?r=2030)

- Added [getElementCollisionsEnabled](mta://scripting/shared/functions/getelementcollisionsenabled.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2030](http://code.google.com/p/mtasa-blue/source/detail?r=2030)

- Added [setWaterColor](mta://scripting/shared/functions/setwatercolor.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2092](http://code.google.com/p/mtasa-blue/source/detail?r=2092)

- Added [getWaterColor](mta://scripting/shared/functions/getwatercolor.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2092](http://code.google.com/p/mtasa-blue/source/detail?r=2092)

- Added [getSkyGradient](mta://scripting/shared/functions/getskygradient.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2093](http://code.google.com/p/mtasa-blue/source/detail?r=2093)

- Added [setElementFrozen](mta://scripting/shared/functions/setelementfrozen.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2096](http://code.google.com/p/mtasa-blue/source/detail?r=2096)

- Added [isElementFrozen](mta://scripting/shared/functions/iselementfrozen.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2096](http://code.google.com/p/mtasa-blue/source/detail?r=2096)

- Added [getEasingValue](mta://scripting/shared/functions/geteasingvalue.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2122](http://code.google.com/p/mtasa-blue/source/detail?r=2122)

- Added [interpolateBetween](mta://scripting/shared/functions/interpolatebetween.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2122](http://code.google.com/p/mtasa-blue/source/detail?r=2122)

- Added [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2248](http://code.google.com/p/mtasa-blue/source/detail?r=2248)

- Added [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2248](http://code.google.com/p/mtasa-blue/source/detail?r=2248)

- Added [getNetworkUsageData](mta://scripting/shared/functions/getnetworkusagedata.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2322](http://code.google.com/p/mtasa-blue/source/detail?r=2322)

- Added [setVehicleDoorOpenRatio](mta://scripting/shared/functions/setvehicledooropenratio.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2329](http://code.google.com/p/mtasa-blue/source/detail?r=2329)

- Added [getVehicleDoorOpenRatio](mta://scripting/shared/functions/getvehicledooropenratio.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2329](http://code.google.com/p/mtasa-blue/source/detail?r=2329)

- Added [getHeatHaze](mta://scripting/shared/functions/getheathaze.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2349](http://code.google.com/p/mtasa-blue/source/detail?r=2349)

- Added [setHeatHaze](mta://scripting/shared/functions/setheathaze.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2349](http://code.google.com/p/mtasa-blue/source/detail?r=2349)

- Added [resetHeatHaze](mta://scripting/shared/functions/resetheathaze.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2349](http://code.google.com/p/mtasa-blue/source/detail?r=2349)

- Added [getInteriorSoundsEnabled](mta://scripting/shared/functions/getinteriorsoundsenabled.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [setInteriorSoundsEnabled](mta://scripting/shared/functions/setinteriorsoundsenabled.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [getRainLevel](mta://scripting/shared/functions/getrainlevel.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [setRainLevel](mta://scripting/shared/functions/setrainlevel.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [resetRainLevel](mta://scripting/shared/functions/resetrainlevel.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [getSunSize](mta://scripting/shared/functions/getsunsize.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [setSunSize](mta://scripting/shared/functions/setsunsize.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [resetSunSize](mta://scripting/shared/functions/resetsunsize.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [getSunColor](mta://scripting/shared/functions/getsuncolor.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [setSunColor](mta://scripting/shared/functions/setsuncolor.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [resetSunColor](mta://scripting/shared/functions/resetsuncolor.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [getWindVelocity](mta://scripting/shared/functions/getwindvelocity.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [setWindVelocity](mta://scripting/shared/functions/setwindvelocity.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [resetWindVelocity](mta://scripting/shared/functions/resetwindvelocity.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [getFarClipDistance](mta://scripting/shared/functions/getfarclipdistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [setFarClipDistance](mta://scripting/shared/functions/setfarclipdistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [resetFarClipDistance](mta://scripting/shared/functions/resetfarclipdistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [getFogDistance](mta://scripting/shared/functions/getfogdistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [setFogDistance](mta://scripting/shared/functions/setfogdistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [resetFogDistance](mta://scripting/shared/functions/resetfogdistance.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2449](http://code.google.com/p/mtasa-blue/source/detail?r=2449)

- Added [fileRename](mta://scripting/shared/functions/filerename.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2611](http://code.google.com/p/mtasa-blue/source/detail?r=2611)

- Added [detonatePlayerSatchels](mta://scripting/server/functions/detonateplayersatchels.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2857](http://code.google.com/p/mtasa-blue/source/detail?r=2857)

- Added [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2941](http://code.google.com/p/mtasa-blue/source/detail?r=2941)

- Added [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2971](http://code.google.com/p/mtasa-blue/source/detail?r=2971)

- Added [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2971](http://code.google.com/p/mtasa-blue/source/detail?r=2971)

- Added [getJetpackMaxHeight](mta://scripting/shared/functions/getjetpackmaxheight.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2084](http://code.google.com/p/mtasa-blue/source/detail?r=2084)

- Added [getAircraftMaxHeight](mta://scripting/shared/functions/getaircraftmaxheight.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2975](http://code.google.com/p/mtasa-blue/source/detail?r=2975)

- Added [setAircraftMaxHeight](mta://scripting/shared/functions/setaircraftmaxheight.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2975](http://code.google.com/p/mtasa-blue/source/detail?r=2975)

- Added [getNetworkStats](mta://scripting/shared/functions/getnetworkstats.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2979](http://code.google.com/p/mtasa-blue/source/detail?r=2979)

- Added [setPedAnimationProgress](mta://scripting/shared/functions/setpedanimationprogress.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=3002](http://code.google.com/p/mtasa-blue/source/detail?r=3002)

- Added [setPlayerVoiceIgnoreFrom](mta://scripting/server/functions/setplayervoiceignorefrom.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=3042](http://code.google.com/p/mtasa-blue/source/detail?r=3042)

- Added [setPlayerVoiceBroadcastTo](mta://scripting/server/functions/setplayervoicebroadcastto.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=3000](http://code.google.com/p/mtasa-blue/source/detail?r=3000)

### New Events

- Added [onPlayerMute](mta://scripting/server/events/onplayermute.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1978](http://code.google.com/p/mtasa-blue/source/detail?r=1978)

- Added [onPlayerUnmute](mta://scripting/server/events/onplayerunmute.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1978](http://code.google.com/p/mtasa-blue/source/detail?r=1978)

- Added [onDebugMessage](mta://scripting/server/events/ondebugmessage.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2091](http://code.google.com/p/mtasa-blue/source/detail?r=2091)

- Added [onSettingChange](mta://scripting/server/events/onsettingchange.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2097](http://code.google.com/p/mtasa-blue/source/detail?r=2097)

- Added [onPlayerCommand](mta://scripting/server/events/onplayercommand.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2152](http://code.google.com/p/mtasa-blue/source/detail?r=2152)

- Added [onAccountDataChange](mta://scripting/server/events/onaccountdatachange.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2516](http://code.google.com/p/mtasa-blue/source/detail?r=2516)

- Added [onPlayerModInfo](mta://scripting/server/events/onplayermodinfo.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2881](http://code.google.com/p/mtasa-blue/source/detail?r=2881)

### Changes

- Fixed [isElementInWater](mta://scripting/shared/functions/iselementinwater.md) with unoccupied vehicles Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1803](http://code.google.com/p/mtasa-blue/source/detail?r=1803)

- Allowed responsible element of [kickPlayer](mta://scripting/server/functions/kickplayer.md) be a string Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1979](http://code.google.com/p/mtasa-blue/source/detail?r=1979)

- Allowed responsible element of [banPlayer](mta://scripting/server/functions/banplayer.md)/[addBan](mta://scripting/server/functions/addban.md) be a string Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1980](http://code.google.com/p/mtasa-blue/source/detail?r=1980)

- Added "all" to [showPlayerHudComponent](mta://scripting/shared/functions/showplayerhudcomponent.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=1912](http://code.google.com/p/mtasa-blue/source/detail?r=1912)

- Added "radio" and "wanted" to [showPlayerHudComponent](mta://scripting/shared/functions/showplayerhudcomponent.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2027](http://code.google.com/p/mtasa-blue/source/detail?r=2027)

- Added optional type to [aclListRights](mta://scripting/server/functions/acllistrights.md) Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2036](http://code.google.com/p/mtasa-blue/source/detail?r=2036)

- Updated [setVehicleColor](mta://scripting/shared/functions/setvehiclecolor.md) and [getVehicleColor](mta://scripting/shared/functions/getvehiclecolor.md) to support RGB vehicle colors

- Raised max player count to 65535 Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2118](http://code.google.com/p/mtasa-blue/source/detail?r=2118)

- Made [onPlayerWeaponSwitch](mta://scripting/server/events/onplayerweaponswitch.md) work Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2137](http://code.google.com/p/mtasa-blue/source/detail?r=2137)

- Rotation parameter in [createPed](mta://scripting/shared/functions/createped.md) now works Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2246](http://code.google.com/p/mtasa-blue/source/detail?r=2246)

- Added resources cataloges ([likethis]) Starting at: [http://code.google.com/p/mtasa-blue/source/detail?r=2716](http://code.google.com/p/mtasa-blue/source/detail?r=2716)

- [split](mta://scripting/shared/functions/split.md) and [gettok](mta://scripting/shared/functions/gettok.md) no longer require string.byte Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2808](http://code.google.com/p/mtasa-blue/source/detail?r=2808)

- Added bandwidth stats to performance browser Details: [http://code.google.com/p/mtasa-blue/source/detail?r=2901](http://code.google.com/p/mtasa-blue/source/detail?r=2901)

- Added bandwidth reduction options Details: [http://code.google.com/p/mtasa-blue/source/detail?r=3028](http://code.google.com/p/mtasa-blue/source/detail?r=3028)

- Large amount of crash fixes, bug fixes and optimizations

## Resources

- Removed set blur from admin due to it causing conflicts with other gamemodes

- Fixed a variety of debug warnings and errors in resources

- Players can no longer capture the vehicle in an enemy base in CTV gamemode

- Fixed a problem in the maplimits resource causing performance problems over time

- Added HTTP runcode interface

- Changed resources structure to use the [catalog] system

- Added RGB vehicle colors and headlight colors to freeroam

- Upgraded from newly deprecated functions setPedFrozen and setVehicleFrozen

- Make play resource give out new special skins

- Removed redundant localPlayer defines as already predefined in 1.1

- Encoded all resources in UTF-8

- Added special skins to freeroam

- Improved reliability of admin flags

- Fixed stats reset after a respawn with default stats

- Improved reliability of parachutes

- Sped up map ratings resource

- Improvements to performancebrowser resource

- Fixed resourcebrowser display problems in IE

- Made it easier to close the freeroam spawn selector

- Fixed lag during startup of admin

- Added normal dates to resourcemanager

- Fixed lag caused by country flags

## Map Editor

- Added a loading bar when loading a map is taking a long time

- Added basic test mode to allow single players to test their map without starting test

- Fixed object position and rotation not saving if selected during the save

- Added trains to the Map Editor

- Fixed some element attributes not cloning with clone element

- Made map settings function in test mode

- Added trailers to the Map Editor

- Added various safety checks to saving and loading

- Added option to clone world buildings

- Fixed a bug when not being able to open maps
