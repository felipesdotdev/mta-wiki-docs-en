---
doc_id: "mta-wiki:13513"
title: "Modules/FileSystem/translator/absPathRoot"
source_title: "Modules/FileSystem/translator/absPathRoot"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/absPathRoot"
revision_id: 73773
language: "en"
categories: []
---

# Modules/FileSystem/translator/absPathRoot

This function resolves a specified path into its absolute version. The path is resolved from the translator root. This function can be used to get a unique version of a path (without scripting symbols such as '..').

## Syntax

```
string translator:absPathRoot ( string path )
```

## Arguments

- **path:** the path that should be resolved into an absolute path; can be nil to return the absolute location of the translator (on host filesystems such as NTFS or ext3)

## Returns

This function returns the absolute version of the path that is passed to it, **false** if the specified path is not accessible by the translator.

## Example

Click to collapse [-]
Client

This snippet checks whether the path given to it is valid for the resource.

```
-- Get a handle to the resource instance directory.
local resRoot = fileCreateTranslator( "/" );

-- Create our utility function.
local function isPathValidForResource( path )
    return not ( resRoot:absPathRoot( path ) == false );
end

-- Is the path inside of/valid for our resource? Should return false.
local myPathValidity = isPathValidForResource( "C:/Windows/System32/" );

outputChatBox( "the windows system directory is " .. ( myPathValidity and "" or "not " ) .. "valid." );
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

- [absPath](mta://reference/misc/modules-filesystem-translator-abspath.md)

- absPathRoot

- [scanDir](mta://reference/misc/modules-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/modules-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/modules-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/modules-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/modules-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)
