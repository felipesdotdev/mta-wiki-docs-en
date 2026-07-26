---
doc_id: "mta-wiki:5531"
title: "Resource : Irc"
source_title: "Resource:Irc"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AIrc"
revision_id: 73849
language: "en"
categories: ["Resource"]
---

# Resource : Irc

The "irc" resource provides an echobot that outputs information such as chatmessages on a irc channel.
Information about "irc" or "Internet Relay Chat" can be found on [Wikipedia.](http://en.wikipedia.org/wiki/Irc)

## Installation

To get this resource working on your Linux or Windows server, follow these steps:

- **Install the sockets module**

- **Download the module**: You can download the module [here](https://wiki.multitheftauto.com/wiki/Modules/Sockets). Download the ml_sockets.dll file for Windows and the ml_sockets.so file for Linux

- **Put the module in the MTA folder**: In order for MTA to load the module it must be placed in the mods/deathmatch/modules folder, if this folder does not exist yet, make it.

- **Add the module to the mtaserver.conf file**: To load the module when the MTA server starts, put this line <module src="ml_sockets.dll"/> in your config file for Windows and <module src="ml_sockets.so"/> in the config file for Linux.

- **Install the IRC resource**

- **Download the resource**: The IRC resource can be found on the [community](http://community.mtasa.com/index.php?p=resources&s=details&id=731), put it in the resources folder.

- **Mod the settings.xml file**: Open this file and follow the instructions inside to configure the IRC bot.

- **Mod the meta.xml file**: In this file a few settings can be found regarding ads and ingame gui's, **do not mod anything else!** You can also change these settings in the admin panel once the resource has been loaded.

- **Acl rights** The resource needs a couple of acl rights in order to work properly, including addBan, kickPlayer & callRemote. Any missing rights will prevent the resource from loading and will output a message in the console.

Now you can run the resource, if the server was running during this installation proces you will have to do /loadmodule ml_sockets.dll or /loadmodule ml_sockets.so and /refreshall before doing /start irc

## The acl.xml file

The acl.xml file inside the irc resource takes care of the acl rights for irc commands.

Syntax

```
<command name="!kick" level="2" echoChannelOnly="true" />
```

- The name is the command including the exclamation mark

- The level is the minimum level the irc user needs to have in order to use this command

- The echoChannelOnly is wether the command can be used outside the echo channel

## Elements

All users, channels & servers known by the irc resource are represented by elements.

- Servers are the following elements type: 'irc-server'

- Channels are the following elements type: 'irc-channel'

- Users are the following elements type: 'irc-user'

## Level system

The irc resource doesn't use the irc modes system for its acl, instead the modes were replaced with numbers.

- Owner (~) is now level 5

- Super Operator (&) is now level 4

- Operator (@) is now level 3

- Helper (%) is now level 2

- Voice (+) is now level 1

All other users without a special mode are level 0

## Events

During the irc proces some events are triggered to help you write extensions for the irc resource.
You may want to use addEvent("eventName") to use them.

| Name | Source | Parameters |
| --- | --- | --- |

| onIRCConnecting | server theIRCServer |  |
| --- | --- | --- |

| onIRCConnect | server theIRCServer |  |
| --- | --- | --- |

| onIRCFailConnect | server theIRCServer | string reason |
| --- | --- | --- |

| onIRCUserJoin | user theIRCUser | channel theIRCChannel, string vhost |
| --- | --- | --- |

| onIRCUserNickChange | user theIRCUser | string oldNick, string newNick |
| --- | --- | --- |

| onIRCUserPart | user theIRCUser | channel theIRCChannel, string theReason |
| --- | --- | --- |

**NOTE:** 'theReason' can be nil if 'theUser' has quit without a reason.

| onIRCUserKick | user theIRCUser | channel theIRCChannel, string theReason, user theKicker |
| --- | --- | --- |

**NOTE:** 'theKicker' can be false if 'theUser' was kicked by a service like the NickServ.

| onIRCPrivateMessage | user theIRCUser | string theMessage |
| --- | --- | --- |

| onIRCMessage | user theIRCUser | channel theIRCChannel, string theMessage |
| --- | --- | --- |

| onIRCPrivateNotice | user theIRCUser | string theMessage |
| --- | --- | --- |

| onIRCNotice | user theIRCUser | channel theIRCChannel, string theMessage |
| --- | --- | --- |

| onIRCUserMode | user theIRCUser | channel theIRCChannel, boolean positive, string theMode, user theSetter |
| --- | --- | --- |

**NOTE:** 'theSetter' can be false if 'theUser' was opped by a service like the NickServ.

| onIRCChannelMode | channel theIRCChannel | boolean positive, string theMode, user theSetter |
| --- | --- | --- |

**NOTE:** 'theSetter' can be false if the mode was set by a service like the NickServ.

| onIRCLevelChange | user theIRCUser | channel theIRCChannel, number oldlevel, number newlevel |
| --- | --- | --- |

| onIRCUserQuit | user theIRCUser | string theReason |
| --- | --- | --- |

## Exported functions

These functions can be called from another resource to help you write extensions for the irc resource.
Use the exports table or [call](mta://scripting/shared/functions/call.md) to use them

Example 1:

```
[Lua]
	exports.irc:ircConnect("irc.gtanet.com","bot",6667)
```

Example 2:

```
[Lua]
	call(getResourceFromName("irc"),"ircConnect","irc.gtanet.com","bot",6667)
```

| returns | function name | Parameters |
| --- | --- | --- |

| boolean | ircHop | server theIRCServer, (string theReason) |
| --- | --- | --- |

| boolean | ircSay | channel theIRCChannel/user theIRCUser, string theMessage |
| --- | --- | --- |

| boolean | ircRaw | server theIRCServer, string theRaw |
| --- | --- | --- |

| boolean | ircPart | channel theIRCChannel, (string theReason) |
| --- | --- | --- |

| irc-channel | ircJoin | server theIRCServer, string theChannelName, (string theChannelPassword) |
| --- | --- | --- |

| boolean | ircAction | channel theIRCChannel/user theIRCUser, string theMessage |
| --- | --- | --- |

| boolean | ircNotice | channel theIRCChannel/user theUserChannel, string theMessage |
| --- | --- | --- |

| boolean | outputIRC | string theMessage |
| --- | --- | --- |

| boolean | ircConnect | string serverHost/IP, string nickname, (number serverPort), (string serverPassword), (boolean secure) |
| --- | --- | --- |

 

**NOTE:** Secure connections are not available yet due to the module not suporting SSL yet.

| boolean | ircIdentify | server theIRCServer, string thePassword |
| --- | --- | --- |

| boolean | ircReconnect | server theIRCServer |
| --- | --- | --- |

| boolean | ircDisconnect | server theIRCServer, string theReason |
| --- | --- | --- |

| boolean | ircChangeNick | server theIRCServer, string newNick |
| --- | --- | --- |

| table | ircGetServers |  |
| --- | --- | --- |

| string | ircGetServerName | server theIRCServer |
| --- | --- | --- |

| string | ircGetServerHost | server theIRCServer |
| --- | --- | --- |

| number | ircGetServerPort | server theIRCServer |
| --- | --- | --- |

| string | ircGetServerPass | server theIRCServer |
| --- | --- | --- |

| string | ircGetServerNick | server theIRCServer |
| --- | --- | --- |

| boolean | ircIsServerSecure | server theIRCServer |
| --- | --- | --- |

| table | ircGetServerChannels | server theIRCServer |
| --- | --- | --- |

| userdata | ircGetChannelServer | channel theIRCChannel |
| --- | --- | --- |

| table | ircGetChannels | (server theIRCServer) |
| --- | --- | --- |

| boolean | ircSetChannelMode | channel theIRCChannel, string theMode |
| --- | --- | --- |

| string | ircGetChannelName | channel theIRCChannel |
| --- | --- | --- |

| string | ircGetChannelMode | channel theIRCChannel |
| --- | --- | --- |

| table | ircGetChannelUsers | channel theIRCChannel |
| --- | --- | --- |

| string | ircGetChannelTopic | channel theIRCChannel |
| --- | --- | --- |

| userdata | ircGetChannelFromName | string theChannelName |
| --- | --- | --- |

| bool | ircIsEchoChannel | channel theIRCChannel |
| --- | --- | --- |

| boolean | ircSetUserMode | user theIRCUser, string theMode |
| --- | --- | --- |

| string | ircGetUserMode | user theIRCUser |
| --- | --- | --- |

| string | ircGetUserNick | user theIRCUser |
| --- | --- | --- |

| number | ircGetUserLevel | user theIRCUser |
| --- | --- | --- |

| table | ircGetUsers | (server theIRCServer) |
| --- | --- | --- |

| userdata | ircGetUserServer | user theIRCUser |
| --- | --- | --- |

| number | ircGetUserLevel | user theIRCUser, channel theIRCChannel |
| --- | --- | --- |

| string | ircGetUserVhost | user theIRCUser |
| --- | --- | --- |

| userdata | ircGetUserFromNick | string theNickname |
| --- | --- | --- |

| bool | addIRCCommandHandler | string theCommandName, function theFunctionToCall/string functionName, (number minimumLevel), (boolean echoChannelOnly) |
| --- | --- | --- |

 

**NOTE:** Use a string with the function name for the second argument if your are calling this function from another resource, also make sure the function is exported.

| table | ircGetCommands |  |
| --- | --- | --- |

| number | ircGetCommandLevel | string theCommand |
| --- | --- | --- |

| boolean | ircIsCommandEchoChannelOnly | string theCommand |
| --- | --- | --- |

**NOTE:** All parameters that are between brackets are optional, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments)

## Commands

| command | level |
| --- | --- |

| !kick | 2 |
| --- | --- |

| !uptime | 0 |
| --- | --- |

| !say | 0 |
| --- | --- |

| !s | 0 |
| --- | --- |

| !m | 0 |
| --- | --- |

| !players | 0 |
| --- | --- |

| !pm | 0 |
| --- | --- |

| !ts | 0 |
| --- | --- |

| !getip | 2 |
| --- | --- |

| !getserial | 2 |
| --- | --- |

| !mute | 2 |
| --- | --- |

| !unmute | 2 |
| --- | --- |

| !mutes | 2 |
| --- | --- |

| !freeze | 2 |
| --- | --- |

| !unfreeze | 2 |
| --- | --- |

| !kill | 2 |
| --- | --- |

| !slap | 2 |
| --- | --- |

| !ban | 3 |
| --- | --- |

| !banip | 3 |
| --- | --- |

| !banserial | 3 |
| --- | --- |

| !banname | 3 |
| --- | --- |

| !unbanip | 3 |
| --- | --- |

| !unbanserial | 3 |
| --- | --- |

| !unban | 3 |
| --- | --- |

| !bans | 3 |
| --- | --- |

| !commands | 0 |
| --- | --- |

| !cmds | 0 |
| --- | --- |

| !lua | 4 |
| --- | --- |

| !run | 4 |
| --- | --- |

| !crun | 4 |
| --- | --- |

| !resources | 3 |
| --- | --- |

| !start | 3 |
| --- | --- |

| !restart | 3 |
| --- | --- |

| !stop | 3 |
| --- | --- |

| !account | 3 |
| --- | --- |

| !community | 3 |
| --- | --- |

| !money | 0 |
| --- | --- |

| !health | 0 |
| --- | --- |

| !wantedlevel | 0 |
| --- | --- |

| !team | 0 |
| --- | --- |

| !ping | 0 |
| --- | --- |

| !modules | 3 |
| --- | --- |

| !changemap | 3 |
| --- | --- |

| !map | 0 |
| --- | --- |

| !shutdown | 5 |
| --- | --- |

| !password | 4 |
| --- | --- |

| !gravity | 3 |
| --- | --- |

| !weather | 3 |
| --- | --- |

| !server | 0 |
| --- | --- |

| !zone | 0 |
| --- | --- |

| !refreshall | 4 |
| --- | --- |

| !refresh | 4 |
| --- | --- |

| !checkmap | 2 |
| --- | --- |

| !country | 2 |
| --- | --- |

## Modding

Please don't mod the resource, you might break it and cause it to malfunction or to spam errors.
If this happens you will not get any support.
Write extensions instead.

## Contact

The author (MCvarial) can be contacted using IRC (#mta,#mta.dutch)
Or by email (MCvarial@gmail.com)
