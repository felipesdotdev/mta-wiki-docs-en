---
doc_id: "mta-wiki:5800"
title: "FR/Meta.xml"
source_title: "Fr/Meta.xml"
source_url: "https://wiki.multitheftauto.com/wiki/Fr/Meta.xml"
revision_id: 69219
language: "en"
categories: ["Translated/Scripting_Concepts"]
generated_at: "2026-07-26T16:10:33.637370+00:00"
---

# FR/Meta.xml

Le ficher *meta.xml* presents MTA with a set of metadata, such as the resource's name, the scripts to include, and which files to precache for sending to clients among other things. It is also the scope of "elements". It is written in XML, which is based on HTML and is the parent of XHTML.

Note: Vous pouvez essayer le generateur de Meta.xml crée par 50p: [http://forum.mtasa.com/viewtopic.php?f=91&t=22247](http://forum.mtasa.com/viewtopic.php?f=91&t=22247)

# Balises

XML est un format de donnée textuel (par balisage) qui est largement utilisé pour la représentation de donnée. MTA utilise un langage basé sur XML pour décrire les métadonnées des ressources en utilisant les balises suivantes:

- **<info />** Informations sur la ressource. Quelques paramètres possibles (tous paramètres arbitraire peut être utilsé/lu avec[getResourceInfo](mta://scripting/server/functions/getresourceinfo.md)):

- **author:** L'auteur de la ressource

- **version:** La version de la ressource

- **name:** Le nom de la ressource

- **description:** Une petite description de la ressource

- **type:** Le type de ressource, ça peut être "gamemode", "script", "map" ou "misc".

- **<script />** Le code source de la ressource, les paramètres possibles sont:

- **src:** Le nom du fichier

- **type:** Le type du code source: "client" ou "server"

- **<map />** La map pour le gamemode, les paramètres possibles sont:

- **src:** Nom du fichier .map (Peut être distant. "maps/filename.map")

- **<file />** Fichier côté client. Principalement des images, .txd, .col, .dff or .xml files. Ces fichiers seront téléchargés par le client lorsque la ressource sera chargée/lancée (ou lors de la connexion)

- **src:** le nom du fichier (peut être un chemin, ex: "images/image.png")

- **<include />** Ressource(s) utilisée(s) par votre ressource

- **resource:** Nom d'une ressource qui sera chargée

- **minversion:** Version minimum de cette **resource** (optionnel)

- **maxversion:** Version maximum de cette **resource** (optionnel)

- **<config />** Fichier de configuration (.xml) auquel la ressource peut accéder, les paramètres possibles sont:

- **src:** Nom du fichier de configuration

- **type:** Type de fichier: "client" ou "server"

- **<export />** Utilisé ceci pour exporter des fonctions, de votre ressource, qui pourront être utilisées par d'autres ressources [call](mta://scripting/shared/functions/call.md)

- **function:** Nom de la fonction

- **type** Si la fonction est côté client ou serveur (valeurs valides: "server" et "client")

- **http:** Permettre d'appeler la fonction via HTTP (true/false)

- **<html />**

- **src:** Le nom du fichier HTTP (peut être un chemin)

- **default:** The html file is one that is shown by default when visiting /resourceName/ on the server. Only one html can be default, the rest are ignored. (true/false)

- **raw:** Le fichier html n'est pas analyser par l'intrepreteur LUA et est traité comme une donnée binaire. Doit être utiliser pour les données binaires (images principalement) (truel/false).

- **<settings> <setting name="" value=""/> </settings>:** La plupart des gamemodes utilisent [settings system](mta://reference/misc/settings-system.md) pour laisser aux administrateurs le choix de la configuration du serveur. Par exemple vous pouvez définir le temps d'une partie et utiliser ensuite [get](mta://scripting/server/functions/get.md) et [set](mta://scripting/server/functions/set.md) pour respectivement récupérer ou changer cette valeur.

- **<min_mta_version />** Version minimum requise pour que cette ressource fonctionne. Pour les ressources officielles, la version minimum doit être généralement définie sur la version courante de MTA:SA (actuellement : "1.6.0"). Voir exemple pour démonstration.

- **client:** Version minimum du client

- **server:** Version minimum du serveur

- **<aclrequest />** Liste des droits nécessaires à cette ressource, [ACL](https://wiki.multitheftauto.com/wiki/FR/ACL).

- **<sync_map_element_data />**

Permet de contrôler si les [données d’éléments](mta://reference/misc/element-data--975d1ea3.md) du mapping telle que "PosX" et "DoubleSided" sont transférées au client. Ces données ne sont généralement pas requis pour la plupart des gamemodes ou ressources. (Pour que les intérieurs et Map Editor fonctionne cette donnée ne doit pas être sur *false*). Quand ceci est configuré dans meta.xml, la modification s'applique à toutes les maps chargées par cette ressource.

- - **false:** Désactive le transfert des données d'élements de mapping pour toutes les ressources. Cela peut réduire considérablement le temps de téléchargement des maps.

- **true:** Active le transfert des données d’éléments de mapping. (Si **false** et **true** sont configurés dans des ressources différentes, *true* aura la priorité et les données seront transférés.)

- **<oop/>** OOP - Veuillez vous référer à [client scripting classes](mta://scripting/concepts/client-scripting-classes.md) pour la documentation.

- **false:** Désactive OOP.

- **true:** Active OOP.

## Exemple

Un exemple de fichier *meta* utilisant quelques unes de ces balises :

```
<meta>
    <info author="Slothman" type="gamemode" name="Stealth" />
    <config src="help.xml" type="client"/>

    <script src="stealthmain_server.lua" />
    <script src="noiseblip.lua" />
    <script src="mission_timer.lua" />
    <script src="gadgets_server.lua" />
    <script src="gadgets_client.lua" type="client"/>
    <script src="stealthmain_client.lua" type="client"/>
    <script src="noisebar.lua" type="client"/>
    <script src="spycam.lua" type="client"/>

    <file src="riot_shield.txd" />
    <file src="riot_shield.dff" />
    <file src="riot_shield.col" />
    <file src="armor.png" />
    <file src="camera.png" />
    <file src="cloak.png" />
    <file src="goggles.png" />
    <file src="mine.png" />
    <file src="radar.png" />
    <file src="shield.png" />

    <include resource="scoreboard" />
    <include resource="killmessages" />
    <include resource="maplimits" />

    <settings>
         <setting name="roundlimit" value="[6]" /> 
	 <setting name="teamdamage" value="[1]" /> 
	 <setting name="teambalance" value="[1]" /> 
	 <setting name="spazammo" value="[25]" /> 
	 <setting name="m4ammo" value="[100]" />
	 <setting name="shotgunammo" value="[25]" />
	 <setting name="sniperammo" value="[20]" />
	 <setting name="ak47ammo" value="[120]" />
	 <setting name="rifleammo" value="[40]" />
	 <setting name="deserteagleammo" value="[45]" />
	 <setting name="pistolammo" value="[132]" />
	 <setting name="uziammo" value="[150]" />
	 <setting name="tec9ammo" value="[150]" />
	 <setting name="silencedammo" value="[65]" />
	 <setting name="grenadeammo" value="[4]" />
	 <setting name="satchelammo" value="[4]" />
	 <setting name="teargasammo" value="[4]" />
	 <setting name="molatovammo" value="[4]" />
     </settings>

     <aclrequest>
	 <right name="function.startResource" access="true" />
	 <right name="function.stopResource" access="true" />
	 <right name="function.setPlayerMuted" access="true" />
     </aclrequest>
```

</syntaxhighlight>
