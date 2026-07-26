---
doc_id: "mta-wiki:12470"
title: "PT-BR/AddCommandHandler"
source_title: "AddCommandHandler/PT-BR"
source_url: "https://wiki.multitheftauto.com/wiki/AddCommandHandler/PT-BR"
revision_id: 69183
language: "en"
categories: []
generated_at: "2026-07-26T16:07:35.793668+00:00"
---

# PT-BR/AddCommandHandler

| [[{{{image}}}\|link=\|]] | Nota Importante: NÃO use o mesmo nome do comando para a sua função, pois isso pode causar confusão se várias funções forem usadas pelo mesmo comando. Use um nome que descreva o objetivo de sua função mais especificamente. |
| --- | --- |
|  |  |

Essa função anexará uma função (handler) de script à um comando do console, para que sempre que um jogador ou administrador use o comando, a função seja chamada.

Vários manipuladores de comando podem ser anexados a um único comando e serão chamados na ordem em que os manipuladores foram anexados. Da mesma forma, vários comandos podem ser manipulados por uma única função e o parâmetro *nomeDoComando* é usado para decidir o curso da ação.

Para usuários, um comando está no formato:

*nomeDoComando* *argumento1* *argumento2*

Isso pode ser acionado no console do jogador ou diretamente da caixa de bate-papo, prefixando a mensagem com uma barra (*/*). O administrador do servidor também poderá executar o comando através do console do servidor, da mesma maneira que são acionados no console do jogador.

|  | Nota: Você não pode usar "check", "list", "test" ou outro nome que já exista de forma nativa como um nome de comando. |
| --- | --- |
|  |  |

## Sintaxe

Click to collapse [-]
Lado servidor

```
bool addCommandHandler ( string commandName, function handlerFunction [, bool restricted = false, bool caseSensitive = true ] )
```

### Argumentos Necessários

- **commandName:** Este é o nome do comando ao qual você deseja anexar um manipulador. É isso que deve ser digitado no console para ativar a função.

- **handlerFunction:** Essa é a função que você deseja que o comando seja acionado, que deve ser definida antes da adição do manipulador. Esta função pode ter dois parâmetros, *playerSource* e *commandName*, seguidos de quantos parâmetros você espera após o seu comando (veja abaixo). Tudo isso é opcional.

#### Parâmetros da função callback

Esses são os parâmetros que serão definidos na função quando o comando for executado

```
player playerSource, string commandName [, string arg1, string arg2, ... ]
```

- **playerSource:** O jogador que acionou o comando ou o [server console](mta://reference/misc/element-console.md). Se não for acionado por um jogador e nem pelo console do servidor, isso será *false*.

- **commandName:** O nome do comando acionado. Isso é útil se vários comandos acionam uma só função.

- **arg1, arg2, ...:** Cada palavra após o nome do comando no comando original é passada aqui em uma variável separada. Se não houver valor para um argumento, sua variável conterá [nil](mta://reference/misc/nil.md). Você pode lidar com um número variável de argumentos usando a expressão vararg, conforme mostrado em **Exemplo 2 (server-side)** abaixo.

### Argumentos Opcionais

*NOTA:* Ao usar argumentos opcionais, pode ser necessário fornecer todos os argumentos anteriores ao que você deseja usar. Para obter mais informações sobre argumentos opcionais, consulte [Argumentos Opcionais](https://wiki.multitheftauto.com/wiki/BR/Argumentos_Opcionais).

- **restricted:** Especifique se esse comando deve ou não ser restrito por padrão. Use isso em comandos que devem estar inacessíveis para todos como padrão, exceto usuários especiais especificados na ACL (Lista de controle de acesso). Isso é para garantir que comandos de administração, como por exemplo: 'punish' não estará disponível para todos se um administrador de servidor esquecer de mascará-lo na ACL. Certifique-se de adicionar o comando à sua ACL no grupo apropriado para que seja útil (ou seja, <right name = "command.punish" access = "true"> </right>). O argumento padrão é false se nada for especificado.

- **caseSensitive:** Especifica se o manipulador de comando ignorará o caso sensitivo para esse nome de comando. Se true, para executar o comando deve digitá-lo da mesma forma como foi especificado no 1° argumento, se false, independente de maiúsculas ou minúsculas, o comando será executado.

Click to collapse [-]
Lado cliente

```
bool addCommandHandler ( string commandName, function handlerFunction [, bool caseSensitive = true ] )
```

### Argumentos Necessários

- **commandName:** Este é o nome do comando ao qual você deseja anexar um manipulador. É isso que deve ser digitado no console para ativar a função.

- **handlerFunction:** Essa é a função que você deseja que o comando seja acionado, que deve ser definida antes da adição do manipulador. Esta função pode ter o parâmetro *commandName*, seguido de quantos parâmetros você espera após o seu comando (veja abaixo). Tudo isso é opcional.

#### Parâmetros da função callback

Esses são os parâmetros que serão definidos na função quando o comando for executado

```
string commandName [, string arg1, string arg2, ... ]
```

- **commandName:** O nome do comando acionado. Isso é útil se vários comandos acionam uma só função.

- **arg1, arg2, ...:** Cada palavra após o nome do comando no comando original é passada aqui em uma variável separada. Se não houver valor para um argumento, sua variável conterá [nil](mta://reference/misc/nil.md). Você pode lidar com um número variável de argumentos usando a expressão vararg, conforme mostrado em **Exemplo 2 (server-side)** abaixo.

### Argumentos Opcionais

*NOTA:* Ao usar argumentos opcionais, pode ser necessário fornecer todos os argumentos anteriores ao que você deseja usar. Para obter mais informações sobre argumentos opcionais, consulte [Argumentos Opcionais](https://wiki.multitheftauto.com/wiki/BR/Argumentos_Opcionais).

- **caseSensitive:** Especifica se o manipulador de comando ignorará o caso sensitivo para esse nome de comando. Se true, para executar o comando deve digitá-lo da mesma forma como foi especificado no 1° argumento, se false, independente de maiúsculas ou minúsculas, o comando será executado.

### Retornos

Retorna *true* se o manipulador de comandos foi adicionado com sucesso, *false* caso contrário.

## Exemplos

Click to collapse [-]
Lado servidor

**Exemplo 1:** Este exemplo criará um comando chamado *createmarker*. Isso vai criar um [marker](mta://reference/misc/marker.md) vermelho na posição do jogador que o usa.

```
-- Defina nossa função que será chamada pelo comando
function consoleCreateMarker ( playerSource, commandName )
        -- Se um jogador quem acionou a função (em vez do administrador) então
	if ( playerSource ) then
		-- Obtém a posição do jogador
		local x, y, z = getElementPosition ( playerSource )
		-- Cria um marker vermelho do tipo checkpoint e de tamanho 2 na posição do jogador
		createMarker ( x, y, z, "checkpoint", 2, 255, 0, 0, 255 )
		-- Diga ao jogador sobre o marker
		outputChatBox ( "Você tem um marker vermelho :D", playerSource )
	end
end
-- Anexe a função 'consoleCreateMarker' ao comando "createmarker"
addCommandHandler ( "createmarker", consoleCreateMarker )
```

Click to expand [+]
Lado servidor

**Exemplo 2:** Este exemplo utiliza a expressão vararg de Lua para implementar um comando *check_parameters* para contar o número de parâmetros passados, mesclá-los todos em uma única string e produzi-los. Isso também mostra como você pode usar o *table.concat* para mesclar todos os argumentos passados. Isso é particularmente útil quando você deseja ler uma frase do texto passada pelo usuário.

```
-- Defina a função que será acionada pelo comando (que pode aceitar várias quantidades de variáveis de argumentos após commandName)
function consoleCheckParameters ( playerSource, commandName, ... )
	-- Se o jogador (não admin) que chamou esta função
	if playerSource then
		local arg = {...}
		-- Obtém o número de argumentos na tabela arg (a tabela arg é o mesmo que: {...})
		local parameterCount = #arg
		-- Mencione isso no chat do jogador
		outputChatBox ( "Number of parameters: " .. parameterCount, playerSource )
		-- Junte-os em uma única sequência separada por vírgula
		local stringWithAllParameters = table.concat( arg, ", " )
		-- Mostre isto para o jogador através do chat
		outputChatBox ( "Parameters passed: " .. stringWithAllParameters, playerSource )
	end
end
-- Anexe a função 'consoleCheckParameters' ao comando "check_parameters"
addCommandHandler ( "check_parameters", consoleCheckParameters )
```

Click to expand [+]
Lado servidor

**Exemplo 3:** Este exemplo mostra o uso de uma única função que é acionada por vários comandos. Isso não é recomendado para uso geral, pois torna o código mais difícil de entender, mas onde vários comandos compartilham alguma lógica, pode ser uma maneira útil de reduzir o código duplicado. Geralmente, seria preferível colocar essa lógica compartilhada em uma função separada, pois isso oferece mais controle sobre o fluxo.

```
-- crie a função
function moneyCmd(player, commandName, amount)
    if getElementData(player, "canUseMoneyFunctions") then -- a lógica compartilhada
        if commandName == "givemoney" then
            amount  = tonumber(amount)
            if amount then
                givePlayerMoney(player, amount)
            else
                outputChatBox("[usage] /givemoney [amount]", player)
            end
        else if commandName == "takemoney" then
            amount = tonumber(amount)
            if amount then
                takePlayerMoney(player, amount)
            else
                outputChatBox("[usage] /takemoney [amount]", player)
            end
        end
    else
        outputChatBox("Você não pode usar este comando", player)
    end
end
 
addCommandHandler("givemoney", moneyCmd);
addCommandHandler("takemoney", moneyCmd);
```

Click to expand [+]
Lado cliente

**Example 1:** Este exemplo direciona o player para um local aleatório próximo (útil para quando um player fica preso em algum lugar).

```
function escapeMe ( commandName )
	local x, y, z = getElementPosition ( localPlayer ) -- Obtém a posição do jogador
	setElementPosition ( localPlayer, x+(math.random(-10,10)), y+(math.random(-10,10)), z+(math.random(1,15)) ) -- Move o jogador aleatoriamente para uma posição perto da anterior. X é x + um número entre -10, 10 e assim por diante.
end    
addCommandHandler ( "escape", escapeMe ) -- Quando o jogador digita o comando "/escape" no chat, ou "escape" in console
```

## Veja também

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIpFromMasterServer](mta://scripting/server/functions/getserveripfrommasterserver.md)

- [getServerName](mta://scripting/server/functions/getservername.md)

- [getServerPassword](mta://scripting/server/functions/getserverpassword.md)

- [getServerPort](mta://scripting/server/functions/getserverport.md)

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)
