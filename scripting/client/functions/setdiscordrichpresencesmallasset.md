---
doc_id: "mta-wiki:14171"
title: "SetDiscordRichPresenceSmallAsset"
source_title: "SetDiscordRichPresenceSmallAsset"
source_url: "https://wiki.multitheftauto.com/wiki/SetDiscordRichPresenceSmallAsset"
revision_id: 78204
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:39.438989+00:00"
---

# SetDiscordRichPresenceSmallAsset

| [[{{{image}}}\|link=\|]] | Important Note: To use this function, you must set up your own application setDiscordApplicationID |
| --- | --- |
|  |  |

ADDED/UPDATED IN VERSION 1.6.0 [r22270](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22270):

Using this function, you can set the small image asset of the application. The maximum size of assets is *1024x1024*, the minimum *512x512*.

## Syntax

```
bool setDiscordRichPresenceSmallAsset(string assetImage, string text)
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DiscordRPC](https://wiki.multitheftauto.com/index.php?title=DiscordRPC&action=edit&redlink=1):setSmallAsset(...)*

### Required arguments

- **assetImage**: a string containing the key of the small image asset you uploaded to your application's asset list.

- **text**: a string containing the hover text of the small image asset.

### Returns

Returns *true* if function succeeds, *false* otherwise.

## Example

The example sets the small image asset to my_logo.

```
addCommandHandler("setsmalllogo",
    function ()
        if isDiscordRichPresenceConnected() then 
            setDiscordRichPresenceSmallAsset("my_small_logo", "This is my small logo!")
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

- setDiscordRichPresenceSmallAsset

- [setDiscordRichPresenceState](mta://scripting/client/functions/setdiscordrichpresencestate.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22276](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22276):

- [setDiscordRichPresencePartySize](mta://scripting/client/functions/setdiscordrichpresencepartysize.md)

- [setDiscordRichPresenceStartTime](mta://scripting/client/functions/setdiscordrichpresencestarttime.md)

- [setDiscordRichPresenceEndTime](mta://scripting/client/functions/setdiscordrichpresenceendtime.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22342](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22342):

- [getDiscordRichPresenceUserID](mta://scripting/client/functions/getdiscordrichpresenceuserid.md)
