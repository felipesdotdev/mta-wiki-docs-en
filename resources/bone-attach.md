---
doc_id: "mta-wiki:10648"
title: "Resource : Bone attach"
source_title: "Resource:Bone attach"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ABone_attach"
revision_id: 62833
language: "en"
categories: ["Utility_templates", "Resource"]
generated_at: "2026-07-26T16:16:58.736822+00:00"
---

# Resource : Bone attach

This resource lets you attach elements to players/peds bones using its exported functions.
Download can be found at the [MTA community page](https://community.multitheftauto.com/index.php?p=resources&s=details&id=2540).  

Resource developed by: [Devan_LT](https://community.multitheftauto.com/index.php?p=profile&id=5138) (also known as [CrystalMV](https://forum.mtasa.com/profile/1985-crystalmv/))

## Exported functions/events

Click to collapse [-]
Server or Client

This function attaches element to the bone of the ped or player.

```
bool attachElementToBone (element theElement, element theAttachToPed, int theBone[, float xPosOffset = 0, float yPosOffset = 0, float zPosOffset = 0, float xRotOffset = 0, float yRotOffset = 0, float zRotOffset = 0])
```

#### Required Arguments

- **theElement:** Element which you want to attach..

- **theAttachToPed:** The ped or player which you want to attach element to.

- **theBone:** The number of the ped or player's bone which you want to attach element to.

 

Bone numbers

- **1:**  head

- **2:**  neck

- **3:**  spine

- **4:**  pelvis

- **5:**  left clavicle

- **6:**  right clavicle

- **7:**  left shoulder

- **8:**  right shoulder

- **9:**  left elbow

- **10:**  right elbow

- **11:**  left hand

- **12:**  right hand

- **13:**  left hip

- **14:**  right hip

- **15:**  left knee

- **16:**  right knee

- **17:**  left ankle

- **18:**  right ankle

- **19:**  left foot

- **20:**  right foot

#### Optional arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **xPosOffset:** The x offset, if you want the elements to be a certain distance from one another (default 0).

- **yPosOffset:** The y offset (default 0).

- **zPosOffset:** The z offset (default 0).

- **xRotOffset:** The x rotation offset (default 0).

- **yRotOffset:** The y rotation offset (default 0).

- **zRotOffset:** The z rotation offset (default 0).

#### Returns

Returns true if element was successfully attached, false otherwise.

This function detaches element from the bone of the ped.

```
bool detachElementFromBone (element theElement)
```

#### Required Arguments

- **theElement:** Element which you want to detach.

#### Returns

Returns true if element was successfully detached, false otherwise.

This function checks if element is attached to a bone.

```
bool isElementAttachedToBone (element theElement)
```

#### Required Arguments

- **theElement:** Element which you want to check.

#### Returns

Returns true if element is attached to a bone, false otherwise.

This function gets ped, bone and offset details of attached element.

```
bool getElementBoneAttachmentDetails (element theElement)
```

#### Required Arguments

- **theElement:** Element which you want to get attachment details of.

#### Returns

Returns ped, bone, x, y, z, rx, ry, rz used in attachElementToBone if element is attached, false otherwise.

This function changes position offset of attached element.

```
bool setElementBonePositionOffset (element theElement, float xPosOffset, float yPosOffset, float zPosOffset)
```

#### Required Arguments

- **theElement:** Element which you want to change offset of.

- **xPosOffset:** New x position offset.

- **yPosOffset:** New y position offset.

- **zPosOffset:** New z position offset.

#### Returns

Returns true if position set successfully, false otherwise.

This function changes rotation offset of attached element.

```
bool setElementBoneRotationOffset (element theElement, float xRotOffset, float yRotOffset, float zRotOffset)
```

#### Required Arguments

- **theElement:** Element which you want to change offset of.

- **xRotOffset:** New x rotation offset.

- **yRotOffset:** New y rotation offset.

- **zRotOffset:** New z rotation offset.

#### Returns

Returns true if rotation set successfully, false otherwise.

Click to collapse [-]
Client-Only

This function gets position and rotation of the ped bone.

```
bool getBonePositionAndRotation (element theAttachToPed, int theBone)
```

#### Required Arguments

- **theAttachToPed:** The ped or player which bone you want to get position.

- **theBone:** The number of the ped or player's bone which you want to get position.

#### Returns

Returns bone x, y, z position and rotation if ped is streamed in and bone number is valid, false otherwise.

## Example

Click to collapse [-]
Example 1

This example makes the player carry a money bag when they type 'getbag':

```
-- this function is called whenever someone types 'getbag' in the console:
function attachCash (thePlayer)
    local x, y, z = getElementPosition (thePlayer)
    setPedAnimation (thePlayer, "ROB_BANK", "CAT_Safe_Rob", -1, true, false, false)
    local objPick = createObject (1550, x, y, z)
    setTimer (function (thePlayer)
        setPedAnimation (thePlayer, nil)
        exports.bone_attach:attachElementToBone (objPick, thePlayer, 4, -0.3, 0.2, 0, -125, 0, 0)
    end, 1000, 1, thePlayer)
end
addCommandHandler ("getbag", attachCash)
```
