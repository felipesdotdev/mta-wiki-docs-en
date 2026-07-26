---
doc_id: "mta-wiki:11751"
title: "G2D"
source_title: "G2D"
source_url: "https://wiki.multitheftauto.com/wiki/G2D"
revision_id: 74532
language: "en"
categories: []
---

# G2D

Description

1. G2D aims to convert GUI to DGS without a lot of complex steps.
2. There are 2 versions of G2D:

- **1) Server-sided G2D script converter (G2DSC)**

- G2DSC is used to convert GUI functions/events to DGS ones by editing scripts. (Useful for converting scripts created by GUI Editor, but it will cause a lot of errors/bugs if you make it convert complicated scripts, because of compatibility)

- **2) Client-sided G2D hooker (G2D Hooker)**

- G2D Hooker is used to convert complex scripts by injecting hooker before executing the script instead of editing files. (The hooker is valid in one resource)

## Usage

### Server-Sided G2D script converter (G2DSC)

Command: g2d [Option] [Arguments]

These command can only be used in MTA Server console.

| Options | Arguments | Comment |
| --- | --- | --- |
| add | Resource Name | Retain selections and select other resources (-m :Pattern Match) |
| clear |  | Clear selections |
| help |  | G2D Help |
| remove | Resource Name | Remove specific selected resources from list (-m :Pattern Match) |
| list |  | List all selected resources |
| start |  | Start to convert (execute) |
| stop |  | Stop converting process |
| type |  | Change the type of G2D, can be hooker or convertor (by default) |

**Example For Convertor**

Basic:

```
g2d add resA
g2d start
```

Advanced Pattern Mode:

```
g2d add .A match
g2d start
```

**Output** files are stored in **dgs/G2DOutput/**

**Example For Hooker**  

This is used to add [dgsG2DLoadHooker](mta://scripting/client/functions/dgsg2dloadhooker.md) into script in batch.

OInly first clientsided script with **guiCreate** functions will be modified.

```
g2d type hooker
g2d add . match
g2d start
```

**Backup** files are stored in **dgs/G2DBackup/**

### Client-Sided G2D Hooker (G2D Hooker)

See detail [dgsG2DLoadHooker](mta://scripting/client/functions/dgsg2dloadhooker.md)

**Example**

```
loadstring(exports.dgs:dgsImportFunction())() --Import functions before
loadstring(exports.dgs:dgsG2DLoadHooker())()  --Load G2D Hooker
local buttonElement = guiCreateButton(200,200,300,300,"Test",false)  --Though you are using gui functions and events, but they have already hooked by DGS
addEventHandler ( "onClientGUIClick", buttonElement, function()
	outputChatBox("clicked")
end, false )
```
