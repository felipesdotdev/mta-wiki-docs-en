---
doc_id: "mta-wiki:4153"
title: "Resource : IT/Scoreboard"
source_title: "Resource:IT/Scoreboard"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AIT/Scoreboard"
revision_id: 17376
language: "en"
categories: ["IT/Pagine_italiane", "100%", "IT/Risorse"]
generated_at: "2026-07-26T16:17:12.777002+00:00"
---

# Resource : IT/Scoreboard

**«** Torna alla [Pagina principale italiana ▇▇▇](https://wiki.multitheftauto.com/wiki/IT/Pagina_principale).

La **scoreboard** mostra i giocatori connessi, i [team](https://wiki.multitheftauto.com/wiki/IT/Elemento/Team), i ping e altri dati in una tabella per i giocatori ingame. Possiede anche una interfaccia Javascript, può quindi essere vista da un browser web.

Quando aggiungi una colonna alla scoreboard, essa viene linkata all'[element data](https://wiki.multitheftauto.com/index.php?title=IT/Element_data&action=edit&redlink=1) con quello stesso nome, quindi se aggiungi una colonna *score*, essa mostrerà il valore dell'element data di nome *score* di ogni team e giocatore.

## Funzioni esportate

Queste sono le funzioni dello scroreboard utilizzabili tramite la funzione [call()](https://wiki.multitheftauto.com/index.php?title=IT/call&action=edit&redlink=1).

- ```
bool addScoreboardColumn( string columnName, [ element visibleToElement = getRootElement(), int columnPosition = #columns - 1, float columnSize = 0.1 ] )
```

Aggiunge una colonna alla scoreboard.

- ```
bool removeScoreboardColumn( string columnName )
```

Rimuove una colonna dalla scoreboard.

- ```
bool setPlayerScoreboardForced( player thePlayer, bool forced )
```

Setta a forzata (true) o nono forata (false) la visualizzazione della scoreboard ad un [player](https://wiki.multitheftauto.com/wiki/IT/Elemento/Player).

- ```
table getScoreboardColumns( )
```

Ritorna un [array](https://wiki.multitheftauto.com/index.php?title=IT/Table&action=edit&redlink=1) ordinato di valori {name=columnName,size=columnSize}.

- ```
bool resetScoreboardColumns( )
```

Elimina tutte le colonne meno *nome* e *ping*.

Puoi impostare l'element data della scoreboard usando [setElementData](https://wiki.multitheftauto.com/index.php?title=IT/setElementData&action=edit&redlink=1):

```
setElementData ( thePlayer, "wanted level", 3 ) --3 viene inserito nella colonna "wanted level" del giocatore
```

## Problemi/Da fare

- Il nome della colonna deve essere unico, non puoi ancora aggiungere una colonna con nome identico a due [elementi](https://wiki.multitheftauto.com/wiki/IT/Elemento).

- I dati della scoreboard per il web vengono inviati tutti in una volta, deve essere possibile inviarne pezzi separati.
