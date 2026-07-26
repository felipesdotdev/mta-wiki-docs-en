---
doc_id: "mta-wiki:4651"
title: "IT/Resource:Admin"
source_title: "Resource:IT/Admin"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AIT/Admin"
revision_id: 49954
language: "en"
categories: ["IT/Risorse", "IT/Concetti_di_scripting", "IT/Pagine_italiane"]
generated_at: "2026-07-26T16:17:01.656309+00:00"
---

# IT/Resource:Admin

**«** Torna alla [Pagina principale italiana ▇▇▇](https://wiki.multitheftauto.com/wiki/IT/Pagina_principale).

Un breve tutorial su come ottenere i privilegi da admin ed installare la resource **admin** sul proprio server.

**Nota:** Il server non dovrebbe essere avviato durante le operazioni sottostanti.

## accounts.xml

Per prima cosa apri il file **accounts.xml** dislocato in **<SERVER>\mods\deathmatch\** ed aggiungi un nodo con le informazioni del tuo account, come nell'esempio.

 

Esempio 1: accounts.xml

## acl.xml

Poi apri il file **acl.xml**, nella stessa cartella, e aggiungiti come oggetto al gruppo Admin usando la sintassi *user.**, dove *** è il tuo Nickname come nell'esempio.

 

Esempio 2: acl.xml

## mtaserver.conf

Adesso apri il file **mtaserver.conf** e vai fino in fondo, accertati che la resource **admin** sia presente nella lista di quelle che vengono avviate con il server.
**Nota:** L'attributo **protected="1"** indica che la risorsa non può essere fermata.

 

Esempio 3: mtaserver.conf

## Login

Ora che haio finito con i file del server, puoi finalmente avviarlo. Connettiti al server ed esegui il login con i dati del tuo account usando il comando

```
/login [username] <password>
```

(rimuovi lo slash iniziale se esegui il comando da console). Se ti viene richiesto di premere il tasto **p** hai fatto tutto correttamente, congratulazioni!
