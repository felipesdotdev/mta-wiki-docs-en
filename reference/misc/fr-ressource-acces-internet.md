---
doc_id: "mta-wiki:12820"
title: "FR/Ressource Acces Internet"
source_title: "Fr/Ressource Acces Internet"
source_url: "https://wiki.multitheftauto.com/wiki/Fr/Ressource_Acces_Internet"
revision_id: 69367
language: "en"
categories: ["Translated/Scripting_Concepts"]
generated_at: "2026-07-26T16:07:49.831029+00:00"
---

# FR/Ressource Acces Internet

Le serveur Multi Theft Auto dispose d'une interface web que les ressources peuvent utiliser pour un tas de choses. Ce document va vous expliquer quelques les différentes manières et comment se servir de cette interface.

## Introduction

Il y a deux choses primordiales à avoir. La première : un serveur web qui autorise les navigateurs internent à demander des pages et les fichiers que vous avez dans votre ressource. La seconde est un système qui autorise le navigateur à appeler des fonctions exportées depuis votre ressource.

## Pages

### Spécification de fichiers dans le meta.xml

Vous pouvez spécifier dans votre fichier meta.xml certaines ressources qui pourront être accessible depuis le serveur wev. Pour se faire, ajoutez les lignes suivantes :

```
<html src="filename.ext" />
```

