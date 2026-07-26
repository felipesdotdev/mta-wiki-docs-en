---
doc_id: "mta-wiki:13492"
title: "Modules/FileSystem/copyStreamCount"
source_title: "Modules/FileSystem/copyStreamCount"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/copyStreamCount"
revision_id: 73788
language: "en"
categories: []
---

# Modules/FileSystem/copyStreamCount

This function copies data starting from a source file stream into a specified destination stream. The copy of data is performed starting from the source file seek. The copy is only performed up to a specified count of bytes.

Read operations on the file streams advance the seek pointers. Thus the seek pointers stay changed after the function has completed.

## Syntax

```
bool fsnamespace.copyStreamCount( file src, file dst, int count )
```

## Arguments

- **src**: source of the copy operation, starting from the seek pointer

- **dst**: target of the copy operation, starting from the seek pointer

- **count**: the amount of bytes to copy (has to be above 0)

## Returns

This function returns true if the copy operation has completed successfully, false otherwise.

## Example

```
-- TODO
```

## [FileSystem](mta://reference/misc/modules-filesystem.md) Namespace Functions

- [createTranslator](mta://reference/misc/modules-filesystem-createtranslator.md)

- [createRAMDisk](mta://reference/misc/modules-filesystem-createramdisk.md)

- [createMemoryFile](mta://reference/misc/modules-filesystem-creatememoryfile.md)

- [createFileIterative](mta://reference/misc/modules-filesystem-createfileiterative.md)

- [copyFile](mta://reference/misc/modules-filesystem-copyfile.md)

- [copyStream](mta://reference/misc/modules-filesystem-copystream.md)

- copyStreamCount

- [pathToFilename](mta://reference/misc/modules-filesystem-pathtofilename.md)

- [streamCompare](mta://reference/misc/modules-filesystem-streamcompare.md)

- [topointer](mta://reference/misc/modules-filesystem-topointer.md)

- [type](mta://reference/misc/modules-filesystem-type.md)

- [setDoBufferAllRaw](mta://reference/misc/modules-filesystem-setdobufferallraw.md)

- [getDoBufferAllRaw](mta://reference/misc/modules-filesystem-getdobufferallraw.md)

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

- [isReadable](mta://reference/misc/modules-filesystem-file-isreadable.md)
