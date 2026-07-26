---
doc_id: "mta-wiki:7852"
title: "Scripting Tips"
source_title: "Scripting Tips"
source_url: "https://wiki.multitheftauto.com/wiki/Scripting_Tips"
revision_id: 81964
language: "en"
categories: []
generated_at: "2026-07-26T16:16:36.335970+00:00"
---

# Scripting Tips

This page contains a variety of things that knowing, make life easier for MTA scripters.

## General Lua

- The *infinite loop / too long execution error* which aborts execution can be disabled with *debug.sethook(nil)*

- Be careful when looping a table where you intend to delete multiple rows, if 2 of them are in a row the 2nd one will get skipped! You must loop the table backwards (reverse ipairs). For example: *for i = #table, 1, -1 do*

- Rather than having if checks inside if checks inside if checks, consider using *return* for example *if (not ready) then return false end*

- A quick way to clamp a number between a lower and upper value: math.min(math.max(x, min), max) and easy to remember, just think: "min max min max"

## MTA Scripting

- Remember that 'false' boolean has a value - If you want to delete a variable or element/account data, use 'nil' instead - this will reduce memory and disk usage (minuscule optimization, only notable on larger servers)

- Remember that 99% of the time it's a bug in your script, not an MTA bug! Don't report something to GitHub Issues until you're absolutely certain the bug can be reproduced with a small piece of script.

- As MTA already has so many functions and events virtually everything you want to do is already possible, as long as you're willing to do the work! You'll find better solutions to problems as there are many ways to achieve the same thing as long as you know all the functions and events.

- If a script is getting too complicated, try putting back-end stuff in another file so the main script calls the functions in the 2nd one. For example rather than having meaningless things like *vehicleTable[vehicle][7]* in the main file, put that in a function in the 2nd file and have the main file call a meaningfully named function so rather than seeing a useless *7* you'd see something like *getFuel* and although this might take longer to set-up you'll save time in the long run as you'll spend less time being confused when you come back to it in a weeks time to debug a problem.

- Your client side scripts can cause desync if you're not careful, try to keep the psychical world equal with every player. For example if your script creates a client side object make sure your script will create it for everyone nearby, else people will be wondering why a player appears to be constantly floating and falling.

- Instead of using *onClientResourceStart* or *onResourceStart* events attached to *resourceRoot* like this:

```
function warnPeopleThatThisResourceStarted()
    outputChatBox("The resource " .. getResourceName(resource) .. " has just started!", 0, 255, 0)
end
addEventHandler("onClientResourceStart", resourceRoot, warnPeopleThatThisResourceStarted)
```

You can also use this outside of any function:

```
outputChatBox("The resource " .. getResourceName(resource) .. " has just started!", 0, 255, 0)
```

However the result won't be exactly the same, as onClientResourceStart gets called only when all resource scripts are fully loaded, whilst code outside of it will be ran once **this specific** script is loaded. This is important, because load order of scripts exists, and you might want to call other script function (which gets loaded into memory afterwards), resulting in **attempt to call global** error. By using this specific event you have reliable time-frame to call it.

- string.dump produces unsigned compiled Lua code which is not allowed for security reasons. The only way to transport code now is by using the source code. e.g.:

```
exampleFunction = [===[
    return param
]===]

local loadedFunction = loadstring(exampleFunction)
```

## MTA Scripting - Element IDs Being Reused

