---
doc_id: "mta-wiki:13551"
title: "Modules/FileSystem/file/isReadable"
source_title: "Modules/FileSystem/file/isReadable"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/isReadable"
revision_id: 73760
language: "en"
categories: []
generated_at: "2026-07-26T16:16:11.834124+00:00"
---

# Modules/FileSystem/file/isReadable

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

- [isWritable](mta://reference/misc/modules-filesystem-file-iswritable.md)

- isReadable
