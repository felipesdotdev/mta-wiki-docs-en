---
doc_id: "mta-wiki:7516"
title: "MTA:Eir/FileSystem/file/read"
source_title: "MTA:Eir/FileSystem/file/read"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/file/read"
revision_id: 73554
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.604650+00:00"
---

# MTA:Eir/FileSystem/file/read

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

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- [open](mta://reference/misc/mta-eir-filesystem-translator-open.md)

- [exists](mta://reference/misc/mta-eir-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/mta-eir-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/mta-eir-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/mta-eir-filesystem-translator-delete.md)

- [copy](mta://reference/misc/mta-eir-filesystem-translator-copy.md)

- [rename](mta://reference/misc/mta-eir-filesystem-translator-rename.md)

- [size](mta://reference/misc/mta-eir-filesystem-translator-size.md)

- [stat](mta://reference/misc/mta-eir-filesystem-translator-stat.md)

- [relPath](mta://reference/misc/mta-eir-filesystem-translator-relpath.md)

- [relPathRoot](mta://reference/misc/mta-eir-filesystem-translator-relpathroot.md)

- [absPath](mta://reference/misc/mta-eir-filesystem-translator-abspath.md)

- [absPathRoot](mta://reference/misc/mta-eir-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/mta-eir-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/mta-eir-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/mta-eir-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/mta-eir-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) File Functions

- read

- [readByte](mta://reference/misc/mta-eir-filesystem-file-readbyte.md)

- [readUByte](mta://reference/misc/mta-eir-filesystem-file-readubyte.md)

- [readShort](mta://reference/misc/mta-eir-filesystem-file-readshort.md)

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
