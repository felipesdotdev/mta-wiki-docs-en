---
doc_id: "mta-wiki:7496"
title: "MTA:Eir/FileSystem/createZIPArchive"
source_title: "MTA:Eir/FileSystem/createZIPArchive"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/createZIPArchive"
revision_id: 38791
language: "en"
categories: []
---

# MTA:Eir/FileSystem/createZIPArchive

This function creates a .zip archive inside of the given MTA:Eir file/stream class and returns its translator handle. The archive will not be written into the stream unless the **save** method of the archive translator is called.

## Syntax

```
atranslator fsnamespace.createZIPArchive ( file fileHandle )
```

## Arguments

- **fileHandle:** a MTA:Eir FileSystem file/stream class that is writable.

## Returns

This function returns the **FileSystem translator** that grants access to contents of an archive if fileHandle is a valid file pointer to create a .zip archive in, **false** otherwise.

## Remarks

This function is currently unavailable in the fileSystem.dll module.

## Example

Click to collapse [-]
Server

This snippet packs all server resources into .zip archives and puts them into an output directory, which can be a shared release directory.
This sample should be expanded to support resource sub-directories. It is highly conceptual for now.

```
-- Create our FileSystem interface.
local fsys = createFilesystemInterface();

if not ( fsys ) then
    outputDebugString( "cannot create FileSystem interface" );
    return false;
end

-- Gain access to the resource root.
local resourcesRoot = fsys.createTranslator( fsys.root.absPath() .. "mods/deathmatch/resources/" );

if not ( resourcesRoot ) then
    outputDebugString( "cannot link server resources directory" );
    return false;
end

-- Create an output release directory next to the actual resources directory.
fsys.root.createDir( "mods/deathmatch/release_resources/" );

-- Attempt to link it.
local releaseRoot = fsys.createTranslator( fsys.root.absPath() .. "mods/deathmatch/release_resources/" );

if not ( releaseRoot ) then
    outputDebugString( "cannot link release directory" );
    return false;
end

-- Archive the resources.
local function dirIterator( dirPath )
    -- Get the simple name of the resource.
    -- It should be the name of the .zip archive
    local relPath = resourcesRoot.relPath( dirPath );

    local simpleName = string.sub( relPath, 1, #relPath - 1 );

    -- Get the resource instance directory link.
    local resRoot = fsys.createTranslator( dirPath );

    if not ( resRoot ) then
        outputDebugString( "resource " .. simpleName .. " could not be linked" );
        return;
    end

    -- todo: validate the resource.

    -- Create our resource .zip
    local zipFile = releaseRoot.open( simpleName .. ".zip", "wb+" );

    if ( zipFile ) then
        local zipTranslator = fsys.createZIPArchive( zipFile );

        if ( zipTranslator ) then
            -- Copy all files into it.
            local function copyIterator( filePath )
                -- todo: optimize this operation.
                -- can be done by splitting up into multiple write operations.
                local copyFile = resRoot.open( filePath, "rb" );

                if ( copyFile ) then
                    local outFile = zipTranslator.open( resRoot.relPath( filePath ), "wb" );

                    if ( outFile ) then
                        zipTranslator.write( copyFile.read( copyFile.size() ) );

                        outFile.destroy();
                    end

                    copyFile.destroy();
                end
            end

            resRoot.scanDirEx( "/", "*", nil, copyIterator, true );

            -- Write the .zip archive and close the link.
            zipTranslator.save();
            zipTranslator.destroy();
        end

        -- We can close the file now.
        zipFile.destroy();
    end

    -- Clean up.
    resRoot.destroy();
end

resourcesRoot.scanDirEx( "/", "*", dirIterator, nil, false );

-- Clean up after ourselves.
resourcesRoot.destroy();
releaseRoot.destroy();
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Namespace Functions

- [createTranslator](mta://reference/misc/mta-eir-filesystem-createtranslator.md)

- [createRAMDisk](mta://reference/misc/mta-eir-filesystem-createramdisk.md)

- [createMemoryFile](mta://reference/misc/mta-eir-filesystem-creatememoryfile.md)

- [createFileIterative](mta://reference/misc/mta-eir-filesystem-createfileiterative.md)

- [createArchiveTranslator](mta://reference/misc/mta-eir-filesystem-createarchivetranslator.md) (not module)

- createZIPArchive (not module)

- [copyFile](mta://reference/misc/mta-eir-filesystem-copyfile.md)

- [copyStream](mta://reference/misc/mta-eir-filesystem-copystream.md)

- [copyStreamCount](mta://reference/misc/mta-eir-filesystem-copystreamcount.md)

- [pathToFilename](mta://reference/misc/mta-eir-filesystem-pathtofilename.md)

- [streamCompare](mta://reference/misc/mta-eir-filesystem-streamcompare.md)

- [topointer](mta://reference/misc/mta-eir-filesystem-topointer.md)

- [type](mta://reference/misc/mta-eir-filesystem-type.md)

- [setDoBufferAllRaw](mta://reference/misc/mta-eir-filesystem-setdobufferallraw.md)

- [getDoBufferAllRaw](mta://reference/misc/mta-eir-filesystem-getdobufferallraw.md)

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

- [scanDirEx](mta://reference/misc/mta-eir-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/mta-eir-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/mta-eir-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Archive Translator Functions

- [save](mta://reference/misc/mta-eir-filesystem-atranslator-save.md) (not module)
