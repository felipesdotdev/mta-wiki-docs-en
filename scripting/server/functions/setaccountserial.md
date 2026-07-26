---
doc_id: "mta-wiki:14592"
title: "SetAccountSerial"
source_title: "SetAccountSerial"
source_url: "https://wiki.multitheftauto.com/wiki/SetAccountSerial"
revision_id: 82302
language: "en"
categories: ["Server_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:37.858215+00:00"
---

# SetAccountSerial

ADDED/UPDATED IN VERSION 1.6.0 [r23232](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23232):

This function sets the serial number for a specified player account. It allows administrators to update or assign a new [serial](mta://reference/misc/serial.md) to registered accounts. 

## Syntax

```
bool setAccountSerial ( account theAccount, string serial )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):setSerial(...)*

**Variable**: *.serial*

### Required Arguments

- **theAccount:** The account element to set the serial for

- **serial:** A valid 32-character hexadecimal string representing the new serial number

### Returns

Returns *true* if the serial was successfully set, *false* otherwise.

## Example

```
-- Simple example: Set a serial for a player's account
local player = getPlayerFromName("John")
local account = getPlayerAccount(player)
local newSerial = "A1B2C3D4E5F6789012345678901234AB"

if setAccountSerial(account, newSerial) then
    outputChatBox("Serial updated successfully!")
else
    outputChatBox("Failed to update serial!")
end
```

```
-- Advanced example: Administrative command system
function changePlayerSerial(player, newSerial)
    local account = getPlayerAccount(player)
    if account and not isGuestAccount(account) then
        if setAccountSerial(account, newSerial) then
            outputChatBox("Serial number updated successfully!", player, 0, 255, 0)
            return true
        else
            outputChatBox("Failed to update serial number. Invalid format!", player, 255, 0, 0)
            return false
        end
    else
        outputChatBox("You must be logged into a registered account.", player, 255, 0, 0)
        return false
    end
end

-- Command to set a player's account serial
addCommandHandler("setserial", function(player, cmd, targetPlayer, newSerial)
    if not targetPlayer or not newSerial then
        outputChatBox("Usage: /setserial <player> <32-char-hex-serial>", player)
        return
    end
    
    local target = getPlayerFromName(targetPlayer)
    if target then
        if string.len(newSerial) == 32 and string.match(newSerial, "^[A-Fa-f0-9]+$") then
            changePlayerSerial(target, newSerial)
        else
            outputChatBox("Serial must be 32 hexadecimal characters!", player, 255, 0, 0)
        end
    else
        outputChatBox("Player not found!", player, 255, 0, 0)
    end
end)
```

## See Also

- [getAccountSerial](mta://scripting/server/functions/getaccountserial.md)

- [getAccountsBySerial](mta://scripting/server/functions/getaccountsbyserial.md)

- [addAccount](mta://scripting/server/functions/addaccount.md)

- [removeAccount](mta://scripting/server/functions/removeaccount.md)

- [isGuestAccount](mta://scripting/server/functions/isguestaccount.md)

- [getPlayerAccount](mta://scripting/server/functions/getplayeraccount.md)

- [addAccount](mta://scripting/server/functions/addaccount.md)

- [copyAccountData](mta://scripting/server/functions/copyaccountdata.md)

- [getAccount](mta://scripting/server/functions/getaccount.md)

- [getAccountData](mta://scripting/server/functions/getaccountdata.md)

- [getAccountName](mta://scripting/server/functions/getaccountname.md)

- [getAccountPlayer](mta://scripting/server/functions/getaccountplayer.md)

- [getAccountSerial](mta://scripting/server/functions/getaccountserial.md)

- [getAccounts](mta://scripting/server/functions/getaccounts.md)

- [getAccountsBySerial](mta://scripting/server/functions/getaccountsbyserial.md)

- [getAllAccountData](mta://scripting/server/functions/getallaccountdata.md)

- [getPlayerAccount](mta://scripting/server/functions/getplayeraccount.md)

- [isGuestAccount](mta://scripting/server/functions/isguestaccount.md)

- [logIn](mta://scripting/server/functions/login.md)

- [logOut](mta://scripting/server/functions/logout.md)

- [removeAccount](mta://scripting/server/functions/removeaccount.md)

- [setAccountData](mta://scripting/server/functions/setaccountdata.md)

- [setAccountPassword](mta://scripting/server/functions/setaccountpassword.md)

- [getAccountByID](mta://scripting/server/functions/getaccountbyid.md)

- [getAccountID](mta://scripting/server/functions/getaccountid.md)

- [getAccountIP](mta://scripting/server/functions/getaccountip.md)

- [getAccountsByData](mta://scripting/server/functions/getaccountsbydata.md)

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
