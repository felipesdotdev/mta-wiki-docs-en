---
doc_id: "mta-wiki:13548"
title: "Modules/FileSystem/file/eof"
source_title: "Modules/FileSystem/file/eof"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/eof"
revision_id: 73757
language: "en"
categories: []
generated_at: "2026-07-26T16:16:11.786092+00:00"
---

# Modules/FileSystem/file/eof

This function returns whether the runtime can still read data from the file/stream. This is an implementation defined state that should return false if no data can be immediately received using **read operations**. Asynchronous file/stream objects could use this function to return true when new data is available to receive from the socket. If wanting to read an entire file/stream object, this function is more reliable than the [file.size](mta://reference/misc/mta-eir-filesystem-file-size.md) approach.

## Syntax

```
boolean file:eof ()
```

## Returns

Returns true if data is available to be read from the file/stream object. Return **false** if data is not immediately available to receive from it.

## Example

Click to collapse [-]
Client

This snippet is guaranteed to read an entire file/stream object.

```
local fileGetContentSafe( theFile )
    -- Allocate a string buffer where all information is saved in.
    local buffer = "";

    -- Read from the stream until it cannot anymore.
    while not ( theFile:eof() ) do
        buffer = buffer .. theFile:read( 1024 );
    end

    -- At this point, some implementations could wait for data.
    -- Implementations are advised to use blocking I/O, implement additional Lua functions or throw exceptions.

    -- Clean up the file/stream handle and return the result buffer.
    theFile:destroy();
    return buffer;
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

- eof

- [flush](mta://reference/misc/modules-filesystem-file-flush.md)

- [isWritable](mta://reference/misc/modules-filesystem-file-iswritable.md)

- [isReadable](mta://reference/misc/modules-filesystem-file-isreadable.md)
