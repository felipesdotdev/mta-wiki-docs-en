---
doc_id: "mta-wiki:7495"
title: "MTA:Eir/FileSystem/createArchiveTranslator"
source_title: "MTA:Eir/FileSystem/createArchiveTranslator"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/createArchiveTranslator"
revision_id: 38790
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.408309+00:00"
---

# MTA:Eir/FileSystem/createArchiveTranslator

This function creates a FileSystem archive translator. A FileSystem archive translator is a virtual FileSystem that grants access to the contents of archives. You can browse archives the same way as you would with native OS directories. The archive implementations usually cache their operations inside of the OS temp directory.

Currently, only .zip archives are supported.

## Syntax

```
atranslator fsnamespace.createArchiveTranslator ( file fileHandle )
```

## Arguments

- **fileHandle:** a MTA:Eir FileSystem file/stream class that contains the archive.

## Returns

This function returns the **FileSystem translator** that grants access to contents of an archive.

## Remarks

This function is currently unavailable in the fileSystem.dll module.

## Example

Click to collapse [-]
Client

This snippet lists the contents of a .zip archive.

```
-- Opens the file link to our .zip archive.
-- The input fileStream can actually be any file/stream class that is exported to the script.
-- The implementation is allowed to throw exceptions if a file/stream class is incompatible.
local zipFile = fileOpen( "theArchive.zip", "rb" );

-- Check that we can access that .zip archive.
if not ( zipFile ) then
    outputDebugString( "could not open theArchive.zip" );
    return false;
end

-- Try to open a content link to the .zip archive.
-- This operation will fail is the archive is not valid.
local zipTranslator = fileOpenArchive( zipFile );

if not ( zipTranslator ) then
    outputDebugString( "could not access the contents of theArchive.zip" );
    outputDebugString( "the archive could be damaged" );
    return false;
end

-- This table shall contain all filenames of the archive.
local fileEntries = {};

local function fileIterator( filePath )
    -- Add the filename to our list.
    table.insert( fileEntries, zipTranslator.relPathRoot( filePath ) );
end

zipTranslator.scanDirEx( "/", "*", nil, fileIterator, true );

-- List the filenames on the chatbox.
for m,n in ipairs( fileEntries ) do
    outputChatBox( n );
end
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Namespace Functions

- [createTranslator](mta://reference/misc/mta-eir-filesystem-createtranslator.md)

- [createRAMDisk](mta://reference/misc/mta-eir-filesystem-createramdisk.md)

- [createMemoryFile](mta://reference/misc/mta-eir-filesystem-creatememoryfile.md)

- [createFileIterative](mta://reference/misc/mta-eir-filesystem-createfileiterative.md)

- createArchiveTranslator (not module)

- [createZIPArchive](mta://reference/misc/mta-eir-filesystem-createziparchive.md) (not module)

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
