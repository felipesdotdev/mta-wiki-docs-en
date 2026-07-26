---
doc_id: "mta-wiki:13504"
title: "Modules/FileSystem/translator/chdir"
source_title: "Modules/FileSystem/translator/chdir"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/chdir"
revision_id: 73764
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.404929+00:00"
---

# Modules/FileSystem/translator/chdir

This function changes the current directory pointer of the translator. All operations on the FileSystem translator are executed relative to the current directory. The translator, if possible, is asked to prevent deletion of the current directory.

## Syntax

```
bool translator:chdir ( string dirPath )
```

## Arguments

- **dirPath:** a path to a directory that should be made current directory

## Returns

This function returns **true** if the directory pointed at by dirPath is an existing directory and can be accessed by the translator, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet creates a simple command-based filesystem explorer.

```
-- Create a generic FileSystem translator.
local cmdTranslator = fileCreateTranslator( "/" );

-- Set up some commands.
addCommandHandler( "chdir",
    function(...)
        local myPath = table.concat( { ... }, " " );

        cmdTranslator:chdir( myPath );
    end
);

addCommandHandler( "dir",
    function()
        -- todo: resolve a path given as arguments.

        local myEntries = {};

        local function itemIterator( path )
            table.insert( myEntries, cmdTranslator:relPath( path ) );
        end

        cmdTranslator:scanDirEx( "/", "*", itemIterator, itemIterator, false );

        -- Output the filesystem entries to the chatbox.
        for m,n in ipairs( myEntries ) do
            outputChatBox( n );
        end

        -- todo: print statistics (file size, number of files, number of directories, ...)
    end
);
```

## [FileSystem](mta://reference/misc/modules-filesystem.md) Translator Functions

- [open](mta://reference/misc/modules-filesystem-translator-open.md)

- [exists](mta://reference/misc/modules-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/modules-filesystem-translator-createdir.md)

- chdir

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
