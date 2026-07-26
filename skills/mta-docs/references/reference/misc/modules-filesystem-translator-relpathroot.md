---
doc_id: "mta-wiki:13511"
title: "Modules/FileSystem/translator/relPathRoot"
source_title: "Modules/FileSystem/translator/relPathRoot"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/relPathRoot"
revision_id: 73771
language: "en"
categories: []
---

# Modules/FileSystem/translator/relPathRoot

This function transform a path that is passed to it into a path that is relative to the translators root directory. The path must be accessible from the translator. The path can either be absolute or relative.

## Syntax

```
string translator:relPathRoot ( string path )
```

## Arguments

- **path:** the path that should be transformed into a relative path; can be nil to return the **null path**

## Returns

This function returns the relative version of the path that is passed to it, **false** if the specified path is not accessible by the translator.

## Example

Click to collapse [-]
Client

This snippet returns the relative-to-root version of a translator relative path.

```
-- Create a generic file translator to the resource instance directory.
local resRoot = fileCreateTranslator( "/" );

-- Change into another directory.
resRoot:createDir( "myDir/" );
resRoot:chdir( "myDir/" );

-- Output the path relative to the current directory and relative to the translator root directory.
local thePath = "someDir/../myFile.txt";
local relativeToCurrent = resRoot:relPath( thePath );
local relativeToRoot = resRoot:relPathRoot( thePath );

outputChatBox( "input-path: " .. thePath );
outputChatBox( "relative-to-current: " .. relativeToCurrent );
outputChatBox( "relative-to-root: " .. relativeToRoot );
```

## [FileSystem](mta://reference/misc/modules-filesystem.md) Translator Functions

- [open](mta://reference/misc/modules-filesystem-translator-open.md)

- [exists](mta://reference/misc/modules-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/modules-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/modules-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/modules-filesystem-translator-delete.md)

- [copy](mta://reference/misc/modules-filesystem-translator-copy.md)

- [rename](mta://reference/misc/modules-filesystem-translator-rename.md)

- [size](mta://reference/misc/modules-filesystem-translator-size.md)

- [stat](mta://reference/misc/modules-filesystem-translator-stat.md)

- [relPath](mta://reference/misc/modules-filesystem-translator-relpath.md)

- relPathRoot

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
