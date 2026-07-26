---
doc_id: "mta-wiki:7537"
title: "MTA:Eir/FileSystem/file/tell"
source_title: "MTA:Eir/FileSystem/file/tell"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/file/tell"
revision_id: 73577
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.772877+00:00"
---

# MTA:Eir/FileSystem/file/tell

This function returns the current absolute position inside of the file/stream object. It should be the number of bytes that the current stream pointer is set from the beginning of the object. Not all stream classes have to support this operation.

## Syntax

```
int file:tell ()
```

## Returns

Returns the amount of bytes that this file/stream object has already traversed. If the operation is not supported by the underlying stream class, it returns **false**.

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

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) File Functions

- [read](mta://reference/misc/mta-eir-filesystem-file-read.md)

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

- tell

- [seek](mta://reference/misc/mta-eir-filesystem-file-seek.md)

- [eof](mta://reference/misc/mta-eir-filesystem-file-eof.md)

- [flush](mta://reference/misc/mta-eir-filesystem-file-flush.md)

- [isWritable](mta://reference/misc/mta-eir-filesystem-file-iswritable.md)

- [isReadable](mta://reference/misc/mta-eir-filesystem-file-isreadable.md)
