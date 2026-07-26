---
doc_id: "mta-wiki:9156"
title: "ES/getPlayerName"
source_title: "Es/getPlayerName"
source_url: "https://wiki.multitheftauto.com/wiki/Es/getPlayerName"
revision_id: 49537
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:14:59.696726+00:00"
---

# ES/getPlayerName

Esta funcion devuelve un string conteniendo el nombre de un jugador especifico.

## Syntax

```
string getPlayerName ( player thePlayer )
```

### Argumentos requeridos

- **thePlayer:** el jugador de quien quieres obtener el nombre.

### Returns

Devuelve un string conteniendo el nombre del jugador, o *false* si el jugador pasado en el argumento no es valido.

### Limites

- El nombre de un jugador puede en caracteres ASCII entre 33 y 126 estan permitidos ( latino basico ):

```
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
```

- Minimo de caracteres en el nombre de un jugador es de 1.

- Maximo de caracteres en el nombre de un jugador es de 22.

- No es posible obtener el nombre de un jugador repetido.

## Ejemplo

Click to collapse [-]
Server

```
addCommandHandler("myname",
  function(playerSource)
    outputChatBox("Tu nombre: "..getPlayerName(playerSource), playerSource)
  end
)
```

Click to collapse [-]
Client

Este ejemplo pone el nombre del jugador en el chat.

```
addCommandHandler("myname",
  function()
   local localPlayerName = getPlayerName(getLocalPlayer())
   --y nosotros lo ponemos en el chat
   outputChatBox(localPlayerName)
  end
)
```

## Mira tambien

- [getLocalPlayer](mta://scripting/client/functions/getlocalplayer.md)

- [getPlayerMapBoundingBox](mta://scripting/client/functions/getplayermapboundingbox.md)

- [getPlayerMapOpacity](mta://scripting/client/functions/getplayermapopacity.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [getPlayerHudComponentProperty](mta://scripting/client/functions/getplayerhudcomponentproperty.md)

- [isPlayerMapVisible](mta://scripting/client/functions/isplayermapvisible.md)

- [isPlayerHudComponentVisible](mta://scripting/client/functions/isplayerhudcomponentvisible.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22751](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22751):

- [isPlayerCrosshairVisible](mta://scripting/client/functions/isplayercrosshairvisible.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [resetPlayerHudComponentProperty](mta://scripting/client/functions/resetplayerhudcomponentproperty.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [setPlayerHudComponentProperty](mta://scripting/client/functions/setplayerhudcomponentproperty.md)

- **Shared**

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
