---
doc_id: "mta-wiki:12044"
title: "Elemento/Collision shape"
source_title: "Elemento/Collision shape"
source_url: "https://wiki.multitheftauto.com/wiki/Elemento/Collision_shape"
revision_id: 65294
language: "en"
categories: ["Element_Types"]
generated_at: "2026-07-26T16:14:54.370055+00:00"
---

# Elemento/Collision shape

A classe de formas de colisões representa formas invisíveis de detecção de colisão que podem ser criadas no mundo do GTA. Formas de colisão são tipicamente usados para detectar quando entidades físicas passam por ela, e executam ações quando isso acontece.

O tipo de elemento para esta classe é **colshape**.

## Sintaxe XML

```
<colcube posX="1024.768" posY="1248.1024" posZ="800.600" width="100" height="100" depth="100"/>
<colsphere posX="1024.768" posY="1248.1024" posZ="800.600" radius="100"/>
<coltube posX="1024.768" posY="1248.1024" posZ="800.600" radius="30" height="15"/>
<colrectangle posX="1024.768" posY="1248.1024" posZ="800.600" width="100" depth="61.8"/>
<colcircle posX="1024.768" posY="1248.1024" posZ="800.600" radius="30"/>
```

### Atributos Necessários

- **posX**: Um [float](mta://reference/misc/float.md) representando a posição X do colshape.

- **posY**: Um [float](mta://reference/misc/float.md) representando a posição Y do colshape.

- **posZ**: Um [float](mta://reference/misc/float.md) representando a posição Z do colshape.

- **radius**: O raio do colshape (somente esferas, círculos e tubos).

- **width**: A largura do colshape (somente retângulos e cubos).

- **depth**: A profundidade do colshape (somente retângulos e cubos).

- **height**: A altura do colshape (somente cubos).

### Atributos Opcionais

- **dimension**: A dimensão que o colshape estará.

## Funções de scripting relacionadas

- [addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)

- [createColCircle](mta://scripting/shared/functions/createcolcircle.md)

- [createColCuboid](mta://scripting/shared/functions/createcolcuboid.md)

- [createColPolygon](mta://scripting/shared/functions/createcolpolygon.md)

- [createColRectangle](mta://scripting/shared/functions/createcolrectangle.md)

- [createColSphere](mta://scripting/shared/functions/createcolsphere.md)

- [createColTube](mta://scripting/shared/functions/createcoltube.md)

- [getColPolygonHeight](mta://scripting/shared/functions/getcolpolygonheight.md)

- [getColPolygonPoints](mta://scripting/shared/functions/getcolpolygonpoints.md)

- [getColPolygonPointPosition](mta://scripting/shared/functions/getcolpolygonpointposition.md)

- [getColShapeType](mta://scripting/shared/functions/getcolshapetype.md)

- [getColShapeRadius](mta://scripting/shared/functions/getcolshaperadius.md)

- [getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)

- [isInsideColShape](mta://scripting/shared/functions/isinsidecolshape.md)

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)
