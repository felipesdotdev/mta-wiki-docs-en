---
doc_id: "mta-wiki:2368"
title: "Client side scripts"
source_title: "Client side scripts"
source_url: "https://wiki.multitheftauto.com/wiki/Client_side_scripts"
revision_id: 81080
language: "en"
categories: ["Scripting_Concepts"]
---

# Client side scripts

Client side scripts are scripts that run inside the deathmatch mod client side. This means that the game has access to more information about the game world, but slightly less information about the rest of the players in the game.

This is useful for things that need to be done client side, such as visual effects, creation and manipulation of GUI elements.

## How does it work?

Client side scripts follow the same pattern as server side scripts. We will try to provide the necessary functionality for client side scripts. Interfacing between a server side and client side script is done by using the same event system as we already have. The server side and client side scripts will need to be in two different files, which are included from the resource (in the metafile) by using a <script> tag (and type attribute).

For example:

**meta.xml**

```
<meta>
	<script src="c_gui.lua" type="client" />
	<script src="s_gui.lua" type="server" />
</meta>
```

If you wanted to trigger a client side event from the server, you would first have to register the client side event using [addEvent](mta://scripting/shared/functions/addevent.md). Then, you can attach a handler to the event as you would in a server side script. Then in the server side script, you'll be able to call [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md), which will trigger the event client side. The same can be done in reverse using [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md).

For example:

**Client side**

```
function showObjectBrowser ( id )
	-- code here
end
addEvent( "doShowObjectBrowser", true )
addEventHandler( "doShowObjectBrowser", localPlayer, showObjectBrowser )
```

**Server side**

```
triggerClientEvent ( somePlayer, "doShowObjectBrowser", somePlayer, 1034 )
```
