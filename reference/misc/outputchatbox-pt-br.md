---
doc_id: "mta-wiki:12472"
title: "PT-BR/OutputChatBox"
source_title: "OutputChatBox/PT-BR"
source_url: "https://wiki.multitheftauto.com/wiki/OutputChatBox/PT-BR"
revision_id: 70885
language: "en"
categories: ["Mudanças_em_1.5.7"]
generated_at: "2026-07-26T16:07:35.784290+00:00"
---

# PT-BR/OutputChatBox

|  | Nota: Evite enviar texto para a caixa de bate-papo que não seja realmente um bate-papo, pois isso pode ser irritante para os jogadores. Envie informações e mensagens de status para o HUD. OBS: Isto é algo opcional mas de muita utilidade, fica a critério dos desenvolvedores do servidor. |
| --- | --- |
|  |  |

|  | Nota: A partir da versão r20391, visibleTo aceita tabela de jogadores e elemento-equipe |
| --- | --- |
|  |  |

Esta função envia texto para a caixa de bate-papo. Pode ser interpretado como uma mensagem, aviso, etc. para determinados jogadores ou todos os jogadores.

Opcionalmente, pode incorporar alterações de cores na sequência, definindo o valor booleano *colorCoded* como true. Isso permite:

```
outputChatBox ( "#FF0000E aí #00FF00Brasil!", getRootElement(), 255, 255, 255, true )
```

Isto mostrará: **E aí Brasil!**

## Sintaxe

Click to collapse [-]
Server

```
bool outputChatBox ( string text [, element visibleTo = getRootElement(), int r = 231, int g = 217, int b = 176, bool colorCoded = false ] )
```

