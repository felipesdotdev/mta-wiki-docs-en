---
doc_id: "mta-wiki:7619"
title: "Créer un mode de jeu"
source_title: "Créer un mode de jeu"
source_url: "https://wiki.multitheftauto.com/wiki/Cr%C3%A9er_un_mode_de_jeu"
revision_id: 43417
language: "en"
categories: []
generated_at: "2026-07-26T16:11:05.129935+00:00"
---

# Créer un mode de jeu

Un **mode de jeu**, appelé aussi ***gamemode***, est une ressource de *Multi Theft Auto* qui une fois lancée contrôle tous les éléments du *gameplay* du jeu. Cela inclut notamment l'explication de ce même mode de jeu aux joueurs qui l'essaieront. Le mode de jeu peut ainsi expliquer par exemple comment gagner des points ou de l'argent. Il existe plusieurs modes de jeu, tous différents : la course, les matchs à mort (*Deathmatchs*), la capture de drapeau (*Capture the Flag*), le jeu libre (*Freeroam*) et beaucoup d'autres.

## Que signifie « coder proprement un mode de jeu » ?

Pour faire simple, un mode de jeu doit utiliser les fonctionnalités du système de *maps* dans *Multi Theft Auto*. Autrement dit, il faut que le script des *maps* soit accompagné des positions précises des véhicules ou bien des joueurs lorsque ceux-ci apparaissent. Cela permet au mode de jeu d'être indépendant des *maps* proposées par les autres joueurs.

Toutefois, le mode de jeu doit donc pouvoir charger les fichiers .map qui définissent ces données. De cette façon, le mode de jeu peut avoir de nombreuses *maps* ; ainsi, les joueurs peuvent créer des fichiers .map pour leurs modes de jeu avec l'éditeur de *maps* de *MTA*, ce qui en rend la conception moins fastidieuse qu'avec des lignes de code.

An obvious example of a "proper gamemode" is MTA:Race. It allows usermade maps with lots of possibilities within the .map file. To alter spawnpoints, objects etc., the user doesn't need to edit the gamemode itself.

### Les fichier .map

Les fichiers .map sont des fichiers XML enregistrés avec l'extension .map. Ils définissent l'environnement pour un mode de jeu ou plusieurs si la map est compatible avec d'aures. Ils ne sont cependant pas supposés changer les règles du jeu. Les règles sont définies dans le mode de jeu.

Chaque élémment dans une map correspond à un noeud dans le fichier .map. Il y a une syntaxe particulière pour les points de spawn, objets ou véhicules. Cependant il est possible, pour des cas d'ajouts d'objets spéciaux d'inventer votre propre syntaxe.

#### Exemple

Commencons par un mode de jeu bien connu, la capture de drapeau. Une map pour ce mode de jeu à besoin de point de spawn et de positions pour les drapeaux des deux équipes. On peut aussi y ajouter des véhicules et d'autres objets. Un fichier de map simplifié pourrait ressembler à ça :

```
<map>
    <spawnpoint id="spawnpoint1" posX="1959.5487060547" posY="-1714.4613037109" posZ="877.25219726563" rot="63.350006103516" model="0"/>
    <pickup id="Armor 1" posX="1911.083984375" posY="-1658.8798828125" posZ="885.40216064453" type="armor" health="50" respawn="60000"/>
    <flag posX="1959.5487060547" posY="-1714.4613037109" posZ="877.25219726563" team="blue" />
    ...
</map>
```