En vous rendant sur : [http://host:port/resourcename/filename.ext](http://host:port/resourcename/filename.ext)  
 
vous pouvez y accèder.
Par exemple, sur un serveur local utilisant le port http par défaut, l'adresse sera : [http://127.0.0.1:22005/webmap/map.htm](http://127.0.0.1:22005/webmap/map.htm)

### Les fichiers binaires

Malgré ce nom, les fichiers utilisent le HTML (de n'importe quel type). S'il y a des fichiers binaires (comme les images, archive zip...) vous devez le spécifier dans le meta.xml en ajoutant *raw="true"* dans la noeud *html*. Cela signifie que les fichiers ne sont pas modifiés avant d'êtres envoyés au navugateur.

Par exemple :

```
<html src="image.gif" raw="true" />
```

### Fichiers parsés

Si un fichier n'est pas spécifié en tant que "rax" dans le meta.xml, il est passé par un pré-processeur avant d'être retourné au client. Ce pré-processeur marche mieux avec PHP ou ASP mais est utilisable en LUA. Vous pouvez intégrer des pages HTML dans des scripts MTA tout en controllant la sortie. Presque toutes les fonctions standards de MTA fonctionnent, ainsi que les [Fonctions HTTP](https://wiki.multitheftauto.com/wiki/Template:HTTP_functions), comme [httpWrite](mta://reference/misc/httpwrite.md).

Par exemple :

```
<html>
    <body>
        Cette ressource est appelée <* httpWrite( getResourceName(getThisResource()) ) *>
    </body>
<html>
```

Note : é est un caractère spécial ("é").

Le ternaire fonctionne aussi (comme en PHP ou en ASP) pour ce code. Vous pouvez donc faire :

```
<html>
    <body>
        Cette ressource est appelée <* = getResourceName(getThisResource()) *>
    </body>
<html>
```

Toutes les fonctions HTTP intégrées au LUA ont accès aux variables d'environnement suivantes, qui contiennent les informations de la façon dont la page est demandée :

- table **requestHeaders**: Tableau contenant tous les "headers HTTP" demandés avec la page. Vous pouvez modifier les "headers HTTP" retournés avec [httpSetResponseHeader](mta://reference/misc/httpsetresponseheader.md).

- table **form**: Tableau contenant toutes les données envoyées par un formulaire (méthode POST) ainsi que les variable passées dans la requête (méthode GET).

- table **cookies**: Tableau contenant tous les cookies, modifiable via la fonction [httpSetResponseCookie](mta://reference/misc/httpsetresponsecookie.md).

- string **hostname**: Chaîne de caractères contenant l'adresse IP ou le nom d'hôte (hostname) de la page.

- string **url**: Chaîne de caractères contenant l'url de la page.

- account **user**: C'est le compte de l'utilisateur.

Il est important de noter que les fichiers parsés tournent dans une machine virtuelle différente à celle de la ressource. Par conséquent, si vous voulez appeler une fonction dans votre ressource, vous devez exporter la fonction et utilisé la fonction [call](mta://scripting/shared/functions/call.md) depuis le fichier parsé.

## Calls

Vous pouvez autoriser certaines fonctions exportées dans votre ressource à être appeller depuis l'interface HTTP. Tous les SDKs (listes ci-dessous) vous autorise à appeler ces fonctions depuis un emplacement distant.

Pour spécifier une fonction exportée accessible depuis HTTP, ajoutez les lignes suivantes dans votre meta.xml :

```
<export function='nomDeFonction' http='true' />
```

Vous pouvez coder votre fonction comme si c'était une fonction "normal", elle peut retourner plusieurs valeurs (ainsi que des tableaux, ressources, "elements"). Vous ne pouvez jamais retourner d'autres 'userdata' comme [[xmlnode|xmlnodes] ou des fonctions.

### Protocole

{{note_box|Vous n'êtes pas obliger de savoir ça, vous pouvez utiliser l'un des [[#SDK SDK] ci-dessous.}}

Les appels sont fait avec cette requête HTTP POST : *http://<your IP>:<your port>/<resource_name>/call/<exported_function_name>*. Le corps de cette requête peut être un tableau JSON avec les arguments pour la fonction.

La requête va retourner un tableau JSON avec la(les) value(s) retourné depuis la fonction comme une réponse HTTP.

Le serveur supporte l'authentification HTTP basique, et vous pouvez configurer l'accès via l'ACL et le système de compte de base.

### Appels depuis une interface HTTP

Utiliser les appels est probablement la façon la plus simple et peut être fait de façon presque transparente.

D'abord, ajoutez ces lignes dans votre meta.xml :

```
<include resource="ajax" />
```

Après, ajouté les lignes suivantes entre les balises <head> de votre page :

```
<* = exports.ajax:start(getResourceName(getThisResource())) *>
```

Finalement, vous pouvez créer un bloc javascript dans votre page et appeler vos fonctions quasiment comme si elles étaient locales.
La seule différence est que l'appel des fonctions est asynchrone - vous devez spécifier une "callback" comme dernier arguement pour votre appel. Elle est appelé quand la fonction est retournée.

Voici un simple exemple d'utilisation :

**meta.xml**

```
<meta>
   <include resource="ajax" />
   <script src='code.lua' />
   <html src='page.htm' default='true' />
   <export function='showChatMessage' http='true' />
</meta>
```

**code.lua**

```
function showChatMessage ( message )
    outputChatBox ( message )
    return 5;
end
```

**page.htm**

```
<html>
    <head>
        <* = exports.ajax:start(getResourceName(getThisResource())) *>
        <script type='text/javascript'>
            function say() {
                var message = document.getElementById('message')
                showChatMessage ( message.value, 
                    function ( number ) {
                        // the function has been called and returned something
                        message.value = "The function returned " + number;
                    }
                );
            }
        </script>
    </head>
    <body>
        <input type='text' id='message' /><input type='button' value='say' onclick='say();' />
    </body>
</html>
```

Vous pouvez voir les exemples de comment cela peut être fait dans les ressources : *resourcebrowser*, *resourcemanager* et *webadmin*.

## Sécurisé l'interface web

L'[ACL](mta://tutorials/acl.md) a un nombre de droits qui peuvent qui peuvent dire quels fichiers peuvent accèder à quels fichiers.

- general.http: S'il est désactivé, aucuns des fichiers http peuvent être accèdés (sauf par le client)

- resource.**ResourceName**: S'il est désactivé, aucun des fichiers de la ressource ne peuvent être accèdés.

- resource.**ResourceName**.file.**FileName**: S'il est désactivé, le fichier nommé ne peut être accèdé.

- resource.**ResourceName**.function.**FunctionName**: S'il est désactivé, la fonction ne peut être appelée.

Ils peuvent également marcher avec les autres droits ACL - vous pouvez désactiver ceci pour les utilisateurs normaux et juste activés pour les Admins, ou un autre groupe ou utilisateur.

## SDK

Il y a un grand nombre de soi-disant 'SDKs' disponible qui vous permet d'accèder à votre interface depuis d'autres langages de programmation. Avec, vous pouvez (en théorie) écrire un gamemode. Dans la pratique, c'est probablement une mauvaise idée, mais c'est utile pour les statistiques et l'administration. Le PHP SDK est la version la plus développée. Vous pouvez faire votre propre SDK - si vous le faites, envoyez-nous une copie (^^).

- [Java SDK](mta://tutorials/java-sdk.md)

- [Javascript SDK](mta://tutorials/javascript-sdk.md)

- [Perl SDK](mta://tutorials/perl-sdk.md)

- [PHP SDK](mta://tutorials/php-sdk.md)

- [C# SDK](mta://reference/misc/csharp-sdk.md)

## Voir aussi

[callRemote](mta://scripting/server/functions/callremote.md) - Autoriser le serveur à appeler des foncions dans des pages PHP (avec le PHP SDK) et sur d'autres serveurs.
