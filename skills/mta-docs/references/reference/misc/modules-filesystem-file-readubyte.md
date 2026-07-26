---
doc_id: "mta-wiki:13526"
title: "Modules/FileSystem/file/readUByte"
source_title: "Modules/FileSystem/file/readUByte"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/readUByte"
revision_id: 73734
language: "en"
categories: []
---

# Modules/FileSystem/file/readUByte

This function attempts to read an unsigned byte (native type) from a file and returns it. The amount of bytes read should be one.

## Syntax

```
unsigned_byte file:readUByte ()
```

## Returns

Returns the unsigned byte if it was successfully read from the file, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet writes a Lua type into a file stream. The lua type can be anything that can be traversed over the network. It must be context-less data.

```
-- A table specifying descriptor information about Lua types.
local typeDescriptors = {
    ["boolean"] = { networkId = 0 },
    ["number"] = { networkId = 1 },
    ["string"] = { networkId = 2 },
    ["table"] = { networkId = 3 },
    ["nil"] = { networkId = 4 }
};

local function isValidNetworkType( typeName )
    return not ( typeDescriptors[typeName] == nil );
end

local function writeLuaData( theFile, data )
    -- Get the descriptor for the type.
    local typeName = rawtype(data);
    local info = typeDescriptors[typeName];

    -- Some types cannot be transfered over the network.
    if not ( info ) then return; end;

    -- Write the network identifier.
    theFile:writeUByte( info.networkId );

    -- Check what we are dealing with.
    if ( typeName == "boolean") then
        theFile:writeBoolean( data );
    elseif ( typeName == "number" ) then
        theFile:writeDouble( data );
    elseif ( typeName == "string" ) then
        theFile:writeUShort( #data );
        theFile:write( data );
    elseif ( typeName == "table" ) then
        -- First write iterated entries of the table.
        local numIteration = #data;
        do
            theFile:writeUInt( numIteration );

            local n = 1;

            while ( n <= numIteration ) do
                writeLuaData( data[n] );
                n = n + 1;
            end
        end

        -- Next write the data entries.
        do
            -- Construct a data entry table.
            local dataTable = {};
            local entryCount = 0;

            for m,n in pairs( data ) do
                if ( isValidNetworkType( rawtype( n ) ) ) then
                    if not ( rawtype( n ) == "number" ) or ( n <= 0 ) or ( n > numIteration ) then
                        entryCount = entryCount + 1;

                        dataTable[entryCount] = {
                            key = m,
                            value = n
                        };
                    end
                end
            end

            -- Write the amount of data entries.
            theFile:writeUInt( entryCount );

            -- Write all data entries.
            for m,n in ipairs( dataTable ) do
                writeLuaData( n.key );
                writeLuaData( n.value );
            end
        end
    elseif ( typeName == "nil" ) then
        -- Do nothing.
    end
end

-- task for the reader: write a function to read the Lua data again.
```

## [FileSystem](mta://reference/misc/modules-filesystem.md) File Functions

- [read](mta://reference/misc/modules-filesystem-file-read.md)

- [readByte](mta://reference/misc/modules-filesystem-file-readbyte.md)

- readUByte

- [readShort](mta://reference/misc/modules-filesystem-file-readshort.md)

- [readUShort](mta://reference/misc/modules-filesystem-file-readushort.md)

- [readInt](mta://reference/misc/modules-filesystem-file-readint.md)

- [readUInt](mta://reference/misc/modules-filesystem-file-readuint.md)

- [readFloat](mta://reference/misc/modules-filesystem-file-readfloat.md)

- [readDouble](mta://reference/misc/modules-filesystem-file-readdouble.md)

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
