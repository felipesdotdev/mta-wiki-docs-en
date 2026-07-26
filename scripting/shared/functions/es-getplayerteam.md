---
doc_id: "mta-wiki:12818"
title: "ES/getPlayerTeam"
source_title: "Es/getPlayerTeam"
source_url: "https://wiki.multitheftauto.com/wiki/Es/getPlayerTeam"
revision_id: 69210
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:14:59.709418+00:00"
---

# ES/getPlayerTeam

Esta funcion permite obtener el equipo en el que esta un jugador.

## Syntax

```
team getPlayerTeam ( player thePlayer )
```

### Argumentos requeridos

- **thePlayer**: El [player](mta://reference/misc/player.md) ( Jugador ) de quien quieres obtener el equipo.

### Returns

Nos devuelve el *equipo* en el que esta el player, devuelve *false* si el jugador no pertenece a ningun equipo.

## Ejemplo

Click to collapse [-]
Server

Este ejemplo busca el equipo del jugador, y luego le cambia de nombre.

```
function teamName ( source, key, newTeamName )
    local playerTeam = getPlayerTeam ( source )          -- obtener el equipo del jugador
    if ( playerTeam ) then                               -- si el esta en un equipo...
        local oldTeamName = getTeamName ( playerTeam )   -- obtener el nombre del equipo
        setTeamName ( playerTeam, newTeamName )          -- cambiar el nombre del equipo
        outputChatBox ( "El jugador " .. getPlayerName ( source ).." ha cambiado el nombre del equipo " .. oldTeamName .. " por " .. newTeamName, root, 0, 255, 0, false )
    else
        outputChatBox ( getPlayerName ( source ) .. " no estas en un equipo", source, 255, 0, 0, false )
    end
end
addCommandHandler ( "teamname", teamName )
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
