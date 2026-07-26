---
doc_id: "mta-wiki:7517"
title: "MTA:Eir/FileSystem/file/readShort"
source_title: "MTA:Eir/FileSystem/file/readShort"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/file/readShort"
revision_id: 73557
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.678309+00:00"
---

# MTA:Eir/FileSystem/file/readShort

This function attempts to read a short (native type) from a file and returns it. The amount of bytes read should be two.

## Syntax

```
short file:readShort ()
```

## Returns

Returns the short integer if it was successfully read from the file, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet reads and writes string buffers into a custom file format.

```
local function writeBuffers( outFile, buffers )
    -- Write header information.
    outFile:writeInt( #buffers ); -- number of buffers
    
    -- Write the buffers.
    for m,n in ipairs( buffers ) do
        local bufferContent = tostring( n );

        -- Write header of buffer.
        outFile:writeShort( #bufferContent ); -- length of buffer

        -- Write the content
        outFile:write( bufferContent );
    end
end

local function readBuffers( inFile )
    local buffers = {};

    -- Read header information.
    local numBuffers = inFile:readInt();

    -- Make sure we read the int correctly.
    -- Fails if the file has less than 4 bytes to read.
    if ( numBuffers ) then
        local n = 1;

        while ( n <= numBuffers ) do
            -- Read buffer header.
            local bufferSize = inFile:readShort();

            -- We always have to add the amount of buffers specified by the header.
            -- Hence we always add a buffer to the result array.
            local buffer = "";

            if ( bufferSize ) then
                -- Read the buffer.
                buffer = inFile:read( bufferSize );
            end

            -- Append the result buffer.
            buffers[n] = buffer;

            n = n + 1;
        end
    end

    return buffers;
end

-- Manager some buffers in a file.
local myBuffers = { "Hello World!", "Cooking eggs on a frying pan", "The American Pizzas taste awesome", "There is no bathroom." };

local theFile = fileCreate( "buffers.dat" );

-- First write the buffers into the file.
writeBuffers( theFile, myBuffers );

-- Now retrieve them again.
theFile:seek( 0, "set" );

myBuffers = readBuffers( theFile );

-- Output the buffers.
for m,n in ipairs( myBuffers ) do
    outputChatBox( n );
end
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) File Functions

- [read](mta://reference/misc/mta-eir-filesystem-file-read.md)

- [readByte](mta://reference/misc/mta-eir-filesystem-file-readbyte.md)

- [readUByte](mta://reference/misc/mta-eir-filesystem-file-readubyte.md)

- readShort

- [readUShort](mta://reference/misc/mta-eir-filesystem-file-readushort.md)

- [readInt](mta://reference/misc/mta-eir-filesystem-file-readint.md)

- [readUInt](mta://reference/misc/mta-eir-filesystem-file-readuint.md)

- [readFloat](mta://reference/misc/mta-eir-filesystem-file-readfloat.md)

- [readDouble](mta://reference/misc/mta-eir-filesystem-file-readdouble.md)

- [readBoolean](mta://reference/misc/mta-eir-filesystem-file-readboolean.md)

- [write](mta://reference/misc/mta-eir-filesystem-file-write.md)

- [writeByte](mta://reference/misc/mta-eir-filesystem-file-writebyte.md)

- [writeUByte](mta://reference/misc/mta-eir-filesystem-file-writeubyte.md)

- [writeShort](mta://reference/misc/mta-eir-filesystem-file-writeshort.md)

- [writeUShort](mta://reference/misc/mta-eir-filesystem-file-writeushort.md)

- [writeInt](mta://reference/misc/mta-eir-filesystem-file-writeint.md)

- [writeUInt](mta://reference/misc/mta-eir-filesystem-file-writeuint.md)

- [writeFloat](mta://reference/misc/mta-eir-filesystem-file-writefloat.md)

- [writeDouble](mta://reference/misc/mta-eir-filesystem-file-writedouble.md)

- [writeBoolean](mta://reference/misc/mta-eir-filesystem-file-writeboolean.md)

- [size](mta://reference/misc/mta-eir-filesystem-file-size.md)

- [stat](mta://reference/misc/mta-eir-filesystem-file-stat.md)

- [tell](mta://reference/misc/mta-eir-filesystem-file-tell.md)

- [seek](mta://reference/misc/mta-eir-filesystem-file-seek.md)

- [eof](mta://reference/misc/mta-eir-filesystem-file-eof.md)

- [flush](mta://reference/misc/mta-eir-filesystem-file-flush.md)

- [isWritable](mta://reference/misc/mta-eir-filesystem-file-iswritable.md)

- [isReadable](mta://reference/misc/mta-eir-filesystem-file-isreadable.md)
