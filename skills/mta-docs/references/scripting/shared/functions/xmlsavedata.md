---
doc_id: "mta-wiki:11734"
title: "XmlSaveData"
source_title: "XmlSaveData"
source_url: "https://wiki.multitheftauto.com/wiki/XmlSaveData"
revision_id: 64325
language: "en"
categories: ["Useful_Functions"]
---

# XmlSaveData

| [[{{{image}}}\|link=\|]] | Important Note: This is an unofficial MTA function, so its not included into the game by default. Its an exported function of the xmlData resource. To access this function you need to have the resource running on your server. |
| --- | --- |
|  |  |

This function provides an automated way of loading your data from an [XML](mta://reference/misc/xml.md) file created by xmlSaveData   

To call it, see the [call](mta://scripting/shared/functions/call.md) function or the tip in this resources page: [Simplifying the export](https://wiki.multitheftauto.com/wiki/XmlData#Simplifying_the_export)

# Syntax

Click to collapse [-]
Client

```
bool xmlSaveData ( string fileName, table data [, bool serverProtected = true, bool encryptData = false, bool resourceProtected = false ] )
```

```
bool xmlSaveData ( string fileName, table data [, int securityLevel = 4] )
```

#### Required Arguments

- **fileName:** The name of the file you want to create

- **data:** The data you want to save (must be a table!)

#### Optional Arguments

- **serverProtected:** If set to *true* the script will protect the file so, that can only the creator server can access it.****

- **encryptData:** If set to *true* the script will generate a random key and use it to encrypt your stored data. **Note: If you want to store "sensitive data", always use encryption!**

- **resourceProtected:** If set to *true* the script will add the sourceResource name (so the name of the resource from which it got called) to the fileName, preventing it from getting read/overwritten/deleted by any other resource. If set to *false* you can use this script to call/send/modify tables from different resources without the use of events/other export functions.

or

- **securityLevel:** The level of security on which you want to store your data at. (Details on the resource page: [Security Levels](https://wiki.multitheftauto.com/wiki/XmlData#Security_Levels))

**See [xmlData Variables and Specified names](https://wiki.multitheftauto.com/wiki/XmlData#Variables_and_Specified_Names) for more detail.**

### Returns

Returns *true* if successful, *false* otherwise.

Click to collapse [-]
Server

```
bool xmlSaveData ( string fileName, table data [, bool encryptData = false, bool resourceProtected = false ] )
```

```
bool xmlSaveData ( string fileName, table data [, int securityLevel = 4] )
```

#### Required Arguments

- **fileName:** The name of the file you want to create

- **data:** The data you want to save (must be a table!)

#### Optional Arguments

- **encryptData:** If set to *true* the script will generate a random key and use it to encrypt your stored data. **Note: If you want to store "sensitive data", always use encryption! (Account data should never be stored in serverside files - use a database instead!)**

- **resourceProtected:** If set to *true* the script will add the sourceResource name (so the name of the resource from which it got called) to the fileName, preventing it from getting read/overwritten/deleted by any other resource. If set to *false* you can use this script to call/send/modify tables from different resources without the use of events/other export functions.

or

- **securityLevel:** The level of security on which you want to store your data at. (Details on the resource page: [Security Levels](https://wiki.multitheftauto.com/wiki/XmlData#Security_Levels))

**See [xmlData Variables and Specified names](https://wiki.multitheftauto.com/wiki/XmlData#Variables_and_Specified_Names) for more detail.**

### Returns

Returns *true* if successful, *false* otherwise.

## Example

Click to collapse [-]
Client

This is the script where we specify the export shortcut and the data table which we want to store.

```
local xml = exports.xmlData
local tblScriptSettings = {posX = 800, posY = 500, sizeX = 500, sizeY = 300, settings = {show = true, tab = 1}}

xml:xmlSaveData("myFileName", tblScriptSettings , true, true) -- Save the data as "myFileName"
```

This will create a server-protected, encrypted file on the clients computer called "myFileName.xml". Also it will generate a random generated key and stores it.  

The created file will -(could, because encrypted with a random key)- like this:

```
<root posY="VgEN0+TERhg=" posX="mjX4Tj5u6oM=" sizeX="VgEN0+TERhg=" sizeY="htgOMaZurQQ=">
    <settings show="yeiNs/ne1Ks=" tab="OpijtdPvYqQ="></settings>
</root>
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
