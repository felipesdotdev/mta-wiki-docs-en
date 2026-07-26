---
doc_id: "mta-wiki:7349"
title: "Zombiesystem script"
source_title: "Zombiesystem script"
source_url: "https://wiki.multitheftauto.com/wiki/Zombiesystem_script"
revision_id: 37747
language: "en"
categories: []
---

# Zombiesystem script

```
== Zombiesystem script ==
you can use this script for different things
it contains:
zombies with use of their own ai
housesystem
inventory/loot system
a carsystem to create cars that wil respawn 
at their original position when exploded
a spawnsystem
a accountsystem
```

you can use all in one or just parts of the script
this is an explanation of the configs in meta.xml
to help you so

## I.zombielimit

```
<setting name="*zombielimit" value="100"/>
```

serves to put the limit of the scripts zombies
the limit counts per player,
for ex:adding 100 zombies to limit == 1000 zombies for 10 players
if you are low on players it can work fine,but more players will lag your server
setting it to 0 will make no zombie spawn

## II.start items:

```
<setting name="*startweapon" value="22"/>
    <setting name="*startammo" value="60"/>
    <setting name="*startweapon2" value="26"/>
    <setting name="*startammo2" value="60"/>
    <setting name="*startpills" value="10"/>
    <setting name="*startbandage" value="10"/>
```

these settings are for the start/respawn weapons/items to be given to a player

## III. spawnsystem

```
<setting name="*allowspawn" value="true"/>
```

this setting is to use the scripts spawnsystem
putting the value to false will dectivate the spawnsys

## IV.modsystem

```
<setting name="*allowmods" value="true"/>
```

allow the scripts mods to be replaced
setting it to false wil disable the replacing

## V.commands

```
<setting name="*carcreator" value="showcarcreator"/>
    <setting name="*colcreator" value="showcolcreator"/>
    <setting name="*spawncreator" value="showspawncreator"/>
    <setting name="*housecreator" value="showhousecreator"/>
    <setting name="*killcommand" value="iwannadie"/>
    <setting name="*killcount" value="mykills"/>
    <setting name="*skillcount" value="mystats"/>
```

```
these are for vital commands of the script
some need to be changed for security
or anybody could create stuff on your server
```

## VI.Houseblips

```
<setting name="*houseblips" value="true"/>
```

adding blips to the scripts houses or not

## VII.Pingkicker

```
<setting name="*maxping" value="1000"/>
maximum ping limit for pingkicker
as players with high ping lag the other players
```

## VII. smal extra

```
<setting name="*slothbot" value="false"/>
can the zombies from script use slothbot ai or not
(you need to have slothbot running)
```

## VIII.Decay

```
<setting name="*decay" value="20000"/>
the timer for decay of body's and pickups
body's decay is 3X a round so actualy the body will disapear
in 60000 ms
pickups 6X
```

## IX.Savesystem

using the savesystem :

```
<setting name="*savesystem" value="true"/>
if you choose to use the savesystem only
the load and save of the items to be saved will
happens with the events  onPlayerLogin and onPlayerLogOut
setting to fals wil disable the savesystemfalse
```

using the autologin :

```
<setting name="*autologin" value="true"/>
```

```
the autologin sytem will create an account 
for the player based on the serial fom his pc
the player logs in when all files are downloaded
```

setting this to false will deactivate the autologin

password for autologinaccounts

```
<setting name="password" value="password"/>
```

```
!!!!!CHANGE THE VALUE!!!!!
```

no worry to change it more then 1 time
the script tags the accounts created by it
and updates the password (for those accounts only) on each restart of the script

i hope this is usefull
