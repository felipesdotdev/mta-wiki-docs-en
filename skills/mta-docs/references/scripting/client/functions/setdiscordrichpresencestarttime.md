---
doc_id: "mta-wiki:14175"
title: "SetDiscordRichPresenceStartTime"
source_title: "SetDiscordRichPresenceStartTime"
source_url: "https://wiki.multitheftauto.com/wiki/SetDiscordRichPresenceStartTime"
revision_id: 78342
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# SetDiscordRichPresenceStartTime

| [[{{{image}}}\|link=\|]] | Important Note: To use this function, you must set up your own application setDiscordApplicationID |
| --- | --- |
|  |  |

ADDED/UPDATED IN VERSION 1.6.0 [r22276](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22276):

This function sets the elapsed time of Discord Rich Presence.

## Syntax

```
bool setDiscordRichPresenceStartTime(int seconds)
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DiscordRPC](https://wiki.multitheftauto.com/index.php?title=DiscordRPC&action=edit&redlink=1):setStartTime(...)*

### Required arguments

- **seconds**: an integer representing the number of seconds that has elapsed. If 0, the timer will not be displayed.

### Returns

Returns *true* if function succeeds, *false* otherwise.

## Example

This example shows how to change the elapsed timer of the Discord Rich Presence application.

```
local app_id = "YOUR_APPLICATION_ID"
if setDiscordApplicationID(app_id) then 
    setDiscordRichPresenceState("In-game")
    setDiscordRichPresenceStartTime(1)
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

- [setDiscordRichPresenceState](mta://scripting/client/functions/setdiscordrichpresencestate.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22276](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22276):

- [setDiscordRichPresencePartySize](mta://scripting/client/functions/setdiscordrichpresencepartysize.md)

- setDiscordRichPresenceStartTime

- [setDiscordRichPresenceEndTime](mta://scripting/client/functions/setdiscordrichpresenceendtime.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22342](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22342):

- [getDiscordRichPresenceUserID](mta://scripting/client/functions/getdiscordrichpresenceuserid.md)
