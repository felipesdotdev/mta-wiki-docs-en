---
doc_id: "mta-wiki:12809"
title: "PT-BR/Argumentos Opcionais"
source_title: "Argumentos Opcionais/PT-BR"
source_url: "https://wiki.multitheftauto.com/wiki/Argumentos_Opcionais/PT-BR"
revision_id: 69088
language: "en"
categories: []
generated_at: "2026-07-26T16:07:49.348041+00:00"
---

# PT-BR/Argumentos Opcionais

**Argumentos Opcionais** são argumentos que podem opcionalmente ser passados para qualquer função Lua, incluindo os internos do MTA: SA. Eles não são necessários para a função ser executada e podem ser desabilitados (valor == *[nil](mta://reference/misc/nil.md)*). Frequentemente, esse tipo de argumento não faz uma enorme diferença no comportamento da função.

É uma convenção Lua em que os argumentos escritos entre colchetes são opcionais, portanto, neste Wiki, você também pode encontrar funções com alguns argumentos entre colchetes. Isso significa que eles são opcionais e que não é necessário fornecê-los.

Vamos dar uma olhada nesta função:

```
vehicle createVehicle ( int model, float x, float y, float z, [ float rx, float ry, float rz ] )
```

Neste exemplo, *rx*, *ry*, and *rz* são argumentos opcionais, pois estão entre colchetes. Eles não precisam ser fornecidos para a função; será padronizado para nenhuma rotação em todos os eixos. Se fornecida, a função utilizará as rotações especificadas.

## Por que argumentos opcionais são usados?

Na maioria das vezes, é chato ter que fornecer todos os argumentos de uma determinada função, especialmente se eles são os mesmos repetidamente. Os argumentos opcionais permitem que o scripter transmita apenas os dados realmente necessários para seu script, e isso ajuda a melhorar a legibilidade e o tamanho do código.

## Usando os argumentos opcionais

O argumento opcional é utilizado como argumentos normais. A única diferença é que eles serão padronizados para um determinado valor, se não for fornecido (em outras palavras, se *opcionalArgument == nil*, será então *opcionalArgument = defaultValue*).

Um problema comum para programadores novos é quando eles desejam fornecer apenas um argumento opcional, sem definir os que estão antes dele. Bem, isso é realmente simples de "consertar". Normalmente, eles podem ser definidos como *[nil](mta://reference/misc/nil.md)*, então eles serão padronizados com seus valores correspondentes enquanto o scripter ainda é capaz de definir o que ele realmente deseja. Por exemplo, se você quer somente definir a rotação do eixo Z da função [createVehicle](mta://scripting/shared/functions/createvehicle.md) (e não sabe que *rx* e *ry* tem como padrão, o zero):

```
vehicle createVehicle ( int model, float x, float y, float z, [ float rx, float ry, float rz ] )
```

Você pode usar:

```
local meuCarrinho = createVehicle( getVehicleModelFromName( "Infernus" ), 0, 0, 5, nil, nil, 180 )
```

E o resultado será o carro Infernus girado 180 graus no eixo Z, no centro do mapa.

|  | Aviso: Existem algumas funções nativas do MTA: SA que não seguem esta concordância, especialmente quando um argumento opcional está intimamente relacionado a outro (ex.: argumentos de cores nas funções DX e provavelmente outros): ao invés de substituir o valor nil , eles informam o erro 'bad argument' e não fazem nada. Sempre verifique se isso funciona com uma função antes de usá-la em um script . |
| --- | --- |
|  |  |

## Funções personalizadas com argumentos opcionais

Estas funções com argumentos opcionais ficam fáceis de ser gerenciada quando usado o **if** :

```
function aNotSoUsefulFunction( text )
    if type( text ) == "string" or type( text ) == "nil" then -- Verifica se os argumentos corretos foram fornecidos
        local realTextToOutput
        if text == nil then
            realTextToOutput = "Eu <3 argumentos opcionais" -- Se a variável text for igual a nil (não especificado), é usado um padrão
        else
            realTextToOutput = text -- Aqui é definido o texto que o usuário especificou, isso se ele definiu
        end
        outputChatBox( realTextToOutput ) -- Texto publicado no chat
    end
end
```

Você também pode usar [short-circuit evaluation](http://en.wikipedia.org/wiki/Short-circuit_evaluation), se você preferir:

```
function aNotSoUsefulFunction( text )
    local realTextToOutput = ( type( text ) == "string" or type( text ) == "nil" ) and ( type( text ) == "string" and text or "Eu <3 argumentos opcionais" ) or nil
    if realTextToOutput then -- Verifica se há algo para postar no chat
        outputChatBox( realTextToOutput ) -- Poste o texto
    end
end
```
