---
doc_id: "mta-wiki:14671"
title: "IsCursorOnElement"
source_title: "IsCursorOnElement"
source_url: "https://wiki.multitheftauto.com/wiki/IsCursorOnElement"
revision_id: 82798
language: "en"
categories: []
---

# IsCursorOnElement

Client-Side Function: isCursorOnElement

 

**Description:**
This function is used in GUI / DX to create interactive buttons or effects in a professional way. 
It allows you to make elements like buttons, rectangles, or any selectable area responsive to the player's cursor. 
You can also add many enhancements to make the appearance of the button or element look visually appealing and professional.
---

### Function

```
function isCursorOnElement( posX, posY, width, height )

	if isCursorShowing( ) then

		local mouseX, mouseY = getCursorPosition( )

		local clientW, clientH = guiGetScreenSize( )

		local mouseX, mouseY = mouseX * clientW, mouseY * clientH

		if ( mouseX > posX and mouseX < ( posX + width ) and mouseY > posY and mouseY < ( posY + height ) ) then

			return true

		end

	end

	return false

end
```

---

### Example Usage

```
-- Example: Interactive button on screen

local SelectBut = 1 -- Stores the button selected by player
local x, y, w, h = 100, 100, 150, 50 -- Element position and size

if isCursorOnElement(x, y, w, h) then
    -- Cursor is on the element → full alpha
    dxDrawImage(x, y, w, h, "img.png", 0, 0, 0, tocolor(255, 254, 254, 255), false)
else
    if SelectBut == 1 then
        -- Cursor is not on the element but already selected → full alpha
        dxDrawImage(x, y, w, h, "img.png", 0, 0, 0, tocolor(255, 254, 254, 255), false)
    else
        -- Cursor is not on the element and not selected → reduce alpha
        dxDrawImage(x, y, w, h, "img.png", 0, 0, 0, tocolor(255, 254, 254, 50), false)
    end
end
```

---

### Explanation

- **isCursorOnElement(posX, posY, width, height)** Function to check cursor position relative to an element

---

### Notes

- This function is safe for Client-Side only and will not affect other players.

- GUI/DX Example can be adapted for multiple buttons or GUI elements easily.
