---
doc_id: "mta-wiki:13493"
title: "Modules/FileSystem/pathToFilename"
source_title: "Modules/FileSystem/pathToFilename"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/pathToFilename"
revision_id: 73789
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.310195+00:00"
---

# Modules/FileSystem/pathToFilename

This function returns the filename and the directory portions of a filepath, separated into two strings.

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

## [FileSystem](mta://reference/misc/modules-filesystem.md) Namespace Functions

- [createTranslator](mta://reference/misc/modules-filesystem-createtranslator.md)

- [createRAMDisk](mta://reference/misc/modules-filesystem-createramdisk.md)

- [createMemoryFile](mta://reference/misc/modules-filesystem-creatememoryfile.md)

- [createFileIterative](mta://reference/misc/modules-filesystem-createfileiterative.md)

- [copyFile](mta://reference/misc/modules-filesystem-copyfile.md)

- [copyStream](mta://reference/misc/modules-filesystem-copystream.md)

- [copyStreamCount](mta://reference/misc/modules-filesystem-copystreamcount.md)

- pathToFilename

- [streamCompare](mta://reference/misc/modules-filesystem-streamcompare.md)

- [topointer](mta://reference/misc/modules-filesystem-topointer.md)

- [type](mta://reference/misc/modules-filesystem-type.md)

- [setDoBufferAllRaw](mta://reference/misc/modules-filesystem-setdobufferallraw.md)

- [getDoBufferAllRaw](mta://reference/misc/modules-filesystem-getdobufferallraw.md)
