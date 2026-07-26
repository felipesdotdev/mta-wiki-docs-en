---
doc_id: "mta-wiki:7524"
title: "MTA:Eir/FileSystem/file/readByte"
source_title: "MTA:Eir/FileSystem/file/readByte"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/file/readByte"
revision_id: 73555
language: "en"
categories: []
generated_at: "2026-07-26T16:16:05.630018+00:00"
---

# MTA:Eir/FileSystem/file/readByte

This function attempts to read a signed byte (native type) from a file and returns it. The amount of bytes read should be one.

## Syntax

```
signed_byte file:readByte ()
```

## Returns

Returns the signed byte if it was successfully read from the file, **false** otherwise.

## Example

Click to collapse [-]
Server

This snippet writes a snapshot of server-side player information into a file. This is a system that keeps persistent player data on a server based on the nickname. It should be expanded to manage the lifetime of player information, so the database does not grow too big. This is theoretical code and should be used as basis.

```
-- Create the filesystem interface.
local fsys = createFilesystemInterface();

if not ( fsys ) then
    outputDebugString( "could not acquire filesystem interface handle" );
    return false;
end

-- Get a file translator to this resource.
local resRoot = fsys.createTranslator( "mods/deathmatch/resources/playerManager/" );

-- Keep track of player information.
local playerData = {};

local function createPlayerInfo( nickname )
    local info = {
        nickname = nickname,
        weapons = {},
        player = false
    };
    
    function info.setPlayer( player )
        if ( player ) then
            local weapons = info.weapons;

            for m=1,12 do
                local weapInfo = weapons[m];

                if ( weapInfo ) then
                    -- Update the players weapon information.
                    setPlayerWeapon( m, weapInfo.weaponType );
                    setPlayerAmmoInClip( m, weapInfo.currentAmmo );
                    setPlayerTotalAmmo( m, weapInfo.maxAmmo );
                end
            end
        end

        -- Save the player object.
        info.player = player;
    end

    function info.saveState()
        local weapons = info.weapons;
        local player = info.player;

        if ( player ) then return; end;

        for m=1,12 do
            weapons[m] = {
                weaponType = getPlayerWeapon( player ),
                currentAmmo = getPlayerAmmoInClip( player ),
                maxAmmo = getPlayerTotalAmmo( player )
            };
        end
    end

    return info;
end

-- Utilities for writing and reading short strings.
-- Here our byte functions come into play.
local function readSmallString( theFile )
    theFile:read( theFile:readUByte() );
end

local function writeSmallString( theFile, string )
    theFile:writeUByte( #string );
    theFile:write( string );
end

-- Create player information from persistent storage.
local storageFile = false;

if ( resRoot:exists( "player.dat" ) ) then
    -- Load player information.
    storageFile = resRoot:open( "player.dat", "rb+" );

    -- Make sure we could open the file correctly.
    if ( storageFile ) then
        -- Read the header.
        local numPlayerEntries = storageFile:readInt();

        -- Process each player entry.
        local n = 1;

        while ( n <= numPlayerEntries ) do
            local nickname = readSmallString( storageFile );
            local weapons = {};

            for m=1,12 do
                local info = {
                    weaponType = theFile:readUByte(),
                    currentAmmo = theFile:readUShort(),
                    totalAmmo = theFile:readUShort()
                };
                table.insert( weapons, info );
            end

            -- Create and store the player information.
            local playerInfo = createPlayerInfo( nickname );
            playerInfo.weapons = weapons;

            table.insert( playerData, playerInfo );
        end
    end
else
    storageFile = resRoot:open( "player.dat", "wb" );
end

local function getPlayerInfo( player, createNew )
    if ( createNew == nil ) then createNew = true; end

    -- Attempt to get by player handle.
    for m,n in ipairs(playerData) do
        if ( n.player == player ) then
            return n;
        end
    end

    -- Attempt to get by player nick.
    local nickname = getPlayerName( player );

    for m,n in ipairs(playerData) do
        if ( n.nickname == nickname ) then
            n.setPlayer( player );
            return n;
        end
    end

    if ( createNew ) then
        -- We found nothing, so lets create a new player info.
        local newInfo = createPlayerInfo( nickname );
        newInfo.setPlayer( player );
        return newInfo;
    end

    return false;
end

addEventHandler( "onPlayerJoin", root,
    function()
        -- Cache the player information.
        getPlayerInfo( source );
    end
);

addEventHandler( "onPlayerQuit", root,
    function()
        -- Make sure we do not have a player information attached to the quit player anymore.
        local info = getPlayerInfo( source, false );

        if not ( info ) then return; end;

        info.saveStatus();
        info.setPlayer( false );
    end
);

addEventHandler( "onResourceStop", resourceRoot,
    function()
        -- Store the player information to disk.
        if ( storageFile ) then
            -- Write the number of playerData entries.
            storageFile:writeInt( #playerData );

            for m,n in ipairs( playerData ) do
                -- Make sure the info is up to date.
                n.saveState();

                -- Write player header.
                writeSmallString( storageFile, getPlayerName( n.nickname ) );

                -- Now write the player information.
                for m,n in ipairs( n.weapons ) do
                    theFile:writeUByte( n.weaponType );
                    theFile:writeUShort( n.currentAmmo );
                    theFile:writeUShort( n.maxAmmo );
                end
            end

            -- Clean up the file handle.
            storageFile:destroy();

            -- We are finished saving. Tell the server owner.
            outputDebugString( "wrote persistent player storage." );
        end
    end
);
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) File Functions

- [read](mta://reference/misc/mta-eir-filesystem-file-read.md)

- readByte

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
