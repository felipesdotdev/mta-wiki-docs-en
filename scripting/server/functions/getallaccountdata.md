---
doc_id: "mta-wiki:6078"
title: "GetAllAccountData"
source_title: "GetAllAccountData"
source_url: "https://wiki.multitheftauto.com/wiki/GetAllAccountData"
revision_id: 81070
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:06.809697+00:00"
---

# GetAllAccountData

This function returns a table containing all the user data for the [account](mta://reference/misc/account.md) provided

## Syntax

```
table getAllAccountData ( account theAccount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):getAllData(...)*

**Variable**: *.data*

### Required Arguments

- **theAccount:** The account you wish to retrieve all data from.

### Returns

A [table](mta://reference/misc/table.md) containing all the user data. This table might be empty.

## Example

```
function printAllData ( thePlayer )
    local playerAccount = getPlayerAccount( thePlayer ) -- get his account
    if ( playerAccount ) then -- if we got the account then
        local data = getAllAccountData( playerAccount ) -- get data
        count = 0
        for _ in pairs(data) do count = count + 1 end -- get the count
        outputChatBox ( "table holds " .. count .. " entries" ) -- output number of rows
        if ( data ) then
            for k,v in pairs ( data ) do
                outputChatBox(k..": "..v) -- print the key and value of each entry of data
            end
        end
    end
end
addCommandHandler( "getall", printAllData ) -- add a command handler for command 'getall'
```

## See Also

- [addAccount](mta://scripting/server/functions/addaccount.md)

- [copyAccountData](mta://scripting/server/functions/copyaccountdata.md)

- [getAccount](mta://scripting/server/functions/getaccount.md)

- [getAccountData](mta://scripting/server/functions/getaccountdata.md)

- [getAccountName](mta://scripting/server/functions/getaccountname.md)

- [getAccountPlayer](mta://scripting/server/functions/getaccountplayer.md)

- [getAccountSerial](mta://scripting/server/functions/getaccountserial.md)

- [getAccounts](mta://scripting/server/functions/getaccounts.md)

- [getAccountsBySerial](mta://scripting/server/functions/getaccountsbyserial.md)

- getAllAccountData

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
