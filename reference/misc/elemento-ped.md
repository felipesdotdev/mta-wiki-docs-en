---
doc_id: "mta-wiki:11954"
title: "Elemento/Ped"
source_title: "Elemento/Ped"
source_url: "https://wiki.multitheftauto.com/wiki/Elemento/Ped"
revision_id: 65035
language: "en"
categories: []
generated_at: "2026-07-26T16:14:54.467088+00:00"
---

# Elemento/Ped

A palavra "ped" é um encurtado de "pedestrian" que significa *pedestre* e descreve qualquer pessoa do GTA, seja ele um jogador ou um personagem NPC. (E mesmo que "pedestre" não se aplique tecnicamente às pessoas que dirigem, elas ainda se enquadram nesse nome)

A função [createPed](mta://scripting/shared/functions/createped.md) cria especificamente um NPC, mas todas as outras funções de ped funcionam para jogadores e NPC, pois eles são praticamente a mesma coisa para San Andreas.

O tipo de elemento de um NPC é **"ped"**.

## XML syntax

```
<ped model="" posX="" posY="" posZ="" rotZ="" interior="" frozen="" />
```

### Atributos Obrigatórios

- **model**: O [ID de personagem](mta://reference/misc/character-skins.md) do ped que está sendo criado.

- **posX**: Um float representando a posição X do ped.

- **posY**: Um float representando a posição Y do ped.

- **posZ**: Um float representando a posição Z do ped.

### Atributos Opcionais

- **rotZ**: Um float representando a rotação Z do ped.

- **interior**: Um interior onde o ped será spawnado.

- **frozen**: Um booleano que indica se o ped será capaz de se mover ou não

## Funções de scripting relacionada

- [addPedClothes](mta://scripting/shared/functions/addpedclothes.md)

- [getPedClothes](mta://scripting/shared/functions/getpedclothes.md)

- [removePedClothes](mta://scripting/shared/functions/removepedclothes.md)

- [createPed](mta://scripting/shared/functions/createped.md)

- [getPedAmmoInClip](mta://scripting/shared/functions/getpedammoinclip.md)

- [getPedArmor](mta://scripting/shared/functions/getpedarmor.md)

- [getPedFightingStyle](mta://scripting/shared/functions/getpedfightingstyle.md)

- [getPedOccupiedVehicle](mta://scripting/shared/functions/getpedoccupiedvehicle.md)

- [getPedOccupiedVehicleSeat](mta://scripting/shared/functions/getpedoccupiedvehicleseat.md)

- [getPedStat](mta://scripting/shared/functions/getpedstat.md)

- [getPedTarget](mta://scripting/shared/functions/getpedtarget.md)

- [getPedTotalAmmo](mta://scripting/shared/functions/getpedtotalammo.md)

- [getPedWalkingStyle](mta://scripting/shared/functions/getpedwalkingstyle.md)

- [getPedWeapon](mta://scripting/shared/functions/getpedweapon.md)

- [getPedWeaponSlot](mta://scripting/shared/functions/getpedweaponslot.md)

- [getPedContactElement](mta://scripting/shared/functions/getpedcontactelement.md)

- [getValidPedModels](mta://scripting/shared/functions/getvalidpedmodels.md)

- [isPedChoking](mta://scripting/shared/functions/ispedchoking.md)

- [isPedDead](mta://scripting/shared/functions/ispeddead.md)

- [isPedDoingGangDriveby](mta://scripting/shared/functions/ispeddoinggangdriveby.md)

- [isPedDucked](mta://scripting/shared/functions/ispedducked.md)

- [isPedHeadless](mta://scripting/shared/functions/ispedheadless.md)

- [isPedInVehicle](mta://scripting/shared/functions/ispedinvehicle.md)

- [isPedOnGround](mta://scripting/shared/functions/ispedonground.md)

- [isPedReloadingWeapon](mta://scripting/shared/functions/ispedreloadingweapon.md)

- [isPedWearingJetpack](mta://scripting/shared/functions/ispedwearingjetpack.md)

- [killPed](mta://scripting/shared/functions/killped.md)

- [removePedFromVehicle](mta://scripting/shared/functions/removepedfromvehicle.md)

- [setPedAnimation](mta://scripting/shared/functions/setpedanimation.md)

- [setPedAnimationProgress](mta://scripting/shared/functions/setpedanimationprogress.md)

- [setPedAnimationSpeed](mta://scripting/shared/functions/setpedanimationspeed.md)

- [setPedArmor](mta://scripting/shared/functions/setpedarmor.md)

- [setPedDoingGangDriveby](mta://scripting/shared/functions/setpeddoinggangdriveby.md)

- [setPedFightingStyle](mta://scripting/shared/functions/setpedfightingstyle.md)

- [setPedHeadless](mta://scripting/shared/functions/setpedheadless.md)

- [setPedStat](mta://scripting/shared/functions/setpedstat.md)

- [setPedWalkingStyle](mta://scripting/shared/functions/setpedwalkingstyle.md)

- [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md)

- [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md)
