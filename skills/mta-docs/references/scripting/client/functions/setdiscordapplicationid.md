---
doc_id: "mta-wiki:14169"
title: "SetDiscordApplicationID"
source_title: "SetDiscordApplicationID"
source_url: "https://wiki.multitheftauto.com/wiki/SetDiscordApplicationID"
revision_id: 78350
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# SetDiscordApplicationID

| [[{{{image}}}\|link=\|]] | Important Note: To reset the application ID, please use resetDiscordRichPresenceData |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Important Note: In order for the function to work correctly, the user must have their activity privacy/status enabled in Discord. |
| --- | --- |
|  |  |

ADDED/UPDATED IN VERSION 1.6.0 [r22270](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22270):

The function can assign your own application to use in Rich Presence.
You can create an application **[here](https://discord.com/developers/applications)**

## Syntax

```
bool setDiscordApplicationID(string applicationID)
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DiscordRPC](https://wiki.multitheftauto.com/index.php?title=DiscordRPC&action=edit&redlink=1):setApplication(...)*

### Required arguments

- **applicationID**: a string representing your Discord application's ID.

### Returns

Returns *true* if function succeeds, *false* if the client has disabled rich presence.

## Example

This example outputs whether the application was successfully setup and sets a custom asset image.

```
local app_id = "YOUR_APPLICATION_ID"
if setDiscordApplicationID(app_id) then 
    setDiscordRichPresenceAsset("asset_name_from_application")
    outputChatBox("Yay, we're now using our own application!")
end
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22270](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22270):

- [isDiscordRichPresenceConnected](mta://scripting/client/functions/isdiscordrichpresenceconnected.md)

- [resetDiscordRichPresenceData](mta://scripting/client/functions/resetdiscordrichpresencedata.md)

- setDiscordApplicationID

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
