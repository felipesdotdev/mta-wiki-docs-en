---
doc_id: "mta-wiki:13508"
title: "Modules/FileSystem/translator/size"
source_title: "Modules/FileSystem/translator/size"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/size"
revision_id: 73768
language: "en"
categories: []
---

# Modules/FileSystem/translator/size

This function queries the size of a filesystem object. The size of a filesystem object is the count of bytes that it logically fills on the storage media.

## Syntax

```
int translator:size ( string filePath )
```

## Arguments

- **filePath:** the path to the filesystem object that you want to get the size of

## Returns

This function returns the count of bytes that the filesystem object is logically taking on the storage medium, **false** if **filePath** is not a valid path in the translator or the filesystem object pointed at by it is not accessible.

## Example

Click to collapse [-]
Client

This snippet calculates the size of a resource and prints it to the debug console.

```
-- Get the handle to the resource instance directory.
local resRoot = fileCreateTranslator( "/" );

-- Calculate the size of every file in it.
local fileSizeCount = 0;

local function fileIteratorSum( filePath )
    fileSizeCount = fileSizeCount + resRoot:size( filePath );
end

-- Iterate through the entire directory tree, including the sub-directories.
resRoot:scanDirEx( "/", "*", nil, fileIteratorSum, true );

-- Output the size to the console.
outputDebugString( "resource size: " .. fileSizeCount );
```

## [FileSystem](mta://reference/misc/modules-filesystem.md) Translator Functions

- [open](mta://reference/misc/modules-filesystem-translator-open.md)

- [exists](mta://reference/misc/modules-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/modules-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/modules-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/modules-filesystem-translator-delete.md)

- [copy](mta://reference/misc/modules-filesystem-translator-copy.md)

- [rename](mta://reference/misc/modules-filesystem-translator-rename.md)

- size

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
