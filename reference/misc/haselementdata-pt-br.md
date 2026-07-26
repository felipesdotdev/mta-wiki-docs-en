---
doc_id: "mta-wiki:12827"
title: "PT-BR/HasElementData"
source_title: "HasElementData/PT-BR"
source_url: "https://wiki.multitheftauto.com/wiki/HasElementData/PT-BR"
revision_id: 81235
language: "en"
categories: []
generated_at: "2026-07-26T16:07:50.169745+00:00"
---

# PT-BR/HasElementData

Esta função verifica se um elemento tem [dado de elemento](https://wiki.multitheftauto.com/wiki/PT-BR/Element_data)(element data) disponível.

## Sintaxe

```
bool hasElementData ( element oElemento, string chave [, bool herdar = true] )
```

**Sintaxe POO(OOP)** [Não entendeu o que significa isso?](mta://tutorials/oop-introduction.md)

**Método**: *[elemento](mta://reference/misc/elemento.md):hasData(...)*

### Argumentos Necessários

- **oElemento:** Este é o elemento que você quer verificar se armazena dados.

- **chave:** O nome da chave de dado em que o elemento está ou não armazenando. (Máximo 31 caracteres.)

### Argumentos Opcionais

- **herdar:** Alterna se a função deve ou não ir para o topo da hierarquia para achar a chave requisitada nos casos específicos em que o elemento não tenha isso.

### Retorna

Retorna *true* se o elemento contém dado da *chave*, ou *false* se o elemento não existe ou não há dado associado à *chave*.

## Exemplo

Este exemplo mostra o animal favorito ao jogador usando o comando 'bichinho' se ele tiver um definido.

Click to collapse [-]
Server

```
function MeuAmigaozao ( source, commandName, playerName )
    local oJogador = source
    if playerName then -- veja se o nick de algum jogador foi especificado
        oJogador = getPlayerFromName (playerName) -- obtenha o elemento-jogador através do nick especificado
        if not oJogador then -- Se nós ainda não encontramos um jogador então...
            outputChatBox ( "Não foi possível encontrar: '" .. playerName .. "'", source ) -- mostre a mensagem de erro
            return
        end
    end

    if hasElementData ( oJogador, "animal_favorito" ) then -- verifique se o jogador tem um animal favorito definido
        local favAnimal = getElementData ( oJogador, "animal_favorito" ) -- obtém o animal favorito do jogador  .-.
        outputChatBox ( "O animal favorito de"..getPlayerName ( oJogador ).." : "..favAnimal, source ) -- informe o animal favorito do jogador
    else
        outputChatBox ( getPlayerName ( oJogador ).." não tem um animal favorito", source ) -- informa que o jogador não tem animal favorito
    end
end
-- Adicionamos um comando para executar a função MeuAmigaozao e ver o animal favorito de um jogador especificado
addCommandHandler ( "bichinho", MeuAmigaozao )
```

## Veja também

- [attachElements](mta://scripting/shared/functions/attachelements.md)

- [createElement](mta://scripting/shared/functions/createelement.md)

- [destroyElement](mta://scripting/shared/functions/destroyelement.md)

- [detachElements](mta://scripting/shared/functions/detachelements.md)

- [getAttachedElements](mta://scripting/shared/functions/getattachedelements.md)

- [getElementAlpha](mta://scripting/shared/functions/getelementalpha.md)

- [getElementAttachedOffsets](mta://scripting/shared/functions/getelementattachedoffsets.md)

- [getElementAttachedTo](mta://scripting/shared/functions/getelementattachedto.md)

- [getElementByIndex](mta://scripting/shared/functions/getelementbyindex.md)

- [getElementByID](mta://scripting/shared/functions/getelementbyid.md)

- [getElementChild](mta://scripting/shared/functions/getelementchild.md)

- [getElementChildren](mta://scripting/shared/functions/getelementchildren.md)

- [getElementChildrenCount](mta://scripting/shared/functions/getelementchildrencount.md)

- [getElementCollisionsEnabled](mta://scripting/shared/functions/getelementcollisionsenabled.md)

- [getElementColShape](mta://scripting/shared/functions/getelementcolshape.md)

- [getElementData](mta://scripting/shared/functions/getelementdata.md)

- [getAllElementData](mta://scripting/shared/functions/getallelementdata.md)

- [hasElementData](mta://scripting/shared/functions/haselementdata.md)

- [getElementDimension](mta://scripting/shared/functions/getelementdimension.md)

- [getElementHealth](mta://scripting/shared/functions/getelementhealth.md)

- [getElementID](mta://scripting/shared/functions/getelementid.md)

- [getElementInterior](mta://scripting/shared/functions/getelementinterior.md)

- [getElementMatrix](mta://scripting/shared/functions/getelementmatrix.md)

- [getElementModel](mta://scripting/shared/functions/getelementmodel.md)

- [getElementParent](mta://scripting/shared/functions/getelementparent.md)

- [getElementPosition](mta://scripting/shared/functions/getelementposition.md)

- [getElementRotation](mta://scripting/shared/functions/getelementrotation.md)

- [getElementsByType](mta://scripting/shared/functions/getelementsbytype.md)

- [getElementsWithinColShape](mta://scripting/shared/functions/getelementswithincolshape.md)

- [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md)

- [getElementType](mta://scripting/shared/functions/getelementtype.md)

- [getElementVelocity](mta://scripting/shared/functions/getelementvelocity.md)

- [getLowLODElement](mta://scripting/shared/functions/getlowlodelement.md)

- [getRootElement](mta://scripting/shared/functions/getrootelement.md)

- [isElement](mta://scripting/shared/functions/iselement.md)

- [isElementAttached](mta://scripting/shared/functions/iselementattached.md)

- [isElementCallPropagationEnabled](mta://scripting/shared/functions/iselementcallpropagationenabled.md)

- [isElementDoubleSided](mta://scripting/shared/functions/iselementdoublesided.md)

- [isElementFrozen](mta://scripting/shared/functions/iselementfrozen.md)

- [isElementInWater](mta://scripting/shared/functions/iselementinwater.md)

- [isElementLowLOD](mta://scripting/shared/functions/iselementlowlod.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22864](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22864):

- [isElementOnFire](mta://scripting/shared/functions/iselementonfire.md)

- [isElementWithinColShape](mta://scripting/shared/functions/iselementwithincolshape.md)

- [isElementWithinMarker](mta://scripting/shared/functions/iselementwithinmarker.md)

- [setElementAlpha](mta://scripting/shared/functions/setelementalpha.md)

- [setElementAngularVelocity](mta://scripting/shared/functions/setelementangularvelocity.md)

- [getElementAngularVelocity](mta://scripting/shared/functions/getelementangularvelocity.md)

- [setElementAttachedOffsets](mta://scripting/shared/functions/setelementattachedoffsets.md)

- [setElementCallPropagationEnabled](mta://scripting/shared/functions/setelementcallpropagationenabled.md)

- [setElementCollisionsEnabled](mta://scripting/shared/functions/setelementcollisionsenabled.md)

- [setElementData](mta://scripting/shared/functions/setelementdata.md)

- [setElementDimension](mta://scripting/shared/functions/setelementdimension.md)

- [setElementDoubleSided](mta://scripting/shared/functions/setelementdoublesided.md)

- [setElementFrozen](mta://scripting/shared/functions/setelementfrozen.md)

- [setElementHealth](mta://scripting/shared/functions/setelementhealth.md)

- [setElementID](mta://scripting/shared/functions/setelementid.md)

- [setElementInterior](mta://scripting/shared/functions/setelementinterior.md)

- [setElementModel](mta://scripting/shared/functions/setelementmodel.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22864](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22864):

- [setElementOnFire](mta://scripting/shared/functions/setelementonfire.md)

- [setElementParent](mta://scripting/shared/functions/setelementparent.md)

- [setElementPosition](mta://scripting/shared/functions/setelementposition.md)

- [setElementRotation](mta://scripting/shared/functions/setelementrotation.md)

- [setElementVelocity](mta://scripting/shared/functions/setelementvelocity.md)

- [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)
