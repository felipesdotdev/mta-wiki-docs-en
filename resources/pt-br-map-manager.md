---
doc_id: "mta-wiki:6592"
title: "PT-BR/Recursos:Map Manager"
source_title: "Resource:PT-BR/Map manager"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3APT-BR/Map_manager"
revision_id: 34499
language: "en"
categories: ["PT-BR/Recursos"]
generated_at: "2026-07-26T16:10:45.245480+00:00"
---

# PT-BR/Recursos:Map Manager

O map manager é um recurso que já está incluido na instalação do servidor. Ele oferece comandos, funções e eventos para que gamemodes administrem dinamicamente seus mapas. Por exemplo, quando um servidor de corrida precisa carregar mapas diferentes para cada partida, em vez de armazenar todos esses mapas em um único recurso, estes podem ser amarzenados em recursos separados e carregados com uma função simples, chamada de "changeGamemodeMap".

Esta ferramenta faz uma lista de gamemodes/mapas e gerencia o carregamento destes no servidor. Com base em certas informações, contidas em cada mapa, o map manager afeta o mundo do jogo (exemplo: o nível do mar ou a gravidade), afeta o gamemode em execução e altera o nome do mapa que está vigorando no momento. Está incluido também uma ferramenta para disponibilizar em tempo real, via a um website, o mapa e o gamemode que estão sendo execultados no momento.

## Um simples tutorial

