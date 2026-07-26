---
doc_id: "mta-wiki:14168"
title: "ResetDiscordRichPresenceData"
source_title: "ResetDiscordRichPresenceData"
source_url: "https://wiki.multitheftauto.com/wiki/ResetDiscordRichPresenceData"
revision_id: 82342
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# ResetDiscordRichPresenceData

ADDED/UPDATED IN VERSION 1.6.0 [r22270](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22270):

The function resets the Discord Rich Presence configuration to default.

## Syntax

```
bool resetDiscordRichPresenceData()
```

### Returns

Returns *true* if function succeeds, *false* otherwise.

## Example

The example shows how to reset Discord Rich Presence after using a custom application.

```
setDiscordApplicationID("you_application_key")
setDiscordRichPresenceAsset("asset_logo", "Name of Asset")
if resetDiscordRichPresenceData()  then -- we reset to default by MTA Application.
    outputChatBox("Discord Rich Presence has been cleared and restored to default settings.")
end
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22270](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22270):

- [isDiscordRichPresenceConnected](mta://scripting/client/functions/isdiscordrichpresenceconnected.md)

- resetDiscordRichPresenceData

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
