---
doc_id: "mta-wiki:7539"
title: "MTA:Eir/FileSystem/file/eof"
source_title: "MTA:Eir/FileSystem/file/eof"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/file/eof"
revision_id: 73579
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.541372+00:00"
---

# MTA:Eir/FileSystem/file/eof

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

- eof

- [flush](mta://reference/misc/mta-eir-filesystem-file-flush.md)

- [isWritable](mta://reference/misc/mta-eir-filesystem-file-iswritable.md)

- [isReadable](mta://reference/misc/mta-eir-filesystem-file-isreadable.md)
