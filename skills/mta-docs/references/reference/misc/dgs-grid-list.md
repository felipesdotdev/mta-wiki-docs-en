---
doc_id: "mta-wiki:10301"
title: "DGS Grid List"
source_title: "DGS Grid List"
source_url: "https://wiki.multitheftauto.com/wiki/DGS_Grid_List"
revision_id: 69634
language: "en"
categories: []
---

# DGS Grid List

[Back To DGS](https://wiki.multitheftauto.com/index.php?search=Back%20To%20DGS)

### Sotring

- DGS Grid List fixed sorting problem

```
loadstring(exports.dgs:dgsImportFunction())()
local gridlist = dgsCreateGridList(100,100,400,400,false)
dgsGridListAddColumn(gridlist,"test1",0.4)
dgsGridListAddColumn(gridlist,"test2",0.4)

----------------Click the column to enable the built-in sorting.
addCommandHandler("addRow",function()
	for i=1,20 do
		local row = dgsGridListAddRow(gridlist)
		dgsGridListSetItemText(gridlist,row,1,i)
		dgsGridListSetItemText(gridlist,row,2,i-1) --No Bugs
	end
end)
```

### Row Index

- The Row Index of DGS Grid List is different from GUI Grid List (dgs row = gui row + 1)

```
-------------------------DGS
loadstring(exports.dgs:dgsImportFunction())()
local gridlist = dgsCreateGridList(100,100,400,400,false)
dgsGridListAddColumn(gridlist,"test1",0.4)
local row = dgsGridListAddRow(gridlist)  --Add the first row
outputChatBox(row) --Output the index of the first row: 1
-------------------------GUI
local gridlist = guiCreateGridList(100,100,400,400,false)
guiGridListAddColumn(gridlist,"test1",0.4)
local row = guiGridListAddRow(gridlist)  --Add the first row
outputChatBox(row) --Output the index of the first row: 0
```
