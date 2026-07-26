---
doc_id: "mta-wiki:9860"
title: "Resource : Settingsmanager"
source_title: "Resource:Settingsmanager"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ASettingsmanager"
revision_id: 53277
language: "en"
categories: []
generated_at: "2026-07-26T16:17:14.288029+00:00"
---

# Resource : Settingsmanager

[Settings manager](https://community.multitheftauto.com/index.php?p=resources&s=details&id=15127) is a simple resource to save/load player settings (any data). All settings stored client-side in a XML file placed using private [filepath](mta://reference/misc/filepath.md) ( *\MTA San Andreas\mods\deathmatch\priv\<server-id>\settingsmanager* )

## Exported functions:

```
saveSetting ( string settingName, var value [, string resourceName ] )
```

Returns *true* if value was successfully saved, *false* otherwise.

```
loadSetting ( string settingName [, string resourceName ] )
```

Returns the value if it was received successfully, *nil* otherwise. Strings "true" and "false" will be returned as booleans.

- Last argument is optional for both functions. It used to store settings in XML file under resourceName node. Default argument is the resource name of the resource which called the exported function.  See example below for more information.

## Example:

For example we have a "language-manager" resource with script like this:

```
function changeLanguage ( _, newLang )
   if no newLang then
      outputChatBox('Error. Command syntax: /lang <language name>. Available languages: "english", "russian"')
      return
   end
   exports.settingsmanager:saveSetting("language", newLang)
end
addCommandHandler( "lang", changeLaguage )

function onStart ()
   local playerLanguage = exports.settingsmanager:loadSetting ( "language" )
   if playerLanguage == nil then --if no language set
       playerLanguage = "english"
       exports.settingsmanager:saveSetting("language", playerLanguage ) --set default language
   end
   outputChatBox ( "Current language is " ..playerLanguage.. ". Type /language to change")
end
addEventHandler( "onClientResourceStart", resourceRoot, onStart )
```

Then XML file will look like this:

```
<settings>
    <language-manager>
        <language>english</language>
    </language-manager>
</settings>
```

XML node called "language-manager" because resource name of the resource which called exported function is "language-manager".
