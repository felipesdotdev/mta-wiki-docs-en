---
doc_id: "mta-wiki:13539"
title: "Modules/FileSystem/file/writeInt"
source_title: "Modules/FileSystem/file/writeInt"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/writeInt"
revision_id: 73748
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.163571+00:00"
---

# Modules/FileSystem/file/writeInt

This function attempts to write an integer into a file/stream and returns how many bytes have actually been written. The amount of bytes written should be four.

## Syntax

```
int file:writeInt ( int value )
```

## Arguments

- **value:** a number in the range of [-2147483648..2147483647] to write into the file/stream

## Returns

Returns the amount of bytes written during the write operation. Returns **false** if **value** is not a valid number type.

## Example

todo.

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

- writeInt

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

- [isReadable](mta://reference/misc/modules-filesystem-file-isreadable.md)
