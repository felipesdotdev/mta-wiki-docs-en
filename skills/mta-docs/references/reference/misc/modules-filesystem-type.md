---
doc_id: "mta-wiki:13496"
title: "Modules/FileSystem/type"
source_title: "Modules/FileSystem/type"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/type"
revision_id: 73792
language: "en"
categories: []
---

# Modules/FileSystem/type

This function returns the type of the given Eir FileSystem object.

## Syntax

```
string fsnamespace.type( userdata obj )
```

## Arguments

- **obj**: the Eir FileSystem object to retrieve the type from

## Returns

This function returns the type string of the queried object, false if not successful. For destroyed objects the return value is always false.

### Possible Return Values

- file

- file-translator

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

- type

- [setDoBufferAllRaw](mta://reference/misc/modules-filesystem-setdobufferallraw.md)

- [getDoBufferAllRaw](mta://reference/misc/modules-filesystem-getdobufferallraw.md)
