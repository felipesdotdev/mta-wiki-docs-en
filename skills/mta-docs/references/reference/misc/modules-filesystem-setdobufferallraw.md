---
doc_id: "mta-wiki:13497"
title: "Modules/FileSystem/setDoBufferAllRaw"
source_title: "Modules/FileSystem/setDoBufferAllRaw"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/setDoBufferAllRaw"
revision_id: 73793
language: "en"
categories: []
---

# Modules/FileSystem/setDoBufferAllRaw

This function changes the raw-file buffering policy of newly created file streams. If the buffering-policy is enabled then each newly created file stream is wrapped inside of a custom FileSystem buffering handle. File stream modifications that are close to each other are batched together for optimizational purposes.

## Syntax

```
void fsnamespace.setDoBufferAllRaw( bool enabled )
```

## Arguments

- **enabled**: new value for the buffering-policy

## Returns

This function does return nil.

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

- [topointer](mta://reference/misc/modules-filesystem-topointer.md)

- [type](mta://reference/misc/modules-filesystem-type.md)

- setDoBufferAllRaw

- [getDoBufferAllRaw](mta://reference/misc/modules-filesystem-getdobufferallraw.md)
