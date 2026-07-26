---
doc_id: "mta-wiki:13505"
title: "Modules/FileSystem/translator/delete"
source_title: "Modules/FileSystem/translator/delete"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/delete"
revision_id: 73765
language: "en"
categories: []
---

# Modules/FileSystem/translator/delete

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

## [FileSystem](mta://reference/misc/modules-filesystem.md) Translator Functions

- [open](mta://reference/misc/modules-filesystem-translator-open.md)

- [exists](mta://reference/misc/modules-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/modules-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/modules-filesystem-translator-chdir.md)

- delete

- [copy](mta://reference/misc/modules-filesystem-translator-copy.md)

- [rename](mta://reference/misc/modules-filesystem-translator-rename.md)

- [size](mta://reference/misc/modules-filesystem-translator-size.md)

- [stat](mta://reference/misc/modules-filesystem-translator-stat.md)

- [relPath](mta://reference/misc/modules-filesystem-translator-relpath.md)

- [relPathRoot](mta://reference/misc/modules-filesystem-translator-relpathroot.md)

- [absPath](mta://reference/misc/modules-filesystem-translator-abspath.md)

- [absPathRoot](mta://reference/misc/modules-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/modules-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/modules-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/modules-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/modules-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/modules-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)
