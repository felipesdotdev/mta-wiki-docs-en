---
doc_id: "mta-wiki:7512"
title: "MTA:Eir/FileSystem/translator/scanDirEx"
source_title: "MTA:Eir/FileSystem/translator/scanDirEx"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/scanDirEx"
revision_id: 73547
language: "en"
categories: []
---

# MTA:Eir/FileSystem/translator/scanDirEx

This function loops through all translator filesystem entries that are captured by the wildcard and the directory specifier. The wildcard is glob-style and supports ***** and **?** modifiers. The scan can be made recursive to enter every directory it finds, so that files and folders of a whole directory tree are captured. This function is used to process filesystem objects inside of directories without having to add the filenames into a configuration file. This greatly increases flexibility when processing files. This function is more flexible than [scanDir](mta://reference/misc/mta-eir-filesystem-translator-scandir.md) as it triggers callbacks directly when either files or directories are found, making a distinction between files and directories very easy.

## Syntax

```
bool translator:scanDirEx ( string dirPath, string wildcard, function dirCallback, function fileCallback, bool recursive )
```

## Arguments

- **dirPath:** a path to the directory the scan shall take place or start in

- **wildcard:** glob-style wild-card for filename matching; every filename that matches the wild-card is returned

- **dirCallback:** the function callback that should trigger for every directory found (can be nil); the absolute path of the directory is passed to it

- **fileCallback:** the directory callback that should trigger for every file found (can be nil); the absolute path of the file is passed to it

- **recursive:** a boolean that specifies whether the whole directory tree at dirPath should be included into the scan

## Returns

This function performs a scan of all filesystem objects captured inside of the **dirPath** folder using the **wild-card** glob-style pattern. It returns **false** if **dirPath** is an invalid path specifier for the translator.

## Example

Click to collapse [-]
Client

This snippet outputs the count of directories and files in a specified directory relative to the resource instance root. This is an alternative to the **scanDir** way.

```
-- Get a handle to the resource instance directory.
local resRoot = fileCreateTranslator( "/" );

local function getFilesystemObjectCounts( path )
    local fileCount = 0;
    local dirCount = 0;

    -- Create iterator closures that are triggered for each file and directory
    local function fileIterator( filePath )
        -- filePath is always an absolute path.
        fileCount = fileCount + 1;
    end

    local function dirIterator( dirPath )
        -- filePath is always an absolute path.
        dirCount = dirCount + 1;
    end

    -- Get a list of all fs objects.
    local fsObjects =
        resRoot:scanDirEx(
            path, -- scan anywhere the script wants us to
            "*", -- include all files
            dirIterator, -- pass the callbacks to the routine
            fileIterator,
            false -- scan the specified directory only
        );

    -- We do not need to loop anymore.

    -- Return the counts.
    return fileCount, dirCount;
end

-- Output the filesystem object counts for the resource instance root.
local fileCount, dirCount = getFilesystemObjectCounts( "/" );

outputChatBox( "found " .. fileCount .. " files and " .. dirCount .. " directories in the resource folder root." );
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

- [absPathRoot](mta://reference/misc/mta-eir-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/mta-eir-filesystem-translator-scandir.md)

- scanDirEx

- [getDirs](mta://reference/misc/mta-eir-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/mta-eir-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)
