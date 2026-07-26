---
doc_id: "mta-wiki:14172"
title: "SetDiscordRichPresenceState"
source_title: "SetDiscordRichPresenceState"
source_url: "https://wiki.multitheftauto.com/wiki/SetDiscordRichPresenceState"
revision_id: 78347
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# SetDiscordRichPresenceState

| [[{{{image}}}\|link=\|]] | Important Note: To use this function, you must set up your own application setDiscordApplicationID |
| --- | --- |
|  |  |

ADDED/UPDATED IN VERSION 1.6.0 [r22270](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22270):

This function sets the status of the Discord Rich Presence application.

## Syntax

```
bool setDiscordRichPresenceState(string state)
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DiscordRPC](https://wiki.multitheftauto.com/index.php?title=DiscordRPC&action=edit&redlink=1):setState(...)*

### Required arguments

- **state**: a string containing the status text

### Returns

Returns *true* if function succeeds, *false* otherwise.

## Example

This example shows how to set the state of the Discord Rich Presence application.

```
local app_id = "YOUR_APPLICATION_ID"
if setDiscordApplicationID(app_id) then 
    setDiscordRichPresenceState("waiting in lobby")
end
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

- setDiscordRichPresenceState

ADDED/UPDATED IN VERSION 1.6.0 [r22276](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22276):

- [setDiscordRichPresencePartySize](mta://scripting/client/functions/setdiscordrichpresencepartysize.md)

- [setDiscordRichPresenceStartTime](mta://scripting/client/functions/setdiscordrichpresencestarttime.md)

- [setDiscordRichPresenceEndTime](mta://scripting/client/functions/setdiscordrichpresenceendtime.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22342](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22342):

- [getDiscordRichPresenceUserID](mta://scripting/client/functions/getdiscordrichpresenceuserid.md)
