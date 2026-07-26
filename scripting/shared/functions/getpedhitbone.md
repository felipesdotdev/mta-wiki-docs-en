---
doc_id: "mta-wiki:13658"
title: "GetPedHitBone"
source_title: "GetPedHitBone"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedHitBone"
revision_id: 74526
language: "en"
categories: ["Useful_Functions"]
generated_at: "2026-07-26T16:15:17.534922+00:00"
---

# GetPedHitBone

This function gets the approximate number of the bone where the ped is hit

## Syntax

```
int getPedHitBone( ped thePed, float hitX, float hitY, float hitZ )
```

### Required Arguments

- **thePed:** the [ped](mta://reference/misc/ped.md) whose bone you want to get.

- **hitX**, **hitY**, **hitZ**: [float](mta://reference/misc/float.md) world coordinates representing a hit point.

### Returns

An **int** with the approximate bone where the [ped](mta://reference/misc/ped.md) take damage, does not work properly serverside

## Code

Click to collapse [-]
Function source

```
function getPedHitBone(thePed, hitX, hitY, hitZ)
   assert(isElement(thePed) and (getElementType(thePed) == "ped" or getElementType(thePed) == "player"), "Bad argument @ 'getPedHitBone' [Expected ped/player at argument 1, got " .. tostring(thePed) .. "]")
   assert(tonumber(hitX), "Bad argument @ 'getPedHitBone' [Expected vector3 at argument 2, got " .. tostring(hitX) .. "]")
   assert(tonumber(hitY), "Bad argument @ 'getPedHitBone' [Expected vector3 at argument 3, got " .. tostring(hitY) .. "]")
   assert(tonumber(hitZ), "Bad argument @ 'getPedHitBone' [Expected vector3 at argument 4, got " .. tostring(hitZ) .. "]")
   local nowDistance, hitBone
   local boneIDs = {0, 1, 2, 3, 4, 5, 6, 7, 8, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 51, 52, 53, 54}
   for _,bone in pairs(boneIDs) do
      local boneX, boneY, boneZ = getPedBonePosition(thePed, bone)
      local distance = getDistanceBetweenPoints3D(hitX, hitY, hitZ, boneX, boneY, boneZ)
      if nowDistance and (distance < nowDistance) then
         nowDistance, hitBone = distance, bone
      elseif not nowDistance then
         nowDistance, hitBone = distance, bone
      end
   end
   return hitBone
end
```

## Example

Click to collapse [-]
Client

```
function getPedHitBone(thePed, hitX, hitY, hitZ)
   assert(isElement(thePed) and (getElementType(thePed) == "ped" or getElementType(thePed) == "player"), "Bad argument @ 'getPedHitBone' [Expected ped/player at argument 1, got " .. tostring(thePed) .. "]")
   assert(tonumber(hitX), "Bad argument @ 'getPedHitBone' [Expected vector3 at argument 2, got " .. tostring(hitX) .. "]")
   assert(tonumber(hitY), "Bad argument @ 'getPedHitBone' [Expected vector3 at argument 3, got " .. tostring(hitY) .. "]")
   assert(tonumber(hitZ), "Bad argument @ 'getPedHitBone' [Expected vector3 at argument 4, got " .. tostring(hitZ) .. "]")
   local nowDistance, hitBone
   local boneIDs = {0, 1, 2, 3, 4, 5, 6, 7, 8, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36, 41, 42, 43, 44, 51, 52, 53, 54}
   for _,bone in pairs(boneIDs) do
      local boneX, boneY, boneZ = getPedBonePosition(thePed, bone)
      local distance = getDistanceBetweenPoints3D(hitX, hitY, hitZ, boneX, boneY, boneZ)
      if nowDistance and (distance < nowDistance) then
         nowDistance, hitBone = distance, bone
      elseif not nowDistance then
         nowDistance, hitBone = distance, bone
      end
   end
   return hitBone
end

addEventHandler( "onClientPlayerWeaponFire", root, function(weapon, ammo, ammoInClip, hitX, hitY, hitZ, hitElement, startX, startY, startZ)
   if isElement(hitElement) then
      outputChatBox("You hit bone "..getPedHitBone(hitElement, hitX, hitY, hitZ) )
   end
end)
```

**Author:** Rick
