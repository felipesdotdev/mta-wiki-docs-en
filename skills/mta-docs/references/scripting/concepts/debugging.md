---
doc_id: "mta-wiki:9304"
title: "Debugging"
source_title: "Debugging"
source_url: "https://wiki.multitheftauto.com/wiki/Debugging"
revision_id: 75222
language: "en"
categories: ["Scripting_Concepts", "Tutorials"]
---

# Debugging

When scripting you will often come across problems that are not immediately apparent. This page tries to point out some basic strategies to locate the error.

## Debug console

MTA features a built-in debug console that shows debug messages output from MTA functions or from scripts. Keeping it mind that you should have administrator access (unless you modify the ACL to change this), you can open the debug console by typing *debugscript *x** in the console, where *x* is the debug level:

- **0:** close debug console

- **1:** only errors

- **2:** errors and warnings

- **3:** errors, warnings and info messages

By typing *debugscript 3* all messages are visible. Level 3 and level 2 are recommended for most occasions. You should have *debugscript* enabled whenever you are testing your scripts as it will help you easily detect and solve typos and other issues.

### Example

This example code has two errors:

```
function SayHello(message, player)
    if (getPlayerName(player) == "Fedor")
        outputChatbox("Hello Fedor")
    end
end
addEventHandler("onChatMessage", root, SayHello)
```

When the script this piece of code is in is tried to be loaded, debugscript will output something similiar to this:

INFO: Loading script failed: myResource\script.lua:2: 'then' expected near ´outputChatbox'

This means the script could not be parsed because there was a syntax error. It shows the script path relative to the resource directory so you can identify to script where the error originated from. After the filename it shows a colon and a number, this number presents the line number - this is so you can find out where in your script the error is - it is very helpful for large scripts. After that is the error message, which varies depending on the error made. Looking at the error message, we can easily determine that the error originated from the resource **myResource** and line two of the script file **script.lua**. The error message is very clear, we forgot the "then"! We can easily fix that!

```
function SayHello(message, player)
    if (getPlayerName(player) == "Fedor") then
        outputChatbox("Hello Fedor")
    end
end
addEventHandler("onChatMessage", root, SayHello)
```

Now the script will load fine and won't output any errors until a player with the name 'Fedor' says something in the chat. At that moment, the debug console will output:

ERROR: myResource\script.lua:2: attempt to call global 'outputChatbox' (a nil value)

This error means that the function **outputChatbox** is a nil value, that is - it doesn't exist! This is because the function is actually called [outputChatBox](mta://scripting/shared/functions/outputchatbox.md), not [outputChatbox](https://wiki.multitheftauto.com/index.php?title=OutputChatbox&action=edit&redlink=1) - take care of that capital B.:

```
function SayHello(message, player)
    if (getPlayerName(player) == "Fedor") then
        outputChatBox("Hello Fedor")
    end
end
addEventHandler("onChatMessage", root, SayHello)
```

Of course, this is just an example and I've only skimmed the surface of error messages. There are plenty of other messages and scenarios, but you should get a general idea.

### Clears the debug view

By typing **cleardebug**

## Server & client debug logging

#### Server

Navigate to: *(MTA root folder)>server>mods>deathmatch*

There are two nearly identical files:

- The local.conf is the settings for the "host game" menu item in the main menu of MTA. This is a quick and easy way of starting a temporary server from inside the client. When the client is turned off the server will also turn off.

- The mtaserver.conf is used when "MTA Server.exe" is executed from (MTA root folder)>server. This runs the server in its own console window which does not need the client to exist or to be run. This is can be useful if you're interested in hosting servers for a longer time period or if you want to experiment with a real-world console.

Depending on which way you host, you will want to edit those files. The settings in question are:

```
<!-- Specifies the location and name of the debugscript log file. If left blank, the server won't be saving this file. -->
	<scriptdebuglogfile>logs/scripts.log</scriptdebuglogfile> 
	
	<!-- Specifies the level of the debugscript log file. Available values: 0, 1, 2, 3. When not set, defaults to 0. -->
	<scriptdebugloglevel>0</scriptdebugloglevel>
```

