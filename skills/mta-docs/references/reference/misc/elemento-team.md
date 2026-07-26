---
doc_id: "mta-wiki:12073"
title: "Elemento/Team"
source_title: "Elemento/Team"
source_url: "https://wiki.multitheftauto.com/wiki/Elemento/Team"
revision_id: 65382
language: "en"
categories: []
---

# Elemento/Team

A classe Grupo representa os grupos de jogadores. Jogadores de mesmo grupo podem usar recursos de grupo como chat de grupo ou até fogo amigo.

O tipo de elemento desta classe é: **"team"**.

**NOTA:** É provável que os valores da cor R/G/B sejam alterados para a cor mais padrão ="#RRGGBB" antes da versão final

## Sintaxe XML

```
<team name="" colorR="" colorG="" colorB="" friendlyfire=""/>
```

### Atributos Necessários

- **name**: Nome do grupo

### Optional Attributes

- **colorR**: O componente vermelho da cor do grupo

- **colorG**: O componente verde da cor do grupo

- **colorB**: O componente azul da cor do grupo

- **friendlyfire**: Fogo amigo deve(true) ou não(false) ser ativado

## Funções de scripting relacionadas

### Cliente

- **Shared**

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)

### Servidor

- [getTeamColor](mta://scripting/shared/functions/getteamcolor.md)

- [getTeamFriendlyFire](mta://scripting/shared/functions/getteamfriendlyfire.md)

- [getTeamFromName](mta://scripting/shared/functions/getteamfromname.md)

- [getTeamName](mta://scripting/shared/functions/getteamname.md)
