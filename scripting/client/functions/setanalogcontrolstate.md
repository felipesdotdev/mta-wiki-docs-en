---
doc_id: "mta-wiki:6748"
title: "SetAnalogControlState"
source_title: "SetAnalogControlState"
source_url: "https://wiki.multitheftauto.com/wiki/SetAnalogControlState"
revision_id: 72677
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:38.018439+00:00"
---

# SetAnalogControlState

This sets the analog control state of a control for the local player. To change the analog controls for a [ped](mta://reference/misc/ped.md), please use [setPedAnalogControlState](mta://scripting/client/functions/setpedanalogcontrolstate.md).

## Syntax

```
bool setAnalogControlState ( string control [, float state, bool forceOverrideNextFrame = false ] )
```

### Required Arguments

- **control:** The control that you want to set the state of. See [control names](mta://reference/misc/control-names.md) for a list of possible controls.

### Optional Arguments

- **state:** A [float](mta://reference/misc/float.md) between 0 and 1 indicating the amount the control is pressed. If no value is provided, the analog control is removed.

- **forceOverrideNextFrame:** A [bool](mta://reference/misc/bool.md) indicating if the player input should force fully overriden for the next frame.

### Returns

Returns *true* if the control state was successfully set, *false* otherwise.

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

This script invertes left and right vehicle steering for the player.

```
addEventHandler("onClientPreRender", root,
    function()
        local right = getAnalogControlState("vehicle_right", true)
        local left = getAnalogControlState("vehicle_left", true)
        
        if right > left then
            setAnalogControlState("vehicle_left", right, true)
        else
            setAnalogControlState("vehicle_right", left, true)
        end
    end
)
```

## See Also

- [getAnalogControlState](mta://scripting/client/functions/getanalogcontrolstate.md)

- [getBoundKeys](mta://scripting/client/functions/getboundkeys.md)

- [getCommandsBoundToKey](mta://scripting/client/functions/getcommandsboundtokey.md)

- [getKeyBoundToCommand](mta://scripting/client/functions/getkeyboundtocommand.md)

- [getKeyState](mta://scripting/client/functions/getkeystate.md)

- [isCapsLockEnabled](mta://scripting/client/functions/iscapslockenabled.md)

- setAnalogControlState
  

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
