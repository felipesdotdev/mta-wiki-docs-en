---
doc_id: "mta-wiki:12819"
title: "ES/setPlayerMoney"
source_title: "Es/setPlayerMoney"
source_url: "https://wiki.multitheftauto.com/wiki/Es/setPlayerMoney"
revision_id: 69212
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:14:59.729985+00:00"
---

# ES/setPlayerMoney

Esta funcion pone una cantidad fija al dinero de un jugador. Debería ser notado que el ajuste de valores negativos no trabaja y de hecho da cantidades de dinero grandes al jugador.

**Nota:** Usar esta funcion en client side (no recomendado) no cambiara el dinero del jugador en el server side.

## Syntax

Click to collapse [-]
Server

```
bool setPlayerMoney ( player thePlayer, int amount )
```

### Argumentos requeridos

- **thePlayer:** El jugador el cual quieres indicar la cantidad de su dinero.

- **amount:** La cantidad del cual quieres indicarle.

Click to collapse [-]
Client

```
bool setPlayerMoney ( int amount )
```

### Argumentos requeridos

- **amount:** La cantidad del dinero el cual quieres indicarle.

### Returns

Devuelve *true* si el dinero fue añadido, o *false* si los parametros pasados son invalidos.

## Ejemplo

**Ejemplo 1:** Este ejemplo hace que cuando tu ejecutes el comando /setcash <cantidad> le ponga la cantidad indicada al jugador que ejecuto el comando.

```
function setCash ( thePlayer, command, amount )       -- cuando el comando setcash es ejecutado
    setPlayerMoney ( thePlayer, tonumber(amount) )    -- cambiar el dinero del jugador por la indicada
end
addCommandHandler ( "setcash", setCash )           -- agrega el comando setcash
```

**Example 2:** Este ejemplo le pone el dinero indicado a todos los jugadores en el server con el comando /leet.

```
function leetmoney()
	setPlayerMoney( getRootElement(), 1337 )
end
addCommandHandler("leet", leetmoney)
```

## Mira tambien

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- [forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)

- [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md)

- [getPlayerFromName](mta://scripting/shared/functions/getplayerfromname.md)

- [getPlayerMoney](mta://scripting/shared/functions/getplayermoney.md)

- [getPlayerName](mta://scripting/shared/functions/getplayername.md)

- [getPlayerNametagColor](mta://scripting/shared/functions/getplayernametagcolor.md)

- [getPlayerNametagText](mta://scripting/shared/functions/getplayernametagtext.md)

- [getPlayerPing](mta://scripting/shared/functions/getplayerping.md)

- [getPlayerWantedLevel](mta://scripting/shared/functions/getplayerwantedlevel.md)

- [givePlayerMoney](mta://scripting/shared/functions/giveplayermoney.md)

- [isPlayerMapForced](mta://scripting/shared/functions/isplayermapforced.md)

- [isPlayerNametagShowing](mta://scripting/shared/functions/isplayernametagshowing.md)

- [setPlayerHudComponentVisible](mta://scripting/shared/functions/setplayerhudcomponentvisible.md)

- [setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md)

- [setPlayerNametagColor](mta://scripting/shared/functions/setplayernametagcolor.md)

- [setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md)

- [setPlayerNametagText](mta://scripting/shared/functions/setplayernametagtext.md)

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)
