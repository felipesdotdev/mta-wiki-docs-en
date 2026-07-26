---
doc_id: "mta-wiki:4512"
title: "XML"
source_title: "XML"
source_url: "https://wiki.multitheftauto.com/wiki/XML"
revision_id: 49243
language: "en"
categories: ["Scripting_Concepts"]
---

# XML

XML stands for *Extensible Markup Language*, XML can be used in MTA to read or write data. 
MTA's map files are also in XML format.

Example of XML:

```
<meta>
    <info author="Slothman" type="gamemode" name="Stealth" />
    <config src="help.xml" type="client"/>

    <script src="stealthmain_server.lua" />
    <script src="noiseblip.lua" />
    <script src="mission_timer.lua" />
    <script src="gadgets_server.lua" />
    <script src="gadgets_client.lua" type="client"/>
    <script src="stealthmain_client.lua" type="client"/>
    <script src="noisebar.lua" type="client"/>
    <script src="spycam.lua" type="client"/>

    <file src="riot_shield.txd" />
    <file src="riot_shield.dff" />
    <file src="riot_shield.col" />
    <file src="armor.png" />
    <file src="camera.png" />
    <file src="cloak.png" />
    <file src="goggles.png" />
    <file src="mine.png" />
    <file src="radar.png" />
    <file src="shield.png" />

    <include resource="scoreboard" />
    <include resource="killmessages" />
    <include resource="maplimits" />
</meta>
```

## Related Scripting Functions

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

## See Also

- [Xmlnode](mta://reference/misc/xmlnode.md)

- [Meta.xml](mta://reference/misc/meta-xml.md)

- [Resource:Editor/EDF](mta://resources/editor-edf.md)

- [Meta.xml generator](http://forum.multitheftauto.com/viewtopic.php?f=91&t=22247)

- [XML on Wikipedia](http://en.wikipedia.org/wiki/XML)

- [W3C XML homepage](http://www.w3.org/XML/)
