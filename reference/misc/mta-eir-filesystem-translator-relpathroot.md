---
doc_id: "mta-wiki:7507"
title: "MTA:Eir/FileSystem/translator/relPathRoot"
source_title: "MTA:Eir/FileSystem/translator/relPathRoot"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/relPathRoot"
revision_id: 73543
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.205535+00:00"
---

# MTA:Eir/FileSystem/translator/relPathRoot

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

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- [open](mta://reference/misc/mta-eir-filesystem-translator-open.md)

- [exists](mta://reference/misc/mta-eir-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/mta-eir-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/mta-eir-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/mta-eir-filesystem-translator-delete.md)

- [copy](mta://reference/misc/mta-eir-filesystem-translator-copy.md)

- [rename](mta://reference/misc/mta-eir-filesystem-translator-rename.md)

- [size](mta://reference/misc/mta-eir-filesystem-translator-size.md)

- [stat](mta://reference/misc/mta-eir-filesystem-translator-stat.md)

- [relPath](mta://reference/misc/mta-eir-filesystem-translator-relpath.md)

- relPathRoot

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
