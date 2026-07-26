---
doc_id: "mta-wiki:13512"
title: "Modules/FileSystem/translator/absPath"
source_title: "Modules/FileSystem/translator/absPath"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/absPath"
revision_id: 73772
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.374567+00:00"
---

# Modules/FileSystem/translator/absPath

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

- [relPathRoot](mta://reference/misc/modules-filesystem-translator-relpathroot.md)

- absPath

- [absPathRoot](mta://reference/misc/modules-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/modules-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/modules-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/modules-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/modules-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/modules-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)
