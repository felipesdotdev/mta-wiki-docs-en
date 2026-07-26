---
doc_id: "mta-wiki:14176"
title: "SetDiscordRichPresencePartySize"
source_title: "SetDiscordRichPresencePartySize"
source_url: "https://wiki.multitheftauto.com/wiki/SetDiscordRichPresencePartySize"
revision_id: 78346
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# SetDiscordRichPresencePartySize

| [[{{{image}}}\|link=\|]] | Important Note: To use this function, you must set up your own application setDiscordApplicationID |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: For the party size to be displayed, the state must be set setDiscordRichPresenceState |
| --- | --- |
|  |  |

ADDED/UPDATED IN VERSION 1.6.0 [r22276](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22276):

This function sets the party size of Discord Rich Presence.

## Syntax

```
bool setDiscordRichPresencePartySize(int size, int max)
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DiscordRPC](https://wiki.multitheftauto.com/index.php?title=DiscordRPC&action=edit&redlink=1):setPartySize(...)*

### Required arguments

- **size**: an integer representing the current party size.

- **max**: an integer representing the maximum party size.

**If both values are 0, the party size will not be displayed**

### Returns

Returns *true* if function succeeds, *false* otherwise.

## Example

This example shows how to change the party size of the Discord Rich Presence application.

```
local app_id = "YOUR_APPLICATION_ID"
if setDiscordApplicationID(app_id) then 
    setDiscordRichPresenceState("In-game")
    setDiscordRichPresencePartySize(1, 32)
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

- setDiscordRichPresencePartySize

- [setDiscordRichPresenceStartTime](mta://scripting/client/functions/setdiscordrichpresencestarttime.md)

- [setDiscordRichPresenceEndTime](mta://scripting/client/functions/setdiscordrichpresenceendtime.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22342](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22342):

- [getDiscordRichPresenceUserID](mta://scripting/client/functions/getdiscordrichpresenceuserid.md)
