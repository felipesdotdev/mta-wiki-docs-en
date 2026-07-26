---
doc_id: "mta-wiki:7497"
title: "MTA:Eir/FileSystem/translator/open"
source_title: "MTA:Eir/FileSystem/translator/open"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/open"
revision_id: 73535
language: "en"
categories: []
---

# MTA:Eir/FileSystem/translator/open

This function opens a link to a file instance on a given MTA:Eir FileSystem translator. Using a file link, you can write and/or receive data from filesystems.

## Syntax

```
file, string translator:open ( string filePath, string fileMode )
```

## Arguments

- **filePath:** the path to the file that should be opened

- **fileMode:** an ANSI file mode descriptor (can be 'w', 'r' or 'a', with 'b' and/or '+' appended)

## Returns

This function returns the **FileSystem file** class that can be used to retrieve or store data persistently. Returns **false** if the file failed to open and the **reason of failure as string**.

### Failure reasons

- unknown error

- path out of scope

- invalid parameters

- resources exhausted

- access denied

- not found

- already exists

## Example

Click to collapse [-]
Server

This snippet lists information about the registered MTA server modules. This information can be retrieved through a command.

```
-- The table that will contain all module information.
local moduleInfo = {};

-- Attempt to get a handle to the FileSystem module namespace.
local fsys = createFilesystemInterface();

-- Could fail if the server restrictions are set tight.
if not ( fsys ) then
    outputDebugString( "could not get a handle to the FileSystem module namespace" );
    return false;
end

local function moduleFileIterator( filePath )
    -- Create an entry for this module.
    local moduleName = fsys.root:relPath( filePath );
    local moduleStats = fsys.root:stat( filePath );

    local entry = {
        name = moduleName,
        stats = moduleStats
    };

    -- Add the entry into the registry.
    table.insert( moduleInfo, entry );
end

-- Loop through all server modules.
fsys.root:chdir( "mods/deathmatch/modules/" );
fsys.root:scanDirEx( "", "*", nil, moduleFileIterator, false );

-- Function to get a module into by name.
local function getModuleByName( name )
    for m,n in ipairs( moduleInfo ) do
        if ( n.name == name ) then
            return n;
        end
    end

    return false;
end

-- Command to request server module information.
addCommandHandler( "modules",
    function(player, moduleName)
        -- Output module information to the player.
        local module = getModuleByName( moduleName );

        if not ( module ) then
            outputChatBox( "could not find module named " .. tostring( moduleName ), player );
            return false;
        end

        -- Output it.
        outputChatBox( "module-name: " .. module.name );
        outputChatBox( "module-size: " .. module.stats.size );
        
        -- todo: add more info about the module.
    end
);
```

Click to collapse [-]
Client

This snippet attempts to open a file and output its contents inside of a CEGUI memo.

```
-- Get the screen size so we can scale the memo properly
local screenWidth, screenHeight = guiGetScreenSize();

-- Make the memo cover nearly the entire screen.
local myMemo = guiCreateMemo( 20, 20, screenWidth - 40, screenHeight - 40, "", false );

-- Read the contents of some file.
local fileContents = "";

local fileHandle = fileOpen( "someFile.txt", "rb" );

if ( fileHandle ) then
    fileContents = fileHandle:read( fileHandle.size() );

    -- Clean up our file handle.
    fileHandle:destroy();
end

-- Update the memo.
guiSetText( myMemo, fileContents );
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- open

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

- [scanDirEx](mta://reference/misc/mta-eir-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/mta-eir-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/mta-eir-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) File Functions

- [read](mta://reference/misc/mta-eir-filesystem-file-read.md)

- [readByte](mta://reference/misc/mta-eir-filesystem-file-readbyte.md)

- [readUByte](mta://reference/misc/mta-eir-filesystem-file-readubyte.md)

- [readShort](mta://reference/misc/mta-eir-filesystem-file-readshort.md)

- [readUShort](mta://reference/misc/mta-eir-filesystem-file-readushort.md)

- [readInt](mta://reference/misc/mta-eir-filesystem-file-readint.md)

- [readUInt](mta://reference/misc/mta-eir-filesystem-file-readuint.md)

- [readFloat](mta://reference/misc/mta-eir-filesystem-file-readfloat.md)

- [readDouble](mta://reference/misc/mta-eir-filesystem-file-readdouble.md)

- [readBoolean](mta://reference/misc/mta-eir-filesystem-file-readboolean.md)

- [write](mta://reference/misc/mta-eir-filesystem-file-write.md)

- [writeByte](mta://reference/misc/mta-eir-filesystem-file-writebyte.md)

- [writeUByte](mta://reference/misc/mta-eir-filesystem-file-writeubyte.md)

- [writeShort](mta://reference/misc/mta-eir-filesystem-file-writeshort.md)

- [writeUShort](mta://reference/misc/mta-eir-filesystem-file-writeushort.md)

- [writeInt](mta://reference/misc/mta-eir-filesystem-file-writeint.md)

- [writeUInt](mta://reference/misc/mta-eir-filesystem-file-writeuint.md)

- [writeFloat](mta://reference/misc/mta-eir-filesystem-file-writefloat.md)

- [writeDouble](mta://reference/misc/mta-eir-filesystem-file-writedouble.md)

- [writeBoolean](mta://reference/misc/mta-eir-filesystem-file-writeboolean.md)

- [size](mta://reference/misc/mta-eir-filesystem-file-size.md)

- [stat](mta://reference/misc/mta-eir-filesystem-file-stat.md)

- [tell](mta://reference/misc/mta-eir-filesystem-file-tell.md)

- [seek](mta://reference/misc/mta-eir-filesystem-file-seek.md)

- [eof](mta://reference/misc/mta-eir-filesystem-file-eof.md)

- [flush](mta://reference/misc/mta-eir-filesystem-file-flush.md)

- [isWritable](mta://reference/misc/mta-eir-filesystem-file-iswritable.md)

- [isReadable](mta://reference/misc/mta-eir-filesystem-file-isreadable.md)
