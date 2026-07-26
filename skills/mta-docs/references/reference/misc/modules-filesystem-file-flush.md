---
doc_id: "mta-wiki:13549"
title: "Modules/FileSystem/file/flush"
source_title: "Modules/FileSystem/file/flush"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/flush"
revision_id: 73758
language: "en"
categories: []
---

# Modules/FileSystem/file/flush

This function writes all temporary buffers of a file/stream object into the output storage. This feature shall be interpreted as a hint, not a necessity. Implementations do not have to support this feature.

## Syntax

```
boolean file:flush ()
```

## Returns

Returns **true** if the file/stream has been successfully flushed, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet writes a text into a file and flushes its buffers, while the file handle is being kept alive as a global. The MTA:Eir FileSystem implementation is encouraged to make sure that the data is written to the harddisk.

```
-- Open a text file to store something into.
local textFile = fileCreate( "my_poem.txt" );

-- Write a nice poem.
textFile:write(
[[Roses are red,
Violets are blue,
Blueberries are sweet,
Cupcakes are too.]]
);

-- At this point, the implementation does not have to write the buffers into the textfile.
-- If delayed, the text file will be empty if opened by an external editor.

-- Make sure the world knows about our poem.
textFile:flush();

-- Now the text-file should be filled with the data. The MTA:Eir FileSystem implementation has
-- support for buffer flushing, so the flush method should always return true if used with raw files.

-- We do not want to loose the grip to our lovely poem, so lets keep it alive, forever. <3
_G.poemFile = textFile;
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

- flush

- [isWritable](mta://reference/misc/modules-filesystem-file-iswritable.md)

- [isReadable](mta://reference/misc/modules-filesystem-file-isreadable.md)
