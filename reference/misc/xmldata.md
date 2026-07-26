---
doc_id: "mta-wiki:11733"
title: "XmlData"
source_title: "XmlData"
source_url: "https://wiki.multitheftauto.com/wiki/XmlData"
revision_id: 64324
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:17:07.736712+00:00"
---

# XmlData

| xmlData v1.1 |  |
| --- | --- |
|  |  |
| Status: | Up to date |
| Latest Release: | 13.09.2019 |
| Working on: | MTA v1.5.7 |

## Resource Information

This resource let you save and load data in an [XML](mta://reference/misc/xml.md) File.  

It's an easy to use resource, providing 3 exported functions.

## Download

**Note: You have to put all the files of the .zip into a folder called "xmlData" and then upload the folder to your server!**  

Download can be found at the [MTA Community Page](https://community.multitheftauto.com/index.php?p=resources&s=details&id=16187).  

Resource developed by: [Ceeser](https://community.multitheftauto.com/index.php?p=profile&id=477820)

## Exported functions

**Note: These functions are available for Server and Client**

- [xmlSaveData](mta://scripting/shared/functions/xmlsavedata.md)

- [xmlLoadData](mta://scripting/shared/functions/xmlloaddata.md)

- [xmlDeleteData](mta://scripting/shared/functions/xmldeletedata.md)

## Security

Next to the point of easy access this resource has its focus on security.
You can specify how much protection you want to have for your data:

- **Server protection** - With this only the server that has created the file will be able to read/modify/delete it.

- **Encryption** - With this the stored data will be encrypted by a generated key, making it unreadable and unmodifyable by humans.

- **Resource protection** - With this only the resource that has created the file will be able to read/modify/delete it.

Note: No matter what settings you use - no server will have access to any file without its specific filename.

### Key generation / Data encryption

If you want to save your data encrypted the script will generate a random key and stores it, so that the file can get read again.
If you enable server protection for the file, the key can also only be read by the same server that has generated the data file.
The same also goes for the resource protection.

### Security Levels

Instead of manually adding bool parameters to the functions you can also just pass the security level you want to use for each function:

- **0** - No protection (any server, any resource or humans could read/modify)

- **1** - Very low protection (creator resource on any server or humans could read/modify)

- **2** - Very low protection (any resource on any server could read/modify, humans cant)

- **3** - Low protection (only creator resource on any server could read/modify, humans cant)

- **4** - Medium protection (any resource on the creator server or humans could read/modify) - DEFAULT

- **5** - Medium protection (only creator resource on the creator server or humans could read/modify)

- **6** - High protection (any resource on the creator server could read/modify, humans cant)

- **7** - Very high protection (only creator resource on creator server could read/modify, humans cant.

## Simplifying the export

For simplifying reasons I recommend the use this shortcut variable to call the exported functions:

```
local xml = exports.xmlData -- Define this variable at the top of your script

-- And then use it like this for example:
xml:xmlSaveData("yourFileName", yourData)
```

## Variables and Specified Names

In the exported functions are some names which I will explain here to keep the function pages as clean and small as possible.

### serverProtected / Creator-Server

With **creator-server** I mean the server that has created a file.
So if a file is serverProtected only the server that called the function is able to read/modify/delete it.  

This includes client-side: The function call have been on the client-side of any server, so the link to the server exist anyways.

### resourceProtected / Creator-Resource

With **creator-resource** I mean the resource that has created a file.
Example how it works: If you call xmlSaveData with resourceProtection from resource "login", only "login" will then be able to read that xml file.  

If you don't use serverProtection in combination to this, every "login" resource on any server COULD read that file if it calls xmlLoadData with the correct file name.

## Data type warning

**This resource will save everything, no matter what you give as data input.**  

So be sure that there is no userdata stored inside the table you are passing to the xmlSaveData function.
In case you have any kind of userdata it will output warnings in the debugscript - you should fix that by removing all userdata from the input table, because: Any Userdata is temporary. It will change after a script restart, reconnect, server restart.. or even while a resource is running/ you are playing.

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
