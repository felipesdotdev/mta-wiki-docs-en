---
doc_id: "mta-wiki:3520"
title: "Server Manual"
source_title: "Server Manual"
source_url: "https://wiki.multitheftauto.com/wiki/Server_Manual"
revision_id: 82160
language: "en"
categories: ["Support"]
---

# Server Manual

Getting started

It is much easier than it looks to get a server up and running for your internet or LAN buddies; follow this wiki article and you will hopefully be on your way to hosting your own MTA:SA server in no time!

## Installing the server

The dedicated server application is available in different flavours depending on the platform of the server.

### Linux installation

There are different ways of getting a Linux server up and running:

- [Getting a precompiled package](https://linux.mtasa.com)

- [Installing and Running MTASA Server on GNU Linux](mta://getting-started/installing-and-running-mtasa-server-on-gnu-linux.md)

- [Building MTASA Server on GNU Linux](mta://development/building-mtasa-server-on-gnu-linux.md)

Should you have any problems with errors when starting the server some common problems and solutions are listed here:

- [Building MTASA Server on GNU Linux#Troubleshooting](mta://development/building-mtasa-server-on-gnu-linux.md)

### FreeBSD installation

You can run MTA:SA under FreeBSD using Linux emulation.

- Enable [Linux binary compatibility](https://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/linuxemu-lbc-install.html)

- Install following packages or compile them from ports: hs-terminfo, linux_base-f10, linux-f10-sqlite3

- Install [Linux precompiled package](https://linux.mtasa.com/)

### Windows installation

Installation of the MTA:SA server on Windows is easy as pie.

- Go to the [download page](https://mtasa.com/) and download the installer.

- Once the installer is downloaded, open it.

- Select a folder where you want to install the server.

- Click Install.

- Done!

*For a full explanation of acl.xml (access control list) read: [Access Control List](mta://tutorials/access-control-list.md)*

## Configuring your server

The Multi Theft Auto dedicated server is initially configurable through it's console window, from within the game, and from a webbrowser. In order to make use of the two last options, it is necessary to add at least one administrator user to your configuration file.

### General configuration

All general configuration options can be found in the 'mods/deathmatch/[**mtaserver.conf**](mta://reference/misc/server-mtaserver-conf.md)' file and can be opened by any regular text editor.

This file is fairly straightforward; every variable has a [description of what to do with it and how to change it](mta://reference/misc/server-mtaserver-conf.md).

### Port forwarding

If you run your server on your own private computer, and you have an router between the internet and your computer. You need to forward 3 ports.

First of all open the file 'mods/deathmatch/[**mtaserver.conf**](mta://reference/misc/server-mtaserver-conf.md)' and search for the next lines:

```
<serverport>22003</serverport> 
<httpport>22005</httpport>
```

The ports are needed to setup the server correctly. We explain later how to set them, but first if you want your server to appear in the server browser there is another port we need, and that is the ASE port. 
(quick example for how to turn ASE on or off):

```
<ase>1</ase> <!-- 0 = off, 1 = on -->
```

Now we going to forward the ports in your router, which is not needed if you already have all ports open, or if you don't have a router with a firewall. If so, skip this part.

If you don't know how port forwarding works in your router, go to the [Port Forward website](https://portforward.com/), find your router model there, and follow the instructions there.

In almost every router you can set the port type: UDP or TCP. The following list will explain which port type is needed for what:

Main server port: UDP

HTTP Port: TCP

ASE Port: UDP (this is needed if you want your server to appear in the server list)

The ASE port is also simple to get:

ASE port = Main server port + 123

So, if you have the main server port set to 22003, then the ASE port will be 22126.

Good luck!

**If you somehow get stuck while forwarding ports** (and have looked for the aforementioned [portforward.com](https://portforward.com/) page designed for your router model, you can give this extended (generic) forwarding guide a try:
  

[**Port forwarding for MTA servers**](https://forum.mtasa.com/topic/115141-guide-port-forwarding-in-order-to-run-a-mta-server/)

*In the latest version of the server, you can check the port status by using the server command [openports](mta://reference/misc/server-commands.md).*

### Client Checks

The MTA server can be configured to disable the anti-cheat. It can also allow specific or all files to be modified (e.g. carmods.dat), and make sure clients are of a minimum version.

All of these settings are within the file 'mods/deathmatch/[**mtaserver.conf**](mta://reference/misc/server-mtaserver-conf.md)'. See the [Anti-cheat guide](mta://scripting/concepts/anti-cheat-guide.md) for more details.

If you want to force a minimum client version, search for the following line:

```
<minclientversion></minclientversion>
```

Accepted values look like: 1.1.1-9.02320

### Adding administrators

It is strongly recommended to add at least one administrator to your server in order to make use of the built-in webserver to easily maintain and configure your server. This administrator will then also be able to log-in from within the game and control the server.

To add an administrator to your server, follow these steps:

- While the server is running, add a new account by typing **[addaccount name password](mta://reference/misc/server-commands.md)** into the server window. For example, to add user BennyLava you could type:

```
addaccount BennyLava 123password
```

*Note: If you do not have access to the server window, and the 'admin' resource is running, you can add  the example account by issuing the client console (F8) command **register BennyLava 123password***
- The server should display a message confirming the account has been added.
- Next, shutdown the server by typing **shutdown** into the server window.
- Make sure your server is stopped; if your server is still running, the following changes you make will be overwritten

- Open the file 'mods/deathmatch/acl.xml' with any text editor

- Add the account to the *Admin* group by using the XML-syntax below

```
<acl>
  ...
  <group name="Admin">
    <acl name="Admin"/>
    ...
    <object name="user.BennyLava" />
  </group>
  ...
</acl>
```

You're done! You can add as many administrators or users as you want this way, take a look at some of the other groups and ACLs for example. The ACL is also accessible through the [Lua scripting engine](mta://tutorials/access-control-list.md).

It is recommended to take a look at the web interface, we will explain how to do this below.

**Note**: There are also ways to add accounts and edit rights for the server while it's running. "[addaccount <user> <password>](mta://reference/misc/server-commands.md)" is an internal command to add accounts, but you will have to use the web interface to add these accounts to specific groups/ACLs!

### Using the web interface

The dedicated server comes with a few Lua [resources](mta://reference/misc/resources.md) that provide a nice little web interface to your server. This can be used to easily maintain your server, as it allows you to add users, start/stop resources, and more.

The web interface resources are enabled by default and are served through the built-in HTTP web server. To make sure the built-in HTTP web server runs on a port you like (22005 by default), follow these steps:

- Make sure your server is stopped
- Open the file 'mods/deathmatch/[**mtaserver.conf**](mta://reference/misc/server-mtaserver-conf.md)' with any text editor

- Verify that the HTTP server is enabled:

```
<httpserver>1</httpserver>
```

- Change the HTTP server port to your liking:

```
<httpport>22005</httpport>
```

- Save and close the configuration file

- Start your server

- If you happened to have changed the start-up resources in your configuration file, make sure the following resources are started:

- resourcebrowser

- resourcemanager

- webadmin

- webmap

These are automatically started in the default configuration file, in case you just installed your server.

- Open a web browser (Internet Explorer 6 or 7 are NOT supported; use [Mozilla Firefox](https://www.mozilla.com/firefox), [Google Chrome](https://www.google.com/chrome), [Apple Safari](https://www.apple.com/safari/download), [Opera](https://www.opera.com) or others) and navigate to the HTTP server URL: **[http://server:port/](http://server:port/)**. For example, If you are running a local server on HTTP port 22005, use **[http://127.0.0.1:22005/](http://127.0.0.1:22005/)**.

- Enter the username and password of the administrator you added in the previous section.

You should now be able to maintain your server from the web interface.

### Configuring an external web server

The built-in web server is also used to serve files that are required by resources running on your server to any player that is connected to your server. For example, if you are running a game script with a scripted graphical user interface, or custom models, these need to be transferred to every connected player in order to function properly. This is done by either the built-in web server, or an external web server (that is usually a bit faster) but needs to be set up separately.

For performance or consistency reasons during the game, you could choose to make use of such an external web server if you have one set up. The external web server needs to be accessible for the public, so any client will be able to download the necessary client-side files in order to join and play on your server.

To enable downloading off an external web server, you should configure the [httpdownloadurl](mta://reference/misc/server-mtaserver-conf.md) tag in your server configuration:

```
<httpdownloadurl>http://www.myserver.tld/directory/here</httpdownloadurl>
```

When you launch the server, the directory **<SERVER>/mods/deathmatch/resource-cache/http-client-files** will contain the correct client files for hosting on an external web server. If the web server is on the same machine, you can simply link the appropriate web server directory to **http-client-files**. If the web server is on a separate machine, ensure it has access to **http-client-files** via a network path, or maintain a remote copy using synchronization software.

**Note 1**: Please try to avoid any special characters (e.g. ~, !) in your download URLs.  

**Note 2**: Please do not use a trailing slash in your download URL (e.g. *http://www.myserver.tld/directory* rather than *http://www.myserver.tld/directory/*)  

**Note 3**: The web server must use 'ContentType: application/octet-stream' for Lua files. Most web servers will do this by default, or you can add the following line to the .htaccess file:

```
AddType application/octet-stream .lua
```

Instructions on how to install and configure Nginx as an external web server for MTA is here: [Installing and Configuring Nginx as an External Web Server](mta://getting-started/installing-and-configuring-nginx-as-an-external-web-server.md)

## Starting your server

Begin by making sure that you have finished all configuration of your server, starting your server is the last stage so everything must be ready!

To start your server double click on MTA Server.exe, make sure you allow it through any firewalls and forward ports where necessary.

## Installing/Updating resources on your server

Resources can come in two formats, either a ZIP format or just a normal folder with the script files inside it. The MTA:SA server supports both these methods.

- Move or copy the new resource to your <SERVER>\mods\deathmatch\resources folder.

- In the server window type in the command [refresh](mta://reference/misc/server-commands.md), this will re-scan the resources folder and update the live resources where necessary.

## Uninstalling resources

Resources can easily be removed from your server if you no longer want them.

- Delete the ZIP file or the folder of the resource you wish to uninstall

- In the server window type in the command "refresh" (without the quotes), this will re-scan the resources folder and update the live resources where necessary.

## Administrating your server

You can start resources by typing the command "start resourcename" in the server console, or stop ones with "stop resourcename".

It's also possible to execute these and other admin commands from the in-game console (which you can bring up with the ` key or F8); for this to work, you first need to log in with the command "[login username password](mta://reference/misc/server-commands.md)". Additionally, you can press the p key to bring up the admin panel: this is a graphical interface which allows you to easily kick or ban misbehaving players, among others.

For further commands, type [help](mta://reference/misc/server-commands.md) in a console.

## Starting a map/gamemode

See the commands section of the documentation for [mapmanager](https://wiki.multitheftauto.com/index.php?search=mapmanager) for more information.

## Keeping your server alive

To keep your server stable, you should avoid letting your server run unmanaged after you launched it.

- It is good to keep an eye on the process memory usage in Task manager, use performancebrowser/ipb, if the MTA Server process starts using more than 1.2 gb you're close to an Out Of Memory (OOM) error. At this point, you should:

- Restart the server

- Start checking for memory leaks in your code

- An OOM happens your server runs out of memory.

- Like with every process or application, not all elements and function calls can get efficiently freed.

- For example, if you start the server, you will have average memory usage of 50mb. If you have some players on it for a while, and all of them disconnected, you will have increased memory usage on the MTA Server process, even if the server returned to 0 players. This known as [*software aging*](https://www.google.com/search?q=software+aging).

- It is the leftover from the server's running time and can eventually increase until the server process can become unreliable and has chance of failure, memory exception or in other words, server crashes.

- To keep it short and simple: Always keep an eye on your servers and restart them once in a while to prevent this from happening, 50% of all server crashes asked support for are caused by it and it's better to be aware that you need this kind of maintenance to ensure stability!

- In other words: If you launch your server and leave it unmanaged for a long period, it won't hold out and it will crash at a certain point without the maintenance as described above. That means you cannot just start a server and not check back on it, because at one point you'll find it crashed if it gains memory usage over (very) long periods, depending on server load, player counts and other variables.

## Useful Notes

- You may also update the resources while in-game as long as you have the correct access levels by typing "refresh" in the clients console or "/refresh" in the chat window. This may cause a second of lag if you have many resources.

- In the above instructions, <SERVER> is the path to your server's main directory. In most cases this is C:\Program Files\MTA San Andreas\server

- You can choose a different config file for the server to use by passing it in the command line after a --config argument, e.g. mtaserver.exe --config anotherconfig.cfg.

- Do not be alarmed by the warning regarding the parsing of the settings.xml file. This happens because your server installation is still clean and unused.

#### Need further help?

Why not pop over to our [Forums](https://forum.mtasa.com/) or join us on [Discord](https://discord.com/invite/mtasa).
