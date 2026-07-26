---
doc_id: "mta-wiki:13544"
title: "Modules/FileSystem/file/size"
source_title: "Modules/FileSystem/file/size"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/size"
revision_id: 73753
language: "en"
categories: []
---

# Modules/FileSystem/file/size

This function returns the size of a specific file/stream from beginning to end. Not all streams have to support this operation.

## Syntax

```
int file:size ()
```

## Returns

Returns the amount of bytes that this file/stream object is made of.

## Example

Click to collapse [-]
Client

This snippet returns the contents of a file in a string buffer.

```
local function fileGetContents( path )
    -- Prevent a warning being output by checking for file existance first.
    if not ( fileExists( path ) ) then return false; end;

    -- Open the requested file.
    local theFile = fileOpen( path );

    if not ( theFile ) then return false; end;

    -- The the whole content of the file into a string buffer.
    local content = theFile:read( theFile:size() );

    -- Clean up the file handle.
    theFile:destroy();
    return content;
end
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

- size

- [stat](mta://reference/misc/modules-filesystem-file-stat.md)

- [tell](mta://reference/misc/modules-filesystem-file-tell.md)

- [seek](mta://reference/misc/modules-filesystem-file-seek.md)

- [eof](mta://reference/misc/modules-filesystem-file-eof.md)

- [flush](mta://reference/misc/modules-filesystem-file-flush.md)

- [isWritable](mta://reference/misc/modules-filesystem-file-iswritable.md)

- [isReadable](mta://reference/misc/modules-filesystem-file-isreadable.md)
