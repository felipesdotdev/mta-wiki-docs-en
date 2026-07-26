---
doc_id: "mta-wiki:1575"
title: "OutputDebugString"
source_title: "OutputDebugString"
source_url: "https://wiki.multitheftauto.com/wiki/OutputDebugString"
revision_id: 79628
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# OutputDebugString

This function outputs scripting debug messages, which can be read by enabling the debug textbox. The debug display level can then be set so that info or warning messages get filtered out.

## Syntax

```
bool outputDebugString ( string text, [ int level=3, int red=255, int green=255, int blue=255 ] )
```

### Required Arguments

- **text:** the text to be output to the debug box.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **level:** the debug message level. Possible values are:

- **0:** Debug message

- **1:** Error message

- **2:** Warning message

- **3:** Information message (default)

- **4:** Custom message (omits file path and line number)

- **red:** The amount of red in the color of the text. Default value is 255.

- **green:** The amount of green in the color of the text. Default value is 255.

- **blue:** The amount of blue in the color of the text. Default value is 255.

| [[{{{image}}}\|link=\|]] | Note: Color values are only applied when debug level is 0 or 4. |
| --- | --- |
|  |  |

### Returns

Returns *true* if the debug message was successfully output, *false* if invalid arguments are specified.

## Example

Click to collapse [-]
Server

This script notifies when its resource has been loaded using a debug message:

```
function resourceStartNotify ( resourcename )
	-- if the started resource is this one
	if ( resourcename == getThisResource() ) then
		-- send an info debug message as a notification
		outputDebugString ( "Resource " .. getResourceName(resourcename) .. " loaded." )
	end
end
addEventHandler( "onResourceStart", root, resourceStartNotify )
```

## See Also

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIpFromMasterServer](mta://scripting/server/functions/getserveripfrommasterserver.md)

- [getServerName](mta://scripting/server/functions/getservername.md)

- [getServerPassword](mta://scripting/server/functions/getserverpassword.md)

- [getServerPort](mta://scripting/server/functions/getserverport.md)

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)
