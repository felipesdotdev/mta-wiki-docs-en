---
doc_id: "mta-wiki:7542"
title: "MTA:Eir/FileSystem/file/isReadable"
source_title: "MTA:Eir/FileSystem/file/isReadable"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/file/isReadable"
revision_id: 73582
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.575311+00:00"
---

# MTA:Eir/FileSystem/file/isReadable

This function returns whether a stream is readable. If a stream is not readable, then all read operations should result in nil operations (they will return zero bytes read or false if value reading). This state should be immutable across the lifetime of a file/stream class.

## Syntax

```
boolean file:isReadable ()
```

## Returns

Returns **true** if the file/stream is readable, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet is the counterpart of the [file.isWritable](mta://reference/misc/mta-eir-filesystem-file-iswritable.md) example. It attempts to read the header from the file, but throws an exception if it cannot be read from.

```
local function readHeader( theFile )
    -- Check whether we can read anything from the file.
    if not ( theFile:isReadable() ) then
        error( "fatal error: file cannot be read from" );
    end

    -- Read the generic header back into the engine.
    local headerInfo = {
        chunkSize = theFile:readUInt(),
        version = theFile:readFloat(),
        isRaw = theFile:readBoolean()
    };

    -- Return the header information.
    return headerInfo;
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

- [isWritable](mta://reference/misc/mta-eir-filesystem-file-iswritable.md)

- isReadable
