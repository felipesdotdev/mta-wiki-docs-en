---
doc_id: "mta-wiki:13514"
title: "Modules/FileSystem/translator/scanDir"
source_title: "Modules/FileSystem/translator/scanDir"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/scanDir"
revision_id: 78580
language: "en"
categories: []
---

# Modules/FileSystem/translator/scanDir

This function loops through all translator filesystem entries that are captured by the wildcard and the directory specifier. The wildcard is glob-style and supports ***** and **?** modifiers. The scan can be made recursive to enter every directory it finds, so that files and folders of a whole directory tree are captured. This function is used to process filesystem objects inside of directories without having to add the filenames into a configuration file. This greatly increases flexibility when processing files. Other than [scanDirEx](mta://reference/misc/mta-eir-filesystem-translator-scandirex.md), this function returns a table of directories and files.

## Syntax

```
table translator:scanDir ( string dirPath, string wildcard, bool recursive )
```

## Arguments

- **dirPath:** a path to the directory the scan shall take place or start in

- **wildcard:** glob-style wild-card for filename matching; every filename that matches the wild-card is returned

- **recursive:** a boolean that specifies whether the whole directory tree at dirPath should be included into the scan

## Returns

This function returns a table consisting of all directories and all matching file entries which were found during the scan. It returns **false** if **dirPath** is an invalid path specifier for the translator.

## Example

Click to collapse [-]
Client

This snippet outputs the count of directories and files in a specified directory relative to the resource instance root.

```
-- Attempt to get a handle to the FileSystem module namespace.
local fsys = createFilesystemInterface();

-- Get a handle to the resource instance directory.
local resRoot = fsys.createTranslator( "mods/deathmatch/resources/" .. getResourceName(resource) .. "/" );

-- Function that returns whether the given path is a directory path.
local function isDirectoryPath( path )
   local lastChar = string.sub( path, #path, #path );

   return ( lastChar == "/" ) or ( lastChar == "\\" );
end

local function getFilesystemObjectCounts( path )
    local fileCount = 0;
    local dirCount = 0;

    -- Get a list of all fs objects.
    local fsObjects =
        resRoot:scanDir(
            path, -- scan anywhere the script wants us to
            "*", -- include all files
            false -- scan the specified directory only
        );

    -- Loop through all object names to set up the counts.
    -- An object can either be a directory or a file.
    for m,n in ipairs(fsObjects) do
        if ( isDirectoryPath( n ) ) then
            dirCount = dirCount + 1;
        else
            fileCount = fileCount + 1;
        end
    end

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

- scanDir

- [scanDirEx](mta://reference/misc/modules-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/modules-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/modules-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/modules-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)
