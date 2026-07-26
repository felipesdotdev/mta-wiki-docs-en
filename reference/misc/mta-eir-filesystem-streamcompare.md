---
doc_id: "mta-wiki:13475"
title: "MTA:Eir/FileSystem/streamCompare"
source_title: "MTA:Eir/FileSystem/streamCompare"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/streamCompare"
revision_id: 73516
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.989079+00:00"
---

# MTA:Eir/FileSystem/streamCompare

This function compares the bytes of two streams for equality. The comparison starts from the current file seek and finishes at the end of the respective file stream. If the read count of either stream does not match the other, then this function fails.

## Syntax

```
bool fsnamespace.streamCompare( file left, file right )
```

## Arguments

- **left**: first file for equality comparison

- **right**: second file for equality comparison

## Returns

This function returns true if the data stream was equal, false otherwise.

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

- [pathToFilename](mta://reference/misc/mta-eir-filesystem-pathtofilename.md)

- streamCompare

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
