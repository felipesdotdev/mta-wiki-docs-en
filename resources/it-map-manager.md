---
doc_id: "mta-wiki:4043"
title: "IT/Resource:Mapmanager"
source_title: "Resource:IT/Map manager"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AIT/Map_manager"
revision_id: 76903
language: "en"
categories: ["IT/Pagine_italiane", "100%", "IT/Risorse"]
generated_at: "2026-07-26T16:17:12.768256+00:00"
---

# IT/Resource:Mapmanager

**«** Torna alla [Pagina principale italiana ▇▇▇](https://wiki.multitheftauto.com/wiki/IT/Pagina_principale).

Il **map manager** è una risorsa inclusa nel pacchetto server di MTA:SA DM e comprende comandi, funzioni ed eventi per le gamemodes per gestire dinamicamente le loro mappe. Ad esempio, quando un server ha bisogno di caricare diverse mappe per una race mode, invece di essere messe tutte nella risorsa della gamemode, possono essere inserite in una risorsa separata ed essere successivamente richiamate con la funzione "changeGamemodeMap" quando una nuova gara inizia.

Più specificamente, il map manager memorizza la lista di tutte le gamemodes/mappe e ne gestisce il caricamento; applica alcune impostazioni della mappa che hanno effetto sul mondo del gioco e setta le regole della mappa e il tipo di gioco su ASE. Comprende inoltre una funzione che visualizza ed aggiorna automaticamente nel browser la mode/mappa.

## Un semplice tutorial

In questa sezione continueremo a lavorare sulla gamemode che abbiamo creato nella pagina [introduzione allo Scripting](https://wiki.multitheftauto.com/wiki/IT/Introduzione_allo_scripting). Aggiungeremo una semplice risorsa mappa che conterrà gli spawn dei giocatori e caricherà i dati nello script principale quando un giocatore dovrà spawnare.

Innanzitutto crea una cartella sotto

```
<SERVER>/mods/deathmatch/resources/
```

, che chiamerai **mymap**. Dentro

```
/mymap/
```

crea un file di testo chiamato **meta.xml**, che è necessario a tutte le risorse.

Inserisci questo codice all'interno di *meta.xml*:

```
<meta>
   <info type="map" gamemodes="myserver"/>
   <map src="mymap.map"/>
</meta>
```

Notare che questa risorsa è collegata allo script principale tramite l'attributo

```
gamemodes=""
```

, che contiene il nome della risorsa principale. Nel tag

```
map
```

è indicato il nome del file .map che contiene le informazioni sulla mappa.
Ora crea un altro file di testo sotto

```
/mymap/
```

e chiamalo **mymap.map**, inserendovi questo codice:

```
<map>
   <spawnpoint id="spawnpoint1" posX="1959.5487060547" posY="-1714.4613037109" posZ="18" rot="63.350006103516" model="0"/>
</map>
```

Notare che

```
spawnpoint
```

è il tipo di elemento usato nella funzione [getElementsByType](https://wiki.multitheftauto.com/index.php?title=IT/getElementsByType&action=edit&redlink=1); così come

```
id
```

è usato nella funzione [getElementByID](https://wiki.multitheftauto.com/index.php?title=IT/getElementByID&action=edit&redlink=1). 
Per caricare i dati della mappa lo script principale ha bisogno di un collegamento con la risorsa della mappa. Modifichiamo il file **script.lua** nella risorsa

```
myserver
```

. Inserisci il seguente codice:

```
function loadMap(startedMap)
	mapRoot = getResourceRootElement(startedMap)
end

addEventHandler("onGamemodeMapStart", g_root, loadMap)
```

In pratica, l'evento

```
onGamemodeMapStart
```

ci da l'handle della mappa ("startedMap"), che abbiamo usato per estrarre l'handle della risorsa contenente la mappa ("mapRoot").
Con l'handle della risorsa possiamo estrarne le informazioni sugli spawnpoint. Creando la funzione

```
joinHandler()
```

dentro **script.lua**, invece di specificare le coordinate **x**, **y** e **z**, possiamo usare i dati della mappa come segue:

```
function joinHandler()
	local spawn = getElementsByType("spawnpoint", mapRoot) --Creiamo una table (array) locale contenente gli elementi <spawnpoint>
	local x,y,z,r --Creaiamo delle variabili locali per tutte le coordinate
	for key, value in pairs(spawn) do --Inseriamo nelle variabili delle coordinate le coordinate prese dall'elemento <spawnpoint>
		x = getElementData(value, "posX")
		y = getElementData(value, "posY")
		z = getElementData(value, "posZ")
		r = getElementData(value, "rot")
	end
	spawnPlayer(source, x, y, z) --Spawniamo il giocatore alle coordinate appena prese
	fadeCamera(source, true) --E impostiamo la sua telecamera su di lui
end
```

Ora puoi far partire la gamemode sul tuo server avviando in console il seguente comando:

```
gamemode myserver mymap
```

## Un tutorial più avanzato

In questo tutorial, invece di avviare la mappa con il comando sopra descritto quando avviamo il server, avvieremo la risorsa con qualche linea di script. Questo può tornare utile se hai molte mappe e vuoi che il server le avvii automaticamente.

Prima di tutto dobbiamo creare un handler per l'evento [onResourceStart](https://wiki.multitheftauto.com/index.php?title=IT/onResourceStart&action=edit&redlink=1), che si attiva quando la risorsa principale viene avviata con il comando

```
gamemode
```

. Poi, con la funzione assegnata all'evento, carichiamo la risorsa mappa e inizializziamo la mappa:

```
function Initialize(startedResource)
	mapRes = getResourceFromName("mymap") --Otteniamo l'handle della risorsa "mymap"
	manager = getResourceFromName("mapmanager") --E quello di "mapmanager"
	startResource(mapRes) --Inizializziamo la risorsa "mymap"
	
	call(manager, "changeGamemodeMap", mapRes, getThisResource()) --E chiamiamo la funzione "changeGamemodeMap" dentro mapmanager
end

addEventHandler("onResourceStart", getResourceRootElement(getThisResource()), Initialize) --Impostiamo Inizialize() come handler per onResourceStart
```

La funzione [call](https://wiki.multitheftauto.com/index.php?title=IT/call&action=edit&redlink=1) permette, come visto, di chiamare una funzione presente in un'altra risorsa, in questo caso la funzione

```
changeGamemodeMap
```

dentro la riosrsa **mapmanager**.

Se provassi ad avviare il server adesso, riceveresti molti errori "access denied" (accesso negato). QUesto perché la risorsa principale, **myserver**, non ha ancora accesso di default alla funzione [startResource](https://wiki.multitheftauto.com/index.php?title=IT/startResource&action=edit&redlink=1). Dobbiamo aggiungere la funzione nell'Access Control List con i diritti necessari.

Vai nella cartella

```
<SERVER>/mods/deathmatch/
```

. Vedrai un file chiamato **acl.xml**, aprilo con un qualsiasi editor di testo ed inserisci il seguente codice:

```
<group name="myserver">
   <acl name="acl_myserver"/>
   <object name="resource.myserver"/>
</group>
<acl name="acl_myserver">
   <right name="function.startResource" access="true"/>
   <right name="function.stopResource" access="true"/>
   <right name="function.restartResource" access="true"/>
</acl>
```

Assicurati che **acl.xml** sia chiuso, quindi riavvia il server; esso ricaricherà il file ACL, dando i diritti di accesso della risorsa alla funzione. Ora puoi avviare la funzione con:

```
gamemode myserver
```

E lo script avvierà la mappa per voi.

## Utilizzo

Per usare il map manager, le tue risorse devono essere prima marcate come *gamemodes* o *mappe*.

Devi contrassegnare le **risorse gamemode** con il tipo corretto nel tag

```
info
```

:

```
<info description="Una gamemode" type="gamemode" />
```

Anche le **risorse mappa** hanno bisogno dell'attributo

```
type="map"
```

, più un attributo

```
gamemodes
```

con una lista di gamemodes con cui sono compatibili, *separate da virgole e senza spazi*.

```
<info description="Una mappa" type="map" gamemodes="ctv,koth" />
```

Il server può caricare al massimo una gamemode e una mappa alla volta.

## Attributi opzionali delle resources

Questi attributi vanno nel tag

```
info
```

della risorsa.

- ```
name
```

: Il nome pubblico della risorsa, che verrà visualizzato nella lista di gamemodes e nei messaggi del server al posto del nome del file.

## Comandi

Questi comandi sono eseguibili sulla risorsa map manager:

- ```
changemap nuovamappa [nuovagamemode]
```

 Cambia la mappa attuale, e opzionalmente anche la gamemode.

- ```
changemode nuovagamemode [nuovamappa]
```

 Cambia la gamemode attuale, e opzionalmente anche la mappa.

- ```
gamemode nuovagamemode [nuovamappa]
```

 Come sopra.

- ```
stopmode
```

 Stoppa la gamemode e la mappa corrente.

- ```
stopmap
```

 Stoppa la mappa corrente.

- ```
maps [gamemode]
```

 Mostra tutte le mappe del server, opzionalmente solo quelle collegate alla gamemode specificata.

- ```
gamemodes
```

 Mostra tutte le gamemodes.

## Impostazioni

- ```
mapmanager.color [colore in codice hex]
```

 Cambia il colore dei messaggi di output del mapmanager con quello in codice esadecimale(**#RRGGBB**) (default: **#E1AA5A**).

- ```
mapmanager.messages [booleano]
```

 **true** se i cambiamenti di gamemode/mappa sono abilitati, **false** se no (default: **true**).

- ```
mapmanager.ASE [booleano]
```

 **true** se il mapmanager può mostrare gamemode e mappa su ASE, **false** se no (default: **true**).

## Funzioni esportate

Queste sono le funzioni del mapmanager utilizzabili tramite la funzione [call()](https://wiki.multitheftauto.com/index.php?title=IT/call&action=edit&redlink=1):

- ```
bool changeGamemode ( resource nuovaGamemode, [ resource mappaDaCaricare ] )
```

Cambia la gamemode in **nuovaGamemode**, impostando opzionalmente una mappa iniziale(**mappaDaCaricare**); di default carica con la mappa.

- ```
bool changeGamemodeMap ( resource nuovaMappa, [ resource gamemodeDaCambiare ] )
```

Cambia la mappa in **nuovaMappa**, impostando opzionalmente una gamemode da avviare prima di cambiare(**gamemodeDaCambiare**); di default carica con la gamemode corrente.

- ```
table getGamemodes ( )
```

Ritorna una table con i puntatori di tutte le gamemodes.

- ```
table getGamemodesCompatibleWithMap ( resource laMappa )
```

Ritorna una table con i puntatori di tutte le gamemode compatibili con **laMappa**.

- ```
table getMaps ( )
```

Ritorna una table con i puntatori di tutte le mappe.

- ```
table getMapsCompatibleWithGamemode ( [ resource laGamemode ] )
```

Ritorna una table con i puntatori di tutte le mappe compatibili con **laGamemode**. Se il parametro non viene specificato, ritorna tutte le mappe che non sono compatibili con nessuna gamemode.

- ```
resource getRunningGamemode ( )
```

Ritorna il puntatore della gamemode attualmente in esecuzione.

- ```
resource getRunningGamemodeMap ( )
```

Ritorna il puntatore della mappa attualmente in esecuzione.

- ```
bool isGamemode ( resource laGamemode )
```

Ritorna se **laGamemode** è o no una gamemode.

- ```
bool isGamemodeCompatibleWithMap ( resource laGamemode, resource laMappa )
```

Ritorna se la gamemode è compatibile con la mappa o no.

- ```
bool isMap ( resource laMappa )
```

Determina se **laMappa** è una mappa o no.

- ```
bool isMapCompatibleWithGamemode ( resource laMappa, resource laGamemode )
```

Ritorna se la mappa è compatibile con la gamemode o no.

- ```
bool stopGamemode ( )
```

Stoppa la gamemode e la mappa correnti.

- ```
bool stopGamemodeMap ( )
```

Stoppa la mappa corrente.

## Eventi

Per tutti questi eventi, **source** è l'elemento root della risorsa.

- ```
onGamemodeStart ( resource gamemodeIniziata )
```

Si attiva prima che venga iniziata una gamemode.

- ```
onGamemodeStop ( resource gamemodeFermata )
```

Si attiva prima che venga fermata una gamemode

- ```
onGamemodeMapStart ( resource mappaIniziata )
```

Si attiva prima che venga iniziata una mappa.

- ```
onGamemodeMapStop ( resource mappaFermata )
```

Si attiva prima che venga fermata una mappa.

## Impostazioni supportate dalle mappe

Le seguenti impostazioni tratte dal [registro](https://wiki.multitheftauto.com/index.php?title=IT/Settings_system&action=edit&redlink=1) vengono applicate dal map manager quando una mappa inizia:

- ```
gamespeed [numero]
```

: La velocità di gioco della mappa.

- ```
gravity [numero]
```

: La gravità della mappa.

- ```
time [stringa tipo 'hh:mm']
```

: L'ora della mappa.

- ```
weather [numero]
```

: L'ID del meteo della mappa.

- ```
waveheight [numero]
```

: L'altezza delle onde della mappa.

- ```
locked_time [booleano]
```

: Se l'ora sarà bloccata o meno.

- ```
minplayers [numero]
```

: Il numero minimo di giocatori per iniziare la mappa.

- ```
maxplayers [numero]
```

: Il massimo numero di giocatori per iniziare la mappa.
