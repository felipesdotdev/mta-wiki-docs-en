---
doc_id: "mta-wiki:13487"
title: "Modules/FileSystem/createTranslator"
source_title: "Modules/FileSystem/createTranslator"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/createTranslator"
revision_id: 73845
language: "en"
categories: []
generated_at: "2026-07-26T16:16:11.765342+00:00"
---

# Modules/FileSystem/createTranslator

This function creates a FileSystem translator. A FileSystem translator represents a directory on a real or virtual filesystem. Through translators you get access to the files that reside in their directory trees. The translator returned by this function usually represents an OS filesystem directory.

## Syntax

```
translator fsnamespace.createTranslator( string rootPath )
```

## Arguments

- **rootPath:** the absolute path to the directory that you want access to.

## Returns

This function returns the **FileSystem translator** that grants access to files in the requested directory.

## Example

Click to collapse [-]
Server

This snippet links all directories inside of your resource instance folder using translators and lists them in a dictionary under their name.

```
-- Dictionary that will contain all directory links of our resource.
local dirs = {};

-- Get a handle to the FileSystem module namespace.
local fsys = createFilesystemInterface();

-- Make sure we could obtain the module namespace.
if not ( fsys ) then
    outputDebugString( "could not obtain FileSystem module namespace" );
    return false;
end

-- Create a translator to the resource root.
local resRoot = fsys.createTranslator( "mods/deathmatch/resources/" .. getResourceName(resource) .. "/" );

local function dirIterator( dirPath )
    -- get the simple name of this directory.
    -- the simple name is the path relative to resRoot without the '/'
    local simpleName = resRoot.relPathRoot( dirPath );
    simpleName = string.sub( simpleName, 1, #simpleName - 1 );

    -- link this directory and set it into our dirs dictionary.
    -- we should always pass the absolute directory to this function.
    local translator = fileCreateTranslator( dirPath );

    dirs[simpleName] = translator;
end

local function fileIterator( filePath )
    -- do nothing.
    return;
end

resRoot.scanDirEx( "/", "*", dirIterator, fileIterator, false );
```

## [FileSystem](mta://reference/misc/modules-filesystem.md) Namespace Functions

- createTranslator

- [createRAMDisk](mta://reference/misc/modules-filesystem-createramdisk.md)

- [createMemoryFile](mta://reference/misc/modules-filesystem-creatememoryfile.md)

- [createFileIterative](mta://reference/misc/modules-filesystem-createfileiterative.md)

- [copyFile](mta://reference/misc/modules-filesystem-copyfile.md)

- [copyStream](mta://reference/misc/modules-filesystem-copystream.md)

- [copyStreamCount](mta://reference/misc/modules-filesystem-copystreamcount.md)

- [pathToFilename](mta://reference/misc/modules-filesystem-pathtofilename.md)

- [streamCompare](mta://reference/misc/modules-filesystem-streamcompare.md)

- [topointer](mta://reference/misc/modules-filesystem-topointer.md)

- [type](mta://reference/misc/modules-filesystem-type.md)

- [setDoBufferAllRaw](mta://reference/misc/modules-filesystem-setdobufferallraw.md)

- [getDoBufferAllRaw](mta://reference/misc/modules-filesystem-getdobufferallraw.md)

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

- [getFiles](mta://reference/misc/modules-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/modules-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)
