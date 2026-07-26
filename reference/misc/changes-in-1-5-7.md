---
doc_id: "mta-wiki:10779"
title: "Changes in 1.5.7"
source_title: "Changes in 1.5.7"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.5.7"
revision_id: 72820
language: "en"
categories: ["Changelog"]
generated_at: "2026-07-26T16:10:31.158498+00:00"
---

# Changes in 1.5.7

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

1.5.7 was released on September 1, 2019.

- GitHub commit log: [https://github.com/multitheftauto/mtasa-blue/compare/1.5.6...1.5.7](https://github.com/multitheftauto/mtasa-blue/compare/1.5.6...1.5.7)

- GitHub milestone: [https://github.com/multitheftauto/mtasa-blue/milestone/6](https://github.com/multitheftauto/mtasa-blue/milestone/6)

- Release announcement on forums: [https://forum.mtasa.com/topic/119761-multi-theft-auto-san-andreas-is-released/](https://forum.mtasa.com/topic/119761-multi-theft-auto-san-andreas-is-released/)

## Main Additions / Changes

Click to collapse [-]

- Add new drawing functions: [dxDrawPrimitive](mta://scripting/client/functions/dxdrawprimitive.md) and [dxDrawMaterialPrimitive](mta://scripting/client/functions/dxdrawmaterialprimitive.md)

- Improve game entity pool performance ([#480](https://github.com/multitheftauto/mtasa-blue/pull/480) by **saml1er**)

- Fix swimming speed on higher FPS ([#379](https://github.com/multitheftauto/mtasa-blue/pull/379) by **nonamenoname** and **saml1er**)

- Skimmers can now lift off water at high FPS ([#433](https://github.com/multitheftauto/mtasa-blue/pull/433) by **forkerer**)

- Add [onClientWorldSound](mta://scripting/client/events/onclientworldsound.md) (See commit [8302b4c](https://github.com/multitheftauto/mtasa-blue/commit/8302b4c64da348691303bf56d5f80413b7610fcc) by **botder**)

- Add [onClientPedStep](mta://scripting/client/events/onclientpedstep.md) ([#212](https://github.com/multitheftauto/mtasa-blue/pull/212), see commit [d9b6d20](https://github.com/multitheftauto/mtasa-blue/commit/d9b6d207f63d1d15bd93de956955ed2bd73bb176) by **CrosRoad95**)

- Add [onClientVehicleWeaponHit](mta://scripting/client/events/onclientvehicleweaponhit.md) ([GitHub #477](https://github.com/multitheftauto/mtasa-blue/pull/477) and see commit [1055587](https://github.com/multitheftauto/mtasa-blue/commit/1055587fbf84eaeb3597e1507b98ae842b348ef4), by **CrosRoad95** and **botder**)

- Add [engineGetSurfaceProperties](mta://scripting/client/functions/enginegetsurfaceproperties.md), [engineSetSurfaceProperties](mta://scripting/client/functions/enginesetsurfaceproperties.md) and [engineResetSurfaceProperties](mta://scripting/client/functions/engineresetsurfaceproperties.md) ([#702](https://github.com/multitheftauto/mtasa-blue/pull/702) by **CrosRoad95**)

## Statistics

Click to collapse [-]

These are some statistics since the [previous release](mta://reference/misc/changes-in-1-5-6.md).

- This is the **24th** 1.x.x release, released [31.8.2019](https://buildinfo.mtasa.com/?Revision=18957)

- **359** days

- **27** new functions

- **4** new events

- **0** deprecations

- **5** announced backwards incompatible changes

- **117+** bug fixes and changes

- **544** commits ([see comparison](https://github.com/multitheftauto/mtasa-blue/compare/1.5.6...1.5.7))

- **0** new open Mantis issues

- **4** resolved Mantis issues

- **676** closed Mantis issues

- **330** new open GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+created%3A%3E2018-09-06))

- **93** resolved GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?utf8=%E2%9C%93&q=is%3Aclosed+is%3Aissue+milestone%3A1.5.7+created%3A%3E2018-09-06))

- **93** closed GitHub issues ([see list](https://github.com/multitheftauto/mtasa-blue/issues?utf8=%E2%9C%93&q=is%3Aclosed+is%3Aissue+closed%3A%3E2018-09-06+-milestone%3A1.5.7))

- **46** new open GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?utf8=%E2%9C%93&q=is%3Aopen+is%3Apr+created%3A%3E2018-09-06))

- **82** merged GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?q=is%3Apr+milestone%3A1.5.7+is%3Amerged))

- **30** closed GitHub pull requests ([see list](https://github.com/multitheftauto/mtasa-blue/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aunmerged+closed%3A%3E%3D2018-09-06))

- **30** contributors of which **7** are new ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors?from=2018-09-07&type=c&to=2019-08-31))

- **64+** total contributors ([see list](https://github.com/multitheftauto/mtasa-blue/graphs/contributors))

- **8** vendor updates

**Note:** Last update to these statistics was made
2,521 days ago.

## Scripting

### 5 Backwards Incompatible Changes

These changes will take effect in 1.6:

- [callRemote](mta://scripting/server/functions/callremote.md) callbacks currently set the error code to **nil** when there is no error. In 1.6, to be consistent with [fetchRemote](mta://scripting/shared/functions/fetchremote.md), the error code reported will be **0**. See [GitHub #294](https://github.com/multitheftauto/mtasa-blue/issues/294).

- Since July 2016 if you provide an invalid string like **"randomstring"** when a function expects a number, the string will be treated as **0** and raise a script warning. In 1.6 this will be an error. You will still be able to provide strings containing numbers (e.g. **"100"** and **"12.34"**), this change only affects invalid strings. See [GitHub #1043](https://github.com/multitheftauto/mtasa-blue/issues/1043).

- When providing a width and height of (0, 0) to [createBrowser](mta://scripting/client/functions/createbrowser.md) or [guiCreateBrowser](mta://scripting/client/functions/guicreatebrowser.md) you will encounter a script error instead of a warning. The warning was introduced Feb 2019. See [GitHub #1069](https://github.com/multitheftauto/mtasa-blue/issues/1069).

- Some functions expect only unsigned integers (positive numbers), and since Jan 2016 providing negative numbers would be a warning. This will now be an error. See [GitHub #1070](https://github.com/multitheftauto/mtasa-blue/issues/1070).

- Since Aug 2015, we replaced the custom **mtalocal://** URL scheme with **[http://mta/resourceName/blah.html](http://mta/resourceName/blah.html)**. This **mtalocal://** URL scheme will now be removed. See [GitHub #1071](https://github.com/multitheftauto/mtasa-blue/issues/1071).

This list is inconclusive and we may introduce more changes later.

### Client

Click to collapse [-]

#### 23 New Functions

- Add [guiComboBoxGetItemCount](mta://scripting/client/functions/guicomboboxgetitemcount.md) and [guiComboBoxSetOpen](mta://scripting/client/functions/guicomboboxsetopen.md) and [guiComboBoxIsOpen](mta://scripting/client/functions/guicomboboxisopen.md) ([#280](https://github.com/multitheftauto/mtasa-blue/pull/280) by **FileEX**)

- Add [getVehicleComponentScale](mta://scripting/client/functions/getvehiclecomponentscale.md), [setVehicleComponentScale](mta://scripting/client/functions/setvehiclecomponentscale.md) and [resetVehicleComponentScale](mta://scripting/client/functions/resetvehiclecomponentscale.md) ([#361](https://github.com/multitheftauto/mtasa-blue/pull/361) by **forkerer**)

- Add [guiGridListGetSelectionMode](mta://scripting/client/functions/guigridlistgetselectionmode.md) and [guiGridListIsSortingEnabled](mta://scripting/client/functions/guigridlistissortingenabled.md) ([#691](https://github.com/multitheftauto/mtasa-blue/pull/691) by **StrixG**)

- Add [dxDrawPrimitive](mta://scripting/client/functions/dxdrawprimitive.md) and [dxDrawMaterialPrimitive](mta://scripting/client/functions/dxdrawmaterialprimitive.md) ([#339](https://github.com/multitheftauto/mtasa-blue/pull/339) by **CrosRoad95** and **forkerer**)

- Add [getObjectProperty](mta://scripting/client/functions/getobjectproperty.md) and [setObjectProperty](mta://scripting/client/functions/setobjectproperty.md) ([#162](https://github.com/multitheftauto/mtasa-blue/pull/162) by **lex128**)

- Add [setVehicleModelDummyPosition](mta://scripting/client/functions/setvehiclemodeldummyposition.md) and [getVehicleModelDummyPosition](mta://scripting/client/functions/getvehiclemodeldummyposition.md) ([#390](https://github.com/multitheftauto/mtasa-blue/pull/390) by **forkerer**)

- Add [getSoundBufferLength](mta://scripting/client/functions/getsoundbufferlength.md) ([#679](https://github.com/multitheftauto/mtasa-blue/pull/679) by **StrixG**)

- Add [getCommandHandlers](mta://scripting/shared/functions/getcommandhandlers.md) (previously available server-side only) ([#653](https://github.com/multitheftauto/mtasa-blue/pull/653) by **xLuxy**)

- Add [getPedFightingStyle](mta://scripting/shared/functions/getpedfightingstyle.md) (previously available server-side only) ([#808](https://github.com/multitheftauto/mtasa-blue/pull/808) by **StrixG**)

- Add [guiFocus](mta://scripting/client/functions/guifocus.md) and [guiBlur](mta://scripting/client/functions/guiblur.md) ([#365](https://github.com/multitheftauto/mtasa-blue/pull/365) by **patrikjuvonen**)

- Add [engineGetSurfaceProperties](mta://scripting/client/functions/enginegetsurfaceproperties.md), [engineSetSurfaceProperties](mta://scripting/client/functions/enginesetsurfaceproperties.md) and [engineResetSurfaceProperties](mta://scripting/client/functions/engineresetsurfaceproperties.md) ([#702](https://github.com/multitheftauto/mtasa-blue/pull/702) by **CrosRoad95**)

- Add [getKeyboardLayout](mta://scripting/client/functions/getkeyboardlayout.md) (See commit [10cd2ed](https://github.com/multitheftauto/mtasa-blue/commit/10cd2edcb6b5ce676cd9ac0b6d2138c1913b138d) by **botder**)

#### 4 New Events

- Add [onClientWorldSound](mta://scripting/client/events/onclientworldsound.md) (See commit [8302b4c](https://github.com/multitheftauto/mtasa-blue/commit/8302b4c64da348691303bf56d5f80413b7610fcc) by **botder**)

- Add [onClientPedStep](mta://scripting/client/events/onclientpedstep.md) ([#212](https://github.com/multitheftauto/mtasa-blue/pull/212), see commit [d9b6d20](https://github.com/multitheftauto/mtasa-blue/commit/d9b6d207f63d1d15bd93de956955ed2bd73bb176) by **CrosRoad95**)

- Add [onClientVehicleWeaponHit](mta://scripting/client/events/onclientvehicleweaponhit.md) ([GitHub #477](https://github.com/multitheftauto/mtasa-blue/pull/477) and see commit [1055587](https://github.com/multitheftauto/mtasa-blue/commit/1055587fbf84eaeb3597e1507b98ae842b348ef4), by **CrosRoad95** and **botder**)

- Add [onClientElementModelChange](mta://scripting/client/events/onclientelementmodelchange.md) ([#824](https://github.com/multitheftauto/mtasa-blue/pull/824) by **botder**)

#### New Arguments & Parameters

- *retainPedState* argument for [setPedAnimation](mta://scripting/shared/functions/setpedanimation.md)

#### 9 Bug Fixes & Changes

- Ability to pass [vectors](mta://reference/misc/vector.md) and [matrices](mta://reference/misc/matrix.md) to [shaders](mta://reference/misc/shader.md) ([#391](https://github.com/multitheftauto/mtasa-blue/pull/391) by **tederis**)

- Add option to load raw data in [dxCreateShader](mta://scripting/client/functions/dxcreateshader.md) ([#441](https://github.com/multitheftauto/mtasa-blue/pull/441) by **samr46**)

- [onClientExplosion](mta://scripting/client/events/onclientexplosion.md) is now triggered by barrel explosion ([Fixes #491](https://github.com/multitheftauto/mtasa-blue/pull/491), see commit [700b22](https://github.com/multitheftauto/mtasa-blue/commit/700b22968be95b5793ab8a8532682a259b0af598) by **botder**)

- Show an error for client-side elements in [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md) ([Fixes #692](https://github.com/multitheftauto/mtasa-blue/issues/692), see commit [f843736](https://github.com/multitheftauto/mtasa-blue/commit/f84373637e492aa26a1e67b8d86375a7a5935e1e) by **botder**)

- [engineReplaceAnimation](mta://scripting/client/functions/enginereplaceanimation.md) and [engineRestoreAnimation](mta://scripting/client/functions/enginerestoreanimation.md) will now apply to currently running animations ([Fixes #275](https://github.com/multitheftauto/mtasa-blue/issues/275), see commit [4019806](https://github.com/multitheftauto/mtasa-blue/commit/4019806eb519fbd046bd05db92b9fc3aa738612b) and [80bb898](https://github.com/multitheftauto/mtasa-blue/commit/80bb8988895c537d841409eceed8d5af67d6ac4c) by **Saml1er**)

- Add file integrity check for bassopus.dll (See commit [7d22db6](https://github.com/multitheftauto/mtasa-blue/commit/7d22db689088e7ee22258a35861eb17402228210) by **patrikjuvonen**)

- Allow [setSoundPosition](mta://scripting/client/functions/setsoundposition.md) to be used with file streams ([#703](https://github.com/multitheftauto/mtasa-blue/pull/703) by **forkerer**)

- Add a warning for invalid parameters to [createBrowser](mta://scripting/client/functions/createbrowser.md) and [guiCreateBrowser](mta://scripting/client/functions/guicreatebrowser.md) (See commit [2336f78](https://github.com/multitheftauto/mtasa-blue/commit/2336f780e6dcd250e2aecfe81fe9e5f95ca5d1d4) by **botder**)

- Add OOP method "getNativeSize" for [guiStaticImageGetNativeSize](mta://scripting/client/functions/guistaticimagegetnativesize.md) ([#1045](https://github.com/multitheftauto/mtasa-blue/pull/1045) by **xerox8521**)

### Server

Click to collapse [-]

#### New Arguments & Parameters

- Add optional case sensitivity parameter to [getAccount](mta://scripting/server/functions/getaccount.md) ([#230](https://github.com/multitheftauto/mtasa-blue/pull/230), see commit [7401422](https://github.com/multitheftauto/mtasa-blue/commit/7401422181f2e73df06b6bf66b63163984b2ae46) by **Dezash**)

### Shared (*Client & Server side*)

Click to collapse [-]

#### 4 New Functions

- Add support for [Lua os.* functions](http://lua-users.org/wiki/OsLibraryTutorial) ([#316](https://github.com/multitheftauto/mtasa-blue/pull/316) by **Dezash**)

- Following os functions have been enabled:

- os.clock

- os.date

- os.difftime

- os.time

- Following os functions have been disabled for security reasons:

- os.execute

- os.exit

- os.getenv

- os.remove

- os.rename

- os.setlocale

- os.tmpname

#### 2 Bug Fixes & Changes

- Allow [setTimer](mta://scripting/shared/functions/settimer.md) interval below 50ms (See commit [5910ddf](https://github.com/multitheftauto/mtasa-blue/commit/5910ddf3bb3005f7b1c44f1eb9c888d045fa3c55) by **botder**)

- Add file and function names in "infinite running script" (Fixes [#967](https://github.com/multitheftauto/mtasa-blue/issues/967), see commit [80fe718](https://github.com/multitheftauto/mtasa-blue/commit/80fe71869d6a94682a972894d90727786970734c) by **Jusonex**)

## Client

Click to collapse [-]

### 74 Bug Fixes & Changes

- Various custom animation related bug fixes and improvements by **saml1er**

- Fix swimming speed on higher FPS ([#379](https://github.com/multitheftauto/mtasa-blue/pull/379) by **nonamenoname** and **saml1er**)

- [Added for testing] Fix many collisionless objects ([#378](https://github.com/multitheftauto/mtasa-blue/pull/378) by **samr46**)

- Players can now switch weapons whilst attached to elements ([#533](https://github.com/multitheftauto/mtasa-blue/pull/533) by **CrosRoad95**)

- Using */voiceptt* with a custom bind won't crash the client, using */voiceptt* without further parameters will toggle voice push-to-talk. (See commit [d5e5d46](https://github.com/multitheftauto/mtasa-blue/commit/d5e5d46e7afb62173ca329198a96294c183ed7b0) by **botder**)

- Fix client crash for [fixVehicle](mta://scripting/shared/functions/fixvehicle.md) in [onClientVehicleCollision](mta://scripting/client/functions/onclientvehiclecollision.md) (See commit [5c6db96](https://github.com/multitheftauto/mtasa-blue/commit/5c6db9688875831befcc58ab750c284965b167b2) by **botder**)

- Credits to **FileEX** for providing a temporary fix by disabling the event for blown vehicles ([#600](https://github.com/multitheftauto/mtasa-blue/pull/600))

- Add support for planes, trains and boats for [onClientVehicleCollision](mta://scripting/client/functions/onclientvehiclecollision.md) (Fixes [#540](https://github.com/multitheftauto/mtasa-blue/issues/540), see commit [2017aea](https://github.com/multitheftauto/mtasa-blue/commit/2017aea31c0556aa9827919264faaf27ef70fa90) by **botder**)

- Stream-in an object after attaching if it was streamed-out beforehand (Fixes [#623](https://github.com/multitheftauto/mtasa-blue/issues/623), see commit [3ab471c](https://github.com/multitheftauto/mtasa-blue/commit/3ab471ccb3de31757741da22a60b6132461d362b) by **botder**)

- Fix voice freeze (See commit [39c1ba0](https://github.com/multitheftauto/mtasa-blue/commit/39c1ba00ae122f0393cf5f185033b17c10b392da) by **botder**)

- Fix camera object-clipping, melee damage, sniper damage and helicopter blades collision outside map boundaries (Fixes [#407](https://github.com/multitheftauto/mtasa-blue/issues/407), [#466](https://github.com/multitheftauto/mtasa-blue/issues/466), [#459](https://github.com/multitheftauto/mtasa-blue/issues/459), [#647](https://github.com/multitheftauto/mtasa-blue/issues/647), see commit [6626134](https://github.com/multitheftauto/mtasa-blue/commit/662613429017b722a4a1f11cc58394e22db3fdef) by **lopezloo**)

- Update camera target if warping to passenger seat from other vehicle (Fixes [#625](https://github.com/multitheftauto/mtasa-blue/issues/625), see commit [19cb321](https://github.com/multitheftauto/mtasa-blue/commit/19cb321a0e9ef3cc4d0bdc8d2de4b7b7c8a649d7) by **botder**)

- Moved and restyled language selection to the bottom of the main menu (See commit [6f6b2ed](https://github.com/multitheftauto/mtasa-blue/commit/6f6b2ed336db827d3fc4100e0fc77107c972c6e3) by **ccw**)

- Skimmers can now lift off water at high FPS ([#433](https://github.com/multitheftauto/mtasa-blue/pull/433) by **forkerer**)

- Update frame rate limiter (See commit [98cdd86](https://github.com/multitheftauto/mtasa-blue/commit/98cdd866b3b4d935eac94b10db1e7549d40ac79b) and [bc94009](https://github.com/multitheftauto/mtasa-blue/commit/bc940094f0d910eea90319260644adecc6292b3c) by **ccw**)

- Add Vietnamese translation (See commit [f2149d5](https://github.com/multitheftauto/mtasa-blue/commit/f2149d5bf904d57c0121c564f738b966b57cb738) by **ccw**, with contributions from **bromboy2010**, **steroidz**, and **99 isme**)

- Add support for another *gta-sa.exe* variant to the installer (See commit [e829a20](https://github.com/multitheftauto/mtasa-blue/commit/e829a201c804ae318112efeb111b608d13712281) by **ccw**)

- Fix [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md) from 11 to 0 resets goggle effect (Fixes [#579](https://github.com/multitheftauto/mtasa-blue/issues/579), see commit [e356849](https://github.com/multitheftauto/mtasa-blue/commit/e35684979492b794e060b5eb483dfe3752ae442f) by **FileEX**)

- Fix wrong value for *matchingDimension* in [onClientMarkerLeave](mta://scripting/client/events/onclientmarkerleave.md) (Fixes [#736](https://github.com/multitheftauto/mtasa-blue/issues/736), see commit [8f94072](https://github.com/multitheftauto/mtasa-blue/commit/8f940724a57d3362e224b13486433b2a7cfe4945) by **botder**)

- Fix debug chat movement when changing audio volume (See commit [7febd31](https://github.com/multitheftauto/mtasa-blue/commit/7febd31af79e7392ce077c14750f8eb8d0e76a5f) by **botder**)

- Updated translations (by **ccw**)

- Fix [testLineAgainstWater](mta://scripting/client/functions/testlineagainstwater.md) to prevent crashes and to work in more scenarios ([#836](https://github.com/multitheftauto/mtasa-blue/pull/836) by **forkerer**)

- Fix invalid model ID in engine LOD functions cause a crash ([#299](https://github.com/multitheftauto/mtasa-blue/pull/299) by **patrikjuvonen**)

- Fix [loadBrowserURL](mta://scripting/client/functions/loadbrowserurl.md) crashing the client by enforcing 1x1 minimum size for render item (See commit [8665a72](https://github.com/multitheftauto/mtasa-blue/commit/8665a722e6bb68b5372377525d121ef476c7ba01) by **botder**)

- Fix incorrect progress display for updater download (See commit [557b636](https://github.com/multitheftauto/mtasa-blue/commit/557b636bd219ba6cfcb51531fce6503c18de9015) by **ccw**)

- Delete old update files instead of moving to the recycle bin (See commit [576a5fb](https://github.com/multitheftauto/mtasa-blue/commit/576a5fb3d379eade1068e68a8873b10459a64834) by **ccw**)

- Clamp [setEffectDensity](mta://scripting/client/functions/seteffectdensity.md) to the max client density ([#843](https://github.com/multitheftauto/mtasa-blue/pull/843) by **StrixG**)

- Read the correct amount of bytes in [setPedAnimationSpeed](mta://scripting/shared/functions/setpedanimationspeed.md) (See commit [51fa4a2](https://github.com/multitheftauto/mtasa-blue/commit/51fa4a2db7e389b44641fb2523888190dc5e57bb) by **botder**)

- Fix message box being obscured sometimes ([6cc5af7](https://github.com/multitheftauto/mtasa-blue/commit/6cc5af70b74ab63f2fe2a73512cc36fc9887b5d1) by **ccw**)

- Fix loading dlls from the wrong directory ([ad68ee8](https://github.com/multitheftauto/mtasa-blue/commit/ad68ee8492ffbd8138825b1d3746d995e22ac8d9) by **ccw**)

- Add MS dll to installer ([b7fefff](https://github.com/multitheftauto/mtasa-blue/commit/b7fefffdc5fa4f46e71cd048314bdd259f785ca2) by **ccw**)

- Fix crash when calling [isVehicleWheelOnGround](mta://scripting/client/functions/isvehiclewheelonground.md) with streamed out vehicle ([fed0725](https://github.com/multitheftauto/mtasa-blue/commit/fed0725241e16d3261271c05c59d96c324dd66b8) by **ccw**)

- Fix WidgetLookFeel::getImagerySection exceptions (See commit [5ac8939](https://github.com/multitheftauto/mtasa-blue/commit/5ac8939f079895c19587094c98fe54a0a42b3012) by **qaisjp**)

- Fix invisible disabled scrollbars (See commit [01ee6de](https://github.com/multitheftauto/mtasa-blue/commit/01ee6decb3032962732c80d216d306b29ffe25a6) by **qaisjp**)

- Fix disabled comboboxes showing a hovered arrow (See commit [22b0736](https://github.com/multitheftauto/mtasa-blue/commit/22b0736cfa868a97ef6ba19d245e7e1d605ace07) by **qaisjp**)

- Fix zalgo chat messages spilling over ([#885](https://github.com/multitheftauto/mtasa-blue/pull/885) by **qaisjp**)

- Fix master volume not being applied for GTA:SA sounds after launching the game (See commit [3053bf5](https://github.com/multitheftauto/mtasa-blue/commit/3053bf50acbaf7ca10c3652674ead26c80972593) by **patrikjuvonen**)

- Fix [createTrayNotification](mta://scripting/client/functions/createtraynotification.md) not working for Windows 10 ([#914](https://github.com/multitheftauto/mtasa-blue/pull/914) by **samr46**)

- Add arrow key chat input history ([#822](https://github.com/multitheftauto/mtasa-blue/pull/822) by **patrikjuvonen**)

- Fix [setCloudsEnabled](mta://scripting/shared/functions/setcloudsenabled.md) affects moon and stars but not actual clouds ([#926](https://github.com/multitheftauto/mtasa-blue/pull/926) by **samr46**)

- Don't add duplicate entries to client console input history (See commit [d7656a2](https://github.com/multitheftauto/mtasa-blue/commit/d7656a2ad7cdcdc7c45fc5b9ff81db473dfe4527) by **patrikjuvonen**)

- Fix missing skins crashing settings menu (See commit [9101984](https://github.com/multitheftauto/mtasa-blue/commit/91019844340f39f14cf4596e2b23e385662420e0) by **qaisjp**)

- Fix CEGUI exit crash (See commit [302b83f](https://github.com/multitheftauto/mtasa-blue/commit/302b83f16c9dfc2936310e4eaa7993c97a4cf2e7) by **ccw**)

- Fix crash in CClientPed::IsReloadingWeapon (See commit [627b39d](https://github.com/multitheftauto/mtasa-blue/commit/627b39d9d40bdcfce139abec97a800a855cd7cc6) by **botder**)

- Remove *localhost* from the CEF whitelist (See commit [505467e](https://github.com/multitheftauto/mtasa-blue/commit/505467ec8c3ac1b3ad17fb0247dc15809e013968) by **Jusonex**)

- Add reference counter increment/decrement on dummies change ([#1021](https://github.com/multitheftauto/mtasa-blue/pull/1021) by **forkerer**)

- Allow newlines and tabs for chat/debug/console messages sent from server (Fixes [#684](https://github.com/multitheftauto/mtasa-blue/issues/684), [#1022](https://github.com/multitheftauto/mtasa-blue/pull/1022) by **StrixG**)

- Change client coreconfig.xml *fps_limit* range to 45-100 (See commit [709bc40](https://github.com/multitheftauto/mtasa-blue/commit/709bc40b34ab11e533fe43d364f0a20d4b5245ca) by **ccw**)

- Fix text extent calculation for drawing colorcoded text (See commit [c9e2e2a](https://github.com/multitheftauto/mtasa-blue/commit/c9e2e2a95a3d076e69b4e6252d8ba81752fd2fae) by **botder**)

- Fix memory leak in CBassAudio::GetSoundBPM (See commit [01267f3](https://github.com/multitheftauto/mtasa-blue/commit/01267f34afa99c2b23d98591803b850e1ddc8c9c) by **botder**)

- Fix crash for incorrect usage of *ColumnHeader* CEGUI property (See commit [bc649fb](https://github.com/multitheftauto/mtasa-blue/commit/bc649fb5c89cb2358c8cafad699005923cd5377f) by **botder**)

- Fix [guiCreateStaticImage](mta://scripting/client/functions/guicreatestaticimage.md) to warn on failure ([#1041](https://github.com/multitheftauto/mtasa-blue/pull/1041) by **CrosRoad95**)

- Improve Arabic language pictures ([#1050](https://github.com/multitheftauto/mtasa-blue/pull/1050) by **Haxardous**)

- Fix [setSoundPosition](mta://scripting/client/functions/setsoundposition.md) returning true for streams ([#651](https://github.com/multitheftauto/mtasa-blue/pull/651) by **xLuxy**)

- Fix missing typename for browsers (Fixes [#662](https://github.com/multitheftauto/mtasa-blue/issues/662), see commit [fe560c2](https://github.com/multitheftauto/mtasa-blue/commit/fe560c2d5f725293a22c304ef4f2f89a2b148b59) by **qaisjp**)

- Fix CEF crash on resource restart (See commit [3372f0f](https://github.com/multitheftauto/mtasa-blue/commit/3372f0f52ff782e1b691dc55c4a9da6ac4e1f40a) by **botder**)

- Fix [dxCreateShader](mta://scripting/client/functions/dxcreateshader.md) error logging (See commit [42dd5b3](https://github.com/multitheftauto/mtasa-blue/commit/42dd5b3ba579d28448745ed820fbf460e2a35ee4) by **ccw**)

- Fix [clearChatBox](mta://scripting/shared/functions/clearchatbox.md) not working properly with Low FX quality (Fixes [#733](https://github.com/multitheftauto/mtasa-blue/issues/733), see commit [096ca10](https://github.com/multitheftauto/mtasa-blue/commit/096ca10ba6c6765a09021bbf642032990dad9375) by **ccw**)

- Fix font reset when using [guiGridListSetItemText](mta://scripting/client/functions/guigridlistsetitemtext.md) (Fixes [#622](https://github.com/multitheftauto/mtasa-blue/issues/622), see commit [0a8978a](https://github.com/multitheftauto/mtasa-blue/commit/0a8978a9b9b44743b2c4c50227b14ad627897dad) by **qaisjp**)

- Fix choppy camera movement (Fixes [#763](https://github.com/multitheftauto/mtasa-blue/issues/763), see commit [ca306e4](https://github.com/multitheftauto/mtasa-blue/commit/ca306e469e413c10779e7a6f158667c7ca989fc7) by **botder**)

- Fix crash when changing max handling gear to below current gear (Fixes [#731](https://github.com/multitheftauto/mtasa-blue/issues/731), [#778](https://github.com/multitheftauto/mtasa-blue/pull/778) by **forkerer**)

- Fix [setSoundPanningEnabled](mta://scripting/client/functions/setsoundpanningenabled.md) not working straight after playing a 3D sound (Fixes [#757](https://github.com/multitheftauto/mtasa-blue/issues/757), [#842](https://github.com/multitheftauto/mtasa-blue/pull/842) by **StrixG**)

- Fix bone positions being one frame behind (Fixes [#465](https://github.com/multitheftauto/mtasa-blue/issues/465), see commit [e0fa528](https://github.com/multitheftauto/mtasa-blue/commit/e0fa528fcd6fb6b3717320fc197b83a18edb074c) by **saml1er**)

- Fix server info window not hiding when you return to game (Fixes [#712](https://github.com/multitheftauto/mtasa-blue/issues/712), [#867](https://github.com/multitheftauto/mtasa-blue/pull/867) by **ricksterhd123**)

- Fix "can only run forward" bug (Fixes [#366](https://github.com/multitheftauto/mtasa-blue/issues/366), see commit [a3864d8..426ad3f](https://github.com/multitheftauto/mtasa-blue/compare/a3864d8f9c6c59899bd3858379646cef5140f67e~1...426ad3fcf71b4d41af877a860b371ad2f98f6d17) by **saml1er**)

- Add missing *high_detail_peds* setting that was supposed to be added in [#231](https://github.com/multitheftauto/mtasa-blue/pull/231) (See [#832](https://github.com/multitheftauto/mtasa-blue/pull/832) by **patrikjuvonen**)

- Fix missing typenames for texture subclasses (Fixes [#974](https://github.com/multitheftauto/mtasa-blue/issues/974), see commit [526171c](https://github.com/multitheftauto/mtasa-blue/commit/526171c641c3f62815df988bb4b4db9c343380aa) by **qaisjp**)

- Fix crash when you join a server (Fixes [#983](https://github.com/multitheftauto/mtasa-blue/issues/983), see commit [2996321](https://github.com/multitheftauto/mtasa-blue/commit/299632170d2388f387cf03c01f8626f31dc072b3) by **qaisjp**, **sbx320** and **ccw**)

- Disable forboden programs checks in debug mode (See [#999](https://github.com/multitheftauto/mtasa-blue/pull/999) by **CrosRoad95**)

- Fix possible CEF crash fix by making UTF16ToMbUTF8 handle nullptr (See commit [7808dfb..b71c86d](https://github.com/multitheftauto/mtasa-blue/compare/7808dfb82d29ceb42cf10069b99cbe42dc777b45~1...b71c86dd2a53ac98a53924e386f8c777671d1eaa) by **ccw**)

- Add DPI awareness experimental option to settings (See commit [65020e4](https://github.com/multitheftauto/mtasa-blue/commit/65020e4d6ad9fe51537778b5de1d0fa3ff5aad66) by **botder**)

- Fix crash when attempting to stream audio while disconnecting (Fixes [#1065](https://github.com/multitheftauto/mtasa-blue/issues/1065), see commit [a389d52](https://github.com/multitheftauto/mtasa-blue/commit/a389d5290991f2e39317b59c0e7dbc131c10228c) by **sbx320**)

- Add new Visit News button to main menu (See commit [c008eef](https://github.com/multitheftauto/mtasa-blue/commit/c008eef35f5d1b8223ee4cd0bb3fef0971b9b8f3) by **qaisjp**)

- Tweak main menu news position and text (See commit [742819a](https://github.com/multitheftauto/mtasa-blue/commit/742819a0e6792ce36cb36b2baa7fd942b21bdaa3) by **qaisjp**)

- Fix memory leak in CLuaManager on disconnect ([#1066](https://github.com/multitheftauto/mtasa-blue/pull/1066) by **pentaflops**)

### 5 Vendor Updates

- Update BASS libraries ([7afdde4](https://github.com/multitheftauto/mtasa-blue/commit/7afdde478cf3accee6b9eebe07ed362ca1ab2201) by **Dutchman101** and **botder**)

- Update libpng from 1.6.35 to 1.6.37 ([#899](https://github.com/multitheftauto/mtasa-blue/pull/899) by **patrikjuvonen**)

- Update zlib from 1.2.8 to 1.2.11 ([#919](https://github.com/multitheftauto/mtasa-blue/pull/919) by **patrikjuvonen**)

- Update UnRAR from 5.21 to 5.71 ([#920](https://github.com/multitheftauto/mtasa-blue/pull/920) by **patrikjuvonen**)

- Update [CEF](mta://tutorials/cef-tutorial.md) from 3.3538.1852.gcb937fc (Chromium 70.0.3538.102) to 76.1.13+gf19c584 ([Chromium 76.0.3809.132](https://chromereleases.googleblog.com/2019/08/stable-channel-update-for-desktop_26.html)) (See commit [a82990a](https://github.com/multitheftauto/mtasa-blue/commit/a82990afdd38b0d59a80d44b5a19be55ec7f8fe4) by **Jusonex**)

## Server

Click to collapse [-]

### Additions

- Added error message for resource [meta.xml](mta://reference/misc/meta-xml.md) parsing fail ([#655](https://github.com/multitheftauto/mtasa-blue/pull/655) by **Addlibs**)

### 21 Bug Fixes & Changes

- Prevent multiple kick/ban of a player ([#173](https://github.com/multitheftauto/mtasa-blue/pull/173) by **CrosRoad95**)

- Fix ¿question marks? being replaced in [dbPrepareString](mta://scripting/server/functions/dbpreparestring.md) values (Fixes [#634](https://github.com/multitheftauto/mtasa-blue/issues/634), see commit [c17a52a](https://github.com/multitheftauto/mtasa-blue/commit/c17a52a1d936652516782a8995a05de2a5e75918) by **ccw**)

- Fix radar areas not being deleted after map stop (Fixes [#737](https://github.com/multitheftauto/mtasa-blue/issues/737), see commit [ca747a8](https://github.com/multitheftauto/mtasa-blue/commit/ca747a8b5fe1d841fd037efc9a7422b8c4cfbde6) by **botder**)

- Stop deleted resources before removing them from lists (Fixes [#372](https://github.com/multitheftauto/mtasa-blue/issues/372), see commit [2f8377b](https://github.com/multitheftauto/mtasa-blue/commit/2f8377b0336aba18ff8c670a2cfe61df75c91d5d) by **botder**)

- Disallow file paths with a directory separator suffix (Fixes [#761](https://github.com/multitheftauto/mtasa-blue/issues/761), see commit [13771a4](https://github.com/multitheftauto/mtasa-blue/commit/13771a4f7fbe28f497a1786711e2460c31fb0f9d) by **botder**)

- Disallow empty src attributes in [meta.xml](mta://reference/misc/meta-xml.md) (Fixes [#738](https://github.com/multitheftauto/mtasa-blue/issues/738), see commit [5c85de2](https://github.com/multitheftauto/mtasa-blue/commit/5c85de2c5a3c14e07ecd65e37718b504b3540d9d) by **botder**)

- Improve resource load performance ([#758](https://github.com/multitheftauto/mtasa-blue/pull/758) by **sbx320**)

- Postpone client sync after broadcasting resource to client (See commit [379a2ff](https://github.com/multitheftauto/mtasa-blue/commit/379a2ff6e943d6f39cbf84185af5511d365f7d02) by **botder**)

- Reload zipped resources on restart if changed (See commit [41243a0](https://github.com/multitheftauto/mtasa-blue/commit/41243a08c57dac3bcc6797d7f8b50091572abdda) by **sbx320**)

- Fix client/server ped dead-state inconsistency ([#140](https://github.com/multitheftauto/mtasa-blue/pull/140) by **Necktrox**)

- Add server kick messages for localization (See commit [37087bc](https://github.com/multitheftauto/mtasa-blue/commit/37087bc95e708372deacf35ddbc8269725ae86fe) by **ccw**)

- Set missing spawned and dead state for cloned peds ([#933](https://github.com/multitheftauto/mtasa-blue/pull/933) by **TheNormalnij**)

- Fix [setAccountName](mta://scripting/server/functions/setaccountname.md) not saving name in database ([#939](https://github.com/multitheftauto/mtasa-blue/pull/939) by **StrixG**)

- Add timecyc.dat to the server-side data files check (See commit [8b6bfe2](https://github.com/multitheftauto/mtasa-blue/commit/8b6bfe2b6009e42f5783a023d466cc215885b5cd) by **ccw**)

- Add mapmanger required rights to acl.xml (See commit [764664d](https://github.com/multitheftauto/mtasa-blue/commit/764664d4f47b4805438b22f2b2a8f924e3468aab) by **ccw**)

- Fix *upgrade* command not updating <min_mta_version> (See commit [a487b09](https://github.com/multitheftauto/mtasa-blue/commit/a487b099480925cf19c637f8f09668b87a990cc0) by **ccw**)

- Fix OOP: i.e. ped:setControlState() returns deprecated function (See commit [3418ceb](https://github.com/multitheftauto/mtasa-blue/commit/3418ceb665378750f6b91e61b57a1915e116905d) by **ccw**)

- Fix element dimensions when loading maps (Fixes [#640](https://github.com/multitheftauto/mtasa-blue/issues/640), see commit [2e332ab](https://github.com/multitheftauto/mtasa-blue/commit/2e332ab4a8afa6890d892195bcabfb0862d9fba5) by **botder**)

- Fix [dbQuery](mta://scripting/server/functions/dbquery.md) uncollected result warning when restarting resources (Fixes [#789](https://github.com/multitheftauto/mtasa-blue/issues/789), see commit [af24918](https://github.com/multitheftauto/mtasa-blue/commit/af24918613ff52490a0fe1c63bbb053688726718) by **botder**)

- Fix [setAccountName](mta://scripting/server/functions/setaccountname.md) not working properly (Fixes [#479](https://github.com/multitheftauto/mtasa-blue/issues/479), [#939](https://github.com/multitheftauto/mtasa-blue/pull/939) by **StrixG**)

- Pin down [startResource](mta://scripting/server/functions/startresource.md) and [stopResource](mta://scripting/server/functions/stopresource.md) behaviour (Fixes [#798](https://github.com/multitheftauto/mtasa-blue/issues/798), [#957](https://github.com/multitheftauto/mtasa-blue/pull/957) by **StrixG**)

### 1 Vendor Update

- Update SQLite from 3.24.0 to 3.29.0 ([#1028](https://github.com/multitheftauto/mtasa-blue/pull/1028) by **patrikjuvonen** and **botder**)

## Shared

Click to collapse [-]

### 13 Bug Fixes & Changes

- Refactor and fix a lot of issues with [cloneElement](mta://scripting/server/functions/cloneelement.md) ([#182](https://github.com/multitheftauto/mtasa-blue/pull/182) by **emre1702** and **qaisjp**)

- Allow debug messages in [onDebugMessage](mta://scripting/server/events/ondebugmessage.md) and [onClientDebugMessage](mta://scripting/client/events/onclientdebugmessage.md) (Fixes [#639](https://github.com/multitheftauto/mtasa-blue/issues/639), see commit [81b64e3](https://github.com/multitheftauto/mtasa-blue/commit/81b64e3e0d0ceb9435f5848d10d0b6a7451f00b4) by **botder**)

- Fix Hotring Racers share handlings when set by model ID ([#401](https://github.com/multitheftauto/mtasa-blue/pull/401) by **samr46**)

- Fix dead players appearing to be alive after reconnect ([#746](https://github.com/multitheftauto/mtasa-blue/issues/746), see commit [9e6aace](https://github.com/multitheftauto/mtasa-blue/commit/9e6aace5178c678a20df24369034bfb3525e662e) by **botder**)

- Fix incorrect segment/triangle intersection code ([#816](https://github.com/multitheftauto/mtasa-blue/pull/816) by **forkerer**)

- Add error code to [fileRename](mta://scripting/shared/functions/filerename.md) failed message (See commit [3a7c803](https://github.com/multitheftauto/mtasa-blue/commit/3a7c803936d54636c58aec677d99cbbac68a4ff3) by **ccw**)

- Add alternate file rename strategy for when MoveFile fails with access denied (See commit [e9ce827](https://github.com/multitheftauto/mtasa-blue/commit/e9ce827def7b4dc5dcd97f3ac4e8fd22c3b234ea) by **ccw**)

- Add file and function names in "infinite running script" (See commit [80fe718](https://github.com/multitheftauto/mtasa-blue/commit/80fe71869d6a94682a972894d90727786970734c) by **Jusonex**)

- Fix undefined behavior for ReadColor (See commit [53121a3](https://github.com/multitheftauto/mtasa-blue/commit/53121a3b3084b7e503d57be122f8649dd0bb09a8) by **botder**)

- We no longer use Travis CI or AppVeyor (See commit [a99faa0](https://github.com/multitheftauto/mtasa-blue/commit/a99faa00ba5958c60785f39b63971b8522e2f374) by **Jusonex**)

- Upgrade to C++17 for some projects ([#876](https://github.com/multitheftauto/mtasa-blue/pull/876) by **sbx320** and **Jusonex**)

- Fix build scripts being affected by spaces in build path (Fixes [#648](https://github.com/multitheftauto/mtasa-blue/issues/648), see commit [59b1d30](https://github.com/multitheftauto/mtasa-blue/commit/59b1d30a26f54561a291a96236d1a42cf0f76ce2) by **ccw**)

- Fix binary string reading (See commit [a84ae4c..3b624da](https://github.com/multitheftauto/mtasa-blue/compare/a84ae4cdf3d5c8b9a3fd4469f9c9f083946cde53~1...3b624da9072a61c26f9481da49687b26dbde0325) by **botder**)

### 2 Vendor Updates

- Update curl from 7.61.0 to [7.65.3](https://daniel.haxx.se/blog/2019/07/17/curl-7-65-2-fixes-even-more/) ([#1027](https://github.com/multitheftauto/mtasa-blue/pull/1027) by **patrikjuvonen**)

- Update cryptopp from 5.6.5 to 8.1.0 (See commit [dad907c](https://github.com/multitheftauto/mtasa-blue/commit/dad907c2748a2ac3babc94ee2335ea933ed24aec) by **sbx320**)

## Resources

Click to collapse [-]

- [freeroam] Fixed GUI after destroy vehicle ([#125](https://github.com/multitheftauto/mtasa-resources/pull/125) by **FileEX**)

- [admin2] Add more glitches and world properties into server tab ([#136](https://github.com/multitheftauto/mtasa-resources/pull/136) by **FileEX**)

- [admin2] Add inputs validation, add missing default variables for inputs and missing world properties for refresh button. Add glitch for refresh button and enabled all disabled elements like glitches, world properties, heathaze button etc. Fix triggered binds by input boxes. ([#148](https://github.com/multitheftauto/mtasa-resources/pull/148) by **FileEX**)

- [admin2] Changed to combobox instead of editbox to setting weather and fixed blending weather. ([#154](https://github.com/multitheftauto/mtasa-resources/pull/154) by **FileEX**)

## Extra information

*More detailed information available on our GitHub repositories:*

- [MTA:SA Blue](https://github.com/multitheftauto/mtasa-blue)

- [MTA:SA Official Resources](https://github.com/multitheftauto/mtasa-resources)
