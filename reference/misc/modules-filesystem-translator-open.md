---
doc_id: "mta-wiki:13501"
title: "Modules/FileSystem/translator/open"
source_title: "Modules/FileSystem/translator/open"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/open"
revision_id: 73846
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.569262+00:00"
---

# Modules/FileSystem/translator/open

This function opens a link to a file instance on a given Eir FileSystem translator. Using a file link you can write and/or receive data from filesystems.

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

## [FileSystem](mta://reference/misc/modules-filesystem.md) Translator Functions

- open

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

## [FileSystem](mta://reference/misc/modules-filesystem.md) File Functions

- [read](mta://reference/misc/modules-filesystem-file-read.md)

- [readByte](mta://reference/misc/modules-filesystem-file-readbyte.md)

- [readUByte](mta://reference/misc/modules-filesystem-file-readubyte.md)

- [readShort](mta://reference/misc/modules-filesystem-file-readshort.md)

- [readUShort](mta://reference/misc/modules-filesystem-file-readushort.md)

- [readInt](mta://reference/misc/modules-filesystem-file-readint.md)

- [readUInt](mta://reference/misc/modules-filesystem-file-readuint.md)

- [readFloat](mta://reference/misc/modules-filesystem-file-readfloat.md)

- [readDouble](mta://reference/misc/modules-filesystem-file-readdouble.md)

- [readBoolean](mta://reference/misc/modules-filesystem-file-readboolean.md)

- [write](mta://reference/misc/modules-filesystem-file-write.md)

- [writeByte](mta://reference/misc/modules-filesystem-file-writebyte.md)

- [writeUByte](mta://reference/misc/modules-filesystem-file-writeubyte.md)

- [writeShort](mta://reference/misc/modules-filesystem-file-writeshort.md)

- [writeUShort](mta://reference/misc/modules-filesystem-file-writeushort.md)

- [writeInt](mta://reference/misc/modules-filesystem-file-writeint.md)

- [writeUInt](mta://reference/misc/modules-filesystem-file-writeuint.md)

- [writeFloat](mta://reference/misc/modules-filesystem-file-writefloat.md)

- [writeDouble](mta://reference/misc/modules-filesystem-file-writedouble.md)

- [writeBoolean](mta://reference/misc/modules-filesystem-file-writeboolean.md)

- [size](mta://reference/misc/modules-filesystem-file-size.md)

- [stat](mta://reference/misc/modules-filesystem-file-stat.md)

- [tell](mta://reference/misc/modules-filesystem-file-tell.md)

- [seek](mta://reference/misc/modules-filesystem-file-seek.md)

- [eof](mta://reference/misc/modules-filesystem-file-eof.md)

- [flush](mta://reference/misc/modules-filesystem-file-flush.md)

- [isWritable](mta://reference/misc/modules-filesystem-file-iswritable.md)

- [isReadable](mta://reference/misc/modules-filesystem-file-isreadable.md)
