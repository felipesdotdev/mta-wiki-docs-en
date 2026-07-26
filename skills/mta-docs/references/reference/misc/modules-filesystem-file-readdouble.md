---
doc_id: "mta-wiki:13532"
title: "Modules/FileSystem/file/readDouble"
source_title: "Modules/FileSystem/file/readDouble"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/readDouble"
revision_id: 73741
language: "en"
categories: []
---

# Modules/FileSystem/file/readDouble

This function attempts to read a double (native type) from a file and return it. The amount of bytes read should be eight.

## Syntax

```
double file:readDouble ()
```

## Returns

Returns a double if it was successfully read from the file, **false** otherwise.

## Example

Click to collapse [-]
Server

This snippet demonstrates a basic binary object map format. It can be extended to support more parameters.

```
-- Grab some objects to store into our map.
local storeObjects = getElementsByType( "object" );

-- Function to store data about objects.
local function saveObjects( theFile, objects )
    -- Write the amount of entries into the stream.
    theFile.writeShort( #objects );

    -- Now add every object into it.
    for m,n in ipairs( objects ) do
        local posX, posY, posZ = getElementPosition( n );
        local rotX, rotY, rotZ = getElementRotation( n );
        local model = getElementModel( n );
        local dimension, interior = getElementDimension( n ), getElementInterior( n );

        -- Write the parameters of the object into the stream.
        theFile:writeDouble( posX ); theFile:writeDouble( posY ); theFile:writeDouble( posZ );
        theFile:writeDouble( rotX ); theFile:writeDouble( rotY ); theFile:writeDouble( rotZ );
        theFile:writeShort( model );
        theFile:writeShort( dimension ); theFile:writeShort( interior );
    end
end

-- Function to load back data from a file stream.
local function loadObjects( theFile )
    -- Get the amount of entries.
    local objectCount = theFile:readShort();

    -- Create the objects.
    local n = 1;

    while ( n <= objectCount ) do
        local posX, posY, posZ = theFile:readDouble(), theFile:readDouble(), theFile:readDouble();
        local rotX, rotY, rotZ = theFile:readDouble(), theFile:readDouble(), theFile:readDouble();
        local model = theFile:readShort();
        local dimension, interior = theFile:readShort(), theFile:readShort();

        -- Create this particular object, if all values are properly read.
        -- We can optimize this condition by checking the last value that was read.
        if ( interior ) then
            local object = createObject( model, posX, posY, posZ, rotX, rotY, rotZ );
            
            if ( object ) then
                -- Continue applying advanced properties of creation of object succeeded.
                setElementDimension( object, dimension );
                setElementInterior( object, interior );
            end
        end
    end
end

-- Save our current objects into a file.
local saveFile = fileCreate( "world_objects.dat" );

saveObjects( saveFile, storeObjects );

-- todo: maybe load the objects.
```

## [FileSystem](mta://reference/misc/modules-filesystem.md) File Functions

- [read](mta://reference/misc/modules-filesystem-file-read.md)

- [readByte](mta://reference/misc/modules-filesystem-file-readbyte.md)

- [readUByte](mta://reference/misc/modules-filesystem-file-readubyte.md)

- [readShort](mta://reference/misc/modules-filesystem-file-readshort.md)

- [readUShort](mta://reference/misc/modules-filesystem-file-readushort.md)

- [readInt](mta://reference/misc/modules-filesystem-file-readint.md)

- [readUInt](mta://reference/misc/modules-filesystem-file-readuint.md)

- [readFloat](mta://reference/misc/modules-filesystem-file-readfloat.md)

- readDouble

- [readBoolean](mta://reference/misc/modules-filesystem-file-readboolean.md)

- [write](mta://reference/misc/modules-filesystem-file-write.md)

- [writeByte](mta://reference/misc/modules-filesystem-file-writebyte.md)

- [writeUByte](mta://reference/misc/modules-filesystem-file-writeubyte.md)

- [writeShort](mta://reference/misc/modules-filesystem-file-writeshort.md)

- [writeUShort](mta://reference/misc/modules-filesystem-file-writeushort.md)

- [writeInt](mta://reference/misc/modules-filesystem-file-writeint.md)

- [writeUInt](mta://reference/misc/modules-filesystem-file-writeuint.md)

- [writeFloat](mta://reference/misc/modules-filesystem-file-writefloat.md)

- [writeDouble](mta://reference/misc/modules-filesystem-file-writedouble.md)

- [writeBoolean](mta://reference/misc/modules-filesystem-file-writeboolean.md)

- [size](mta://reference/misc/modules-filesystem-file-size.md)

- [stat](mta://reference/misc/modules-filesystem-file-stat.md)

- [tell](mta://reference/misc/modules-filesystem-file-tell.md)

- [seek](mta://reference/misc/modules-filesystem-file-seek.md)

- [eof](mta://reference/misc/modules-filesystem-file-eof.md)

- [flush](mta://reference/misc/modules-filesystem-file-flush.md)

- [isWritable](mta://reference/misc/modules-filesystem-file-iswritable.md)

- [isReadable](mta://reference/misc/modules-filesystem-file-isreadable.md)
