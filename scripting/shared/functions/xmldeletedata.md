---
doc_id: "mta-wiki:11736"
title: "XmlDeleteData"
source_title: "XmlDeleteData"
source_url: "https://wiki.multitheftauto.com/wiki/XmlDeleteData"
revision_id: 64327
language: "en"
categories: ["Useful_Functions"]
generated_at: "2026-07-26T16:17:07.775789+00:00"
---

# XmlDeleteData

| [[{{{image}}}\|link=\|]] | Important Note: This is an unofficial MTA function, so its not included into the game by default. Its an exported function of the xmlData resource. To access this function you need to have the resource running on your server. |
| --- | --- |
|  |  |

This function provides a way of deleting a [XML](mta://reference/misc/xml.md) file created by [xmlSaveData](mta://scripting/shared/functions/xmlsavedata.md)   

To call it, see the [call](mta://scripting/shared/functions/call.md) function or the tip in this resources page: [Simplifying the export](https://wiki.multitheftauto.com/wiki/XmlData#Simplifying_the_export)

# Info

**For proper deletion you need to pass the same booleans / securityLevel as you did on xmlSaveData.**  

**If you called [xmlSaveData](mta://scripting/shared/functions/xmlsavedata.md) with passing the securityLevel its recommended to pick securityLevel as function paremeter for the deletion as well.**

# Syntax

Click to collapse [-]
Client

```
bool xmlDeleteData ( string fileName [, bool serverProtected = true, bool resourceProtected = false ] )
```

```
bool xmlDeleteData ( string fileName [, int securityLevel = 4 ] )
```

#### Required Arguments

- **fileName:** The name of the file you want to delete.

#### Optional Arguments

- **serverProtected:** If set to *true* it can only delete the file of the creator-server, otherwise it doesn't care which server created it.

- **resourceProtected:** If set to *true* it can only delete the file of the creator-resource, otherwise it doesn't care which resource created it.

or

- **securityLevel:** The level of security on which your data is stored at. (Details on the resource page: [Security Levels](https://wiki.multitheftauto.com/wiki/XmlData#Security_Levels))

**See [xmlData Variables and Specified names](https://wiki.multitheftauto.com/wiki/XmlData#Variables_and_Specified_Names) for more detail.**

### Returns

Returns *true* if successful, *false* and a debug output in case if failure.

**Note: There is no encryption parameter in this function, because xmlDeleteData will auto-search for and delete the key of encrypted files.**

Click to collapse [-]
Server

```
bool xmlDeleteData ( string fileName [, bool resourceProtected = false ] )
```

```
bool xmlDeleteData ( string fileName [, int securityLevel = 4 ] )
```

#### Required Arguments

- **fileName:** The name of the file you want to delete.

#### Optional Arguments

- **resourceProtected:** If set to *true* it can only delete the file of the creator-resource, otherwise it doesn't care which resource created it.

or

- **securityLevel:** The level of security on which your data is stored at. (Details on the resource page: [Security Levels](https://wiki.multitheftauto.com/wiki/XmlData#Security_Levels))

**See [xmlData Variables and Specified names](https://wiki.multitheftauto.com/wiki/XmlData#Variables_and_Specified_Names) for more detail.**

### Returns

Returns *true* if successful, *false* and a debug output in case if failure.

**Note: There is no encryption parameter in this function, because xmlDeleteData will auto-search for and delete the key of encrypted files.**
**Note2: There is no serverProtected parameter, because its server-side already anyways.**

## Example

Click to collapse [-]
Client

```
-- Lets assume we have created a resourceProtected-only file called "settings" already.
local xml = exports.xmlData
xml:xmlDeleteData("settings", false, true) -- not serverProtected, but resourceProtected
-- OR
xml:xmlDeleteData("settings", 1) -- securityLevel 1 equals not serverProtected, unencrypted, but resouceProtected - the encryption bool will be ignored at xmlDeleteData
```

## See Also

- [xmlCopyFile](mta://scripting/shared/functions/xmlcopyfile.md)

- [xmlCreateChild](mta://scripting/shared/functions/xmlcreatechild.md)

- [xmlCreateFile](mta://scripting/shared/functions/xmlcreatefile.md)

- [xmlDestroyNode](mta://scripting/shared/functions/xmldestroynode.md)

- [xmlFindChild](mta://scripting/shared/functions/xmlfindchild.md)

- [xmlLoadFile](mta://scripting/shared/functions/xmlloadfile.md)

- [xmlLoadString](mta://scripting/shared/functions/xmlloadstring.md)

- [xmlNodeGetAttribute](mta://scripting/shared/functions/xmlnodegetattribute.md)

- [xmlNodeGetAttributes](mta://scripting/shared/functions/xmlnodegetattributes.md)

- [xmlNodeGetChildren](mta://scripting/shared/functions/xmlnodegetchildren.md)

- [xmlNodeGetName](mta://scripting/shared/functions/xmlnodegetname.md)

- [xmlNodeGetParent](mta://scripting/shared/functions/xmlnodegetparent.md)

- [xmlNodeGetValue](mta://scripting/shared/functions/xmlnodegetvalue.md)

- [xmlNodeSetAttribute](mta://scripting/shared/functions/xmlnodesetattribute.md)

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
