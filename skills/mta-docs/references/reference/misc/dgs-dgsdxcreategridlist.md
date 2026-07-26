---
doc_id: "mta-wiki:9452"
title: "Dgs/DgsDxCreateGridList"
source_title: "Dgs/DgsDxCreateGridList"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs/DgsDxCreateGridList"
revision_id: 51461
language: "en"
categories: ["Utility_templates"]
---

# Dgs/DgsDxCreateGridList

Syntax

Not completed

```
element dgsDxCreateGridList( float x, float y, float width, float height, bool relative,[ element parent = nil] )
```

### Required Arguments

 
Example Gridlist.

- **x:** A float of the 2D x position of the window on a player's screen. This is affected by the *relative* argument.

- **y:** A float of the 2D y position of the window on a player's screen. This is affected by the *relative* argument.

- **width:** A float of the width of the window. This is affected by the *relative* argument.

- **height:** A float of the height of the window. This is affected by the *relative* argument.

- **relative:** This is whether sizes and positioning are relative. If this is true, then all x, y, width and height floats must be between 0 and 1, representing sizes relative to the parent.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).
Not completed

- **parent:** This is the parent that the DGS button is attached to.  If the *relative* argument is true, sizes and positioning will be made relative to this parent. If the *relative* argument is false, positioning will be the number of offset pixels from the parent's origin. If no parent is passed, the parent will become the screen - causing positioning and sizing according to screen positioning.

### Returns

Returns an element of the created gridlist if it was successfully created, false otherwise.

## Example

**Example 1:** This example creates a player list on the right of the screen and fills it

```
DGS = exports.dgs
function createPlayerList ()
	--Create the grid list element
	local playerList = DGS:dgsDxCreateGridList ( 0.80, 0.10, 0.15, 0.60, true )
	--Create a players column in the list
	local column = DGS:dgsDxGridListAddColumn( playerList, "Player", 0.85 )
	if ( column ) then --If the column has been created, fill it with players
		for id, player in ipairs(getElementsByType("player")) do
			local row = DGS:dgsDxGridListAddRow ( playerList )
			DGS:dgsDxGridListSetItemText ( playerList, row, column, getPlayerName ( player ), false, false )
		end
	end
end
```
