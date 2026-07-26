---
doc_id: "mta-wiki:12473"
title: "PT-BR/RedirectPlayer"
source_title: "RedirectPlayer/PT-BR"
source_url: "https://wiki.multitheftauto.com/wiki/RedirectPlayer/PT-BR"
revision_id: 76369
language: "en"
categories: ["Server_functions", "Changes_in_1.2"]
generated_at: "2026-07-26T16:07:35.826928+00:00"
---

# PT-BR/RedirectPlayer

Esta função redireciona o jogador para um servidor específico.

|  | Nota: O mod que usar esta função precisará de permissões de ACL para funcionar (function.redirectPlayer) |
| --- | --- |
|  |  |

## Sintaxe

```
bool redirectPlayer ( player thePlayer, string serverIP = "", int serverPort = 0 [, string serverPassword = "" ] )
```

**Sintaxe POO(OOP)** [Não entendeu o que significa isso?](mta://tutorials/oop-introduction.md)

**Método**: *[player](mta://reference/misc/player.md):redirect(...)*

### Argumentos necessários

- **thePlayer:** O jogador que você quer redirecionar.

- **serverIP:** O endereço IP (ou nome de domínio que o endereço utilize) do servidor para qual quer redirecionar o jogador. **Use uma string vazia para reconectar no servidor em que já estava.**

- **serverPort:** A porta do servidor para qual quer redirecionar o jogador, que geralmente é 22003. **Coloque 0 para que a porta usada seja a mesma do servidor em que está atualmente.**

### Argumento opcional

- **serverPassword:** A senha para o servidor, caso o mesmo esteja trancado.

### Retorna

Retorna *true* se o jogador foi redirecionado com sucesso, *false* se argumentos inválidos foram especificados.

## Exemplo

Este exemplo auto-redireciona todos os jogadores que entrarem no servidor para o servidor especificado' IP:PORTA.

```
local ip_port = "123.123.1.2:1234"	-- coloque o IP e porta do servidor no seguinte formato: 192.168.1.1:22003
local senha = "senha_para_conectar" -- Se o servidor estiver trancado, coloque a senha aqui (Se não, não precisa especificar a variável na função)

function Redirecionar()
	redirectPlayer(source, gettok(ip_port,1,":"), tonumber(gettok(ip_port,2,":")), senha)
end
addEventHandler ("onPlayerJoin", root, Redirecionar)
```

Este exemplo adiciona o comando "irservidor" usando a sintaxe, "/irservidor IP_servidor Port_servidor [Sen_servidor]".

```
function irParaOServidor (playerSource, commandName, IP_servidor, Port_servidor, Sen_servidor)
	if IP_servidor and Port_servidor then -- Se o IP e a Porta foram especificados, então
		if Sen_servidor then -- Se a senha também foi especificada
			redirectPlayer (playerSource, IP_servidor, tonumber(Port_servidor), Sen_servidor) -- redireciona o jogador
		else -- Se a senha não foi especificada
			redirectPlayer (playerSource, IP_servidor, tonumber(Port_servidor))  -- redireciona o jogador para o servidor sem especificar o parâmetro da senha
		end
	else -- Se o IP e a Porta não foram especificados
		outputChatBox ("Erro! Siga a sintaxe: /irservidor IP Porta [Senha]", playerSource) -- Exiba a mensagem de erro para o jogador
	end
end

addCommandHandler ("irservidor", irParaOServidor)
```

Este exemplo adiciona o comando "reentrar" que pode se parecer com o **/reconnect** nativo do MTA.

```
function Reentrar (oJogador, cmd)
	redirectPlayer(oJogador)
end
addCommandHandler("reentrar", Reentrar) -- Anexe o comando à função designada
```

## Veja também

- [forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)

- [getAlivePlayers](mta://scripting/server/functions/getaliveplayers.md)

- [getDeadPlayers](mta://scripting/server/functions/getdeadplayers.md)

- [getPlayerACInfo](mta://scripting/server/functions/getplayeracinfo.md)

- [getPlayerAnnounceValue](mta://scripting/server/functions/getplayerannouncevalue.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [getPlayerCount](mta://scripting/server/functions/getplayercount.md)

- [getPlayerFromName](mta://scripting/shared/functions/getplayerfromname.md)

- [getPlayerIdleTime](mta://scripting/server/functions/getplayeridletime.md)

- [getPlayerIP](mta://scripting/server/functions/getplayerip.md)

- [getPlayerMoney](mta://scripting/shared/functions/getplayermoney.md)

- [getPlayerName](mta://scripting/shared/functions/getplayername.md)

- [getPlayerNametagColor](mta://scripting/shared/functions/getplayernametagcolor.md)

- [getPlayerNametagText](mta://scripting/shared/functions/getplayernametagtext.md)

- [getPlayerPing](mta://scripting/shared/functions/getplayerping.md)

- [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerVersion](mta://scripting/server/functions/getplayerversion.md)

- [getPlayerWantedLevel](mta://scripting/shared/functions/getplayerwantedlevel.md)

- [getRandomPlayer](mta://scripting/server/functions/getrandomplayer.md)

- [givePlayerMoney](mta://scripting/shared/functions/giveplayermoney.md)

- [isPlayerMapForced](mta://scripting/shared/functions/isplayermapforced.md)

- [isPlayerMuted](mta://scripting/server/functions/isplayermuted.md)

- [isPlayerNametagShowing](mta://scripting/shared/functions/isplayernametagshowing.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [redirectPlayer](mta://scripting/server/functions/redirectplayer-pt-br.md)

- [resendPlayerACInfo](mta://scripting/server/functions/resendplayeracinfo.md)

- [resendPlayerModInfo](mta://scripting/server/functions/resendplayermodinfo.md)

- [setPlayerAnnounceValue](mta://scripting/server/functions/setplayerannouncevalue.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [setPlayerHudComponentVisible](mta://scripting/shared/functions/setplayerhudcomponentvisible.md)

- [setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md)

- [setPlayerMuted](mta://scripting/server/functions/setplayermuted.md)

- [setPlayerName](mta://scripting/server/functions/setplayername.md)

- [setPlayerNametagColor](mta://scripting/shared/functions/setplayernametagcolor.md)

- [setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md)

- [setPlayerNametagText](mta://scripting/shared/functions/setplayernametagtext.md)

- [setPlayerScriptDebugLevel](mta://scripting/server/functions/setplayerscriptdebuglevel.md)

- [setPlayerTeam](mta://scripting/server/functions/setplayerteam.md)

- [setPlayerVoiceBroadcastTo](mta://scripting/server/functions/setplayervoicebroadcastto.md)

- [setPlayerVoiceIgnoreFrom](mta://scripting/server/functions/setplayervoiceignorefrom.md)

- [setPlayerWantedLevel](mta://scripting/server/functions/setplayerwantedlevel.md)

- [spawnPlayer](mta://scripting/server/functions/spawnplayer.md)

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [takePlayerScreenShot](mta://scripting/server/functions/takeplayerscreenshot.md)