Nesta sessão iremos incrementar o gamemode básico que criamos no artigo [Introdução ao Scripting](https://wiki.multitheftauto.com/wiki/PT-BR/Introducao_ao_Scripting). Primeiramente, vamos criar um recurso que funciona como um simples mapa contendo um spawnpoint e vamos fazer com que o script de nosso gamemode criado anteriormente carregue estes dados para que os jogadores possam nascer.

Para começar, criemos uma pasta em /server/mods/deathmatch/resources/[gamemodes]/[meu_gamemode]/[maps]/, e vamos nomea-la como "meu_mapa". Dentro da pasta "meu_mapa", crie um arquivo com o bloco de notas chamado "meta.xml", o qual é requisito existir em todos os recursos.

Copie as seguintes linhas para o arquivo "meta.xml":

```
<meta>
   <info type="map" gamemodes="meu_gamemode"/>
   <map src="mymap.map"/>
</meta>
```

- A marcação **info type=""** indica o que seu recurso é: um script, gamemode ou mapa.

- Note que este mapa está "ligado" ao nosso recurso devido a definição **gamemodes=""**, a qual contém o nome do mesmo.

- A marcação **map src=""** indica qual é o nome do arquivo do tipo .map que vai conter os dados dos posicionamentos de spawnpoints, objetos ou pickups no mundo do GTA.

Agora vamos criar um outro arquivo na mesma pasta chamado "meumapa.map", e escrever as seguintes linhas dentro dele:

```
<map>
   <spawnpoint id="spawnpoint1" posX="1959.5487060547" posY="-1714.4613037109" posZ="18" rot="63.350006103516" model="0"/>
</map>
```

O "spawnpoint" é um tipo de um elemento usado pela função [getElementsByType](mta://scripting/shared/functions/getelementsbytype.md), tanto como "id" é usada pela função [getElementByID](mta://scripting/shared/functions/getelementbyid.md).

Para carregar os dados do mapa, o nosso script precisa ter acesso ao mapa de fato. Então editemos nosso script.lua de nosso gamemode adicionando as seguintes linhas:

```
function loadMap(startedMap)
	mapRoot = getResourceRootElement(startedMap)
end

addEventHandler("onGamemodeMapStart", getRootElement(), loadMap)
```

- Basicamente, o evento "onGamemodeMapStart" nos dá as informações do seguinte mapa ("startedMap") fornecido pelo recurso que nós temos o controle.

```
function joinHandler()
	local spawn = getElementsByType("spawnpoint", mapRoot)
	local x,y,z,r
	for key, value in pairs(spawn) do
		x = getElementData(value, "posX")
		y = getElementData(value, "posY")
		z = getElementData(value, "posZ")
		r = getElementData(value, "rot")
	end
	spawnPlayer(source, x, y, z)
	fadeCamera(source, true)
end
```

- Com o tal recurso "em mãos", vamos extrair as informações do spawnpoint (posição, rotação, skin do personagem...). Dê uma olhada na função joinHandler(). Em vez de especificar as cordenadas x, y e z, usamos as que estão contidas no mapa extraido.

Agora vamos, via o console do servidor (MTAserver.exe), iniciar o nosso gamemode com o seguinte comando:

**gamemode myserver mymap**

Voilà, nascemos exatamente no local onde está posicionado o spawnpoint. Se quiser expandir seus conhecimentos para desenolver mais o seu gamemode é ensenssial que você explore nossa [Página Inicial](https://wiki.multitheftauto.com/wiki/PT-BR/P%C3%A1gina_Inicial) e visite o nosso [Fórum](http://forum.mtasa.com/viewforum.php?f=120) para tirar suas dúvidas ou fazer sugestões.

## Uso

Para usar o map manager, seus recursos precisam ser marcados como gamemodes ou mapas.

Se seu recurso for um **gamemode**, devemos informar isso ao nosso servidor, usando a marcação type na sessção *info*:

```
<info description="Nosso gamemode" type="gamemode" />
```

Se seu recurso for um **mapa** ele precisa tanto da marcação *type="map"*, como também da marcação **gamemodes="..."**, onde os "..." seriam os gamemodes compatíveis com o mapa. Estes precisam ser separados com virgula e *sem espaços*.

```
<info description="Um mapa para o nosso gamemode" type="map" gamemodes="ctv,koth" />
```

- Lembrando que a marcação **description** serve para você adicionar uma descrição para seu recurso.

Só pode haver um gamemode e um mapa rodando no servidor.

## Marcações opicionais

Se você desejar, podes adicionar as seguintes informações na sessão **info**:

**name:** Esta informação serve para você adicionar um nome amigável para seu mapa ou gamemode em vez de ser disponibilizado o nome do arquivo/pasta para os jogadores:

```
<info description="Um mapa para o nosso gamemode" type="map" gamemodes="ctv,koth" name="[Race]Nosso Mapa" />
```

## Comandos

**changemap novomapa [novogamemode]** (muda o mapa para o qual você deseja. É opicional também mudar o gamemode)

**changemode novogamemode [novomapa]** (muda para um novo gamemode. É opicional começar um mapa com ele)

**gamemode newgamemode [newmap]** (tem a mesma função da anterior)

**stopmode** (para o atual gamemode e mapa)

**stopmap** (para o mapa atual)

**maps [gamemode]** (lista todos os mapas instalados no servidor. É opicional também listar somente aqueles que são compatíveis com o gamemode específicado)

**gamemodes** (lista todos os gamemodes)

## Configurando o Map manager

***mapmanager.color** [as cores em hexadecimal] (muda a cor das mensagens do mapmanager. Por padrão é: #E1AA5A)

***mapmanager.messages** [boolean] (Indica se o mapmanager pode enviar uma mensagem a todos a cada vez que um mapa/gm muda. Por padrão é: ture (verdadeiro).

***mapmanager.ASE** [boolean] (Permite que a ferramenta automaticamente publique o gamemode/mapa atual para todos os jogadores que estão na janela Browser ou no site da gamemonitor. Por padrão é: ture)

## Funções

- Essas são as funções que o mapmamanger oferece para ser usado em seu script.

```
bool changeGamemode ( resource novoGamemode, [ resource mapaParaCarregar ] )
```

Muda o gamemode atual para um novo (*novoGamemode*). É opicional especificar um mapa (*mapaParaCarregar*) para carregar junto a ele, pois o gamemode vai iniciar sozinho (sem um mapa junto).

```
bool changeGamemodeMap ( resource novoMapa, [ resource gamemodeParaCarregar ] )
```

Muda o mapa atual para um novo (*novoMapa*). É opicional especificar um gamemode (*gamemodeParaCarregar*) para carregar junto a ele, caso o contrário, o mapa vai carregar sem afetar o gamemode em execulção.

```
table getGamemodes ( )
```

Retorna uma tabela com todos os gamemodes disponíveis.

```
table getGamemodesCompatibleWithMap ( resource oMapa )
```

Retorna uma tabela com os gamemodes compatíveis com o mapa especificado (*oMapa*).

```
table getMaps ( )
```

Retorna uma tabela com todos os mapas disponíveis.

```
table getMapsCompatibleWithGamemode ( [ resource oGamemode ] )
```

Retorna uma tabela com os mapas compatíveis com o gamemode especificado (*oGamemode*). Se o gamemode não for especificado, o resultado será aqueles mapas que não são compatíveis com nenhum gamemode.

```
resource getRunningGamemode ( )
```

Retorna o gamemode que está rodando no servidor.

```
resource getRunningGamemodeMap ( )
```

Retorna o mapa que está rodando no servidor.

```
bool isGamemode ( resource oGamemode )
```

Verifica se o gamemode especificado (*oGamemode*) está rodando ou não.

```
bool isGamemodeCompatibleWithMap ( resource oGamemode, resource oMapa )
```

Verifica se o gamemode (*oGamemode*) especificado é compatível com um mapa (*oMapa*) ou não.

```
bool isMap ( resource oMapa )
```

Verifica se o recurso especificado (*oMapa*) é um mapa ou não.

```
bool isMapCompatibleWithGamemode ( resource oMapa, resource oGamemode )
```

Verifica se o mapa especificado (*oMapa*) é compatível com um gamemode (*oGamememode*) ou não.

```
bool stopGamemode ( )
```

Para de execultar o gamemode e o seu mapa.

```
bool stopGamemodeMap ( )
```

Para de execultar somente o mapa.

## Eventos

*Para todos esses eventos, "source" equivale a todos os recursos que estão rodando no servidor*.

```
onGamemodeStart ( resource oGamemodeQueComeçou )
```

O evento é ativado depois que um gamemode é iniciado.

```
onGamemodeStop ( resource oGamemodeQueParou )
```

O evento é ativado depois que um gamemode é parado.

```
onGamemodeMapStart ( resource oMapaQueComeçou )
```

O evento é ativado depois que um mapa é iniciado.

```
onGamemodeMapStop ( resource oMapaQueParou )
```

O evento é ativado depois que um mapa é parado.

## Configurações suportadas

Todo mapa pode ser configurado para alterar o comportamento do mundo do jogo, como a gravidade, a hora, o clima, o número mínimo/máximo de jogadores que podem jogar e entre outros. Isso só é possivel mediante ao [sistema de preferências](mta://reference/misc/settings-system.md) feito justamente para que os usuários possam customizar de uma maneira mais facil o comportamento dos recursos. A maioria dos recursos que já vem instalados, contam com uma interface simples para adicionar estas informações no meta.xml. Para maiores esclarecimentos, abaixo há uma lista com todos os parametros que o Map manager suporta:

**gamespeed** [um número]: A velocidade do jogo enquanto o mapa está rodando. Exemplo: 3
  
**gravity** [um número]: A gravidade do jogo enquanto o mapa está rodando. Exemplo: 0.6
  
**time** [um conjunto de caracteres no formato HH:MM]: A hora do dia. Exemplo: 18:10
  
**weather** [um núemro]: Como vai estar o tempo (ensolarado, nublado, chovendo...) no momento. É necessário que o número escolhido seja [ID](mta://reference/misc/weather.md) válido para que o mapa seja carregado corretamente.
  
**waveheight** [um núemro]: É a altura das ondas geradas no jogo. 
  
**locked_time** [um valor booleano]: Se a hora e o tempo vão ser congelados pelo map manager.
  
**minplayers** [um núemro]: O número mínimo requisito de jogadores para começar o mapa.
  
**maxplayers** [um núemro]: O número máximo permitido de jogadores para começar o mapa.
