---
doc_id: "mta-wiki:13794"
title: "Code snippet for extracting weapon stats"
source_title: "Code snippet for extracting weapon stats"
source_url: "https://wiki.multitheftauto.com/wiki/Code_snippet_for_extracting_weapon_stats"
revision_id: 79873
language: "en"
categories: ["Scripting_Concepts", "Development"]
---

# Code snippet for extracting weapon stats

Code snippet which might be used to extract weapon stats:

```
count = 22
statid = 3

addCommandHandler("dump", function ()
    while (count < 33) do
        hFile = fileOpen ( "dump.txt" )
        fileSetPos(hFile, fileGetSize ( hFile ))
        i = count
        fileWrite(hFile, "// " .. i .. " - " .. getWeaponNameFromID( i ) .. " Stat: " .. statid )
        fileWrite(hFile, "\r\n")
        for k,v in ipairs(props) do
            outputChatBox(v)
            fileWrite(hFile, Dump(v))
            fileWrite(hFile, "\r\n")
        end
        fileClose(hFile)
        count = count + 1
    end
end)

function Array()
    if (statid == 3) then
        return "OriginalHitmanData["
    elseif ( statid == 2 ) then
        return "OriginalGangsterData["
    else
        return "OriginalWeaponData["
    end
end

function Dump(strInfo)
    i = count
    -- Special case for Vectors
    if ( strInfo == "fire_offset") then
        fx, fy, fz = getWeaponProperty(i, statid, strInfo)
        return Array() .. i .. "]." .. strInfo .. " = CVector ( " .. floatify ( fx ) .. ", " .. floatify ( fy ) .. ", " .. floatify ( fz ) .. " );"
    end
    -- Avoids compile errors ( Cannot convert from x to y )
    if ( strInfo == "skill_level" ) then
        return Array() .. i .. "]." .. strInfo .. " = (eWeaponSkill) " .. getWeaponProperty(i, statid, strInfo) .. ";"
    end
    if ( strInfo == "weapon_slot" ) then
        return Array() .. i .. "]." .. strInfo .. " = (eWeaponSlot) " .. getWeaponProperty(i, statid, strInfo) .. ";"
    end
    if ( strInfo == "fire_type" ) then
        return Array() .. i .. "]." .. strInfo .. " = (eFireType) " .. getWeaponProperty(i, statid, strInfo) .. ";"
    end
    -- end
    -- Avoids Conversion from Double to float warnings.
    if ( strInfo == "weapon_range" or strInfo == "target_range" or strInfo == "accuracy" or strInfo == "move_speed" or strInfo == "anim_loop_start" or
strInfo == "anim_loop_stop" or strInfo == "anim_loop_bullet_fire" or strInfo == "anim2_loop_start" or strInfo == "anim2_loop_stop" or strInfo ==
"anim2_loop_bullet_fire" or strInfo == "anim_breakout_time" or strInfo == "firing_speed" or strInfo == "radius" or strInfo == "life_span" or strInfo ==
"spread") then return Array() .. i .. "]." .. strInfo .. " = " .. floatify ( getWeaponProperty(i, statid, strInfo) ) .. ";" end
    -- Default
    return Array() .. i .. "]." .. strInfo .. " = " .. getWeaponProperty(i, statid, strInfo) .. ";"
end

-- Avoids conversion from Double to float warnings.
function floatify ( fVal )
    if ( fVal == math.floor( fVal ) or fVal == math.ceil( fVal ) ) then
        return fVal .. ".0f"
    end
    return fVal .. "f"
end
```

(mtasa-blue source code contains link to this page)

(moved from [multitheftauto/mtasa-blue/blob/c58c3678f263d810f61eb5aecba48e6c4b4dce0c/Client/game_sa/CWeaponStatManagerSA.cpp#L153-L219](https://github.com/multitheftauto/mtasa-blue/blob/c58c3678f263d810f61eb5aecba48e6c4b4dce0c/Client/game_sa/CWeaponStatManagerSA.cpp#L153-L219))
