---
doc_id: "mta-wiki:5253"
title: "Server Scripting Functions"
source_title: "Server Scripting Functions2"
source_url: "https://wiki.multitheftauto.com/wiki/Server_Scripting_Functions2"
revision_id: 80370
language: "en"
categories: []
generated_at: "2026-07-26T16:16:37.486151+00:00"
---

# Server Scripting Functions

*Contributors:* Did you create a page but it's not on this list? Confused? **Read: [Adding Pages to Categories and Templates](mta://tutorials/adding-pages-to-categories-and-templates.md)**

This page lists all the **server-side** scripting functions that have been implemented and are available as native functions. To request a function, create an issue in [our GitHub repository.](https://github.com/multitheftauto/mtasa-blue/issues)

Please note that the scripting functions can also be extended by loading in dynamic modules that provide new functionality, such as utility functions. These scripting functions are non-native and require the module to be loaded in order to work.

Head over to [Modules](mta://reference/misc/modules.md) for a list of non-native serverside functions and modules that are available.

For more functions, check the [useful functions page](mta://reference/misc/useful-functions.md).

**Client-side scripting functions can be found here: [Client Scripting Functions](mta://scripting/concepts/client-scripting-functions.md).**

## Account functions

- [addAccount](mta://scripting/server/functions/addaccount.md)

- [copyAccountData](mta://scripting/server/functions/copyaccountdata.md)

- [getAccount](mta://scripting/server/functions/getaccount.md)

- [getAccountData](mta://scripting/server/functions/getaccountdata.md)

- [getAccountName](mta://scripting/server/functions/getaccountname.md)

- [getAccountPlayer](mta://scripting/server/functions/getaccountplayer.md)

- [getAccountSerial](mta://scripting/server/functions/getaccountserial.md)

- [getAccounts](mta://scripting/server/functions/getaccounts.md)

- [getAccountsBySerial](mta://scripting/server/functions/getaccountsbyserial.md)

- [getAllAccountData](mta://scripting/server/functions/getallaccountdata.md)

- [getPlayerAccount](mta://scripting/server/functions/getplayeraccount.md)

- [isGuestAccount](mta://scripting/server/functions/isguestaccount.md)

- [logIn](mta://scripting/server/functions/login.md)

- [logOut](mta://scripting/server/functions/logout.md)

- [removeAccount](mta://scripting/server/functions/removeaccount.md)

- [setAccountData](mta://scripting/server/functions/setaccountdata.md)

- [setAccountPassword](mta://scripting/server/functions/setaccountpassword.md)

- [getAccountByID](mta://scripting/server/functions/getaccountbyid.md)

- [getAccountID](mta://scripting/server/functions/getaccountid.md)

- [getAccountIP](mta://scripting/server/functions/getaccountip.md)

- [getAccountsByData](mta://scripting/server/functions/getaccountsbydata.md)

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)

## ACL functions

- [aclCreate](mta://scripting/server/functions/aclcreate.md)

- [aclCreateGroup](mta://scripting/server/functions/aclcreategroup.md)

- [aclDestroy](mta://scripting/server/functions/acldestroy.md)

- [aclDestroyGroup](mta://scripting/server/functions/acldestroygroup.md)

- [aclGet](mta://scripting/server/functions/aclget.md)

- [aclGetGroup](mta://scripting/server/functions/aclgetgroup.md)

- [aclGetName](mta://scripting/server/functions/aclgetname.md)

- [aclGetRight](mta://scripting/server/functions/aclgetright.md)

- [aclGroupAddACL](mta://scripting/server/functions/aclgroupaddacl.md)

- [aclGroupAddObject](mta://scripting/server/functions/aclgroupaddobject.md)

- [aclGroupGetName](mta://scripting/server/functions/aclgroupgetname.md)

- [aclGroupList](mta://scripting/server/functions/aclgrouplist.md)

- [aclGroupListACL](mta://scripting/server/functions/aclgrouplistacl.md)

- [aclGroupListObjects](mta://scripting/server/functions/aclgrouplistobjects.md)

- [aclGroupRemoveACL](mta://scripting/server/functions/aclgroupremoveacl.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22273](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22273):

- [aclObjectGetGroups](mta://scripting/server/functions/aclobjectgetgroups.md)

- [aclGroupRemoveObject](mta://scripting/server/functions/aclgroupremoveobject.md)

- [aclList](mta://scripting/server/functions/acllist.md)

- [aclListRights](mta://scripting/server/functions/acllistrights.md)

- [aclReload](mta://scripting/server/functions/aclreload.md)

- [aclRemoveRight](mta://scripting/server/functions/aclremoveright.md)

- [aclSave](mta://scripting/server/functions/aclsave.md)

- [aclSetRight](mta://scripting/server/functions/aclsetright.md)

- [hasObjectPermissionTo](mta://scripting/server/functions/hasobjectpermissionto.md)

- [isObjectInACLGroup](mta://scripting/server/functions/isobjectinaclgroup.md)

## Admin functions

- [addBan](mta://scripting/server/functions/addban.md)

- [banPlayer](mta://scripting/server/functions/banplayer.md)

- [getBanAdmin](mta://scripting/server/functions/getbanadmin.md)

- [getBanIP](mta://scripting/server/functions/getbanip.md)

- [getBanNick](mta://scripting/server/functions/getbannick.md)

- [getBanReason](mta://scripting/server/functions/getbanreason.md)

- [getBanSerial](mta://scripting/server/functions/getbanserial.md)

- [getBanTime](mta://scripting/server/functions/getbantime.md)

- [getBans](mta://scripting/server/functions/getbans.md)

- [getUnbanTime](mta://scripting/server/functions/getunbantime.md)

- [isBan](mta://scripting/server/functions/isban.md)

- [kickPlayer](mta://scripting/server/functions/kickplayer.md)

- [setBanAdmin](mta://scripting/server/functions/setbanadmin.md)

- [setBanNick](mta://scripting/server/functions/setbannick.md)

- [setBanReason](mta://scripting/server/functions/setbanreason.md)

- [setUnbanTime](mta://scripting/server/functions/setunbantime.md)

- [reloadBans](mta://scripting/server/functions/reloadbans.md)

- [removeBan](mta://scripting/server/functions/removeban.md)

## Audio functions

**Shared**

- [playSoundFrontEnd](mta://scripting/shared/functions/playsoundfrontend.md)

## Announcement functions

- [getGameType](mta://scripting/server/functions/getgametype.md)

- [getMapName](mta://scripting/server/functions/getmapname.md)

- [getRuleValue](mta://scripting/server/functions/getrulevalue.md)

- [removeRuleValue](mta://scripting/server/functions/removerulevalue.md)

- [setGameType](mta://scripting/server/functions/setgametype.md)

- [setMapName](mta://scripting/server/functions/setmapname.md)

- [setRuleValue](mta://scripting/server/functions/setrulevalue.md)

## Blip functions

**Shared**

- [createBlip](mta://scripting/shared/functions/createblip.md)

- [createBlipAttachedTo](mta://scripting/shared/functions/createblipattachedto.md)

- [getBlipColor](mta://scripting/shared/functions/getblipcolor.md)

- [getBlipIcon](mta://scripting/shared/functions/getblipicon.md)

- [getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)

## Camera functions

**Shared**

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)

## Clothes and body functions

**Shared**

- [getBodyPartName](mta://scripting/shared/functions/getbodypartname.md)

- [getClothesByTypeIndex](mta://scripting/shared/functions/getclothesbytypeindex.md)

- [getClothesTypeName](mta://scripting/shared/functions/getclothestypename.md)

- [getTypeIndexFromClothes](mta://scripting/shared/functions/gettypeindexfromclothes.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r23124](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23124))

- [addClothingModel](mta://scripting/client/functions/addclothingmodel.md)

## Collision shape functions

**Shared**

- [addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)

- [createColCircle](mta://scripting/shared/functions/createcolcircle.md)

- [createColCuboid](mta://scripting/shared/functions/createcolcuboid.md)

- [createColPolygon](mta://scripting/shared/functions/createcolpolygon.md)

- [createColRectangle](mta://scripting/shared/functions/createcolrectangle.md)

- [createColSphere](mta://scripting/shared/functions/createcolsphere.md)

- [createColTube](mta://scripting/shared/functions/createcoltube.md)

- [getColPolygonHeight](mta://scripting/shared/functions/getcolpolygonheight.md)

- [getColPolygonPoints](mta://scripting/shared/functions/getcolpolygonpoints.md)

- [getColPolygonPointPosition](mta://scripting/shared/functions/getcolpolygonpointposition.md)

- [getColShapeType](mta://scripting/shared/functions/getcolshapetype.md)

- [getColShapeRadius](mta://scripting/shared/functions/getcolshaperadius.md)

- [getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)

- [isInsideColShape](mta://scripting/shared/functions/isinsidecolshape.md)

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)

## Cursor functions

**Shared**

- [isCursorShowing](mta://scripting/shared/functions/iscursorshowing.md)

- [showCursor](mta://scripting/shared/functions/showcursor.md)

## Element functions

- [addElementDataSubscriber](mta://scripting/server/functions/addelementdatasubscriber.md)

- [clearElementVisibleTo](mta://scripting/server/functions/clearelementvisibleto.md)

- [cloneElement](mta://scripting/server/functions/cloneelement.md)

- [getElementSyncer](mta://scripting/server/functions/getelementsyncer.md)

- [getElementZoneName](mta://scripting/server/functions/getelementzonename.md)

- [hasElementDataSubscriber](mta://scripting/server/functions/haselementdatasubscriber.md)

- [isElementVisibleTo](mta://scripting/server/functions/iselementvisibleto.md)

- [removeElementData](mta://scripting/server/functions/removeelementdata.md)

- [removeElementDataSubscriber](mta://scripting/server/functions/removeelementdatasubscriber.md)

- [setElementSyncer](mta://scripting/server/functions/setelementsyncer.md)

- [setElementVisibleTo](mta://scripting/server/functions/setelementvisibleto.md)
  

- **Shared**

- [attachElements](mta://scripting/shared/functions/attachelements.md)

- [createElement](mta://scripting/shared/functions/createelement.md)

- [destroyElement](mta://scripting/shared/functions/destroyelement.md)

- [detachElements](mta://scripting/shared/functions/detachelements.md)

- [getAttachedElements](mta://scripting/shared/functions/getattachedelements.md)

- [getElementAlpha](mta://scripting/shared/functions/getelementalpha.md)

- [getElementAttachedOffsets](mta://scripting/shared/functions/getelementattachedoffsets.md)

- [getElementAttachedTo](mta://scripting/shared/functions/getelementattachedto.md)

- [getElementByIndex](mta://scripting/shared/functions/getelementbyindex.md)

- [getElementByID](mta://scripting/shared/functions/getelementbyid.md)

- [getElementChild](mta://scripting/shared/functions/getelementchild.md)

- [getElementChildren](mta://scripting/shared/functions/getelementchildren.md)

- [getElementChildrenCount](mta://scripting/shared/functions/getelementchildrencount.md)

- [getElementCollisionsEnabled](mta://scripting/shared/functions/getelementcollisionsenabled.md)

- [getElementColShape](mta://scripting/shared/functions/getelementcolshape.md)

- [getElementData](mta://scripting/shared/functions/getelementdata.md)

- [getAllElementData](mta://scripting/shared/functions/getallelementdata.md)

- [hasElementData](mta://scripting/shared/functions/haselementdata.md)

- [getElementDimension](mta://scripting/shared/functions/getelementdimension.md)

- [getElementHealth](mta://scripting/shared/functions/getelementhealth.md)

- [getElementID](mta://scripting/shared/functions/getelementid.md)

- [getElementInterior](mta://scripting/shared/functions/getelementinterior.md)

- [getElementMatrix](mta://scripting/shared/functions/getelementmatrix.md)

- [getElementModel](mta://scripting/shared/functions/getelementmodel.md)

- [getElementParent](mta://scripting/shared/functions/getelementparent.md)

- [getElementPosition](mta://scripting/shared/functions/getelementposition.md)

- [getElementRotation](mta://scripting/shared/functions/getelementrotation.md)

- [getElementsByType](mta://scripting/shared/functions/getelementsbytype.md)

- [getElementsWithinColShape](mta://scripting/shared/functions/getelementswithincolshape.md)

- [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md)

- [getElementType](mta://scripting/shared/functions/getelementtype.md)

- [getElementVelocity](mta://scripting/shared/functions/getelementvelocity.md)

- [getLowLODElement](mta://scripting/shared/functions/getlowlodelement.md)

- [getRootElement](mta://scripting/shared/functions/getrootelement.md)

- [isElement](mta://scripting/shared/functions/iselement.md)

- [isElementAttached](mta://scripting/shared/functions/iselementattached.md)

- [isElementCallPropagationEnabled](mta://scripting/shared/functions/iselementcallpropagationenabled.md)

- [isElementDoubleSided](mta://scripting/shared/functions/iselementdoublesided.md)

- [isElementFrozen](mta://scripting/shared/functions/iselementfrozen.md)

- [isElementInWater](mta://scripting/shared/functions/iselementinwater.md)

- [isElementLowLOD](mta://scripting/shared/functions/iselementlowlod.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22864](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22864):

- [isElementOnFire](mta://scripting/shared/functions/iselementonfire.md)

- [isElementWithinColShape](mta://scripting/shared/functions/iselementwithincolshape.md)

- [isElementWithinMarker](mta://scripting/shared/functions/iselementwithinmarker.md)

- [setElementAlpha](mta://scripting/shared/functions/setelementalpha.md)

- [setElementAngularVelocity](mta://scripting/shared/functions/setelementangularvelocity.md)

- [getElementAngularVelocity](mta://scripting/shared/functions/getelementangularvelocity.md)

- [setElementAttachedOffsets](mta://scripting/shared/functions/setelementattachedoffsets.md)

- [setElementCallPropagationEnabled](mta://scripting/shared/functions/setelementcallpropagationenabled.md)

- [setElementCollisionsEnabled](mta://scripting/shared/functions/setelementcollisionsenabled.md)

- [setElementData](mta://scripting/shared/functions/setelementdata.md)

- [setElementDimension](mta://scripting/shared/functions/setelementdimension.md)

- [setElementDoubleSided](mta://scripting/shared/functions/setelementdoublesided.md)

- [setElementFrozen](mta://scripting/shared/functions/setelementfrozen.md)

- [setElementHealth](mta://scripting/shared/functions/setelementhealth.md)

- [setElementID](mta://scripting/shared/functions/setelementid.md)

- [setElementInterior](mta://scripting/shared/functions/setelementinterior.md)

- [setElementModel](mta://scripting/shared/functions/setelementmodel.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22864](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22864):

- [setElementOnFire](mta://scripting/shared/functions/setelementonfire.md)

- [setElementParent](mta://scripting/shared/functions/setelementparent.md)

- [setElementPosition](mta://scripting/shared/functions/setelementposition.md)

- [setElementRotation](mta://scripting/shared/functions/setelementrotation.md)

- [setElementVelocity](mta://scripting/shared/functions/setelementvelocity.md)

- [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)

## Event functions

- [getCancelReason](mta://scripting/server/functions/getcancelreason.md)

- [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md)

- [triggerLatentClientEvent](mta://scripting/server/functions/triggerlatentclientevent.md)
  

- **Shared**

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)

## Explosion functions

**Shared**

- [createExplosion](mta://scripting/shared/functions/createexplosion.md)

## File functions

**Shared**

- [fileClose](mta://scripting/shared/functions/fileclose.md)

- [fileCopy](mta://scripting/shared/functions/filecopy.md)

- [fileCreate](mta://scripting/shared/functions/filecreate.md)

- [fileDelete](mta://scripting/shared/functions/filedelete.md)

- [fileExists](mta://scripting/shared/functions/fileexists.md)

- [fileFlush](mta://scripting/shared/functions/fileflush.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21938](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21938):

- [fileGetContents](mta://scripting/shared/functions/filegetcontents.md)

ADDED/UPDATED IN VERSION 1.6.0 [r23289](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23289):

- [fileGetHash](mta://scripting/shared/functions/filegethash.md)

- [fileGetPath](mta://scripting/shared/functions/filegetpath.md)

- [fileGetPos](mta://scripting/shared/functions/filegetpos.md)

- [fileGetSize](mta://scripting/shared/functions/filegetsize.md)

- [fileIsEOF](mta://scripting/shared/functions/fileiseof.md)

- [fileOpen](mta://scripting/shared/functions/fileopen.md)

- [fileRead](mta://scripting/shared/functions/fileread.md)

- [fileRename](mta://scripting/shared/functions/filerename.md)

- [fileSetPos](mta://scripting/shared/functions/filesetpos.md)

- [fileWrite](mta://scripting/shared/functions/filewrite.md)

## HTTP functions

*These functions can only be used from within lua blocks in HTML pages hosted by the server*

- [httpClear](mta://reference/misc/httpclear.md)

- [httpRequestLogin](mta://reference/misc/httprequestlogin.md)

- [httpSetResponseCode](mta://reference/misc/httpsetresponsecode.md)

- [httpSetResponseCookie](mta://reference/misc/httpsetresponsecookie.md)

- [httpSetResponseHeader](mta://reference/misc/httpsetresponseheader.md)

- [httpWrite](mta://reference/misc/httpwrite.md)

## Input functions

- [isKeyBound](mta://scripting/server/functions/iskeybound.md)
  

- **Shared**

- [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md)

- [bindKey](mta://scripting/shared/functions/bindkey.md)

- [executeCommandHandler](mta://scripting/shared/functions/executecommandhandler.md)

- [getCommandHandlers](mta://scripting/shared/functions/getcommandhandlers.md)

- [getFunctionsBoundToKey](mta://scripting/shared/functions/getfunctionsboundtokey.md)

- [getKeyBoundToFunction](mta://scripting/shared/functions/getkeyboundtofunction.md)

- [isControlEnabled](mta://scripting/shared/functions/iscontrolenabled.md)

- [removeCommandHandler](mta://scripting/shared/functions/removecommandhandler.md)

- [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md)

- [toggleControl](mta://scripting/shared/functions/togglecontrol.md)

- [unbindKey](mta://scripting/shared/functions/unbindkey.md)

## Map functions

- [loadMapData](mta://scripting/server/functions/loadmapdata.md)

- [resetMapInfo](mta://scripting/server/functions/resetmapinfo.md)

- [saveMapData](mta://scripting/server/functions/savemapdata.md)

## Marker functions

**Shared**

- [createMarker](mta://scripting/shared/functions/createmarker.md)

- [getMarkerColor](mta://scripting/shared/functions/getmarkercolor.md)

- [getMarkerCount](mta://scripting/shared/functions/getmarkercount.md)

- [getMarkerIcon](mta://scripting/shared/functions/getmarkericon.md)

- [getMarkerSize](mta://scripting/shared/functions/getmarkersize.md)

- [getMarkerTarget](mta://scripting/shared/functions/getmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [getMarkerTargetArrowProperties](mta://scripting/shared/functions/getmarkertargetarrowproperties.md)

- [getMarkerType](mta://scripting/shared/functions/getmarkertype.md)

- [setMarkerColor](mta://scripting/shared/functions/setmarkercolor.md)

- [setMarkerIcon](mta://scripting/shared/functions/setmarkericon.md)

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)

## Matrix functions

**Shared**

- [Matrix](mta://reference/misc/matrix.md)

- [Vector/Vector2](mta://reference/misc/vector-vector2.md)

- [Vector/Vector3](mta://reference/misc/vector-vector3.md)

- [Vector/Vector4](mta://reference/misc/vector-vector4.md)

## Module functions

- [getLoadedModules](mta://scripting/server/functions/getloadedmodules.md)

- [getModuleInfo](mta://scripting/server/functions/getmoduleinfo.md)

## Object functions

**Shared**

- [createObject](mta://scripting/shared/functions/createobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22489](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22489):

- [breakObject](mta://scripting/shared/functions/breakobject.md)

- [getObjectScale](mta://scripting/shared/functions/getobjectscale.md)

- [moveObject](mta://scripting/shared/functions/moveobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22708](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22708):

- [respawnObject](mta://scripting/shared/functions/respawnobject.md)

- [toggleObjectRespawn](mta://scripting/shared/functions/toggleobjectrespawn.md)

- [isObjectRespawnable](mta://scripting/shared/functions/isobjectrespawnable.md)

- [setObjectScale](mta://scripting/shared/functions/setobjectscale.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

- [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

- [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)

## Output functions

- [outputServerLog](mta://scripting/server/functions/outputserverlog.md)
  

- **Shared**

- [clearChatBox](mta://scripting/shared/functions/clearchatbox.md)

- [outputChatBox](mta://scripting/shared/functions/outputchatbox.md)

- [outputConsole](mta://scripting/shared/functions/outputconsole.md)

- [outputDebugString](mta://scripting/shared/functions/outputdebugstring.md)

- [showChat](mta://scripting/shared/functions/showchat.md)

## Ped functions

- [getPedGravity](mta://scripting/server/functions/getpedgravity.md)

- [reloadPedWeapon](mta://scripting/server/functions/reloadpedweapon.md)

- [setPedChoking](mta://scripting/server/functions/setpedchoking.md)

- [setPedGravity](mta://scripting/server/functions/setpedgravity.md)

- [setPedWearingJetpack](mta://scripting/server/functions/setpedwearingjetpack.md)
  

- **Shared**

- [addPedClothes](mta://scripting/shared/functions/addpedclothes.md)

- [getPedClothes](mta://scripting/shared/functions/getpedclothes.md)

- [removePedClothes](mta://scripting/shared/functions/removepedclothes.md)

- [createPed](mta://scripting/shared/functions/createped.md)

- [getPedAmmoInClip](mta://scripting/shared/functions/getpedammoinclip.md)

- [getPedArmor](mta://scripting/shared/functions/getpedarmor.md)

- [getPedFightingStyle](mta://scripting/shared/functions/getpedfightingstyle.md)

- [getPedOccupiedVehicle](mta://scripting/shared/functions/getpedoccupiedvehicle.md)

- [getPedOccupiedVehicleSeat](mta://scripting/shared/functions/getpedoccupiedvehicleseat.md)

- [getPedStat](mta://scripting/shared/functions/getpedstat.md)

- [getPedTarget](mta://scripting/shared/functions/getpedtarget.md)

- [getPedTotalAmmo](mta://scripting/shared/functions/getpedtotalammo.md)

- [getPedWalkingStyle](mta://scripting/shared/functions/getpedwalkingstyle.md)

- [getPedWeapon](mta://scripting/shared/functions/getpedweapon.md)

- [getPedWeaponSlot](mta://scripting/shared/functions/getpedweaponslot.md)

- [getPedContactElement](mta://scripting/shared/functions/getpedcontactelement.md)

- [getValidPedModels](mta://scripting/shared/functions/getvalidpedmodels.md)

- [isPedChoking](mta://scripting/shared/functions/ispedchoking.md)

- [isPedDead](mta://scripting/shared/functions/ispeddead.md)

- [isPedDoingGangDriveby](mta://scripting/shared/functions/ispeddoinggangdriveby.md)

- [isPedDucked](mta://scripting/shared/functions/ispedducked.md)

- [isPedHeadless](mta://scripting/shared/functions/ispedheadless.md)

- [isPedInVehicle](mta://scripting/shared/functions/ispedinvehicle.md)

- [isPedOnGround](mta://scripting/shared/functions/ispedonground.md)

- [isPedReloadingWeapon](mta://scripting/shared/functions/ispedreloadingweapon.md)

- [isPedWearingJetpack](mta://scripting/shared/functions/ispedwearingjetpack.md)

- [killPed](mta://scripting/shared/functions/killped.md)

- [removePedFromVehicle](mta://scripting/shared/functions/removepedfromvehicle.md)

- [setPedAnimation](mta://scripting/shared/functions/setpedanimation.md)

- [setPedAnimationProgress](mta://scripting/shared/functions/setpedanimationprogress.md)

- [setPedAnimationSpeed](mta://scripting/shared/functions/setpedanimationspeed.md)

- [setPedArmor](mta://scripting/shared/functions/setpedarmor.md)

- [setPedDoingGangDriveby](mta://scripting/shared/functions/setpeddoinggangdriveby.md)

- [setPedFightingStyle](mta://scripting/shared/functions/setpedfightingstyle.md)

- [setPedHeadless](mta://scripting/shared/functions/setpedheadless.md)

- [setPedStat](mta://scripting/shared/functions/setpedstat.md)

- [setPedWalkingStyle](mta://scripting/shared/functions/setpedwalkingstyle.md)

- [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md)

- [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md)

## Pickup functions

- [getPickupRespawnInterval](mta://scripting/server/functions/getpickuprespawninterval.md)

- [isPickupSpawned](mta://scripting/server/functions/ispickupspawned.md)

- [setPickupRespawnInterval](mta://scripting/server/functions/setpickuprespawninterval.md)

- [usePickup](mta://scripting/server/functions/usepickup.md)
  

- **Shared**

- [createPickup](mta://scripting/shared/functions/createpickup.md)

- [getPickupAmmo](mta://scripting/shared/functions/getpickupammo.md)

- [getPickupAmount](mta://scripting/shared/functions/getpickupamount.md)

- [getPickupType](mta://scripting/shared/functions/getpickuptype.md)

- [setPickupType](mta://scripting/shared/functions/setpickuptype.md)

- [getPickupWeapon](mta://scripting/shared/functions/getpickupweapon.md)

## Player functions

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

- [takePlayerScreenShot](mta://scripting/server/functions/takeplayerscreenshot.md)
  

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

## Projectile functions

**Shared**

- [detonateSatchels](mta://scripting/shared/functions/detonatesatchels.md)

## Radar area functions

**Shared**

- [createRadarArea](mta://scripting/shared/functions/createradararea.md)

- [getRadarAreaColor](mta://scripting/shared/functions/getradarareacolor.md)

- [getRadarAreaSize](mta://scripting/shared/functions/getradarareasize.md)

- [isInsideRadarArea](mta://scripting/shared/functions/isinsideradararea.md)

- [isRadarAreaFlashing](mta://scripting/shared/functions/isradarareaflashing.md)

- [setRadarAreaColor](mta://scripting/shared/functions/setradarareacolor.md)

- [setRadarAreaFlashing](mta://scripting/shared/functions/setradarareaflashing.md)

- [setRadarAreaSize](mta://scripting/shared/functions/setradarareasize.md)

## Resource functions

- [addResourceConfig](mta://scripting/server/functions/addresourceconfig.md)

- [addResourceMap](mta://scripting/server/functions/addresourcemap.md)

- [callRemote](mta://scripting/server/functions/callremote.md)

- [copyResource](mta://scripting/server/functions/copyresource.md)

- [createResource](mta://scripting/server/functions/createresource.md)

- [deleteResource](mta://scripting/server/functions/deleteresource.md)

- [getResourceACLRequests](mta://scripting/server/functions/getresourceaclrequests.md)

- [getResourceInfo](mta://scripting/server/functions/getresourceinfo.md)

- [getResourceLastStartTime](mta://scripting/server/functions/getresourcelaststarttime.md)

- [getResourceLoadFailureReason](mta://scripting/server/functions/getresourceloadfailurereason.md)

- [getResourceLoadTime](mta://scripting/server/functions/getresourceloadtime.md)

- [getResourceMapRootElement](mta://scripting/server/functions/getresourcemaprootelement.md)

- [getResourceOrganizationalPath](mta://scripting/server/functions/getresourceorganizationalpath.md)

- [getResources](mta://scripting/server/functions/getresources.md)

- [isResourceArchived](mta://scripting/server/functions/isresourcearchived.md)

- [isResourceProtected](mta://scripting/server/functions/isresourceprotected.md)

- [refreshResources](mta://scripting/server/functions/refreshresources.md)

- [removeResourceFile](mta://scripting/server/functions/removeresourcefile.md)

- [renameResource](mta://scripting/server/functions/renameresource.md)

- [restartResource](mta://scripting/server/functions/restartresource.md)

- [setResourceInfo](mta://scripting/server/functions/setresourceinfo.md)

- [startResource](mta://scripting/server/functions/startresource.md)

- [stopResource](mta://scripting/server/functions/stopresource.md)

- [updateResourceACLRequest](mta://scripting/server/functions/updateresourceaclrequest.md)
  

- **Shared**

- [abortRemoteRequest](mta://scripting/shared/functions/abortremoterequest.md)

- [call](mta://scripting/shared/functions/call.md)

- [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

- [getResourceConfig](mta://scripting/shared/functions/getresourceconfig.md)

- [getResourceDynamicElementRoot](mta://scripting/shared/functions/getresourcedynamicelementroot.md)

- [getResourceExportedFunctions](mta://scripting/shared/functions/getresourceexportedfunctions.md)

- [getResourceFromName](mta://scripting/shared/functions/getresourcefromname.md)

- [getResourceName](mta://scripting/shared/functions/getresourcename.md)

- [getResourceRootElement](mta://scripting/shared/functions/getresourcerootelement.md)

- [getResourceState](mta://scripting/shared/functions/getresourcestate.md)

- [getThisResource](mta://scripting/shared/functions/getthisresource.md)

- [getRemoteRequests](mta://scripting/shared/functions/getremoterequests.md)

- [getRemoteRequestInfo](mta://scripting/shared/functions/getremoterequestinfo.md)

## Server functions

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIpFromMasterServer](mta://scripting/server/functions/getserveripfrommasterserver.md)

- [getServerName](mta://scripting/server/functions/getservername.md)

- [getServerPassword](mta://scripting/server/functions/getserverpassword.md)

- [getServerPort](mta://scripting/server/functions/getserverport.md)

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)

## Settings registry functions

- [get](mta://scripting/server/functions/get.md)

- [set](mta://scripting/server/functions/set.md)

## SQL functions

- [executeSQLQuery](mta://scripting/server/functions/executesqlquery.md)

- [dbConnect](mta://scripting/server/functions/dbconnect.md)

- [dbExec](mta://scripting/server/functions/dbexec.md)

- [dbFree](mta://scripting/server/functions/dbfree.md)

- [dbPoll](mta://scripting/server/functions/dbpoll.md)

- [dbPrepareString](mta://scripting/server/functions/dbpreparestring.md)

- [dbQuery](mta://scripting/server/functions/dbquery.md)

## Team functions

- [createTeam](mta://scripting/server/functions/createteam.md)

- [setTeamColor](mta://scripting/server/functions/setteamcolor.md)

- [setTeamFriendlyFire](mta://scripting/server/functions/setteamfriendlyfire.md)

- [setTeamName](mta://scripting/server/functions/setteamname.md)
  

- **Shared**

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)

## Text functions

- [textCreateDisplay](mta://scripting/server/functions/textcreatedisplay.md)

- [textCreateTextItem](mta://scripting/server/functions/textcreatetextitem.md)

- [textDestroyDisplay](mta://scripting/server/functions/textdestroydisplay.md)

- [textDestroyTextItem](mta://scripting/server/functions/textdestroytextitem.md)

- [textDisplayAddObserver](mta://scripting/server/functions/textdisplayaddobserver.md)

- [textDisplayAddText](mta://scripting/server/functions/textdisplayaddtext.md)

- [textDisplayGetObservers](mta://scripting/server/functions/textdisplaygetobservers.md)

- [textDisplayIsObserver](mta://scripting/server/functions/textdisplayisobserver.md)

- [textDisplayRemoveObserver](mta://scripting/server/functions/textdisplayremoveobserver.md)

- [textDisplayRemoveText](mta://scripting/server/functions/textdisplayremovetext.md)

- [textItemGetColor](mta://scripting/server/functions/textitemgetcolor.md)

- [textItemGetPosition](mta://scripting/server/functions/textitemgetposition.md)

- [textItemGetPriority](mta://scripting/server/functions/textitemgetpriority.md)

- [textItemGetScale](mta://scripting/server/functions/textitemgetscale.md)

- [textItemGetText](mta://scripting/server/functions/textitemgettext.md)

- [textItemSetColor](mta://scripting/server/functions/textitemsetcolor.md)

- [textItemSetPosition](mta://scripting/server/functions/textitemsetposition.md)

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)

## Utility functions

- **Shared**

- [addDebugHook](mta://scripting/shared/functions/adddebughook.md)

- [debugSleep](mta://scripting/shared/functions/debugsleep.md)

- [decodeString](mta://scripting/shared/functions/decodestring.md)

- [encodeString](mta://scripting/shared/functions/encodestring.md)

- [fromJSON](mta://scripting/shared/functions/fromjson.md)

- [generateKeyPair](mta://scripting/shared/functions/generatekeypair.md)

- [getColorFromString](mta://scripting/shared/functions/getcolorfromstring.md)

- [getDevelopmentMode](mta://scripting/shared/functions/getdevelopmentmode.md)

- [getDistanceBetweenPoints2D](mta://scripting/shared/functions/getdistancebetweenpoints2d.md)

- [getDistanceBetweenPoints3D](mta://scripting/shared/functions/getdistancebetweenpoints3d.md)

- [getEasingValue](mta://scripting/shared/functions/geteasingvalue.md)

- [getNetworkStats](mta://scripting/shared/functions/getnetworkstats.md)

- [getNetworkUsageData](mta://scripting/shared/functions/getnetworkusagedata.md)

- [getPerformanceStats](mta://scripting/shared/functions/getperformancestats.md)

- [getRealTime](mta://scripting/shared/functions/getrealtime.md)

- [getTickCount](mta://scripting/shared/functions/gettickcount.md)

- [getTimerDetails](mta://scripting/shared/functions/gettimerdetails.md)

- [getTimers](mta://scripting/shared/functions/gettimers.md)

- [getFPSLimit](mta://scripting/shared/functions/getfpslimit.md)

- [getUserdataType](mta://scripting/shared/functions/getuserdatatype.md)

- [getVersion](mta://scripting/shared/functions/getversion.md)

- [gettok](mta://scripting/shared/functions/gettok.md)

- [isTransferBoxVisible](mta://scripting/shared/functions/istransferboxvisible.md)

- [setTransferBoxVisible](mta://scripting/shared/functions/settransferboxvisible.md)

- [hash](mta://scripting/shared/functions/hash.md)

- [inspect](mta://scripting/shared/functions/inspect.md)

- [interpolateBetween](mta://scripting/shared/functions/interpolatebetween.md)

- [iprint](mta://scripting/shared/functions/iprint.md)

- [isOOPEnabled](mta://scripting/shared/functions/isoopenabled.md)

- [isTimer](mta://scripting/shared/functions/istimer.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22701](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22701):

- [isTimerPaused](mta://scripting/shared/functions/istimerpaused.md)

- [setTimerPaused](mta://scripting/shared/functions/settimerpaused.md)

- [killTimer](mta://scripting/shared/functions/killtimer.md)

- [md5](mta://scripting/shared/functions/md5.md)

- [passwordHash](mta://scripting/shared/functions/passwordhash.md)

- [passwordVerify](mta://scripting/shared/functions/passwordverify.md)

- [pregFind](mta://scripting/shared/functions/pregfind.md)

- [pregMatch](mta://scripting/shared/functions/pregmatch.md)

- [pregReplace](mta://scripting/shared/functions/pregreplace.md)

- [removeDebugHook](mta://scripting/shared/functions/removedebughook.md)

- [resetTimer](mta://scripting/shared/functions/resettimer.md)

- [setDevelopmentMode](mta://scripting/shared/functions/setdevelopmentmode.md)

- [setFPSLimit](mta://scripting/shared/functions/setfpslimit.md)

- [setTimer](mta://scripting/shared/functions/settimer.md)

- [ref](mta://scripting/shared/functions/ref.md)

- [deref](mta://scripting/shared/functions/deref.md)

- [sha256](mta://scripting/shared/functions/sha256.md)

- [split](mta://scripting/shared/functions/split.md)

- [teaDecode](mta://scripting/shared/functions/teadecode.md)

- [teaEncode](mta://scripting/shared/functions/teaencode.md)

- [toJSON](mta://scripting/shared/functions/tojson.md)

- [tocolor](mta://scripting/shared/functions/tocolor.md)

- [getProcessMemoryStats](mta://scripting/shared/functions/getprocessmemorystats.md)

- [utfChar](mta://scripting/shared/functions/utfchar.md)

- [utfCode](mta://scripting/shared/functions/utfcode.md)

- [utfLen](mta://scripting/shared/functions/utflen.md)

- [utfSeek](mta://scripting/shared/functions/utfseek.md)

- [utfSub](mta://scripting/shared/functions/utfsub.md)

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)

## UTF8 Library

**Shared**

- [utf8.byte](mta://scripting/shared/functions/utf8-byte.md)

- [utf8.char](mta://scripting/shared/functions/utf8-char.md)

- [utf8.charpos](mta://scripting/shared/functions/utf8-charpos.md)

- [utf8.escape](mta://scripting/shared/functions/utf8-escape.md)

- [utf8.find](mta://scripting/shared/functions/utf8-find.md)

- [utf8.fold](mta://scripting/shared/functions/utf8-fold.md)

- [utf8.gmatch](mta://scripting/shared/functions/utf8-gmatch.md)

- [utf8.gsub](mta://scripting/shared/functions/utf8-gsub.md)

- [utf8.insert](mta://scripting/shared/functions/utf8-insert.md)

- [utf8.len](mta://scripting/shared/functions/utf8-len.md)

- [utf8.lower](mta://scripting/shared/functions/utf8-lower.md)

- [utf8.match](mta://scripting/shared/functions/utf8-match.md)

- [utf8.ncasecmp](mta://scripting/shared/functions/utf8-ncasecmp.md)

- [utf8.next](mta://scripting/shared/functions/utf8-next.md)

- [utf8.remove](mta://scripting/shared/functions/utf8-remove.md)

- [utf8.reverse](mta://scripting/shared/functions/utf8-reverse.md)

- [utf8.sub](mta://scripting/shared/functions/utf8-sub.md)

- [utf8.title](mta://scripting/shared/functions/utf8-title.md)

- [utf8.upper](mta://scripting/shared/functions/utf8-upper.md)

- [utf8.width](mta://scripting/shared/functions/utf8-width.md)

- [utf8.widthindex](mta://scripting/shared/functions/utf8-widthindex.md)

## Vehicle functions

- [getModelHandling](mta://scripting/server/functions/getmodelhandling.md)

- [getVehicleIdleRespawnDelay](mta://scripting/server/functions/getvehicleidlerespawndelay.md)

- [getVehicleRespawnDelay](mta://scripting/server/functions/getvehiclerespawndelay.md)

- [getVehicleRespawnPosition](mta://scripting/server/functions/getvehiclerespawnposition.md)

- [getVehicleRespawnRotation](mta://scripting/server/functions/getvehiclerespawnrotation.md)

- [getVehiclesOfType](mta://scripting/server/functions/getvehiclesoftype.md)

- [isVehicleRespawnable](mta://scripting/server/functions/isvehiclerespawnable.md)

- [resetVehicleExplosionTime](mta://scripting/server/functions/resetvehicleexplosiontime.md)

- [resetVehicleIdleTime](mta://scripting/server/functions/resetvehicleidletime.md)

- [respawnVehicle](mta://scripting/server/functions/respawnvehicle.md)

- [setModelHandling](mta://scripting/server/functions/setmodelhandling.md)

- [setVehicleIdleRespawnDelay](mta://scripting/server/functions/setvehicleidlerespawndelay.md)

- [setVehicleRespawnDelay](mta://scripting/server/functions/setvehiclerespawndelay.md)

- [setVehicleRespawnPosition](mta://scripting/server/functions/setvehiclerespawnposition.md)

- [setVehicleRespawnRotation](mta://scripting/server/functions/setvehiclerespawnrotation.md)

- [spawnVehicle](mta://scripting/server/functions/spawnvehicle.md)

- [toggleVehicleRespawn](mta://scripting/server/functions/togglevehiclerespawn.md)
  

- **Shared**

- [addVehicleUpgrade](mta://scripting/shared/functions/addvehicleupgrade.md)

- [addVehicleSirens](mta://scripting/shared/functions/addvehiclesirens.md)

- [attachTrailerToVehicle](mta://scripting/shared/functions/attachtrailertovehicle.md)

- [blowVehicle](mta://scripting/shared/functions/blowvehicle.md)

- [createVehicle](mta://scripting/shared/functions/createvehicle.md)

- [detachTrailerFromVehicle](mta://scripting/shared/functions/detachtrailerfromvehicle.md)

- [fixVehicle](mta://scripting/shared/functions/fixvehicle.md)

- [getOriginalHandling](mta://scripting/shared/functions/getoriginalhandling.md)

- [getTrainDirection](mta://scripting/shared/functions/gettraindirection.md)

- [getTrainPosition](mta://scripting/shared/functions/gettrainposition.md)

- [getTrainSpeed](mta://scripting/shared/functions/gettrainspeed.md)

- [getVehicleColor](mta://scripting/shared/functions/getvehiclecolor.md)

- [getVehicleCompatibleUpgrades](mta://scripting/shared/functions/getvehiclecompatibleupgrades.md)

- [getVehicleController](mta://scripting/shared/functions/getvehiclecontroller.md)

- [getVehicleDoorOpenRatio](mta://scripting/shared/functions/getvehicledooropenratio.md)

- [getVehicleDoorState](mta://scripting/shared/functions/getvehicledoorstate.md)

- [getVehicleEngineState](mta://scripting/shared/functions/getvehicleenginestate.md)

- [getVehicleHandling](mta://scripting/shared/functions/getvehiclehandling.md)

- [getVehicleHeadLightColor](mta://scripting/shared/functions/getvehicleheadlightcolor.md)

- [getVehicleLandingGearDown](mta://scripting/shared/functions/getvehiclelandinggeardown.md)

- [getVehicleLightState](mta://scripting/shared/functions/getvehiclelightstate.md)

- [getVehicleMaxPassengers](mta://scripting/shared/functions/getvehiclemaxpassengers.md)

- [getVehicleModelFromName](mta://scripting/shared/functions/getvehiclemodelfromname.md)

- [getVehicleName](mta://scripting/shared/functions/getvehiclename.md)

- [getVehicleNameFromModel](mta://scripting/shared/functions/getvehiclenamefrommodel.md)

- [setVehicleNitroActivated](mta://scripting/shared/functions/setvehiclenitroactivated.md)

- [getVehicleOccupant](mta://scripting/shared/functions/getvehicleoccupant.md)

- [getVehicleOccupants](mta://scripting/shared/functions/getvehicleoccupants.md)

- [getVehicleOverrideLights](mta://scripting/shared/functions/getvehicleoverridelights.md)

- [getVehiclePaintjob](mta://scripting/shared/functions/getvehiclepaintjob.md)

- [getVehiclePanelState](mta://scripting/shared/functions/getvehiclepanelstate.md)

- [getVehiclePlateText](mta://scripting/shared/functions/getvehicleplatetext.md)

- [getVehicleSirenParams](mta://scripting/shared/functions/getvehiclesirenparams.md)

- [getVehicleSirens](mta://scripting/shared/functions/getvehiclesirens.md)

- [getVehicleSirensOn](mta://scripting/shared/functions/getvehiclesirenson.md)

- [getVehicleTowedByVehicle](mta://scripting/shared/functions/getvehicletowedbyvehicle.md)

- [getVehicleTowingVehicle](mta://scripting/shared/functions/getvehicletowingvehicle.md)

- [getVehicleTurretPosition](mta://scripting/shared/functions/getvehicleturretposition.md)

- [getVehicleType](mta://scripting/shared/functions/getvehicletype.md)

- [getVehicleUpgradeOnSlot](mta://scripting/shared/functions/getvehicleupgradeonslot.md)

- [getVehicleUpgradeSlotName](mta://scripting/shared/functions/getvehicleupgradeslotname.md)

- [getVehicleUpgrades](mta://scripting/shared/functions/getvehicleupgrades.md)

- [getVehicleVariant](mta://scripting/shared/functions/getvehiclevariant.md)

- [getVehicleWheelStates](mta://scripting/shared/functions/getvehiclewheelstates.md)

- [isTrainDerailable](mta://scripting/shared/functions/istrainderailable.md)

- [isTrainDerailed](mta://scripting/shared/functions/istrainderailed.md)

- [isVehicleBlown](mta://scripting/shared/functions/isvehicleblown.md)

- [isVehicleDamageProof](mta://scripting/shared/functions/isvehicledamageproof.md)

- [isVehicleFuelTankExplodable](mta://scripting/shared/functions/isvehiclefueltankexplodable.md)

- [isVehicleLocked](mta://scripting/shared/functions/isvehiclelocked.md)

- [isVehicleOnGround](mta://scripting/shared/functions/isvehicleonground.md)

- [isVehicleTaxiLightOn](mta://scripting/shared/functions/isvehicletaxilighton.md)

- [removeVehicleUpgrade](mta://scripting/shared/functions/removevehicleupgrade.md)

- [removeVehicleSirens](mta://scripting/shared/functions/removevehiclesirens.md)

- [setTrainDerailable](mta://scripting/shared/functions/settrainderailable.md)

- [setTrainDerailed](mta://scripting/shared/functions/settrainderailed.md)

- [setTrainDirection](mta://scripting/shared/functions/settraindirection.md)

- [setTrainPosition](mta://scripting/shared/functions/settrainposition.md)

- [setTrainSpeed](mta://scripting/shared/functions/settrainspeed.md)

- [setVehicleColor](mta://scripting/shared/functions/setvehiclecolor.md)

- [setVehicleDamageProof](mta://scripting/shared/functions/setvehicledamageproof.md)

- [setVehicleDoorOpenRatio](mta://scripting/shared/functions/setvehicledooropenratio.md)

- [setVehicleDoorState](mta://scripting/shared/functions/setvehicledoorstate.md)

- [setVehicleDoorsUndamageable](mta://scripting/shared/functions/setvehicledoorsundamageable.md)

- [setVehicleEngineState](mta://scripting/shared/functions/setvehicleenginestate.md)

- [setVehicleFuelTankExplodable](mta://scripting/shared/functions/setvehiclefueltankexplodable.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22771](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22771):

- [spawnVehicleFlyingComponent](mta://scripting/shared/functions/spawnvehicleflyingcomponent.md)

- [setVehicleHandling](mta://scripting/shared/functions/setvehiclehandling.md)

- [setVehicleHeadLightColor](mta://scripting/shared/functions/setvehicleheadlightcolor.md)

- [setVehicleLandingGearDown](mta://scripting/shared/functions/setvehiclelandinggeardown.md)

- [setVehicleLightState](mta://scripting/shared/functions/setvehiclelightstate.md)

- [setVehicleLocked](mta://scripting/shared/functions/setvehiclelocked.md)

- [setVehicleOverrideLights](mta://scripting/shared/functions/setvehicleoverridelights.md)

- [setVehiclePaintjob](mta://scripting/shared/functions/setvehiclepaintjob.md)

- [setVehiclePanelState](mta://scripting/shared/functions/setvehiclepanelstate.md)

- [setVehiclePlateText](mta://scripting/shared/functions/setvehicleplatetext.md)

- [setVehicleSirens](mta://scripting/shared/functions/setvehiclesirens.md)

- [setVehicleSirensOn](mta://scripting/shared/functions/setvehiclesirenson.md)

- [setVehicleTaxiLightOn](mta://scripting/shared/functions/setvehicletaxilighton.md)

- [setVehicleTurretPosition](mta://scripting/shared/functions/setvehicleturretposition.md)

- [setVehicleVariant](mta://scripting/shared/functions/setvehiclevariant.md)

- [setVehicleWheelStates](mta://scripting/shared/functions/setvehiclewheelstates.md)

## Water functions

**Shared**

- [createWater](mta://scripting/shared/functions/createwater.md)

- [getWaterColor](mta://scripting/shared/functions/getwatercolor.md)

- [getWaterVertexPosition](mta://scripting/shared/functions/getwatervertexposition.md)

- [getWaveHeight](mta://scripting/shared/functions/getwaveheight.md)

- [resetWaterColor](mta://scripting/shared/functions/resetwatercolor.md)

- [resetWaterLevel](mta://scripting/shared/functions/resetwaterlevel.md)

- [setWaterColor](mta://scripting/shared/functions/setwatercolor.md)

- [setWaterLevel](mta://scripting/shared/functions/setwaterlevel.md)

- [setWaterVertexPosition](mta://scripting/shared/functions/setwatervertexposition.md)

- [setWaveHeight](mta://scripting/shared/functions/setwaveheight.md)

## Weapon functions

- [giveWeapon](mta://scripting/server/functions/giveweapon.md)

- [takeAllWeapons](mta://scripting/server/functions/takeallweapons.md)

- [takeWeapon](mta://scripting/server/functions/takeweapon.md)
  

- **Shared**

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)

## World functions

- [getJetpackWeaponEnabled](mta://scripting/server/functions/getjetpackweaponenabled.md)

- [setJetpackWeaponEnabled](mta://scripting/server/functions/setjetpackweaponenabled.md)
  

- [areTrafficLightsLocked](mta://scripting/shared/functions/aretrafficlightslocked.md)

- [getAircraftMaxHeight](mta://scripting/shared/functions/getaircraftmaxheight.md)

- [getAircraftMaxVelocity](mta://scripting/shared/functions/getaircraftmaxvelocity.md)

- [getCloudsEnabled](mta://scripting/shared/functions/getcloudsenabled.md)

- [getFarClipDistance](mta://scripting/shared/functions/getfarclipdistance.md)

- [getFogDistance](mta://scripting/shared/functions/getfogdistance.md)

- [getGameSpeed](mta://scripting/shared/functions/getgamespeed.md)

- [getGravity](mta://scripting/shared/functions/getgravity.md)

- [getHeatHaze](mta://scripting/shared/functions/getheathaze.md)

- [getInteriorSoundsEnabled](mta://scripting/shared/functions/getinteriorsoundsenabled.md)

- [getJetpackMaxHeight](mta://scripting/shared/functions/getjetpackmaxheight.md)

- [getMinuteDuration](mta://scripting/shared/functions/getminuteduration.md)

- [getMoonSize](mta://scripting/shared/functions/getmoonsize.md)

- [getOcclusionsEnabled](mta://scripting/shared/functions/getocclusionsenabled.md)

- [getRainLevel](mta://scripting/shared/functions/getrainlevel.md)

- [getSunColor](mta://scripting/shared/functions/getsuncolor.md)

- [getSunSize](mta://scripting/shared/functions/getsunsize.md)

- [getTime](mta://scripting/shared/functions/gettime.md)

- [getTrafficLightState](mta://scripting/shared/functions/gettrafficlightstate.md)

- [getWeather](mta://scripting/shared/functions/getweather.md)

- [getWindVelocity](mta://scripting/shared/functions/getwindvelocity.md)

- [getSkyGradient](mta://scripting/shared/functions/getskygradient.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22195](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22195):

- [isWorldSpecialPropertyEnabled](mta://scripting/shared/functions/isworldspecialpropertyenabled.md)

- [getZoneName](mta://scripting/shared/functions/getzonename.md)

- [isGarageOpen](mta://scripting/shared/functions/isgarageopen.md)

- [removeWorldModel](mta://scripting/shared/functions/removeworldmodel.md)

- [resetFarClipDistance](mta://scripting/shared/functions/resetfarclipdistance.md)

- [resetFogDistance](mta://scripting/shared/functions/resetfogdistance.md)

- [resetHeatHaze](mta://scripting/shared/functions/resetheathaze.md)

- [resetMoonSize](mta://scripting/shared/functions/resetmoonsize.md)

- [resetRainLevel](mta://scripting/shared/functions/resetrainlevel.md)

- [resetSkyGradient](mta://scripting/shared/functions/resetskygradient.md)

- [resetSunColor](mta://scripting/shared/functions/resetsuncolor.md)

- [resetSunSize](mta://scripting/shared/functions/resetsunsize.md)

- [resetWindVelocity](mta://scripting/shared/functions/resetwindvelocity.md)

- [restoreAllWorldModels](mta://scripting/shared/functions/restoreallworldmodels.md)

- [restoreWorldModel](mta://scripting/shared/functions/restoreworldmodel.md)

- [setAircraftMaxHeight](mta://scripting/shared/functions/setaircraftmaxheight.md)

- [setAircraftMaxVelocity](mta://scripting/shared/functions/setaircraftmaxvelocity.md)

- [setCloudsEnabled](mta://scripting/shared/functions/setcloudsenabled.md)

- [setFarClipDistance](mta://scripting/shared/functions/setfarclipdistance.md)

- [setFogDistance](mta://scripting/shared/functions/setfogdistance.md)

- [setGameSpeed](mta://scripting/shared/functions/setgamespeed.md)

- [setGarageOpen](mta://scripting/shared/functions/setgarageopen.md)

- [setGravity](mta://scripting/shared/functions/setgravity.md)

- [setHeatHaze](mta://scripting/shared/functions/setheathaze.md)

- [setInteriorSoundsEnabled](mta://scripting/shared/functions/setinteriorsoundsenabled.md)

- [setMinuteDuration](mta://scripting/shared/functions/setminuteduration.md)

- [setMoonSize](mta://scripting/shared/functions/setmoonsize.md)

- [setOcclusionsEnabled](mta://scripting/shared/functions/setocclusionsenabled.md)

- [setRainLevel](mta://scripting/shared/functions/setrainlevel.md)

- [setSkyGradient](mta://scripting/shared/functions/setskygradient.md)

- [setSunColor](mta://scripting/shared/functions/setsuncolor.md)

- [setSunSize](mta://scripting/shared/functions/setsunsize.md)

- [setTime](mta://scripting/shared/functions/settime.md)

- [setTrafficLightState](mta://scripting/shared/functions/settrafficlightstate.md)

- [setTrafficLightsLocked](mta://scripting/shared/functions/settrafficlightslocked.md)

- [setWeather](mta://scripting/shared/functions/setweather.md)

- [setWeatherBlended](mta://scripting/shared/functions/setweatherblended.md)

- [setWindVelocity](mta://scripting/shared/functions/setwindvelocity.md)

- [setJetpackMaxHeight](mta://scripting/shared/functions/setjetpackmaxheight.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22195](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22195):

- [setWorldSpecialPropertyEnabled](mta://scripting/shared/functions/setworldspecialpropertyenabled.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22741](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22741):

- [resetWorldProperties](mta://scripting/shared/functions/resetworldproperties.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22909](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22909):

- [removeGameWorld](mta://scripting/client/functions/removegameworld.md)

- [restoreGameWorld](mta://scripting/client/functions/restoregameworld.md)

## XML functions

**Shared**

- [xmlCopyFile](mta://scripting/shared/functions/xmlcopyfile.md)

- [xmlCreateChild](mta://scripting/shared/functions/xmlcreatechild.md)

- [xmlCreateFile](mta://scripting/shared/functions/xmlcreatefile.md)

- [xmlDestroyNode](mta://scripting/shared/functions/xmldestroynode.md)

- [xmlFindChild](mta://scripting/shared/functions/xmlfindchild.md)

- [xmlLoadFile](mta://scripting/shared/functions/xmlloadfile.md)

- [xmlLoadString](mta://scripting/shared/functions/xmlloadstring.md)

- [xmlNodeGetAttribute](mta://scripting/shared/functions/xmlnodegetattribute.md)

- [xmlNodeGetAttributes](mta://scripting/shared/functions/xmlnodegetattributes.md)

- [xmlNodeGetChildren](mta://scripting/shared/functions/xmlnodegetchildren.md)

- [xmlNodeGetName](mta://scripting/shared/functions/xmlnodegetname.md)

- [xmlNodeGetParent](mta://scripting/shared/functions/xmlnodegetparent.md)

- [xmlNodeGetValue](mta://scripting/shared/functions/xmlnodegetvalue.md)

- [xmlNodeSetAttribute](mta://scripting/shared/functions/xmlnodesetattribute.md)

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
