---
doc_id: "mta-wiki:7541"
title: "MTA:Eir/FileSystem/file/isWritable"
source_title: "MTA:Eir/FileSystem/file/isWritable"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/file/isWritable"
revision_id: 73581
language: "en"
categories: []
---

# MTA:Eir/FileSystem/file/isWritable

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

- [tell](mta://reference/misc/mta-eir-filesystem-file-tell.md)

- [seek](mta://reference/misc/mta-eir-filesystem-file-seek.md)

- [eof](mta://reference/misc/mta-eir-filesystem-file-eof.md)

- [flush](mta://reference/misc/mta-eir-filesystem-file-flush.md)

- isWritable

- [isReadable](mta://reference/misc/mta-eir-filesystem-file-isreadable.md)
