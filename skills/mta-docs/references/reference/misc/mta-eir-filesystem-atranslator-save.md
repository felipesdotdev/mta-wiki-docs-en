---
doc_id: "mta-wiki:7546"
title: "MTA:Eir/FileSystem/atranslator/save"
source_title: "MTA:Eir/FileSystem/atranslator/save"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/atranslator/save"
revision_id: 73583
language: "en"
categories: []
---

# MTA:Eir/FileSystem/atranslator/save

This function attempts to save the contents of an archive into its source file. This is only possible if the source file has been opened as writable.

## Syntax

```
bool atranslator:save ()
```

## Returns

This function returns **true** if the contents of the archive could successfully be saved back into its source file, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet writes a .zip archive and saves it in the end. It handles common errors that could happen during archive management.

```
-- Get a generic translator to the resource instance directory.
local resRoot = fileCreateTranslator( "/" );

-- Open or create some .zip archive.
local zipFile = false;
local zipTranslator = false;

if ( resRoot:exists( "archive.zip" ) ) then
    zipFile = resRoot:open( "archive.zip", "rb+" );

    if ( zipFile ) then
        zipTranslator = fileOpenArchive( zipFile );
    end
else
    zipFile = resRoot:open( "archive.zip", "wb+" );

    if ( zipFile ) then
        zipTranslator = fileCreateZIP( zipFile );
    end
end

-- Check that everything was created alright.
if not ( zipFile ) then
    outputDebugString( "could not open or create the archive stream" );
    return false;
end

if not ( zipTranslator ) then
    outputDebugString( "could not create the .zip translator based on the stream file" );

    -- Clean up the file handle.
    zipFile:destroy();
    return false;
end

-- Write a random file.
local randFile = zipTranslator:open( tostring( math.random( 0, 1 ) ) .. ".rnd", "wb" );

randFile.write(
[[This is a randomly generated file.
Its name is random. ]] .. math.random( 0, 100 )
);

-- Clean up the file handle.
-- We do not actually have to do this, because all files are closed from a translator when it is destroyed.
randFile:destroy();

-- Save the archive and clean up the handles.
zipTranslator:save();
zipTranslator:destroy();
zipFile:destroy();
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

- [scanDirEx](mta://reference/misc/mta-eir-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/mta-eir-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/mta-eir-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Archive Translator Functions

- save (not module)

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
