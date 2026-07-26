---
doc_id: "mta-wiki:5742"
title: "DetonateSatchels"
source_title: "DetonateSatchels"
source_url: "https://wiki.multitheftauto.com/wiki/DetonateSatchels"
revision_id: 75684
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:11:29.430096+00:00"
---

# DetonateSatchels

This function can be used to detonate a players satchels.

## Syntax

Click to collapse [-]
Client

```
bool detonateSatchels()
```

Click to collapse [-]
Server

```
bool detonateSatchels(player Player)
```

## Returns

Returns *true* if successful, *false* otherwise.

## Example

The below example allows a player to detonate any of their placed satchels via the command /blowsatchels (Client-side)

Click to collapse [-]
Client-side

```
addCommandHandler("blowsatchels",
    function()
        detonateSatchels()
    end
)
```

The below example allows a player to detonate any of their placed satchels via the command /blowsatchels (Server-side)

Click to collapse [-]
Server-side

```
addCommandHandler("blowsatchels",
    function(sourcePlayer, commandName)
        detonateSatchels(sourcePlayer)
    end
)
```

## See also

- [createProjectile](mta://scripting/client/functions/createprojectile.md)

- [getProjectileCounter](mta://scripting/client/functions/getprojectilecounter.md)

- [getProjectileCreator](mta://scripting/client/functions/getprojectilecreator.md)

- [getProjectileForce](mta://scripting/client/functions/getprojectileforce.md)

- [getProjectileTarget](mta://scripting/client/functions/getprojectiletarget.md)

- [getProjectileType](mta://scripting/client/functions/getprojectiletype.md)

- [setProjectileCounter](mta://scripting/client/functions/setprojectilecounter.md)
  

- **Shared**

- detonateSatchels
