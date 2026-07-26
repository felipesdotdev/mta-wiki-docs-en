---
doc_id: "mta-wiki:14167"
title: "IsDiscordRichPresenceConnected"
source_title: "IsDiscordRichPresenceConnected"
source_url: "https://wiki.multitheftauto.com/wiki/IsDiscordRichPresenceConnected"
revision_id: 82341
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# IsDiscordRichPresenceConnected

ADDED/UPDATED IN VERSION 1.6.0 [r22270](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22270):

The function checks if the client has Discord Rich Presence enabled.

## Syntax

```
bool isDiscordRichPresenceConnected()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DiscordRPC](https://wiki.multitheftauto.com/index.php?title=DiscordRPC&action=edit&redlink=1):isConnected(...)*

### Returns

Returns *true* if Discord Rich Presence is enabled on the client, *false* if disabled.

## Example

This example outputs whether the client has enabled Discord Rich Presence.

```
addCommandHandler("checkdiscord",
    function ()
        if isDiscordRichPresenceConnected() then 
            outputChatBox("You are using Discord Rich Presence, that's cool!")
        end 
    end
)
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22270](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22270):

- isDiscordRichPresenceConnected

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

- [getDiscordRichPresenceUserID](mta://scripting/client/functions/getdiscordrichpresenceuserid.md)
