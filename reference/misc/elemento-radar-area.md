---
doc_id: "mta-wiki:12060"
title: "Elemento/Radar area"
source_title: "Elemento/Radar area"
source_url: "https://wiki.multitheftauto.com/wiki/Elemento/Radar_area"
revision_id: 65340
language: "en"
categories: ["Element_Types"]
generated_at: "2026-07-26T16:14:54.514964+00:00"
---

# Elemento/Radar area

A classe área do radar representa áreas coloridas que podem ser exibidas no radar do jogador.

O tipo de elemento desta classe é **"radararea"**.

## Sintaxe XML

```
<radararea posX="" posY="" sizeX="" sizeY="" color="" dimension=""/>
```

### Required Attributes

- **posX**: Um [float](mta://reference/misc/float.md) representando a posição X da área.

- **posY**: Um [float](mta://reference/misc/float.md) representando a posição Y da área.

- **sizeX**: Um [float](mta://reference/misc/float.md) representando a largura da área.

- **sizeY**: Um [float](mta://reference/misc/float.md) representando a altura da área.

### Atributos Opcionais

- **color:** A cor da área do radar no formato HTML-style (i.e. #RRGGBBAA). Se não especificado, padrão será vermelho.

- **dimension:** A dimensão em que a área será exibida. Se não especificado, padrão será 0.

## Funções de scripting relacionadas

### Cliente

**Shared**

- [createRadarArea](mta://scripting/shared/functions/createradararea.md)

- [getRadarAreaColor](mta://scripting/shared/functions/getradarareacolor.md)

- [getRadarAreaSize](mta://scripting/shared/functions/getradarareasize.md)

- [isInsideRadarArea](mta://scripting/shared/functions/isinsideradararea.md)

- [isRadarAreaFlashing](mta://scripting/shared/functions/isradarareaflashing.md)

- [setRadarAreaColor](mta://scripting/shared/functions/setradarareacolor.md)

- [setRadarAreaFlashing](mta://scripting/shared/functions/setradarareaflashing.md)

- [setRadarAreaSize](mta://scripting/shared/functions/setradarareasize.md)

### Servidor

- [createRadarArea](mta://scripting/shared/functions/createradararea.md)

- [getRadarAreaColor](mta://scripting/shared/functions/getradarareacolor.md)

- [getRadarAreaSize](mta://scripting/shared/functions/getradarareasize.md)

- [isInsideRadarArea](mta://scripting/shared/functions/isinsideradararea.md)

- [isRadarAreaFlashing](mta://scripting/shared/functions/isradarareaflashing.md)

- [setRadarAreaColor](mta://scripting/shared/functions/setradarareacolor.md)

- [setRadarAreaFlashing](mta://scripting/shared/functions/setradarareaflashing.md)

- [setRadarAreaSize](mta://scripting/shared/functions/setradarareasize.md)
