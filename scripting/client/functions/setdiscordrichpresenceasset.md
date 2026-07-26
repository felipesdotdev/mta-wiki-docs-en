---
doc_id: "mta-wiki:14170"
title: "SetDiscordRichPresenceAsset"
source_title: "SetDiscordRichPresenceAsset"
source_url: "https://wiki.multitheftauto.com/wiki/SetDiscordRichPresenceAsset"
revision_id: 78201
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:39.346989+00:00"
---

# SetDiscordRichPresenceAsset

| [[{{{image}}}\|link=\|]] | Important Note: To use this function, you must set up your own application setDiscordApplicationID |
| --- | --- |
|  |  |

ADDED/UPDATED IN VERSION 1.6.0 [r22270](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22270):

Using this function you can set the large image asset of the application. The maximum size of assets is *1024x1024*, the minimum is *512x512*.

## Syntax

```
bool setDiscordRichPresenceAsset(string assetImage, string text)
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DiscordRPC](https://wiki.multitheftauto.com/index.php?title=DiscordRPC&action=edit&redlink=1):setAsset(...)*

### Required arguments

- **assetImage**: a string containing the key of the image you uploaded to your application's asset list.

- **text**: a string to be displayed when someone hovers over the large image asset in Discord.

### Returns

Returns *true* if function succeeds, *false* otherwise.

## Example

The example sets the large image asset to my_logo.

```
addCommandHandler("setlogo",
    function ()
        if isDiscordRichPresenceConnected() then 
            setDiscordRichPresenceAsset("my_logo", "This is my logo!")
        end 
    end
)
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22270](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22270):

- [isDiscordRichPresenceConnected](mta://scripting/client/functions/isdiscordrichpresenceconnected.md)

- [resetDiscordRichPresenceData](mta://scripting/client/functions/resetdiscordrichpresencedata.md)

- [setDiscordApplicationID](mta://scripting/client/functions/setdiscordapplicationid.md)

- setDiscordRichPresenceAsset

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
