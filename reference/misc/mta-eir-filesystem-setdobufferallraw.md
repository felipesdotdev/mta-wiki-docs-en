---
doc_id: "mta-wiki:13478"
title: "MTA:Eir/FileSystem/setDoBufferAllRaw"
source_title: "MTA:Eir/FileSystem/setDoBufferAllRaw"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/setDoBufferAllRaw"
revision_id: 73521
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.971428+00:00"
---

# MTA:Eir/FileSystem/setDoBufferAllRaw

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

- [type](mta://reference/misc/mta-eir-filesystem-type.md)

- setDoBufferAllRaw

- [getDoBufferAllRaw](mta://reference/misc/mta-eir-filesystem-getdobufferallraw.md)
