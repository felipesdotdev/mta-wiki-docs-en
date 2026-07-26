---
doc_id: "mta-wiki:2597"
title: "OnClientGUIDoubleClick"
source_title: "OnClientGUIDoubleClick"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientGUIDoubleClick"
revision_id: 78803
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:18.677586+00:00"
---

# OnClientGUIDoubleClick

This event is fired when the user double clicks a GUI element. Doesn't work with buttons.

## Parameters

```
string button, string state, int absoluteX, int absoluteY
```

- **button:** the name of the mouse button that the GUI element was double clicked with.

- **state:** the state of the mouse button. Can be *down* or *up*. **Please note currently only the up state is supported.**

- **absoluteX:** the X position of the mouse cursor, in pixels, measured from the left side of the screen.

- **absoluteY:** the Y position of the mouse cursor, in pixels, measured from the top of the screen.

## Source

The source of this event is the GUI element that was double clicked.

## Example

This example displays in chatbox name of double-clicked player in a gridlist.

```
addEventHandler( "onClientResourceStart", getResourceRootElement( ),
    function ( )
        gridList = guiCreateGridList( 10, 200, 100, 50, false ) -- create a gridlist
        local col = guiGridListAddColumn( gridList, "Players", .9 ) -- add "Players" column

        local players = getElementsByType( "player" )
        for i, plr in pairs( players ) do -- loop through the table of players
            local row = guiGridListAddRow( gridList ); -- add row for player
            guiGridListSetItemText( gridList, row, col, getPlayerName( plr ), false, false ) -- change the text of the added row
        end

        addEventHandler( "onClientGUIDoubleClick", gridList, doubleClickedName, false )
    end
);

function doubleClickedName( )
    local selectedRow, selectedCol = guiGridListGetSelectedItem( gridList ); -- get double clicked item in the gridlist
    local playerName = guiGridListGetItemText( gridList, selectedRow, selectedCol ) -- get its text
    outputChatBox( "You double-clicked: " .. playerName ) -- display the text taken from gridlist
end
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

- onClientGUIDoubleClick

- [onClientGUIFocus](mta://scripting/client/events/onclientguifocus.md)

- [onClientGUIMouseDown](mta://scripting/client/events/onclientguimousedown.md)

- [onClientGUIMouseUp](mta://scripting/client/events/onclientguimouseup.md)

- [onClientGUIMove](mta://scripting/client/events/onclientguimove.md)

- [onClientGUIScroll](mta://scripting/client/events/onclientguiscroll.md)

- [onClientGUISize](mta://scripting/client/events/onclientguisize.md)

- [onClientGUITabSwitched](mta://scripting/client/events/onclientguitabswitched.md)

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
