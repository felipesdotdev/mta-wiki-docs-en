---
doc_id: "mta-wiki:12047"
title: "Elemento/Blip"
source_title: "Elemento/Blip"
source_url: "https://wiki.multitheftauto.com/wiki/Elemento/Blip"
revision_id: 69098
language: "en"
categories: ["Element_Types"]
---

# Elemento/Blip

A classe blip representa pequenos ícones ou blips que podem ser visualizados no radar(mapa) do jogador.

O tipo de elemento desta classe é **"blip"**. A lista de ícones de blips estão disponíveis na página de [blips](https://wiki.multitheftauto.com/wiki/PT-BR/Blips).

## Sintaxe XML

```
<blip posX="" posY="" posZ="" icon="" color="" dimension="" ordering=""/>
```

### Atributos necessários

- **posX**: Um [float](mta://reference/misc/float.md) representando a posição X do blip.

- **posY**: Um [float](mta://reference/misc/float.md) representando a posição Y do blip.

- **posZ**: Um [float](mta://reference/misc/float.md) representando a posição Z do blip.

### Atributos opcionais

- **color:** A cor do ícone no formato HTML-style (ou hexadecimal) (i.e. #RRGGBB). A cor padrão é azul se não for declarado.

- **icon:** O ID do ícone do blip. Padrão é 0 se não for declarado.

- **dimension:** A dimensão do blip. Padrão é 0 se não for declarado.

- **ordering:** A ordem Z do blip (de trás para frente). Padrão é 0 se não for declarado.

## Funções de scripting relacionadas

### Cliente

**Shared**

- [createBlip](mta://scripting/shared/functions/createblip.md)

- [createBlipAttachedTo](mta://scripting/shared/functions/createblipattachedto.md)

- [getBlipColor](mta://scripting/shared/functions/getblipcolor.md)

- [getBlipIcon](mta://scripting/shared/functions/getblipicon.md)

- [getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)

### Servidor

- [createBlip](mta://scripting/shared/functions/createblip.md)

- [createBlipAttachedTo](mta://scripting/shared/functions/createblipattachedto.md)

- [getBlipColor](mta://scripting/shared/functions/getblipcolor.md)

- [getBlipIcon](mta://scripting/shared/functions/getblipicon.md)

- [getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)
