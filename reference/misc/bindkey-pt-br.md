---
doc_id: "mta-wiki:12488"
title: "PT-BR/bindKey"
source_title: "BindKey/PT-BR"
source_url: "https://wiki.multitheftauto.com/wiki/BindKey/PT-BR"
revision_id: 69082
language: "en"
categories: []
generated_at: "2026-07-26T16:07:36.605173+00:00"
---

# PT-BR/bindKey

Esta função vincula uma tecla do jogador para uma função ou comando, que será acionado quando a tecla for pressionada.

## Sintaxe

Click to collapse [-]
Servidor - Sintaxe 1

```
bool bindKey ( player thePlayer, string key, string keyState, function handlerFunction,  [ var arguments, ... ] )
```

### Argumentos Necessários

- **thePlayer:** O jogador que você quer vincular a tecla.

- **key:** A tecla ou controle que você quer vincular à função. Veja [nomes de teclas](https://wiki.multitheftauto.com/wiki/PT-BR/Key_names) para uma lista de possíveis teclas e [nomes de controles](https://wiki.multitheftauto.com/wiki/PT-BR/Control_names) para uma lista de possíveis controles.

- **keyState:** Uma string que tem um dos seguintes valores:

- **"up":** Se a tecla vinculada deve acionar a função quando ela é liberada(desapertada)

- **"down":** Se a tecla vinculada deve acionar a função quando ela é pressionada

- **"both":** Se a tecla vinculada deve acionar a função quando ela é pressionada e liberada

- **handlerFunction:** A função que vai ser acionada quando a tecla do jogador for pressionada/liberada. Esta função deve ter o seguinte formato(parâmetros):

```
function functionName ( player keyPresser, string key, string keyState, [ var arguments, ... ] )
```

Os valores passados para esta função são:

- **keyPresser:** O jogador que pressionou a tecla

- **key:** A tecla que foi pressionada

- **keyState:** O estado da tecla que foi pressionada (*down*, *up* ou *both*)

- **arguments:** Os argumentos opcionais que você especificou quando usou bindKey.

Click to collapse [-]
Servidor - Sintaxe 2

Esta sintaxe alternativa permite você vincular uma tecla à um comando. Isto também vai permitir que os usuários modifiquem os controles em seus menus de configurações. Use em conjunção com [addCommandHandler](https://wiki.multitheftauto.com/index.php?title=PT-BR/addCommandHandler&action=edit&redlink=1) para adicionar o vínculo da tecla (que é um comando) à uma função.

```
bool bindKey ( player thePlayer, string key, string keyState, string commandName, [ string arguments, ... ] )
```

### Argumentos Necessários

- **thePlayer:** O jogador que você vai vincular a tecla.

- **key:** A tecla ou controle que você quer vincular ao comando. Veja [nomes de teclas](https://wiki.multitheftauto.com/wiki/PT-BR/Key_names) para uma lista de possíveis teclas.

- **keyState:** Uma [string](https://wiki.multitheftauto.com/wiki/PT-BR/String) que tem um dos seguintes valores:

- **"up":** Se a tecla vinculada deve acionar a função quando ela é liberada(desapertada)

- **"down":** Se a tecla vinculada deve acionar a função quando ela é pressionada

- **"both":** Se a tecla vinculada deve acionar a função quando ela é pressionada e liberada

- **commandName:** O nome do comando em que a tecla deverá ser vinculada.

### Argumentos Opcionais

- **arguments:**   Argumentos ([string](https://wiki.multitheftauto.com/wiki/PT-BR/String)) que serão usados no comando como se estivesse digitando este comando com estes argumentos. Ex.: */comando argumento1 argumento2 etc*

Click to collapse [-]
Cliente - Sintaxe 1

```
bool bindKey ( string key, string keyState, function handlerFunction,  [ var arguments, ... ] )
```

### Argumentos Necessários

- **key:** A tecla ou controle que será vinculado à função. Veja [nomes de teclas](https://wiki.multitheftauto.com/wiki/PT-BR/Key_names) para uma lista de possíveis teclas e [nomes de controles](https://wiki.multitheftauto.com/wiki/PT-BR/Control_names) para uma lista de possíveis controles.

- **keyState:** Uma [string](https://wiki.multitheftauto.com/wiki/PT-BR/String) que tem um dos seguintes valores:

- **"up":** Se a tecla vinculada deve acionar a função quando ela é liberada(desapertada)

- **"down":** Se a tecla vinculada deve acionar a função quando ela é pressionada

- **"both":** Se a tecla vinculada deve acionar a função quando ela é pressionada e liberada

- **handlerFunction:** A função que será acionada quando a tecla for pressionada. Esta função deve ter o seguinte formato(parâmetros):

```
function functionName ( string key, string keyState, [ var arguments, ... ] )
```

Os valores passados para esta função são:

- **key:** A tecla que foi pressionada

- **keyState:** O estado da tecla que foi pressionada (*down*, *up* ou *both*)

- **arguments:** Os argumentos opcionais que você especificou quando usou bindKey.

Click to collapse [-]
Cliente - Sintaxe 2

Esta sintaxe alternativa permite você vincular uma tecla à um comando. Isto também vai permitir que os usuários modifiquem os controles em seus menus de configurações. Use em conjunção com [addCommandHandler](https://wiki.multitheftauto.com/index.php?title=PT-BR/addCommandHandler&action=edit&redlink=1) para adicionar o vínculo da tecla (que é um comando) à uma função.

```
bool bindKey ( string key, string keyState, string commandName, [ string arguments, ...] )
```

### Argumentos Necessários

- **key:** A tecla ou controle que será vinculado ao comando. Veja [nomes de teclas](https://wiki.multitheftauto.com/wiki/PT-BR/Key_names) para uma lista de possíveis teclas.

- **keyState:** Um [string](https://wiki.multitheftauto.com/wiki/PT-BR/String) que tem um dos seguintes valores:

- **"up":** Se a tecla vinculada deve acionar a função quando ela é liberada(desapertada)

- **"down":** Se a tecla vinculada deve acionar a função quando ela é pressionada

- **"both":** Se a tecla vinculada deve acionar a função quando ela é pressionada e liberada

- **commandName:** Nome do comando em que a tecla será vinculada.

- **arguments:**   Argumentos ([string](https://wiki.multitheftauto.com/wiki/PT-BR/String)) que serão usados no comando como se estivesse digitando este comando com estes argumentos. Ex.: */comando argumento1 argumento2 etc*

### Argumentos Opcionais

*NOTA:* Ao usar argumentos opcionais, pode ser necessário fornecer todos os argumentos anteriores ao que você deseja usar. Para obter mais informações sobre argumentos opcionais, consulte [Argumentos Opcionais](https://wiki.multitheftauto.com/wiki/BR/Argumentos_Opcionais).

- **arguments:** Qualquer argumento que você queira passar para a função quando a tecla for pressionada pelo usuário. Qualquer número de argumentos pode ser especificado, cada um sendo passado para a função designada. Você não pode passar funções.

### Retorno

Retorna *true* se a tecla foi vinculada, senão retorna *false*.

## Exemplos

#### Exemplo 1

Click to collapse [-]
Servidor

Este exemplo vai vincular a tecla 'F1' do jogador e o controle 'fire' à uma função que mostra no chat alguns status.

```
function funcInput ( player, key, keyState )
  outputChatBox ( getPlayerName ( player) .. " " .. (keyState == "down" and "pressionado" or "liberado") .. " a tecla " .. key .. " !" )
end

function bindTheKeys ( player, commandName )
  bindKey ( player, "F1", "down", funcInput )
  bindKey ( player, "F1", "up", funcInput )
  bindKey ( player, "fire", "both", funcInput )
end
addCommandHandler ( "bindme", bindTheKeys )
```

#### Exemplo 2

Click to collapse [-]
Cliente

Este exemplo vai vincular a tecla 'F1' do jogador e o controle 'fire' à uma função que mostra no chat alguns status, no lado cliente.

```
function funcInput ( key, keyState )
	outputChatBox( "Você " .. (keyState == "down" and "pressionou" or "liberou") .. " a tecla " .. key .. " !" )
end

function bindTheKeys ( commandName )
	bindKey( "F1", "down", funcInput )
	bindKey( "F1", "up", funcInput )
	bindKey( "fire", "both", funcInput )
end
addCommandHandler ( "bindme", bindTheKeys )
```

#### Exemplo 3

Click to collapse [-]
Servidor

Este exemplo diz quão legal é o MTA se o jogador se mover para frente.

```
function fanFunction()
  bindKey (source,"forwards","down",
    function(player,key,state)
      outputChatBox (getPlayerName (player) .. "#FFFF00 acha o MTA muito legal.",getRootElement(),255,255,0,true)
    end
  )
end
addEventHandler ("onPlayerLogin",getRootElement(),fanFunction)
```

#### Exemplo 4

Click to collapse [-]
Servidor

Este exemplo cria um input personalizado no chatbox e vincula a tecla para os jogadores que estiverem no grupo da ACL **Admin** quando logam e também quando o resource inicia, e somente quem estiver neste grupo poderá ver a mensagem.

```
addCommandHandler('AdminChat', 
    function (player, cmd, ...)
        local conta = getPlayerAccount(player)
        -- Se algum jogador não usar a tecla e preferir pelo comando, estará apto à esta verificação a seguir
        if isGuestAccount(conta) then return end -- Se for conta 'guest' então o código a seguir deste é cancelado
        if not (isObjectInACLGroup('user.'..getAccountName(conta), aclGetGroup('Admin'))) then return end -- Se não estiver no grupo da ACL Admin, então o código a partir deste é cancelado

        for _, v in ipairs(getElementsByType('player')) do
            -- Neste loop por todos os jogadores é obtido a conta de cada um e é verificado se a conta não é 'guest'e se está no grupo da ACL Admin
            -- Então a mensagem que o 'player' enviou, aparecerá para todos os que estiverem no grupo da ACL e para ele próprio (já que ele está neste grupo rs)
            local conta = getPlayerAccount(v)
            if not isGuestAccount(conta) then
                if (isObjectInACLGroup('user.'..getAccountName(conta), aclGetGroup('Admin'))) then
                    outputChatBox('#FFFFFF[Chat Admin] '..getPlayerName(player)..'#FFFFFF: '..tostring(table.concat(arg, " ")), v, 0, 0, 0, true)
                end
            end
        end
    end
)

addEventHandler('onResourceStart', resourceRoot, -- Quando o resource iniciar, a tecla de todos os que estiverem no grupo da ACL Admin serão vinculadas ao chatbox
    function ()
        for i, v in ipairs(getElementsByType('player')) do
            local conta = getPlayerAccount(v)
            if not isGuestAccount(conta) then
                if (isObjectInACLGroup('user.'..getAccountName(conta), aclGetGroup('Admin'))) then
                    bindKey(v, 'U', 'down', 'chatbox', 'AdminChat')
                end
            end
        end
    end
)

addEventHandler('onPlayerLogin', root, -- Se um jogador logar e a conta que ele logou estiver no grupo da ACL Admin, a tecla dele será vinculada ao chatbox
    function (_, acc)
        if (isObjectInACLGroup('user.'..getAccountName(acc), aclGetGroup('Admin'))) then
            bindKey(source, 'U', 'down', 'chatbox', 'AdminChat')
        end
    end
)
```

  

Agradecimento ao Developer(nick na imagem) por ter testado o código*

- 

-

## Veja também

- [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md)

- [bindKey](mta://scripting/shared/functions/bindkey.md)

- [executeCommandHandler](mta://scripting/shared/functions/executecommandhandler.md)

- [getCommandHandlers](mta://scripting/shared/functions/getcommandhandlers.md)

- [getFunctionsBoundToKey](mta://scripting/shared/functions/getfunctionsboundtokey.md)

- [getKeyBoundToFunction](mta://scripting/shared/functions/getkeyboundtofunction.md)

- [isControlEnabled](mta://scripting/shared/functions/iscontrolenabled.md)

- [removeCommandHandler](mta://scripting/shared/functions/removecommandhandler.md)

- [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md)

- [toggleControl](mta://scripting/shared/functions/togglecontrol.md)

- [unbindKey](mta://scripting/shared/functions/unbindkey.md)