- If your script is covered in [isTimer](mta://scripting/shared/functions/istimer.md) and [isElement](mta://scripting/shared/functions/iselement.md) checks to hide debug warnings from deleted elements not being dereferenced (making the variable nil) you will regret it when that element ID or timer pointer has to be re-used by MTA in a weeks time and your script starts acting strangely and you won't have a clue why. Dereference destroyed elements and disconnected players!

- Why would MTA reuse it in a weeks time? Everything has a userdata value whether it's a function or an element, there is a limited amount of these available meaning that eventually the server will be forced to use the same userdata value twice, as long as whatever that userdata value was for is no longer valid. This could happen within hours, weeks or even never depending on how many elements are being created and destroyed by your scripts.

- For example if you have a race server that has 100 objects in every map and the map was changing every 5 minutes your server would go through at least 1200 an hour, 28,800 a day, 201,600 a week in userdata values, it can't keep going up and up though eventually it will have to reuse the same userdata values and as long as you're dereferencing in your scripts, it won't be a problem.

The is an example of a script which fails to dereference, because when the player quits their userdata value remains in the table, but what if in a weeks time another player joins and they get assigned the same userdata value?

```
local admins = {}
local secretPasswordOnlyAdminsShouldKnow = "12345678"

function adminLogin()
    if (hasObjectPermissionTo(source, "command.ban", false)) then
        admins[source] = true
    end
end
addEventHandler("onPlayerLogin", root, adminLogin)

function cmdGetSecretPassword(plr)
    if (not admins[plr]) then
        return false
    end
    outputChatBox("The secret password is "..secretPasswordOnlyAdminsShouldKnow, plr)
end
addCommandHandler("getsecretpass", cmdGetSecretPassword)
```

Some random player who joins in a weeks time gets the same userdata value as an admin, that player can now use "getsecretpass". Solution? De-reference on destruction!

```
function onQuit()
    admins[source] = nil
end
addEventHandler("onPlayerQuit", root, onQuit)
```

## Server Performance

- Server lagging? Check [this page of debugging performance issues](mta://scripting/concepts/debugging.md)

- Using **localPlayer** (or if not possible: **resourceRoot**) in **2nd** argument of triggerServer(Client)Event for events is much more efficient than using root.

- Try to be efficient, but if what you're doing is too time consuming or complex, is it really efficient?

- Unless you have hundreds of players, don't worry about making little optimizations, check *performancebrowser* or *ipb* (ingame performancebrowser) and make sure no resource is using significantly more than the others.

- It's much more efficient to [SetElementHealth](mta://scripting/shared/functions/setelementhealth.md) [setElementRotation](mta://scripting/shared/functions/setelementrotation.md) [setPedArmor](mta://scripting/shared/functions/setpedarmor.md) on a player client side (doing it server side sends an RPC to all players) consider a client event all your server scripts can call to set a players stat on their client and their client will then update the server via puresync and that change is then relayed to clients via the next puresync or lightsync packet. Note that doing this for position client isn't advised as the refresh rate for lightsync is low so would take a few seconds for remote players in another part of the map to see the player's new position.

## Client Performance

- The biggest cause of client script CPU usage is anything done in onClient/Pre/HUD/Render because it is called every frame. For example if you have a script which calls dxDrawLine3D 20 times, 60 times a second, if those lines are only in 1 part of the map, consider adding a [getDistanceBetweenPoints3D](mta://scripting/shared/functions/getdistancebetweenpoints3d.md) check between the local player and the general area that those lines are in and if they're no where near the player, don't draw the lines.

- **dxDraw*** functions can be highly optimised by using [dxCreateRenderTarget](https://wiki.multitheftauto.com/wiki/DxCreateRenderTarget), which will merge them into one single **dxDrawImage** resulting in much less calls. This can be applied to parts of interface which are static, or updated periodically.

- Another thing that gets called a lot and could therefore be quite consuming if not careful are events like [onClientPlayerWeaponFire](mta://scripting/client/events/onclientplayerweaponfire.md) and [onClientPlayerDamage](mta://scripting/client/events/onclientplayerdamage.md) so any scripts that use these should only be bound to the necessary elements (such as localPlayer instead of root) and run the simplest if statements for example if you wanted to handle a certain weapon being fired in a certain dimension it's better to check weapon first as that's a simple weaponID == x rather than getElementDimension(source) == y.

## Speed comparison between local and global variables

### Slower

```
start = getTickCount()
a = 1
for i=1,10000000 do
   a = 1
end
stop = getTickCount()
print("global", stop - start ) -- more than 500ms
```

### Faster

```
start = getTickCount()
local b = 1
for i=1,10000000 do
   b = 1
end
stop = getTickCount()
print("local", stop - start ) -- less than 200ms
```

## Speed comparison between structural and OOP scripting

### Slower

```
start = getTickCount()
a = 1
for i=1,1000000 do
   a = localPlayer.position
end
stop = getTickCount()
print("variable", stop - start ) -- more than 1500ms
```

### Faster

```
start = getTickCount()
b = nil
for i=1,1000000 do
   b = getElementPosition(localPlayer)
end
stop = getTickCount()
print("structural", stop - start ) -- less than 200ms
```
