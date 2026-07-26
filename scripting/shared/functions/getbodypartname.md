---
doc_id: "mta-wiki:1736"
title: "GetBodyPartName"
source_title: "GetBodyPartName"
source_url: "https://wiki.multitheftauto.com/wiki/GetBodyPartName"
revision_id: 59190
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:07.589690+00:00"
---

# GetBodyPartName

This function is used to get the name of a body part on a player.

## Syntax

```
string getBodyPartName ( int bodyPartID )
```

### Required Arguments

- **bodyPartID**: An integer representing the body part ID you wish to retrieve the name of.

- **3:** Torso

- **4:** Ass

- **5:** Left Arm

- **6:** Right Arm

- **7:** Left Leg

- **8:** Right Leg

- **9:** Head

## Returns

This function returns a string containing the body part name if the ID is valid, *false* otherwise.

## Example

This example prints the killer and body part to the chat on the wasted/kill event.

```
function deathMessageOnWasted ( ammo, attacker, weapon, bodypart )
  if ( attacker ) then                                    -- if we have an attacker
    if ( getElementType ( attacker ) == "player" ) then   -- make sure the element that killed him was a player
      tempString = getPlayerName ( attacker ) .. " killed " .. getPlayerName ( source ) .. " (" .. getWeaponNameFromID ( weapon ) .. ")"
      if ( bodypart == 9 ) then -- if he was shot in the head
        tempString = tempString .. " (HEADSHOT!)"
      else
        tempString = tempString .. " (" .. getBodyPartName ( bodypart ) .. ")"
      end
      outputChatBox ( tempString )
    else
      outputChatBox ( getPlayerName ( source ) .. " died. (" .. getWeaponNameFromID ( weapon ) .. ") (" .. getBodyPartName ( bodypart ) .. ")" )
    end
  else
    outputChatBox ( getPlayerName ( source ) .. " died. (" .. getWeaponNameFromID ( weapon ) .. ") (" .. getBodyPartName ( bodypart ) .. ")" )
  end
end
addEventHandler ( "onPlayerWasted", root, deathMessageOnWasted )
```

## See Also

- getBodyPartName

- [getClothesByTypeIndex](mta://scripting/shared/functions/getclothesbytypeindex.md)

- [getClothesTypeName](mta://scripting/shared/functions/getclothestypename.md)

- [getTypeIndexFromClothes](mta://scripting/shared/functions/gettypeindexfromclothes.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r23124](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23124))

- [addClothingModel](mta://scripting/client/functions/addclothingmodel.md)
