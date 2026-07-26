---
doc_id: "mta-wiki:13495"
title: "Modules/FileSystem/topointer"
source_title: "Modules/FileSystem/topointer"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/topointer"
revision_id: 73791
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.360229+00:00"
---

# Modules/FileSystem/topointer

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

## [FileSystem](mta://reference/misc/modules-filesystem.md) Namespace Functions

- [createTranslator](mta://reference/misc/modules-filesystem-createtranslator.md)

- [createRAMDisk](mta://reference/misc/modules-filesystem-createramdisk.md)

- [createMemoryFile](mta://reference/misc/modules-filesystem-creatememoryfile.md)

- [createFileIterative](mta://reference/misc/modules-filesystem-createfileiterative.md)

- [copyFile](mta://reference/misc/modules-filesystem-copyfile.md)

- [copyStream](mta://reference/misc/modules-filesystem-copystream.md)

- [copyStreamCount](mta://reference/misc/modules-filesystem-copystreamcount.md)

- [pathToFilename](mta://reference/misc/modules-filesystem-pathtofilename.md)

- [streamCompare](mta://reference/misc/modules-filesystem-streamcompare.md)

- topointer

- [type](mta://reference/misc/modules-filesystem-type.md)

- [setDoBufferAllRaw](mta://reference/misc/modules-filesystem-setdobufferallraw.md)

- [getDoBufferAllRaw](mta://reference/misc/modules-filesystem-getdobufferallraw.md)
