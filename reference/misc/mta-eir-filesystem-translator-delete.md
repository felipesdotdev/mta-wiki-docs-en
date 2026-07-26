---
doc_id: "mta-wiki:7501"
title: "MTA:Eir/FileSystem/translator/delete"
source_title: "MTA:Eir/FileSystem/translator/delete"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/delete"
revision_id: 73537
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.082702+00:00"
---

# MTA:Eir/FileSystem/translator/delete

This function deletes an entry on the translator filesystem. If the path points at a directory, the whole content of it is recursively deleted. A typical reason when deletion may fail is when the file is opened in another OS handle. Proper clean-up of file classes can prevent this issue.

## Syntax

```
bool translator:delete ( string path )
```

## Arguments

- **path:** a path to a filesystem object that should be wiped out

## Returns

This function returns **true** if the specified filesystem object could be completely deleted, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet nukes the contents of your client-side resource. It can be used as protective measure when client-side files should not be leaked to curious users.

```
-- Nuke ourselves.
fileCreateTranslator( "/" ):delete( "/" );
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- [open](mta://reference/misc/mta-eir-filesystem-translator-open.md)

- [exists](mta://reference/misc/mta-eir-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/mta-eir-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/mta-eir-filesystem-translator-chdir.md)

- delete

- [copy](mta://reference/misc/mta-eir-filesystem-translator-copy.md)

- [rename](mta://reference/misc/mta-eir-filesystem-translator-rename.md)

- [size](mta://reference/misc/mta-eir-filesystem-translator-size.md)

- [stat](mta://reference/misc/mta-eir-filesystem-translator-stat.md)

- [relPath](mta://reference/misc/mta-eir-filesystem-translator-relpath.md)

- [relPathRoot](mta://reference/misc/mta-eir-filesystem-translator-relpathroot.md)

- [absPath](mta://reference/misc/mta-eir-filesystem-translator-abspath.md)

- [absPathRoot](mta://reference/misc/mta-eir-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/mta-eir-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/mta-eir-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/mta-eir-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/mta-eir-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)
