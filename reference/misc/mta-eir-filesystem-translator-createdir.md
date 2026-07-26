---
doc_id: "mta-wiki:7499"
title: "MTA:Eir/FileSystem/translator/createDir"
source_title: "MTA:Eir/FileSystem/translator/createDir"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/createDir"
revision_id: 73533
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.068925+00:00"
---

# MTA:Eir/FileSystem/translator/createDir

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

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- [open](mta://reference/misc/mta-eir-filesystem-translator-open.md)

- [exists](mta://reference/misc/mta-eir-filesystem-translator-exists.md)

- createDir

- [chdir](mta://reference/misc/mta-eir-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/mta-eir-filesystem-translator-delete.md)

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
