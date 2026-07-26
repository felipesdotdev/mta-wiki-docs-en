---
doc_id: "mta-wiki:7500"
title: "MTA:Eir/FileSystem/translator/chdir"
source_title: "MTA:Eir/FileSystem/translator/chdir"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/chdir"
revision_id: 73536
language: "en"
categories: []
---

# MTA:Eir/FileSystem/translator/chdir

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

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- [open](mta://reference/misc/mta-eir-filesystem-translator-open.md)

- [exists](mta://reference/misc/mta-eir-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/mta-eir-filesystem-translator-createdir.md)

- chdir

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

- [scanDirEx](mta://reference/misc/mta-eir-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/mta-eir-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/mta-eir-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)
