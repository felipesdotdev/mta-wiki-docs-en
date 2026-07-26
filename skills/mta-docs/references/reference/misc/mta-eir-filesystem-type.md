---
doc_id: "mta-wiki:13477"
title: "MTA:Eir/FileSystem/type"
source_title: "MTA:Eir/FileSystem/type"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/type"
revision_id: 73589
language: "en"
categories: []
---

# MTA:Eir/FileSystem/type

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

- [topointer](mta://reference/misc/mta-eir-filesystem-topointer.md)

- type

- [setDoBufferAllRaw](mta://reference/misc/mta-eir-filesystem-setdobufferallraw.md)

- [getDoBufferAllRaw](mta://reference/misc/mta-eir-filesystem-getdobufferallraw.md)
