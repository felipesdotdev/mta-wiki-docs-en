---
doc_id: "mta-wiki:5973"
title: "Server Commands"
source_title: "Server Commands"
source_url: "https://wiki.multitheftauto.com/wiki/Server_Commands"
revision_id: 78945
language: "en"
categories: ["Changes_in_1.5.5", "Changes_in_1.5.6", "Support"]
---

# Server Commands

This page lists all built in commands that the server can process. All these commands can be entered via the server console or the client console depending upon permissions unless otherwise stated.

## Resource commands

#### check

Server console only

Usage: check [ *all* | *<resource-name>* ]  

Checks which files would be changed with [upgrade](mta://reference/misc/server-commands.md) command. Does not modify anything.

#### info

Server console only

Usage: info *<resource-name>*  

Get info for a resource eg: info admin

#### list

Server console only

Shows a list of resources

#### refresh

Refresh resource list to find new resources

#### refreshall

Refresh resources and restart any changed resources

#### restart

Usage: restart *<resource-name>*  

Restarts a running resource eg: restart admin

#### start

Usage: start *<resource-name>*  

Start a loaded resource eg: start admin

#### stop

Usage: stop *<resource-name>*  

Stop a resource eg: stop admin

#### stopall

Stop all running resources

#### upgrade

Server console only

Usage: upgrade [ *all* | *<resource-name>* ]  

Perform a basic upgrade of all resources. The [check](mta://reference/misc/server-commands.md) command shows the list of changes this command will make.

#### aclrequest

Usage: aclrequest [ *list* | *allow* | *deny* ] *<resource-name>* [ *<right>* | *all* ]  

Manage ACL requests from resources implementing <aclrequest> in their [meta.xml](mta://reference/misc/meta-xml.md)

#### reloadacl

Perform a simple ACL reload.

## Account commands

#### aexec

Usage: aexec *<nick>* *<command>*  

Force a player to execute a command eg: aexec playername say hello

#### addaccount

Usage: addaccount *<accountname>* *<password>*  

Add an account eg: addaccount accountname password

#### chgpass

Usage: chgpass *<accountname>* *<password>*  

Change an accounts password eg: chgpass account newpw

#### delaccount

Usage: delaccount *<accountname>*  

Delete an account eg: delaccount accountname

#### reloadbans

Reloads all the bans from *banlist.xml*.

#### authserial

Usage: authserial <account-name> [list|removelast|httppass]

Manage serial authentication for an account.

## Server commands

#### ase

Server console only

See the amount of master server list queries

#### debugdb

Usage: debugdb *<*0-2*>*  

Server console only

Set logging level for database functions. [0-Off  1-Errors only  2-All]

By default, logging output is written to the file **logs/db.log** unless another file is declared in the [<dbfile> section of mtaserver.conf](https://wiki.multitheftauto.com/index.php?search=%3Cdbfile%3E%20section%20of%20mtaserver.conf)

#### debugjoinflood

Server console only

Shows debug information regarding the join flood mitigation feature.

#### debuguptime

Server console only

Shows how many days the server has been up and running.

#### help

Server console only

Displays these list of commands

#### loadmodule

Usage: loadmodule *<module-filename>*  

Load a module eg: loadmodule ml_sockets.dll

#### unloadmodule

Server console only

Usage: unloadmodule *<module-filename>*  

Unload a module eg: unloadmodule ml_sockets.dll

#### reloadmodule

Server console only

Usage: reloadmodule *<module-filename>*  

Reload a module eg: reloadmodule ml_sockets.dll

#### openports

Server console only

Test if server ports are open

#### sfakelag

Usage: sfakelag *<packet loss>* *<extra ping>* *<ping variance>* [*<KBPS limit>*]

**Only available if enabled in the [mtaserver.conf](https://wiki.multitheftauto.com/index.php?search=mtaserver.conf) file.**

Adds artificial packet loss, ping, jitter and bandwidth limits to the server-client connections.

#### shutdown

Usage: shutdown *<reason>*  

Shutdown the server eg: shutdown put reason here

#### sver

Get the server MTA version

## Other commands

#### say

Usage: say *<text>*  

Show a message to all players on the server eg: say hello

#### whois

Usage: whois *<nick>*  

Get the IP of a player currently connected (use **whowas** for IP/serial/version)

#### ver

Get the MTA version

## Client relevant only

#### chgmypass

Client only

Usage: chgmypass *<oldpass>* *<newpass>*  

Change your password eg: chgmypass oldpw newpw

#### debugscript

Client  only

Usage: debugscript *<*0-3*>*  

Remove (This does not work "Incorrect client type for this command")

#### login

Client  only

Usage: login *<accountname>* *<password>*  

Login to an account eg: login accountname password

#### logout

Client  only

Log out of the current account

#### me

Client  only

Usage: me *<text>*  

Show a message to all players on the server, with your nick prepended

#### msg

Client  only

Usage: msg *<nick>* *<text>*  

Send a message to a player eg: msg playername hello

#### nick

Client  only

Usage: nick *<old-nick>* *<new-nick>*  

Change your ingame nickname

#### teamsay

Client  only

Usage: teamsay *<text>*  

Send a message to all players on the same team
