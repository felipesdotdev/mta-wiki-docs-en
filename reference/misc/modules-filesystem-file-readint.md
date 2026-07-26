---
doc_id: "mta-wiki:13529"
title: "Modules/FileSystem/file/readInt"
source_title: "Modules/FileSystem/file/readInt"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/readInt"
revision_id: 73737
language: "en"
categories: []
generated_at: "2026-07-26T16:16:11.953622+00:00"
---

# Modules/FileSystem/file/readInt

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

## [FileSystem](mta://reference/misc/modules-filesystem.md) File Functions

- [read](mta://reference/misc/modules-filesystem-file-read.md)

- [readByte](mta://reference/misc/modules-filesystem-file-readbyte.md)

- [readUByte](mta://reference/misc/modules-filesystem-file-readubyte.md)

- [readShort](mta://reference/misc/modules-filesystem-file-readshort.md)

- [readUShort](mta://reference/misc/modules-filesystem-file-readushort.md)

- readInt

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