You want to make sure you have a log name specified. Also, you want to specify what level of errors will be logged. If it is 0 nothing will be logged. The levels were explained at the top of this article. If the logging level was changed to 3, then, in this case, all **serverside** script errors log to (MTA root folder)>server>mods>deathmatch>logs>scripts.log

#### Client

Navigate to: *(MTA root folder)>MTA>logs>clientscript.log*

This file logs all **clientside** script errors. This is set to log by default, no setup required.

## Debug strategies

There are several strategies that support finding errors, apart from going through the code. Most of them include outputting debug messages, with have different information depending on the situation.

### Useful functions

There are some functions that may come in handy for debugging.

- [outputDebugString](mta://scripting/shared/functions/outputdebugstring.md) or [outputChatBox](mta://scripting/shared/functions/outputchatbox.md) for outputting any information (use outputDebugString for technical output)

- [tostring()](http://www.lua.org/manual/5.1/manual.html#pdf-tostring) on a variable to turn the value into a string. Useful if the value is not a number or string.

- [inspect](mta://scripting/shared/functions/inspect.md) returns a useful human-readable string notation of any datatype including tables, non-element userdatas such as ACL groups, accounts, etc, and elements.

- [iprint](mta://scripting/shared/functions/iprint.md) similar to inspect, except it takes in as many arguments as desired and outputs them into debugscript.

- [getElementType](mta://scripting/shared/functions/getelementtype.md) to check the type of the MTA element.

- [isElement](mta://scripting/shared/functions/iselement.md) to check if the MTA element exists.

### Add debugmessages to check *if*, *when* or *how often* a section of code is executed

A typical example would be verify whether an *if*-section is executed or not. To do that, just add any message you will recognize later within the *if*-section.

```
if (variable1 == variable2) then
    outputDebugString("variable1 is the same as variable2!")
    -- do anything
end
```

Another application would be to check when variable values are modified. First search for all occurrences of the variable being edited and add a message just beside it.

### Add debugmessages to check the *value* of a variable

Let's say you want to create a marker, but it doesn't appear at the position you expect it to be. The first thing you might want to do is check if the [createMarker](mta://scripting/shared/functions/createmarker.md) function is executed. But while doing this, you can also check the values being used in the [createMarker](mta://scripting/shared/functions/createmarker.md) function in one run.

```
outputChatBox("posX is: "..x.." posY is: "..y.." posZ is: "..z)
createMarker(x,y,z)
```

This would output all three variables that are used as coordinates for the marker. Assuming you read those from a map file, you can now compare the debug output to the desired values. The [tostring()](http://www.lua.org/manual/5.1/manual.html#pdf-tostring) will ensure that the values of the variables can be concatenated (put together) as a string, even if it's a boolean value.

## Example

Imagine you created a [collision shape](https://wiki.multitheftauto.com/index.php?search=collision%20shape) somewhere and you want an action to perform after the player stays for ten seconds inside it, you would do this:

```
function colShapeHit(player)
	-- set a timer to output a message (could as well execute another function)
	-- store the timer id in a table, using the player as index
	colshapeTimer[player] = setTimer(outputChatBox,10000,1,"The player stayed 10 seconds in the colshape!")
end
addEventHandler("onColShapeHit", root, colShapeHit)

function colShapeLeave(player)
	-- kill the timer when the player leaves the colshape
	killTimer(colshapeTimer[player])
end
addEventHandler("onColShapeLeave", root, colShapeLeave)
```

When a player enters the colshape, debugscript outputs the following message:

ERROR: ..[path]: attempt to index global 'colshapeTimer' (a nil value)

This means you tried to index a table that does not exist (because the table is a nil value, it doesn't exist). In the example above, this is done when storing the timer id in the table. We need to add a check if the table exists and if it does not exist we should create it.

```
function colShapeHit(player)
	if (colshapeTimer == nil) then
		colshapeTimer = {}
	end
	-- set a timer to output a message (could as well execute another function)
	-- store the timer id in a table, using the player as index
	colshapeTimer[player] = setTimer(outputChatBox,10000,1,"The player stayed 10 seconds in the colshape!")
end
addEventHandler("onColShapeHit", root, colShapeHit)

function colShapeLeave(player)
	-- kill the timer when the player leaves the colshape
	killTimer(colshapeTimer[player])
end
addEventHandler("onColShapeLeave",root,colShapeLeave)
```

Now we will still receive a warning when a player enters the colshape, waits for the message and leaves it again:

WARNING: [..]: Bad argument @ 'killTimer' Line: ..

Except for that (we will talk about that later) everything seems to work fine. A player enters the colshape, the timer is started, if he stays the message occurs, if he leaves the timer is killed.

### A more inconspicuous error

But for some reason, the message gets outputted twice when you stay in the colcircle while in a vehicle. Since it would appear some code is executed twice, we add debug messages to check this.

```
function colShapeHit(player)
	if (colshapeTimer == nil) then
		colshapeTimer = {}
	end
	-- add a debug message
	outputDebugString("colShapeHit")
	-- set a timer to output a message (could as well execute another function)
	-- store the timer id in a table, using the player as index
	colshapeTimer[player] = setTimer(outputChatBox,10000,1,"The player stayed 10 seconds in the colshape!")
end
addEventHandler("onColShapeHit",getRootElement(),colShapeHit)

function colShapeLeave(player)
	-- add a debug message
	outputDebugString("colShapeLeave")
	-- kill the timer when the player leaves the colshape
	killTimer(colshapeTimer[player])
end
addEventHandler("onColShapeLeave",getRootElement(),colShapeLeave)
```

Now we notice that both handler functions get executed twice when we are in a vehicle, but only once when we are on foot. It would appear the vehicle triggers the colshape as well. To confirm this theory, we ensure that the *player* variable actually holds a reference to a player element.

```
function colShapeHit(player)
	if (colshapeTimer == nil) then
		colshapeTimer = {}
	end
	-- add a debug message, with the element type
	outputDebugString("colShapeHit "..getElementType(player))
	-- set a timer to output a message (could as well execute another function)
	-- store the timer id in a table, using the player as index
	colshapeTimer[player] = setTimer(outputChatBox,10000,1,"The player stayed 10 seconds in the colshape!")
end
addEventHandler("onColShapeHit",getRootElement(),colShapeHit)

function colShapeLeave(player)
	-- add a debug message, with the element type
	outputDebugString("colShapeLeave "..getElementType(player))
	-- kill the timer when the player leaves the colshape
	killTimer(colshapeTimer[player])
end
addEventHandler("onColShapeLeave",getRootElement(),colShapeLeave)
```

The debug messages tell us that one of the *player* variables is a player and that the other one is a vehicle element. Since we only want to react when a player enters the colshape, we add an *if* that will end the execution of the function if it's **not** a player element.

```
function colShapeHit(player)
	if (colshapeTimer == nil) then
		colshapeTimer = {}
	end
	-- add a check for the element type
	if (getElementType(player) ~= "player") then return end
	-- add a debug message, with the element type
	outputDebugString("colShapeHit "..getElementType(player))
	-- set a timer to output a message (could as well execute another function)
	-- store the timer id in a table, using the player as index
	colshapeTimer[player] = setTimer(outputChatBox,10000,1,"The player stayed 10 seconds in the colshape!")
end
addEventHandler("onColShapeHit",getRootElement(),colShapeHit)

function colShapeLeave(player)
	-- add a check for the element type
	if (getElementType(player) ~= "player") then return end
	-- add a debug message, with the element type
	outputDebugString("colShapeLeave "..getElementType(player))
	-- kill the timer when the player leaves the colshape
	killTimer(colshapeTimer[player])
end
addEventHandler("onColShapeLeave",getRootElement(),colShapeLeave)
```

Now the script should work as desired, but it will still output the warning mentioned above. This happens because the timer we try to kill when a player leaves the colshape will not exist anymore when it has reached the 10 seconds (and therefore executed after the 10th second has completed). There are different ways to get rid of that warning (since you know that the timer might not exist anymore and you only want to kill it if it exists). One way would be to check if the timer referenced in the table really exists. To do this, we need to use [isTimer](mta://scripting/shared/functions/istimer.md), which we will use when we kill the timer:

```
if (isTimer(colshapeTimer[player])) then
	killTimer(colshapeTimer[player])
end
```

So the complete working code would be:

```
function colShapeHit(player)
	if (colshapeTimer == nil) then
		colshapeTimer = {}
	end
	-- add a check for the element type
	if (getElementType(player) ~= "player") then return end
	-- add a debug message, with the element type
	outputDebugString("colShapeHit "..getElementType(player))
	-- set a timer to output a message (could as well execute another function)
	-- store the timer id in a table, using the player as index
	colshapeTimer[player] = setTimer(outputChatBox,10000,1,"The player stayed 10 seconds in the colshape!")
end
addEventHandler("onColShapeHit",getRootElement(),colShapeHit)

function colShapeLeave(player)
	-- add a check for the element type
	if (getElementType(player) ~= "player") then return end
	-- add a debug message, with the element type
	outputDebugString("colShapeLeave "..getElementType(player))
	-- kill the timer when the player leaves the colshape
	if (isTimer(colshapeTimer[player])) then
		killTimer(colshapeTimer[player])
	end
end
addEventHandler("onColShapeLeave",getRootElement(),colShapeLeave)
```

## Debugging Performance Issues

If your server is using up more resources than it should or you just want to make sure your scripts are efficient, you can find the source of the issue by using a great tool that comes with the default resource package called [performancebrowser](https://wiki.multitheftauto.com/wiki/Resource:Performancebrowser). You can start it with '**start performancebrowser'**. If it doesn't exist then you can get the latest resources from the [GitHub repository](https://github.com/multitheftauto/mtasa-resources). This tool provides an incredible amount of information for performance debugging. Memory leaks, element leaks, and CPU intensive scripts are all easily findable via performancebrowser. If you use the '**d'** option in Lua timing you can see which functions are using up the CPU.

To access performancebrowser you will need to go to your web browser and enter the address: [http://serverIPHere:serverHTTPPortHere/performancebrowser/](http://serverIPHere:serverHTTPPortHere/performancebrowser/) Note that the / at the end is required. So for example: [http://127.0.0.1:22005/performancebrowser/](http://127.0.0.1:22005/performancebrowser/) You will then need to login with an in-game admin account or any account that has access to '**resource.performancebrowser.http'** and '**resource.ajax.http'**. Most of the information you will need is in the categories Lua timing and Lua memory, look for values that are much higher than other values.

### Examples of scripts that could cause performance problems

Adding data to a table but never removing it. This would take months/years before it causes a problem though.

```
local someData = {}

function storeData()
    someData[source] = true
    -- There is no handling for when a player quits, this is considered a memory leak
    -- Using the Lua timing tab you can detect the RAM usage of each resource.
end
addEventHandler("onPlayerJoin", root, storeData)
```

Element leaking is possible if you use temporary colshapes for whatever reason and may not destroy them. This would cause bandwidth, CPU and memory performance issues over time.

```
function useTemporaryCol()
    local col = createColCircle(some code here)
    if (normally this should happen) then
        destroyElement(col)
    end
    -- But sometimes it didn't so the script ended but the collision area remained and overtime
    -- you may end up with hundreds to thousands of pointless collision areas. 
    -- The Lua timing tab allows you to see the number of elements each script has created.
end
```

High CPU usage resulting in the server FPS dropping so much that the server is unplayable. In under 24 hours, this can create havoc on a very busy server. The amount of "refs" in the Lua timing detect this type of build-up, surprisingly the Lua timing tab didn't help in this case but Lua memory did.

```
addEventHandler("onPlayerJoin", root, function()
    -- Code for joiner
    addEventHandler("onPlayerQuit", root, function()
        -- Code for when they have quit
        -- See the problem? It's bound to root which the event handler is being added again and again and again
    end)
end)
```

A function uses up a lot of your CPU because whatever it does takes a long time. This is just some function that takes a long time to complete. Without performancebrowser you'd have no idea its the cause but with performancebrowser you can see that a resource is using lots of CPU in the Lua timing tab. If you then enter: '**d'** into the options edit box it will even tell you what file name and the first line of the function that is using up so much CPU.

```
function someDodgyCode()
    for i=1, 100000 do
        -- some code
    end
end
```
