---
doc_id: "mta-wiki:7508"
title: "MTA:Eir/FileSystem/translator/absPath"
source_title: "MTA:Eir/FileSystem/translator/absPath"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/absPath"
revision_id: 73591
language: "en"
categories: []
---

# MTA:Eir/FileSystem/translator/absPath

This function resolves a specified path into its absolute version. This function can be used to get a unique version of a path (without scripting symbols such as '..').

## Syntax

```
string translator:absPath ( string path )
```

## Arguments

- **path:** the path that should be resolved into an absolute path; can be nil to return the absolute location of the current directory.

## Returns

This function returns the absolute version of the path that is passed to it, **false** if the specified path is not accessible by the translator.

## Example

Click to collapse [-]
Client

This snippet prints the absolute location of the shared client-side resource folder.

```
-- Get the absolute path to our resource.
local absResourceLocation = fileCreateTranslator( "/" ):absPath();

-- Print it out to the user.
outputChatBox( "running resource from: " .. absResourceLocation );
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

- [relPathRoot](mta://reference/misc/mta-eir-filesystem-translator-relpathroot.md)

- absPath

- [absPathRoot](mta://reference/misc/mta-eir-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/mta-eir-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/mta-eir-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/mta-eir-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/mta-eir-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)
