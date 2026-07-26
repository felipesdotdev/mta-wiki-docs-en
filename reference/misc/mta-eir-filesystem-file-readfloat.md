---
doc_id: "mta-wiki:7519"
title: "MTA:Eir/FileSystem/file/readFloat"
source_title: "MTA:Eir/FileSystem/file/readFloat"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/file/readFloat"
revision_id: 73562
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.652211+00:00"
---

# MTA:Eir/FileSystem/file/readFloat

This function attempts to read a float (native type) from a file and return it. The amount of bytes read should be four.

## Syntax

```
float file:readFloat ()
```

## Returns

Returns a float if it was successfully read from the file, **false** otherwise.

## Example

Click to collapse [-]
Server

This snippet demonstrates a binary vehicle handling format. This saves space in comparison to a .XML based format.

```
local function writeFileString( theFile, string )
    theFile:writeShort( #string );
    theFile:write( string );
end

local function readFileString( theFile )
    local stringLen = theFile:readShort();

    if not ( stringLen ) then
        return false;
    end

    return theFile:read( stringLen );
end

local function saveVehicleHandling( theFile, handlingDict )
    -- Write down the details.
    theFile:writeDouble( handlingDict.mass );
    theFile:writeDouble( handlingDict.turnMass );
    theFile:writeFloat( handlingDict.dragCoeff );

    theFile:writeFloat( handlingDict.centerOfMass[1] );
    theFile:writeFloat( handlingDict.centerOfMass[2] );
    theFile:writeFloat( handlingDict.centerOfMass[3] );

    theFile:writeInt( handlingDict.percentSubmerged );
    theFile:writeDouble( handlingDict.tractionMultiplier );
    theFile:writeFloat( handlingDict.tractionLoss );
    theFile:writeFloat( handlingDict.tractionBias );
    theFile:writeShort( handlingDict.numberOfGears );
    theFile:writeDouble( handlingDict.maxVelocity );
    theFile:writeDouble( handlingDict.engineAcceleration );
    theFile:writeFloat( handlingDict.engineInertia );
    
    writeFileString( theFile, tostring( handlingDict.driveType ) );
    writeFileString( theFile, tostring( handlingDict.engineType ) );

    theFile:writeDouble( handlingDict.brakeDeceleration );
    theFile:writeBoolean( handlingDict.ABS );
    theFile:writeFloat( handlingDict.steeringLock );
    theFile:writeFloat( handlingDict.suspensionForceLevel );
    theFile:writeFloat( handlingDict.suspensionDamping );
    theFile:writeFloat( handlingDict.suspensionHighSpeedDamping );
    theFile:writeFloat( handlingDict.suspensionUpperLimit );
    theFile:writeFloat( handlingDict.suspensionLowerLimit );
    theFile:writeFloat( handlingDict.suspensionFrontRearBias );
    theFile:writeFloat( handlingDict.suspensionAntiDiveMultiplier );
    theFile:writeFloat( handlingDict.seatOffsetDistance );
    theFile:writeFloat( handlingDict.collisionDamageMultiplier );
    theFile:writeInt( handlingDict.monetary );
    theFile:writeInt( handlingDict.modelFlags );
    theFile:writeInt( handlingDict.handlingFlags );
    
    writeFileString( theFile, handlingDict.headLight );
    writeFileString( theFile, handlingDict.tailLight );
    
    theFile:writeShort( handlingDict.animGroup );
end

local function attemptFileRead( theFile, theOperation, defaultOut )
    local output = theOperation( theFile );

    if not ( output ) then
        return defaultOut;
    end

    return output;
end

local function loadVehicleHandling( theFile )
    local handlingEntry = {
        mass = attemptFileRead( theFile, theFile.readDouble, 1000 ),
        turnMass = attemptFileRead( theFile, theFile.readDouble, 1000 ),
        dragCoeff = attemptFileRead( theFile, theFile.readFloat, 0 ),

        {
            [1] = attemptFileRead( theFile, theFile.readFloat, 0 ),
            [2] = attemptFileRead( theFile, theFile.readFloat, 0 ),
            [3] = attemptFileRead( theFile, theFile.readFloat, 0 )
        },

        percentSubmerged = attemptFileRead( theFile, theFile.readInt, 100 ),
        tractionMultiplier = attemptFileRead( theFile, theFile.readDouble, 1.0 ),
        tractionLoss = attemptFileRead( theFile, theFile.readFloat, 1.0 ),
        tractionBias = attemptFileRead( theFile, theFile.readFloat, 1.0 ),
        numberOfGears = attemptFileRead( theFile, theFile.readShort, 4 ),
        maxVelocity = attemptFileRead( theFile, theFile.readDouble, 240 ),
        engineAcceleration = attemptFileRead( theFile, theFile.readDouble, 9 ),
        engineInertia = attemptFileRead( theFile, theFile.readFloat, 3 ),
        
        driveType = attemptFileRead( theFile, function(theFile) return readFileString( theFile ) end, "fwd" ),
        engineType = attemptFileRead( theFile, function(theFile) return readFileString( theFile ) end, "diesel" ),

        brakeDeceleration = attemptFileRead( theFile, theFile.readDouble, 5 ),
        brakeBias = attemptFileRead( theFile, theFile.readFloat, 1.0 ),
        ABS = attemptFileRead( theFile, theFile.readBoolean, false ),
        steeringLock = attemptFileRead( theFile, theFile.readFloat, 180 ),
        suspensionForceLevel = attemptFileRead( theFile, theFile.readFloat, 10 ),
        suspensionDamping = attemptFileRead( theFile, theFile.readFloat, 10 ),
        suspensionHighSpeedDamping = attemptFileRead( theFile, theFile.readFloat, 50 ),
        suspensionUpperLimit = attemptFileRead( theFile, theFile.readFloat, 0 ),
        suspensionLowerLimit = attemptFileRead( theFile, theFile.readFloat, 0 ),
        suspensionFrontRearBias = attemptFileRead( theFile, theFile.readFloat, 0.4 ),
        suspensionAntiDiveMultiplier = attemptFileRead( theFile, theFile.readFloat, 10 ),
        seatOffsetDistance = attemptFileRead( theFile, theFile.readFloat, 4 ),
        collisionDamageMultiplier = attemptFileRead( theFile, theFile.readFloat, 0.5 ),
        monetary = attemptFileRead( theFile, theFile.readInt, 10000 ),
        modelFlags = attemptFileRead( theFile, theFile.readInt, 0 ),
        handlingFlags = attemptFileRead( theFile, theFile.readInt, 0 ),
        
        headLight = attemptFileRead( theFile, function(theFile) return readFileString( theFile ) end, "big" ),
        tailLight = attemptFileRead( theFile, function(theFile) return readFileString( theFile ) end, "big" ),

        animGroup = attemptFileRead( theFile, theFile.readShort, 1 )
    };

    return handlingEntry;
end

-- Save the handling of your vehicle, so you can reuse it later.
addCommandHandler( "savehandling",
    function(player)
        local myVehicle = getPedOccupiedVehicle( player );

        if ( myVehicle ) then
            local handling = getVehicleHandling( myVehicle );

            local handlingFile = fileCreate( getPlayerName( player ) .. "_saved_handling.dat" );

            if ( handlingFile ) then
                saveVehicleHandling( handlingFile, handling );

                handlingFile:destroy();

                outputChatBox( "successfully saved handling" );
            end
        end
    end
);

-- Load the handling of the vehicle for reusage.
addCommandHandler( "loadhandling",
    function(player)
        local handlingName = getPlayerName( player ) .. "_saved_handling.dat";

        if ( fileExists( handlingName ) ) then
            local myVehicle = getPedOccupiedVehicle( player );

            if ( myVehicle ) then
                local handlingFile = fileOpen( handlingName );

                if ( handlingFile ) then
                    local handling = loadVehicleHandling( handlingFile );

                    handlingFile:destroy();

                    -- Apply the saved handling.
                    for m,n in pairs( handling ) do
                        setVehicleHandling( myVehicle, m, n );
                    end

                    outputChatBox( "successfully restored handling" );
                end
            end
        end
    end
);
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) File Functions

- [read](mta://reference/misc/mta-eir-filesystem-file-read.md)

- [readByte](mta://reference/misc/mta-eir-filesystem-file-readbyte.md)

- [readUByte](mta://reference/misc/mta-eir-filesystem-file-readubyte.md)

- [readShort](mta://reference/misc/mta-eir-filesystem-file-readshort.md)

- [readUShort](mta://reference/misc/mta-eir-filesystem-file-readushort.md)

- [readInt](mta://reference/misc/mta-eir-filesystem-file-readint.md)

- [readUInt](mta://reference/misc/mta-eir-filesystem-file-readuint.md)

- readFloat

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
