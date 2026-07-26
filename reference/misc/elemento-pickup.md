---
doc_id: "mta-wiki:11993"
title: "Elemento/Pickup"
source_title: "Elemento/Pickup"
source_url: "https://wiki.multitheftauto.com/wiki/Elemento/Pickup"
revision_id: 65110
language: "en"
categories: []
generated_at: "2026-07-26T16:07:05.808243+00:00"
---

# Elemento/Pickup

A classe pickup representa os pickups de armas, vida, ou colete no mundo do GTA. Pickups podem ser usados pelos jogadores quando passam por ele. Os jogadores não ganharam vida e/ou colete se ele já estiver full.

O tipo de elemento desta classe é **"pickup"**.

## Sintaxe XML

```
<pickup posX="" posY="" posZ="" type="" amount="" respawn=""/>
```

### Argumentos Obrigatórios

- **posX**: Um [float](mta://reference/misc/float.md) representando a posição X do pickup.

- **posY**: Um [float](mta://reference/misc/float.md) representando a posição Y do pickup.

- **posZ**: Um [float](mta://reference/misc/float.md) representando a posição Z do pickup.

- **type**: Uma [string](mta://reference/misc/string.md) indicando o tipo de pickup. Pode ser "health", "armor", ou um integer representando o [ID da arma](mta://reference/misc/weapon.md) do pickup.

### Argumentos Opcionais

- **amount**: Um [integer](mta://reference/misc/integer.md) representando o montante do pickup. Para vida ou colete, isto representa o número de vida que será dada ao jogador. Para armas, isto representa a quantidade de balas.

- **respawn**: Um [integer](mta://reference/misc/integer.md) representa o número de milisegundos que o pickup reaparecerá após ser usado (default: 30000).

## Funções de scripting relacionadas

- [createPickup](mta://scripting/shared/functions/createpickup.md)

- [getPickupAmmo](mta://scripting/shared/functions/getpickupammo.md)

- [getPickupAmount](mta://scripting/shared/functions/getpickupamount.md)

- [getPickupType](mta://scripting/shared/functions/getpickuptype.md)

- [setPickupType](mta://scripting/shared/functions/setpickuptype.md)

- [getPickupWeapon](mta://scripting/shared/functions/getpickupweapon.md)
