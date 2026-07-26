---
doc_id: "mta-wiki:4639"
title: "OnClientGUITabSwitched"
source_title: "OnClientGUITabSwitched"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientGUITabSwitched"
revision_id: 71355
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.868807+00:00"
---

# OnClientGUITabSwitched

This event is triggered each time the user switch from GUI tab.

When adding the event handler on the tab panel, propagate must be true.

## Parameters

```
element theElement
```

- **theElement**: the [tab](mta://scripting/concepts/element-gui-tab.md) which was selected.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the tab.

## Example

This example creates a window with a tabpanel with two tabs. Every time a user changes tabpage a notification will be shown.

First we'll create the window. Then add a tabpanel and couple tabs with some labels in them. Qoute: [GuiCreateWindow#Example](mta://scripting/client/functions/guicreatewindow.md)

```
local myWindow = guiCreateWindow ( 0, 0, 0.5, 0.4, "Information", true )  -- create a window which has "Information" in the title bar.
local tabPanel = guiCreateTabPanel ( 0, 0.1, 1, 1, true, myWindow )       -- create a tab panel which fills the whole window
local tabMap = guiCreateTab( "Map Information", tabPanel )                -- create a tab named "Map Information" on 'tabPanel'
local tabHelp = guiCreateTab( "Help", tabPanel )                          -- create another tab named "Help" on 'tabPanel'
 
-- adds a label (text) to each tab
guiCreateLabel( 0.02, 0.04, 0.94, 0.2, "This is information about the current map", true, tabMap )
guiCreateLabel( 0.02, 0.04, 0.94, 0.92, "This is help text.", true, tabHelp )
```

Now let's add the event handler.

```
function OnChange(selectedTab)
	-- If there is a selected tab.
	if selectedTab ~= nil then 
		outputChatBox( "You've changed your active tab." )
	end	
end

addEventHandler("onClientGUITabSwitched", root, OnChange)
```

## See Also

### Input

- [onClientCharacter](mta://scripting/client/events/onclientcharacter.md)

- [onClientClick](mta://scripting/client/events/onclientclick.md)

- [onClientCursorMove](mta://scripting/client/events/onclientcursormove.md)

- [onClientDoubleClick](mta://scripting/client/events/onclientdoubleclick.md)

- [onClientKey](mta://scripting/client/events/onclientkey.md)

- [onClientPaste](mta://scripting/client/events/onclientpaste.md)

### GUI

- [onClientGUIAccepted](mta://scripting/client/events/onclientguiaccepted.md)

- [onClientGUIBlur](mta://scripting/client/events/onclientguiblur.md)

- [onClientGUIChanged](mta://scripting/client/events/onclientguichanged.md)

- [onClientGUIClick](mta://scripting/client/events/onclientguiclick.md)

- [onClientGUIComboBoxAccepted](mta://scripting/client/events/onclientguicomboboxaccepted.md)

- [onClientGUIDoubleClick](mta://scripting/client/events/onclientguidoubleclick.md)

- [onClientGUIFocus](mta://scripting/client/events/onclientguifocus.md)

- [onClientGUIMouseDown](mta://scripting/client/events/onclientguimousedown.md)

- [onClientGUIMouseUp](mta://scripting/client/events/onclientguimouseup.md)

- [onClientGUIMove](mta://scripting/client/events/onclientguimove.md)

- [onClientGUIScroll](mta://scripting/client/events/onclientguiscroll.md)

- [onClientGUISize](mta://scripting/client/events/onclientguisize.md)

- onClientGUITabSwitched

- [onClientMouseEnter](mta://scripting/client/events/onclientmouseenter.md)

- [onClientMouseLeave](mta://scripting/client/events/onclientmouseleave.md)

- [onClientMouseMove](mta://scripting/client/events/onclientmousemove.md)

- [onClientMouseWheel](mta://scripting/client/events/onclientmousewheel.md)

### Client event functions

- [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md)

- [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md)
  

- **Shared**

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)
