---
doc_id: "mta-wiki:12039"
title: "Elemento/Marker"
source_title: "Elemento/Marker"
source_url: "https://wiki.multitheftauto.com/wiki/Elemento/Marker"
revision_id: 65265
language: "en"
categories: []
generated_at: "2026-07-26T16:07:06.707981+00:00"
---

# Elemento/Marker

A classe marker representa uma forma 3D que pode ter cores variadas no mundo de GTA. Existem alguns tipos de markers, incluindo *cylinder*s e *checkpoint*s. Nos scripts, markers são frequentemente usados para marcar pontos e desencadear algum tipo de ação quando um jogador entra neles.

O tipo de elemento desta classe é **"marker"**.

O tamanho de um marker não pode ser especificado em um XML e seu tamanho padrão é 4.0.

## Sintaxe XML

```
<marker posX="" posY="" posZ="" type="" .../>
```

### Argumentos obrigatórios

- **posX**: Um [float](mta://reference/misc/float.md) representando a posição X do marker.

- **posY**: Um [float](mta://reference/misc/float.md) representando a posição Y do marker.

- **posZ**: Um [float](mta://reference/misc/float.md) representando a posição Z do marker.

### Argumentos Opcionais

- **type:** O tipo visual do marker que será criado. Os tipos disponíveis são:

- **"checkpoint"**: A race checkpoint. These are very tall, but not infinite, light pillars. Checkpoints snap to ground and become invisible after going over a certain Z height.

- **"ring"**: Doughnut shaped ring, normally used for aircraft.

- **"cylinder"**: Small glowing ground ring. These are the glow markers you walk into to activate missions or events in single player.

- **"arrow"**: Arrow pointing down. These are the arrows on the doors you can enter in single player, except MTA's are not animated by default.

- **"corona"**: A glowing ball of light.

- **color:** A cor do marker em hexadecimal: #RRGGBB. Caso a cor não for definida, ela será por padrão vermelho.

## Funções de scripting relacionadas

- [createMarker](mta://scripting/shared/functions/createmarker.md)

- [getMarkerColor](mta://scripting/shared/functions/getmarkercolor.md)

- [getMarkerCount](mta://scripting/shared/functions/getmarkercount.md)

- [getMarkerIcon](mta://scripting/shared/functions/getmarkericon.md)

- [getMarkerSize](mta://scripting/shared/functions/getmarkersize.md)

- [getMarkerTarget](mta://scripting/shared/functions/getmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [getMarkerTargetArrowProperties](mta://scripting/shared/functions/getmarkertargetarrowproperties.md)

- [getMarkerType](mta://scripting/shared/functions/getmarkertype.md)

- [setMarkerColor](mta://scripting/shared/functions/setmarkercolor.md)

- [setMarkerIcon](mta://scripting/shared/functions/setmarkericon.md)

- [setMarkerSize](mta://scripting/shared/functions/setmarkersize.md)

- [setMarkerTarget](mta://scripting/shared/functions/setmarkertarget.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- [setMarkerTargetArrowProperties](mta://scripting/shared/functions/setmarkertargetarrowproperties.md)

- [setMarkerType](mta://scripting/shared/functions/setmarkertype.md)
