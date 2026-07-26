---
doc_id: "mta-wiki:7523"
title: "MTA:Eir/FileSystem/file/write"
source_title: "MTA:Eir/FileSystem/file/write"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/file/write"
revision_id: 73565
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.786788+00:00"
---

# MTA:Eir/FileSystem/file/write

This function attempts to write a string of bytes (characters) into the file. It returns the amount of bytes that have actually been written.

## Syntax

```
int file:write ( string dataString )
```

## Arguments

- **dataString:** the string of data that should be written into the file

## Returns

Returns the amount of bytes that have been actually written into the file. Returns false if **dataString** is not a valid string.

## Example

Click to collapse [-]
Client

This snippet logs the local player's chat output into a file.

```
-- Open up the logfile.
-- If it was not created already, create it.
local logFile = false;

if ( fileExists( "log.dat" ) ) then
    logFile = fileOpen( "log.dat" );
else
    logFile = fileCreate( "log.dat" );
end

-- Table of all log entries.
-- The logfile has to be written at the destruction of the resource environment.
-- This is done so we can have multiple log sessions added into a file stream.
local logEntries = {};

-- Function to append entries into the logfile.
local function addLogEntry( message )
    local entry = {
        message = message,
        time = getRealTime()
    };

    table.insert( logEntries, entry );
end

-- Event handler to add log entries when chat messages are created.
addEventHandler( "onClientChatMessage", root,
    function(message)
        -- Forward the message into our logging system.
        addLogEntry( message );
    end
);
    

-- Write the log when the resource is terminated.
addEventHandler( "onClientResourceStop", root,
    function()
        -- todo: write session start and end times.

        -- Write the amount of log entries.
        logFile:writeShort( #logEntries );

        -- Write the log entries.
        for m,n in ipairs( logEntries ) do
            local encryptedMessage = teaEncode( n.message );

            logFile:writeShort( #encryptedMessage );
            logFile:write( encryptedMessage );

            -- Write date information.
            logFile:writeShort( n.time.second ); logFile:writeShort( n.time.minute ); logFile:writeShort( n.time.hour );
            logFile:writeShort( n.time.monthday ); logFile:writeShort( n.time.month + 1 ); logFile:writeShort( n.time.year + 1900 );
        end
    end
);

-- todo: create a log file viewer.
```

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

- write

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
