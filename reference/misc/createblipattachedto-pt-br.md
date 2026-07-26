---
doc_id: "mta-wiki:12811"
title: "PT-BR/createBlipAttachedTo"
source_title: "CreateBlipAttachedTo/PT-BR"
source_url: "https://wiki.multitheftauto.com/wiki/CreateBlipAttachedTo/PT-BR"
revision_id: 71403
language: "en"
categories: ["Changes_in_1.0"]
generated_at: "2026-07-26T16:07:49.421257+00:00"
---

# PT-BR/createBlipAttachedTo

Esta função cria um [blip](mta://reference/misc/elemento-blip.md) que é anexado à um [elemento](mta://reference/misc/elemento.md). Este blip é exibido como um ícone no radar do client e vai 'seguir' o elemento no qual foi anexado.

## Sintaxe

Click to collapse [-]
Servidor

```
blip createBlipAttachedTo ( element elementoParaAnexar [, int icone = 0, int tamanho = 2, int r = 255, int g = 0, int b = 0, int a = 255, int ordem = 0, float distanciaDeVisibilidade = 16383.0, element visivelPara = getRootElement( ) ] )
```

Click to collapse [-]
Client

```
blip createBlipAttachedTo ( element elementoParaAnexar [, int icone = 0, int tamanho = 2, int r = 255, int g = 0, int b = 0, int a = 255, int ordem = 0, float distanciaDeVisibilidade = 16383.0 ] )
```

**Sintaxe POO(OOP)** [Não entendeu o que significa isso?](mta://tutorials/oop-introduction.md)

**Método**: *[Blip](mta://reference/misc/elemento-blip.md).createAttachedTo(...)*

### Argumentos necessários

- **elementoParaAnexar:** O [elemento](mta://reference/misc/elemento.md) para anexar o blip.

### Argumentos opcionais

*NOTA:* Ao usar argumentos opcionais, pode ser necessário fornecer todos os argumentos anteriores ao que você deseja usar. Para obter mais informações sobre argumentos opcionais, consulte [Argumentos Opcionais](https://wiki.multitheftauto.com/wiki/BR/Argumentos_Opcionais).

- **icone:** Um [int](mta://reference/misc/int.md) para determinar qual blip deve ser criado. Valores válidos disponíveis em [Blips](https://wiki.multitheftauto.com/wiki/PT-BR/Blips).

- **tamanho:** O tamanho do blip. Somente aplicável ao ícone **Marker**. Valor por padrão é 2. Máximo 25.

- **r:** A quantidade de vermelho na cor do blip (0 - 255). Somente aplicável ao ícone **Marker**. Padrão é 255.

- **g:** A quantidade de verde na cor do blip (0 - 255). Somente aplicável ao ícone **Marker**. Padrão é 0.

- **b:** A quantidade de azul na cor do blip (0 - 255). Somente aplicável ao ícone **Marker**. Padrão é 0.

- **a:** A quantidade de alpha na cor do blip (0 - 255). Somente aplicável ao ícone **Marker**. Padrão é 255.

- **ordem:** Isto define a ordem de nível-Z do blip (-32768 à 32767). Padrão é 0.

- **distanciaDeVisibilidade:** A distância máxima que o blip pode ser visto no mini-mapa. (0-65535)

Click to collapse [-]
Servidor

- **visivelPara:** Qual elemento poderá ver o blip. Por padrão todos podem ver. Confira [visibilidade](https://wiki.multitheftauto.com/wiki/PT-BR/Visibility).

### Retorna

Retorna um [blip](mta://reference/misc/elemento-blip.md) se tiver sido criado com sucesso, caso contrário retorna false.

## Exemplo

Click to collapse [-]
Server

Este exemplo cria um blip anexado à um jogador aleatório, visível para todos. O blip seguirá o jogador enquanto ele se move.

```
-- Obtenha um jogador aleatório
function setupRandomRobber ()
	local myPlayer = getRandomPlayer ()
	-- Cria um blip na posição do jogador(grudado nele), com o ícone de cifrão e visível para todos.
	local myBlip = createBlipAttachedTo ( myPlayer, 52 )
end
```

## Veja também

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
