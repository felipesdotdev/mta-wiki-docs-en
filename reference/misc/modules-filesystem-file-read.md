---
doc_id: "mta-wiki:13524"
title: "Modules/FileSystem/file/read"
source_title: "Modules/FileSystem/file/read"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/read"
revision_id: 73732
language: "en"
categories: []
generated_at: "2026-07-26T16:16:11.866957+00:00"
---

# Modules/FileSystem/file/read

This function attempts to read the specified amount of bytes from the file. The actual amount of bytes read equals to the length of the Lua string.

## Syntax

```
string file:read ( int readCount )
```

## Arguments

- **readCount:** the amount of bytes to read from the file

## Returns

This function returns a string that contains the bytes that have been read from the file.

## Example

Click to collapse [-]
Client

This snippet returns whether the file that is passed to it looks like a collision file.

```
local function isCollisionFile( file )
    -- Check whether the file is big enough to be a collision file.
    if ( ( file:size() - file:tell() ) <= 8 ) then
        return false;
    end

    -- Read the header checksum from the file.
    local checksum = file:read( 4 );

    -- Check whether the checksum is correct.
    return ( checksum == "COLL" ) or ( checksum == "COL2" ) or ( checksum == "COL3" ) or ( checksum == "COL4" );
end

-- Verify a collision file.
local myColFile = fileOpen( "collisions/fence.col" );
local result = false;

if ( myColFile ) then
    result = isCollisionFile( myColFile );

    myColFile:destroy();
end

outputChatBox( "proper collision of fence model: " .. result );
```

## [FileSystem](mta://reference/misc/modules-filesystem.md) File Functions

- read

- [readByte](mta://reference/misc/modules-filesystem-file-readbyte.md)

- [readUByte](mta://reference/misc/modules-filesystem-file-readubyte.md)

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
