---
doc_id: "mta-wiki:13474"
title: "MTA:Eir/FileSystem/pathToFilename"
source_title: "MTA:Eir/FileSystem/pathToFilename"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/pathToFilename"
revision_id: 73515
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.959445+00:00"
---

# MTA:Eir/FileSystem/pathToFilename

This function returns the filename and the direction portions of a filepath, seperated into two strings.

## Syntax

```
string, string fsnamespace.pathToFilename( string path, bool includeExtention )
```

## Arguments

- **path**: the file path to extract from

- **includeExtention**: if true then the filename extention is included in the result

## Returns

This function returns the filename and directory of the provided file path.

## Example

```
-- TODO
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Namespace Functions

- [createTranslator](mta://reference/misc/mta-eir-filesystem-createtranslator.md)

- [createRAMDisk](mta://reference/misc/mta-eir-filesystem-createramdisk.md)

- [createMemoryFile](mta://reference/misc/mta-eir-filesystem-creatememoryfile.md)

- [createFileIterative](mta://reference/misc/mta-eir-filesystem-createfileiterative.md)

- [createArchiveTranslator](mta://reference/misc/mta-eir-filesystem-createarchivetranslator.md) (not module)

- [createZIPArchive](mta://reference/misc/mta-eir-filesystem-createziparchive.md) (not module)

- [copyFile](mta://reference/misc/mta-eir-filesystem-copyfile.md)

- [copyStream](mta://reference/misc/mta-eir-filesystem-copystream.md)

- [copyStreamCount](mta://reference/misc/mta-eir-filesystem-copystreamcount.md)

- pathToFilename

- [streamCompare](mta://reference/misc/mta-eir-filesystem-streamcompare.md)

- [topointer](mta://reference/misc/mta-eir-filesystem-topointer.md)

- [type](mta://reference/misc/mta-eir-filesystem-type.md)

- [setDoBufferAllRaw](mta://reference/misc/mta-eir-filesystem-setdobufferallraw.md)

- [getDoBufferAllRaw](mta://reference/misc/mta-eir-filesystem-getdobufferallraw.md)

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

- [isReadable](mta://reference/misc/mta-eir-filesystem-file-isreadable.md)
