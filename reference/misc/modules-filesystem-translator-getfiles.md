---
doc_id: "mta-wiki:13517"
title: "Modules/FileSystem/translator/getFiles"
source_title: "Modules/FileSystem/translator/getFiles"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/getFiles"
revision_id: 73777
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.519593+00:00"
---

# Modules/FileSystem/translator/getFiles

This function returns a list of all files that are found under the wild-card and directory parameters. It is similar to [scanDir](mta://reference/misc/mta-eir-filesystem-translator-scandir.md) but returns files only.

## Syntax

```
table translator:getFiles ( string dirPath, string wildcard, bool recursive )
```

## Arguments

- **dirPath:** a path to the directory the scan shall take place or start in

- **wildcard:** glob-style wild-card for filename matching; every filename that matches the wild-card is returned

- **recursive:** a boolean that specifies whether the whole directory tree at dirPath should be included into the scan

## Returns

This function returns a table of all matching file entries for the performed scan. It returns **false** if **dirPath** is not a valid directory target for the translator.

## Example

Click to collapse [-]
Client

This snippet is yet another alternative to output the count of directories and files in a folder.

```
-- Get a handle to the resource instance directory.
local resRoot = fileCreateTranslator( "/" );

local function getFilesystemObjectCounts( path )
    local fileCount = 0;
    local dirCount = 0;

    -- Query the counts.
    fileCount = #resRoot:getFiles( path, "*", false );
    dirCount = #resRoot:getDirs( path, false );

    -- Return the counts.
    return fileCount, dirCount;
end

-- Output the filesystem object counts for the resource instance root.
local fileCount, dirCount = getFilesystemObjectCounts( "/" );

outputChatBox( "found " .. fileCount .. " files and " .. dirCount .. " directories in the resource folder root." );
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

- [absPathRoot](mta://reference/misc/modules-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/modules-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/modules-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/modules-filesystem-translator-getdirs.md)

- getFiles

- [setOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/modules-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)
