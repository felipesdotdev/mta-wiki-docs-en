---
doc_id: "mta-wiki:13547"
title: "Modules/FileSystem/file/seek"
source_title: "Modules/FileSystem/file/seek"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/seek"
revision_id: 73756
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.036996+00:00"
---

# Modules/FileSystem/file/seek

This function changes the location of the current stream pointer. Like that you can skip file sections, set the stream pointer to a specific location or head to the end of the file/stream object. Not all stream classes have to support this operation.

## Syntax

```
int file:seek ( int offset, string mode )
```

## Arguments

- **offset:** the amount of bytes that should be used for the seeking operation

- **mode:** a specifier that describes where the offset should start at; can be **set** (beginning of file), **cur** (current stream offset) or **end** (end of file/stream)

## Returns

Returns 0 if the operation was successful, otherwise a non-zero value describing an error. If the operation is not supported by the underlying stream class, it returns **false**.

## Example

Click to collapse [-]
Client

This snippet seeks back to the beginning of the file by going back the current stream pointer byte offset.

```
local function alternativeFileReset( theFile )
    -- Get the current stream position.
    local streamOffset = theFile:tell();

    -- Check whether this operation is supported.
    if not ( streamOffset ) then
        return false, "not supported";
    end

    -- Reset the file to its beginning.
    theFile:seek( -streamOffset, "cur" );
    return true;
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

- [size](mta://reference/misc/modules-filesystem-file-size.md)

- [stat](mta://reference/misc/modules-filesystem-file-stat.md)

- [tell](mta://reference/misc/modules-filesystem-file-tell.md)

- seek

- [eof](mta://reference/misc/modules-filesystem-file-eof.md)

- [flush](mta://reference/misc/modules-filesystem-file-flush.md)

- [isWritable](mta://reference/misc/modules-filesystem-file-iswritable.md)

- [isReadable](mta://reference/misc/modules-filesystem-file-isreadable.md)
