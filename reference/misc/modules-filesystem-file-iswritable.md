---
doc_id: "mta-wiki:13550"
title: "Modules/FileSystem/file/isWritable"
source_title: "Modules/FileSystem/file/isWritable"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/isWritable"
revision_id: 73759
language: "en"
categories: []
generated_at: "2026-07-26T16:16:11.852209+00:00"
---

# Modules/FileSystem/file/isWritable

This function returns whether a stream is writable. If a stream is not writable, then all write operations should result in nil operations (they will return zero bytes written). This state should be immutable across the lifetime of a file/stream class.

## Syntax

```
boolean file:isWritable ()
```

## Returns

Returns **true** if the file/stream is writable, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet implements a file function that makes sure the file it has been passed to for writing actually supports writing.

```
local function writeHeader( theFile, headerInfo )
    -- Check whether we can write things into the file.
    if not ( theFile:isWritable() ) then
        error( "fatal error: stream is not writable" );
    end

    -- Write a generic header structure.
    theFile:writeUInt( headerInfo.chunkSize );
    theFile:writeFloat( headerInfo.version );
    theFile:writeBoolean( headerInfo.isRaw );
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

- [seek](mta://reference/misc/modules-filesystem-file-seek.md)

- [eof](mta://reference/misc/modules-filesystem-file-eof.md)

- [flush](mta://reference/misc/modules-filesystem-file-flush.md)

- isWritable

- [isReadable](mta://reference/misc/modules-filesystem-file-isreadable.md)
