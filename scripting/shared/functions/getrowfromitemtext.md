---
doc_id: "mta-wiki:7052"
title: "GetRowFromItemText"
source_title: "GetRowFromItemText"
source_url: "https://wiki.multitheftauto.com/wiki/GetRowFromItemText"
revision_id: 35197
language: "en"
categories: ["Useful_Functions"]
generated_at: "2026-07-26T16:15:23.918874+00:00"
---

# GetRowFromItemText

This function enables you to get row from gridlist by using itemtext.

## Syntax

```
int getRowFromItemText ( element gridList, string itemText [, int column] )
```

### Required Arguments

- **gridList**: The gridlist you want to get the row from.

- **itemText**: The itemtext of the row.

### Optional Arguments

- **column**: The column you want to check the itemtext on.

### Returns

Returns row if successful, false otherwise.

## Code

Click to collapse [-]
Function source

```
function getRowFromItemText ( list, name, colum )
	if ( isElement(list) ) and ( getElementType(list) == "gui-gridlist" ) and ( type(name) == "string" ) then
		local colum = tonumber(colum) or 1
		local rows = guiGridListGetRowCount ( list ) - 1
		for i=0,rows do
			local text = guiGridListGetItemText ( list, i, colum )
			if ( text == name ) then
				return i
			end
		end
	end
	return false
end
```

Author: Bssol