**Sintaxe POO(OOP)** [Não entendeu o que significa isso?](mta://tutorials/oop-introduction.md)

**Método**: *[player](mta://reference/misc/player.md):outputChat(...)*

## Argumento Obrigatório

- **text:** O texto que será enviado para a janela de chat. Se tiver mais que 256 caracteres o texto não será enviado.

## Argumentos Opcionais

*NOTA:* Ao usar argumentos opcionais, pode ser necessário fornecer todos os argumentos anteriores ao que você deseja usar. Para obter mais informações sobre argumentos opcionais, consulte [Argumentos Opcionais](https://wiki.multitheftauto.com/wiki/BR/Argumentos_Opcionais).

- **visibleTo:** Este argumento define para quem você quer que seja enviado o texto.

ADICIONADO/ATUALIZADO NA VERSÃO 1.5.7 [r20391](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=20391):

- **visibleTo:** Você pode especificar uma tabela (de índices numéricos) com jogadores (como valores dos índices), um [elemento-jogador](mta://reference/misc/elemento-player.md), ou um [elemento-equipe](mta://reference/misc/elemento-team.md) (Team). Confira [visibilidade](https://wiki.multitheftauto.com/wiki/PT-BR/Visibility).

- **r:** A quantidade de vermelho na cor do texto. O valor padrão é 231.

- **g:** A quantidade de verde na cor do texto. O valor padrão é 217.

- **b:** A quantidade de azul na cor do texto. O valor padrão é 176.

- **colorCoded:** Um valor booleano que determina ou não se as tags '#RRGGBB' devem ser usadas.

Nota: O formato #RRGGBB deve conter letras maiúsculas, a-f não é aceitável, mas A-F é. Os valores padrões RGB usado neste formato é: '#E7D9B0'.

Click to collapse [-]
Client

```
bool outputChatBox ( string text [, int r = 231, int g = 217, int b = 176, bool colorCoded = false ] )
```

## Argumentos Obrigatórios

- **text:** O texto que será enviado para a janela de chat. Se tiver mais que 256 caracteres o texto não será enviado.

## Argumentos Opcionais

*NOTA:* Ao usar argumentos opcionais, pode ser necessário fornecer todos os argumentos anteriores ao que você deseja usar. Para obter mais informações sobre argumentos opcionais, consulte [Argumentos Opcionais](https://wiki.multitheftauto.com/wiki/BR/Argumentos_Opcionais).

- **r:** A quantidade de vermelho na cor do texto. O valor padrão é 231.

- **g:** A quantidade de verde na cor do texto. O valor padrão é 217.

- **b:** A quantidade de azul na cor do texto. O valor padrão é 176.

- **colorCoded:** Um valor booleano que determina ou não se as tags '#RRGGBB' devem ser usadas.

Nota: O formato #RRGGBB deve conter letras maiúsculas, a-f não é aceitável, mas A-F é. Os valores padrões RGB usado neste formato é: '#E7D9B0'.

## Retorno

Retorna *true* se a mensagem foi enviada com sucesso. Retorna *false* se argumentos inválidos foram especificados.

## Exemplo

Click to collapse [-]
Server

**Exemplo 1:** Este exemplo mostra uma mensagem no chat para todos os jogadores.

```
x = 5
y = 10  
-- Mostra a mensagem
outputChatBox ( "Eu tenho " .. x .. " abacates e " .. y .. " melancias." )
```

**Exemplo 2:** Este evento envia uma simples mensagem com cores, "Vermelho Branco", onde o 'Branco' está na cor branca, e 'Vermelho' na cor vermelha.

```
outputChatBox ( "Vermelho #FFFFFFBranco", getRootElement(), 255, 0, 0, true )
```

**Exemplo 3:** Este exemplo permite o chat colorido, de acordo com a cor que o jogador definiu em seu nick.

```
function colouredChat ( message, theType )
	if theType == 0 then --Se for uma mensagem normal no chat (sem ser /me ou chat de grupo) então
		cancelEvent() -- cancela o envio da mensagem
		message = string.gsub(message, "#%x%x%x%x%x%x", "") -- remove qualquer cor usada na mensagem pelo jogador com a função nativa de Lua: string.gsub
		local r,g,b = getPlayerNametagColor ( source ) -- pegamos a cor que o jogador usa em seu nick
		local chatterName = getPlayerName ( source ) -- pegamos o nick dele
		-- envia a mensagem com o nick e a cor do nick, e o resto em branco.
		outputChatBox ( chatterName..":#FFFFFF "..message, getRootElement(), r, g, b, true )
	end
end
addEventHandler("onPlayerChat", getRootElement(), colouredChat)
```

**Exemplo 4:** Este exemplo mostra uma mensagem no chat para um jogador chamado *fulano*.

```
-- Ache o elemento jogador pelo nick dele: 'fulano'
myPlayer = getPlayerFromName ( "fulano" )
-- Se um jogador foi achado pelo seu nick 'fulano' então...
if ( myPlayer ~= false ) then
    x = 5
    y = 10
    -- Mostre a mensagem
    outputChatBox ( "Eu tenho " .. x .. " celulares e " .. y .. " fones de ouvido.", myPlayer )
end
```

**Exemplo 5:** Essas duas funções podem acelerar a digitação, e mostra a mensagem para quando o jogador entrar no servidor.

```
local msg_red, msg_green, msg_blue = 255, 255, 0

function servertalkprivate(message, sendto)
        -- Fale com o jogador diretamente
	outputChatBox(tostring(message), sendto, msg_red, msg_green, msg_blue, true)
end

function servertalk(message)
        -- Fala para todos
	servertalkprivate(message, getRootElement())
end

function quandoEntrar()
	servertalkprivate("Bem vindo ao Brasil", source)
end

addEventHandler("onPlayerJoin", getRootElement(), quandoEntrar)
```

**Exemplo 6:** Isto pode ser usado para quando um jogador entrar no servidor e então definir o colete dele para 100.

```
function onJoin()
         setPedArmor(source, 100)
         local playerName = getPlayerName(source)
         outputChatBox("Bem vindo ".. playerName .." ao servidor", source, 0, 154, 255)
end
addEventHandler("onPlayerJoin", root, onJoin)
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
