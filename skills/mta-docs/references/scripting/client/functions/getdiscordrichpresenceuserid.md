---
doc_id: "mta-wiki:14201"
title: "GetDiscordRichPresenceUserID"
source_title: "GetDiscordRichPresenceUserID"
source_url: "https://wiki.multitheftauto.com/wiki/GetDiscordRichPresenceUserID"
revision_id: 78678
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# GetDiscordRichPresenceUserID

| [[{{{image}}}\|link=\|]] | Important Note: The function will correctly return the UserID if the user has given consent beforehand and is connected to the Rich Presence application. |
| --- | --- |
|  |  |

ADDED/UPDATED IN VERSION 1.6.0 [r22342](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22342):

The function returns the client Discord UserID.

## Syntax

```
string getDiscordRichPresenceUserID()
```

### Returns

It will return an *empty string ("")* if the user has not given consent or has disabled the Rich Presence synchronization option. Otherwise, it will return the *userid* as a string.

## Example

This example displays the user's userid in the chat if they have granted permission to share data. Otherwise, they will receive an appropriate message.

```
addCommandHandler("getmyuserid",
    function ()
        if isDiscordRichPresenceConnected() then
            local id = getDiscordRichPresenceUserID() 
            if id == "" then 
                outputChatBox("You didn't allow consent to share Discord data! Grant permission in the settings!")
            else 
                outputChatBox("Your Discord userid: "..id)
            end 
        end 
    end
)
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22270](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22270):

- [isDiscordRichPresenceConnected](mta://scripting/client/functions/isdiscordrichpresenceconnected.md)

- [resetDiscordRichPresenceData](mta://scripting/client/functions/resetdiscordrichpresencedata.md)

- [setDiscordApplicationID](mta://scripting/client/functions/setdiscordapplicationid.md)

- [setDiscordRichPresenceAsset](mta://scripting/client/functions/setdiscordrichpresenceasset.md)

- [setDiscordRichPresenceButton](mta://scripting/client/functions/setdiscordrichpresencebutton.md)

- [setDiscordRichPresenceDetails](mta://scripting/client/functions/setdiscordrichpresencedetails.md)

- [setDiscordRichPresenceSmallAsset](mta://scripting/client/functions/setdiscordrichpresencesmallasset.md)

- [setDiscordRichPresenceState](mta://scripting/client/functions/setdiscordrichpresencestate.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22276](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22276):

- [setDiscordRichPresencePartySize](mta://scripting/client/functions/setdiscordrichpresencepartysize.md)

- [setDiscordRichPresenceStartTime](mta://scripting/client/functions/setdiscordrichpresencestarttime.md)

- [setDiscordRichPresenceEndTime](mta://scripting/client/functions/setdiscordrichpresenceendtime.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22342](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22342):

- getDiscordRichPresenceUserID
