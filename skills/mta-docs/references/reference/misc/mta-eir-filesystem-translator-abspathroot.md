---
doc_id: "mta-wiki:7509"
title: "MTA:Eir/FileSystem/translator/absPathRoot"
source_title: "MTA:Eir/FileSystem/translator/absPathRoot"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/absPathRoot"
revision_id: 73545
language: "en"
categories: []
---

# MTA:Eir/FileSystem/translator/absPathRoot

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

- [absPath](mta://reference/misc/mta-eir-filesystem-translator-abspath.md)

- absPathRoot

- [scanDir](mta://reference/misc/mta-eir-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/mta-eir-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/mta-eir-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/mta-eir-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)
