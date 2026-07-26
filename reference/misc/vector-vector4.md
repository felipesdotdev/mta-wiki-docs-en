---
doc_id: "mta-wiki:8115"
title: "Vector/Vector4"
source_title: "Vector/Vector4"
source_url: "https://wiki.multitheftauto.com/wiki/Vector/Vector4"
revision_id: 54156
language: "en"
categories: ["Incomplete"]
generated_at: "2026-07-26T16:17:03.060213+00:00"
---

# Vector/Vector4

The Vector4 class is a class introduced in 1.4

## Methods

### create

This is default constructor for the Vector4 class and returns a Vector4 object.

#### Syntax

```
vector4 Vector4 ( float x = 0, float y = 0, float z = 0, float w = 0 )
```

- **x**,**y**,**z** and **w** coordinates for the vector. If not specified, they default to 0.

- Instead of these four coordinates, a single Vector4 object may be inserted to clone it.

#### Example

This example adds a command called "/garage", allowing you to get any garage bounding box.

Click to collapse [-]
Client

```
function garageBoundingBox ( command, garageID)
   if not garageID then
      outputChatBox("[Usage] /garage <id>")
      return
   end
	
   if tonumber(garageID) then 
      if tonumber(garageID) > 0 and tonumber(garageID) < 50 then
         local boundingBox = Vector4(getGarageBoundingBox (garageID)) 
         outputChatBox("West: "..boundingBox.x..", East: " ..boundingBox.y..", South: "..boundingBox.z.." North: "..boundingBox.w)
      else
         outputChatBox("Garage ID must be between 1 and 49")
      end 
   end 
end 
addCommandHandler ("garage",garageBoundingBox)
```

### dot

### normalize

### getX and setX

### getY and setY

### getZ and setZ

### getW and setW

### getNormalized

### getSquaredLength

### getLength
