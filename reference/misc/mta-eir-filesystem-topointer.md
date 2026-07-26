---
doc_id: "mta-wiki:13476"
title: "MTA:Eir/FileSystem/topointer"
source_title: "MTA:Eir/FileSystem/topointer"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/topointer"
revision_id: 73518
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.001303+00:00"
---

# MTA:Eir/FileSystem/topointer

This function returns the light-userdata representation of the object. This is the direct pointer into the Eir FileSystem module handle.

## Syntax

```
light-userdata fsnamespace.topointer( userdata obj )
```

## Arguments

- **obj**: the userdata of the Eir FileSystem Lua environment

## Returns

This function returns the light-userdata value of the internal object, false if not successful.

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

- [streamCompare](mta://reference/misc/mta-eir-filesystem-streamcompare.md)

- topointer

- [type](mta://reference/misc/mta-eir-filesystem-type.md)

- [setDoBufferAllRaw](mta://reference/misc/mta-eir-filesystem-setdobufferallraw.md)

- [getDoBufferAllRaw](mta://reference/misc/mta-eir-filesystem-getdobufferallraw.md)
