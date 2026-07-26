---
doc_id: "mta-wiki:7518"
title: "MTA:Eir/FileSystem/file/readInt"
source_title: "MTA:Eir/FileSystem/file/readInt"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/file/readInt"
revision_id: 73559
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.665267+00:00"
---

# MTA:Eir/FileSystem/file/readInt

This function attempts to read an integer (native type) from a file and return it. The amount of bytes read should be four.

## Syntax

```
int file:readInt ()
```

## Returns

Returns an integer if it was successfully read from the file, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet demonstrates an encrypted Lua source code format.

```
-- Have some pieces of source code as samples.
local sourceSamples = {
[[print("Hello World!");]],
[[print("Ballas on the streets.");]],
[[return 1+1==0;]]
};

local function packSourceCode( theFile, sourceString )
    -- Encrypt the source code.
    local encryptedCode = teaEncode( sourceString );

    -- Write the file header.
    theFile:writeInt( #encryptedCode );

    -- Write file contents.
    theFile:write( encryptedCode );
end

local function unpackSourceCode( theFile )
    -- Grab the source code from the file.
    local encryptedLen = theFile:readInt();

    -- Has the length been read correctly?
    if not ( encryptedLen ) then
        return false;
    end

    local encryptedSource = theFile:read( encryptedLen );

    -- Make sure it has not been fragmented.
    if not ( #encryptedSource == encryptedLen ) then
        return false;
    end

    -- Decrypt the source code.
    local sourceCode = teaDecode( encryptedSource );

    -- Return it.
    return sourceCode;
end

-- Attempt some encryption.
local theFile = fileCreate( "encryptedSource.lue" );

for m,n in ipairs( sourceSamples ) do
    packSourceCode( theFile, n );
end

-- Get the original source code again.
theFile:seek( 0, "set" );

local unencryptedSources = {};

while ( true ) do
    local code = unpackSourceCode( theFile );

    if not ( code ) then break; end

    table.insert( unencryptedSources, code );
end
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) File Functions

- [read](mta://reference/misc/mta-eir-filesystem-file-read.md)

- [readByte](mta://reference/misc/mta-eir-filesystem-file-readbyte.md)

- [readUByte](mta://reference/misc/mta-eir-filesystem-file-readubyte.md)

- [readShort](mta://reference/misc/mta-eir-filesystem-file-readshort.md)

- [readUShort](mta://reference/misc/mta-eir-filesystem-file-readushort.md)

- readInt

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
