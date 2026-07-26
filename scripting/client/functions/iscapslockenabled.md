---
doc_id: "mta-wiki:13793"
title: "IsCapsLockEnabled"
source_title: "IsCapsLockEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/IsCapsLockEnabled"
revision_id: 82068
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:53.520965+00:00"
---

# IsCapsLockEnabled

This function returns the state of the caps lock.

## Syntax

```
bool isCapsLockEnabled()
```

### Returns

Returns *true* if caps lock is toggled (on), *false* otherwise.

## Example

```
function checkCaps()
    iprint(isCapsLockEnabled(), getTickCount())
end
addCommandHandler("caps", checkCaps)
```

## See Also

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
