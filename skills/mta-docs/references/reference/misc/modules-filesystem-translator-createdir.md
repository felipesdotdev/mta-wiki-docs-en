---
doc_id: "mta-wiki:13503"
title: "Modules/FileSystem/translator/createDir"
source_title: "Modules/FileSystem/translator/createDir"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/createDir"
revision_id: 73763
language: "en"
categories: []
---

# Modules/FileSystem/translator/createDir

This function creates a directory inside of a translator directory hierarchy.

## Syntax

```
bool translator:createDir ( string dirPath )
```

## Arguments

- **dirPath:** a path to a directory that should be created

## Returns

This function returns **true** if the given path is a valid directory path relative to the translator, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet creates a folder hierarchy.

```
-- Create a generic resource root translator
local resRoot = fileCreateTranslator( "/" );

-- Create some folders.
resRoot:createDir( "theDirectory/" ); -- successfully creates "theDirectory" folder
resRoot:createDir( "secondDirectory" ); -- fails to create "secondDirectory" as intended, because it is not a valid dirPath
resRoot:createDir( "thirdDirectory/fourthDirectory/documents/" ); -- successfully creates three directories at a time
resRoot:createDir( "../hax/" ); -- fails to create "hax" directory, because the path is not relative to the translator anymore
```

## [FileSystem](mta://reference/misc/modules-filesystem.md) Translator Functions

- [open](mta://reference/misc/modules-filesystem-translator-open.md)

- [exists](mta://reference/misc/modules-filesystem-translator-exists.md)

- createDir

- [chdir](mta://reference/misc/modules-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/modules-filesystem-translator-delete.md)

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
