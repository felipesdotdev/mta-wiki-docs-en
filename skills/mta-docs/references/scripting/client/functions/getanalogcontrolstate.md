---
doc_id: "mta-wiki:4349"
title: "GetAnalogControlState"
source_title: "GetAnalogControlState"
source_url: "https://wiki.multitheftauto.com/wiki/GetAnalogControlState"
revision_id: 67773
language: "en"
categories: ["Client_functions", "Changes_in_1.5.7"]
---

# GetAnalogControlState

This retrieves the analog control state of a control.  This is useful for detecting sensitive controls, such as those used on a joypad.

To get the analog control state for a [ped](https://wiki.multitheftauto.com/index.php?search=ped), please use [getPedAnalogControlState](mta://scripting/client/functions/getpedanalogcontrolstate.md).

## Syntax

```
float getAnalogControlState ( string control [, bool rawValue ] )
```

### Required Arguments

- **control:** The control that you want to get the state of. See [control names](mta://reference/misc/control-names.md) for a list of possible controls.

### Optional Arguments

- **rawValue:** A bool indicating if it should return the raw player input value.

### Returns

Returns a [float](mta://reference/misc/float.md) between 0 and 1 indicating the amount the control is pressed.

## Example

This creates an */forwards* command, which toggles your *forwards* control state between 0 and 1.

```
addCommandHandler( "forwards",
    function( )
        if ( getAnalogControlState( "forwards" ) == 0 ) then
            setAnalogControlState( "forwards", 1 )
        else
            setAnalogControlState( "forwards", 0 )
        end
    end
)
```

## See Also

- getAnalogControlState

- [getBoundKeys](mta://scripting/client/functions/getboundkeys.md)

- [getCommandsBoundToKey](mta://scripting/client/functions/getcommandsboundtokey.md)

- [getKeyBoundToCommand](mta://scripting/client/functions/getkeyboundtocommand.md)

- [getKeyState](mta://scripting/client/functions/getkeystate.md)

- [isCapsLockEnabled](mta://scripting/client/functions/iscapslockenabled.md)

- [setAnalogControlState](mta://scripting/client/functions/setanalogcontrolstate.md)
  

- **Shared**

- [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md)

- [bindKey](mta://scripting/shared/functions/bindkey.md)

- [executeCommandHandler](mta://scripting/shared/functions/executecommandhandler.md)

- [getCommandHandlers](mta://scripting/shared/functions/getcommandhandlers.md)

- [getFunctionsBoundToKey](mta://scripting/shared/functions/getfunctionsboundtokey.md)

- [getKeyBoundToFunction](mta://scripting/shared/functions/getkeyboundtofunction.md)

- [isControlEnabled](mta://scripting/shared/functions/iscontrolenabled.md)

- [removeCommandHandler](mta://scripting/shared/functions/removecommandhandler.md)

- [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md)

- [toggleControl](mta://scripting/shared/functions/togglecontrol.md)

- [unbindKey](mta://scripting/shared/functions/unbindkey.md)
