---
doc_id: "mta-wiki:11984"
title: "Elemento/Object"
source_title: "Elemento/Object"
source_url: "https://wiki.multitheftauto.com/wiki/Elemento/Object"
revision_id: 65094
language: "en"
categories: []
---

# Elemento/Object

A classe de objeto representa modelos estáticos em 3D no mundo do GTA. Os objetos podem representar apenas modelos criados pelo servidor, não podem representar modelos que fazem parte do cenário padrão do GTA. Exemplos de objetos incluem modelos de construção, estradas e terrenos.

O tipo de elemento desta classe é **"object"**.

## Sintaxe XML

```
<object model="" posX="" posY="" posZ="" rotX="" rotY="" rotZ="" interior="" dimension="" scale="" collisions="" alpha="" frozen="" />
```

### Required Attributes

- **model**: The ID of the object being created. Since GTA has thousands of objects, these are hard to document on the wiki. Instead, they can be found using the object browser in the map editor.

- **posX**: Um [float](mta://reference/misc/float.md) representando a posição X do objeto.

- **posY**: Um [float](mta://reference/misc/float.md) representando a posição Y do objeto..

- **posZ**: Um [float](mta://reference/misc/float.md) representando a posição Z do objeto..

### Optional Attributes

- **rotX**: Um [float](mta://reference/misc/float.md) representando a rotação X do objeto em graus.

- **rotY**: Um [float](mta://reference/misc/float.md) representando a rotação Y do objeto em graus.

- **rotZ**: Um [float](mta://reference/misc/float.md) representando a rotação Z do objeto em graus.

- **interior**: O interior em que o objeto está.

- **dimension**: O número da dimensão do objeto.

- **scale**: Tamanho do objeto.

- **collisions**: Ativado/Desativado as colisões do objeto.

- **alpha**: Altera o alpha.

- **frozen**: Define se o objeto deve ser congelado

## Funções de scripting relacionadas

- [createObject](mta://scripting/shared/functions/createobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22489](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22489):

- [breakObject](mta://scripting/shared/functions/breakobject.md)

- [getObjectScale](mta://scripting/shared/functions/getobjectscale.md)

- [moveObject](mta://scripting/shared/functions/moveobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22708](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22708):

- [respawnObject](mta://scripting/shared/functions/respawnobject.md)

- [toggleObjectRespawn](mta://scripting/shared/functions/toggleobjectrespawn.md)

- [isObjectRespawnable](mta://scripting/shared/functions/isobjectrespawnable.md)

- [setObjectScale](mta://scripting/shared/functions/setobjectscale.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

- [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

- [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)
