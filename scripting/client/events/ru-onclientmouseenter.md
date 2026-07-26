---
doc_id: "mta-wiki:12836"
title: "RU/onClientMouseEnter"
source_title: "Ru/onClientMouseEnter"
source_url: "https://wiki.multitheftauto.com/wiki/Ru/onClientMouseEnter"
revision_id: 69419
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:35.481435+00:00"
---

# RU/onClientMouseEnter

Это событие вызывается, когда игрок наводится на GUI элемент.

## Параметры

```
int absoluteX, int absoluteY, element leftGUI
```

- **absoluteX**:  Позиция мышки по оси X, в пикселях, которая считается от левого края экрана.

- **absoluteY**:  Позиция мышки по оси Y, в пикселях, которая считается от верхнего края экрана.

- **leftGUI**: Элемент GUI, с которого переключился пользователь или *nil*, если его не существует.

## Источник события

[Источником](mta://reference/misc/event-system.md) этого события является GUI элемент, на который наводится пользователь.

## Пример

Этот пример отправляет в чат сообщение, когда игрок навёлся на GUI элемент.

```
addEventHandler( "onClientMouseEnter", getRootElement(), 
    function(aX, aY)
        outputChatBox( "Вы навелись на GUI элемент в позиции ("..tostring(aX)..", "..tostring(aY)..")")
    end
)
```

## Смотрите также

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