Dans le code ci-dessus on peut apercevoir trois éléments : un point de spawn,un pickup et un flag.
Le pickup permettera une fois pris par le joueur de lui rendre 50 points de vie, celui-ci respawn toute les 60 secondes.
Le flag est ici définit au niveau de sa position et de sa couleur (propre à l'équipe).
Le point de spawn et le pickup peuvent être utilisé par une ressource externe. Les éléments personnalisés doievent être gérés par le mode de jeu.

Pour résumé, votre objectif est de facilité la vie des mappeurs. Ceux-ci ne doivent pas avoir à se tracasser du script concernant le mode de jeu.

#### Exemple de récupération d'informations sur un .map

Votre mode de jeu doit appelés les éléments personnalisés définit dans le fichier .map afin des les utilisés. Ce n'est pas bien compliqué et voici une démonstration ci-dessous.

```
-- récupère une liste avec tout les éléments de type flag
local flagElements = getElementsByType ( "flag" )
-- On boucle sur cette liste pour récupérer les positions
for key, value in pairs(flagElements) do
	-- Récupération des informations
	local posX = getElementData ( value, "posX" )
	local posY = getElementData ( value, "posY" )
	local posZ = getElementData ( value, "posZ" )
	local team = getElementData ( value, "team" )
	-- Création de l'objet flag
	createObject ( 1337, posX, posY, posZ )
	-- Affichage dans le tchat que le dreapau est créé
	outputChatBox ( "Base for team " .. team .. " created" )
end
```

La fonction [getElementsByType](mta://scripting/shared/functions/getelementsbytype.md) récupère une table de tout les éléments d'un certain type. (le type correspond au noeud créé dans le fichier .map)
Fonctionne pour les objets presonnalisé mais aussi pour les objets présents par défauts dans MTA comme "vehicle" ou "player".
[getElementData](mta://scripting/shared/functions/getelementdata.md) peut être utilisé pour récupérer les atributs XML définis dans le fichier .map.
Pour exemple, un objet est créé à la position du drapeau et un message s'affiche dans le tchat pour prévenir les joueurs. En réalité, cette action sera plutôt réalisée lors du chargement de la map. Par contre on peut imaginer une action lorsqu'un joueur s'empare du drapeau ennemi.

## Map Manager

Après avoir lu les sections ci-dessus il doit vous paraître clair qu'un mode de jeu est composé en deux parties :

- La ressource du mode de jeu (Unique)

- Les maps qui accompagnent le mode de jeu

A la place d'écrire un [Map manager](mta://mapping/map-manager.md) pour chaque mode de jeu différent, le [Map manager](mta://mapping/map-manager.md) de base fournit des fonctions pour charger mode de jeu et maps. Il suffit simplement d'entrer un commande correcte (par exemple 'gamemode ctf ctf-italy'), cette action va démarrer le mode de jeu et la map pendant que l'évênement déclenché ([onGamemodeMapStart](https://wiki.multitheftauto.com/index.php?title=OnGamemodeMapStart&action=edit&redlink=1)) avertira le mode de jeu q'une map est chargée. La ressource 'ctf' peut alors accéder au informations de la map. Le mode de jeu peut alors faire spawn les joueurs.

### Comment utiliser le Map Manager

Pour utiliser le Map Manager, votre mode de jeu doit être ciblé en premier lieu. Vous devez en fait configurer l'attribut "type" dans la baile <info> du meta.xml avec le mode de jeu souhaité. L'attribut "name" peut contenir un non plus convivial comme 'Capture de drapeau', c'estl enom qui sera affiché dans la liste des serveurs à la place du om de la ressource par défaut.

```
<!-- meta.xml in "shootermode" gamemode -->
<meta>
    <info type="gamemode" name="Shooter Mode 2.0"/>
</meta>
```

Si votre mode de jeu utilise des maps personnalisées, vous devriez utiliser les évênements suivant :

- onGamemodeMapStart

- onGamemodeMapStop (Si la map doit-être déchargée)

Les évênements ci-dessus sont appelés quand une map de votre mode démarre ou s'arrête. Le paramètre passé par ces évênement n'est rien d'autre que le nom de la ressource.
Avec les fonctions sur les évênements, vous pouvez extraire toute les informations de la map ainsi que du fichier de configuration.

#### Example

```
function startCtfMap( startedMap ) -- startedMap contient une référence vers la ressource de la map
    local mapRoot = getResourceRootElement( startedMap )        -- recoit le noeud principal de la map démarrée
    local flagElements = getElementsByType ( "flag" , mapRoot ) -- recoit tout les drapeausx de la map et les stocke dans un tableau
    -- Démarrage du chargement des informations
    -- Spawn les joueurs etc
end
addEventHandler("onGamemodeMapStart", getRootElement(), startCtfMap)
```

### Faire des maps compatibles

Les maps sont des ressources séparées du mode de jeu de telle sorte qu'il ne faut pas modofier le mode de jeu pour chaque nouvelle map. Les maps peuent aussi contenir des scripts et configurations propres à elles.

Pour faire une map compatible avec votre mode, il suffit d'ouvrir le meta.xml et de mettre l'attribut "type" à 'map' et l'attribut "gamemode" doit être composé d'une liste des mode de jeu compatible avec la map (modes séparé d'une virgule).

```
<!--map's meta.xml-->
<meta>
    <info type="map" gamemodes="shootermode,assault,tdm"/>
</meta>
```

Une fois que tout est configuré, les administrateurs peuvent utiliser le panel ou les commandes start/stop suivit du nom du mode.
/gamemode gamemodeName [NomDeLaMap] (paramètre optionel qui permet de démarré une map avec le mode, par défaut pas de map)
/changemap mapName [NomDuModeDeJeu] (paramètre optionnel qui permet dans le cas ou la map est démarrée de lancé le mode de jeu qui lui convient, par défaut le mode de jeu actif)

[Map manager](mta://mapping/map-manager.md) possède d'autres fonctions qui pourrait vous être utliles, mais elle ne sont pas toutes présentées ici.

## Autres possibilités

Il y a une multitude d'autres ressources avec lesquelles les modes de jeu peuvent interférer.

### Helpmanager

L'Helpmanager est une interface en jeu pour les joueurs qui on besopin d'aide. Si vous utilisez l'HelpManager pour l'aide de votre mode de jeu, tous les joueurs qui l'on utilisé précédement serront plus à l'aise car la plupart des modes l'utilise. Il affiche aussi les différentes ressources dans des onglet, si configuré pour.

Il y à deux façons d'utiliser le HelpManager :

- Fournir un simple texte qui explique le mode de jeu.

- Utilisation des éléments graphiques (GUI) (Recommandé)

N'hésitez pas à lire la page sur le HelpManager pour en savoir plus.

### Scoreboard

Il affiche les joueurs et les teams présentes sur le serveur. Vous pouvez y ajouter des colonnes supplémentaires pour afficher d'autres informations. Par exemple une colonne 'Points' peut être utile dans un mode de capture de drapeaux. Consultez la page sur le scoreboard pour plus d'information.

### Map cycler

Il permet de controller quel mode de jeu et map sont joués  sur le serveur. Vous pouvez spécifier combien de fois une map doit être jouée avant changement de mode de jeu apr exemple. Pour celà il faut dire au map cycler que votre mode de jeu est stoppé.

## Voir aussi

- La [page d'accueil](mta://reference/misc/page-d-accueil.md) du wiki, qui propose d'autres tutoriels concernant la programmation.
