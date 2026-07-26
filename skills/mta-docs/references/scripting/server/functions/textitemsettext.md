---
doc_id: "mta-wiki:1491"
title: "TextItemSetText"
source_title: "TextItemSetText"
source_url: "https://wiki.multitheftauto.com/wiki/TextItemSetText"
revision_id: 67671
language: "en"
categories: ["Server_functions"]
---

# TextItemSetText

Overwrites a previously created text item with the specified text.

## Syntax

```
void textItemSetText ( textitem theTextitem, string text )
```

### Required Arguments

- **theTextitem:** An existing text item that was previously created with [textCreateTextItem](mta://scripting/server/functions/textcreatetextitem.md)

- **text:** The new text for the text item

## Example

Here, it is being used to update a scoreboard:

```
function updateScoreOnWasted ( ammo, killer, weapon )
	if ( killer ~= false) then                            -- Check to see if anything killed the player
		local killerTeam = getTeamName ( getPlayerTeam(killer) )
		if ( killerTeam == "grove" ) then             -- if a Grove player scored the kill
			groveteamscore = groveteamscore + 1   -- Grove gets 1 point
			textItemSetText ( scoregrove, tostring(groveteamscore) ) -- Update scoreboard.
		elseif ( killerTeam == "balla" ) then         -- if a Balla player scored the kill
			ballateamscore = ballateamscore + 1   -- Ballas get 1 point
			textItemSetText ( scoreballa, tostring(ballateamscore) ) -- Update scoreboard.
		end
	end
end
addEventHandler ( "onPlayerWasted", root, updateScoreOnWasted )
```

## See Also

- [textCreateDisplay](mta://scripting/server/functions/textcreatedisplay.md)

- [textCreateTextItem](mta://scripting/server/functions/textcreatetextitem.md)

- [textDestroyDisplay](mta://scripting/server/functions/textdestroydisplay.md)

- [textDestroyTextItem](mta://scripting/server/functions/textdestroytextitem.md)

- [textDisplayAddObserver](mta://scripting/server/functions/textdisplayaddobserver.md)

- [textDisplayAddText](mta://scripting/server/functions/textdisplayaddtext.md)

- [textDisplayGetObservers](mta://scripting/server/functions/textdisplaygetobservers.md)

- [textDisplayIsObserver](mta://scripting/server/functions/textdisplayisobserver.md)

- [textDisplayRemoveObserver](mta://scripting/server/functions/textdisplayremoveobserver.md)

- [textDisplayRemoveText](mta://scripting/server/functions/textdisplayremovetext.md)

- [textItemGetColor](mta://scripting/server/functions/textitemgetcolor.md)

- [textItemGetPosition](mta://scripting/server/functions/textitemgetposition.md)

- [textItemGetPriority](mta://scripting/server/functions/textitemgetpriority.md)

- [textItemGetScale](mta://scripting/server/functions/textitemgetscale.md)

- [textItemGetText](mta://scripting/server/functions/textitemgettext.md)

- [textItemSetColor](mta://scripting/server/functions/textitemsetcolor.md)

- [textItemSetPosition](mta://scripting/server/functions/textitemsetposition.md)

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- textItemSetText
