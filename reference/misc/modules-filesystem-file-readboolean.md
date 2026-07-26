---
doc_id: "mta-wiki:13533"
title: "Modules/FileSystem/file/readBoolean"
source_title: "Modules/FileSystem/file/readBoolean"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/file/readBoolean"
revision_id: 73742
language: "en"
categories: []
generated_at: "2026-07-26T16:16:11.883485+00:00"
---

# Modules/FileSystem/file/readBoolean

This function attempts to read a boolean (native type) from a file and return it. The amount of bytes read should be one.

## Syntax

```
boolean file:readBoolean ()
```

## Returns

Returns a boolean if it was successfully read from the file, **nil** otherwise.

## Example

Click to collapse [-]
Client

This snippet demonstrates a variable file format that stores player properties depending on whether they are required.

```
local function saveLocalPlayerState( theFile, saveDetails )
    local player = localPlayer;

    -- Write basic details about the player instance.
    theFile:writeShort( getElementModel( player ) );
    theFile:writeInt( getPlayerMoney() );
    
    -- Next write down special details given by the game.
    local isQuickSave = saveDetails.isQuickSave and true or false;

    theFile:writeBoolean( isQuickSave );

    if not ( isQuickSave ) then
        -- Save things like player position, dimension and interior.
        local posX, posY, posZ = getElementPosition( player );
        local dimension, interior = getElementDimension( player ), getElementInterior( player );

        theFile:writeDouble( posX ); theFile:writeDouble( posY ); theFile:writeDouble( posZ );
        theFile:writeShort( dimension ); theFile:writeShort( interior );
    end

    -- Save the time this snapshot was taken.
    local realTime = getRealTime();

    theFile:writeShort( realTime.minute ); theFile:writeShort( realTime.hour );
    theFile:writeShort( realTime.monthday ); theFile:writeShort( realTime.month + 1 ); theFile:writeShort( realTime.year + 1900 );
    return true;
end

local function readBasicData( obj, operator, callback )
    local data = operator(obj);

    if ( data ) then
        callback( data );
    end
end

-- Function to restore details from a snapshot file stream.
local function loadLocalPlayerState( theFile )
    local player = localPlayer;
    local saveDetails = {};

    -- Restore the basic information.
    readBasicData( theFile, theFile.readShort, function(model) setElementModel( player, model ); end );
    readBasicData( theFile, theFile.readInt, function(money) setPlayerMoney(money); end );

    -- Read advanced parameters,
    local isQuickSave = theFile:readBoolean();
    saveDetails.isQuickSave = isQuickSave;

    if not ( isQuickSave ) then
        -- Restore advanced details.
        local posX, posY, posZ = theFile:readDouble(), theFile:readDouble(), theFile:readDouble();
        local dimension, interior = theFile:readShort(), theFile:readShort();

        -- Set them, if read correctly.
        if ( interior ) then
            setElementPosition( player, posX, posY, posZ );
            setElementDimension( player, dimension );
            setElementInterior( player, interior );
        end
    end

    -- Get the time the snapshot was taken at.
    saveDetails.saveTime = {
        minute = theFile:readShort(),
        hour = theFile:readShort(),
        monthday = theFile:readShort(),
        month = theFile:readShort(),
        year = theFile:readShort()
    };

    -- Return the save details so the runtime can react accordingly.
    return saveDetails;
end

-- Command to save a complete snapshot of the player.
addCommandHandler( "save",
    function()
        local saveDetails =
        {
            isQuickSave = false
        };

        local saveFile = fileCreate( "savestate.dat" );

        if ( saveFile ) then
            saveLocalPlayerState( saveFile, saveDetails );

            saveFile:'''Bold text'''destroy();

            outputChatBox( "successfully saved complete player status" );
        end
    end
);

-- Command to save a quick savestate.
addCommandHandler( "qsave",
    function()
        local saveDetails =
        {
            isQuickSave = true
        };

        local saveFile = fileCreate( "savestate.dat" );

        if ( saveFile ) then
            saveLocalPlayerState( saveFile, saveDetails );

            saveFile:destroy();

            outputChatBox( "successfully saved quick player status" );
        end
    end
);

-- Command to load a savestate from disk.
addCommandHandler( "loadstate",
    function()
        if not ( fileExists( "savestate.dat" ) ) then
            return;
        end

        local saveFile = fileOpen( "savestate.dat" );

        if ( saveFile ) then
            local saveData = loadLocalPlayerState( saveFile );

            saveFile:destroy();

            outputChatBox( "restored from a save (date was " .. saveData.saveTime.monthday .. "." .. saveData.saveTime.month .. "." .. saveData.saveTime.year .. ")" );
        end
    end
);
```

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

- readBoolean

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
