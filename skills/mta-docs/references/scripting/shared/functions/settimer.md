---
doc_id: "mta-wiki:1428"
title: "SetTimer"
source_title: "SetTimer"
source_url: "https://wiki.multitheftauto.com/wiki/SetTimer"
revision_id: 78219
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# SetTimer

| [[{{{image}}}\|link=\|]] | Important Note: The speed at which a client side timer runs can be completely unreliable if a client is maliciously modifying their operating system speed, timers could run much faster or slower. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Important Note: Writing the following code can cause performance issues. Use onClientPreRender instead. setTimer(theFunction, 0, 0) |
| --- | --- |
|  |  |

This function allows you to trigger a function after a number of milliseconds have elapsed. You can call one of your own functions or a built-in function. For example, you could set a timer to spawn a player after a number of seconds have elapsed.

Once a timer has finished repeating, it no longer exists.

The minimum accepted interval is 0ms.

Multi Theft Auto guarantees that the timer will be triggered after *at least* the interval you specify. The resolution of the timer is tied to the frame rate (server side and client-side). All the overdue timers are triggered at a single point each frame. This means that if, for example, the player is running at 30 frames per second, then two timers specified to occur after 100ms and 110ms would more than likely occur during the same frame, as the difference in time between the two timers (10ms) is less than half the length of the frame (33ms). As with most timers provided by other languages, you shouldn't rely on the timer triggering at an exact point in the future.

## Syntax

```
timer setTimer ( function theFunction, int timeInterval, int timesToExecute [, var arguments... ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Timer](mta://reference/misc/timer.md)(...)*

### Required Arguments

- **theFunction:** The function you wish the timer to call.

| [[{{{image}}}\|link=\|]] | Note: The hidden global variable sourceTimer contains the currently executing timer userdata |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: The hidden global variable source becomes nil inside a timer function. You need to declare it on the function arguments if you need to use it. |
| --- | --- |
|  |  |

- **timeInterval:** The number of milliseconds that should elapse before the function is called. The minimum is 0 ms; 1000 milliseconds = 1 second)

- **timesToExecute:** The number of times you want the timer to execute, or 0 for infinite repetitions.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **arguments:** Any arguments you wish to pass to the function can be listed after the *timesToExecute* argument. Note that any tables you want to pass will get cloned, whereas metatables and functions/function references in that passed table will get lost. Also changes you make in the original table before the function gets called won't get transferred.

### Returns

Returns a [timer](mta://reference/misc/timer.md) pointer if the timer was set successfully, *false* if the arguments are invalid or the timer could not be set.

## Example

Click to collapse [-]
Example 1

This example will output some text after a small delay.

```
-- define function to be called
function delayedChat ( text )
	outputChatBox ( "Delayed text: " .. text )
end

-- set a timer so the function is called after 1 second
setTimer ( delayedChat, 1000, 1, "Hello, World!" )
```

1 second after the line above has been executed, the text *Delayed text: Hello, World!* will be displayed in the chat box.

Click to collapse [-]
Example 2

This example will nest a whole function within a timer. This is nice for things like setting variables without having to call a function outside of your code block.

```
function mainFunction()
        outputChatBox ("Instant text!")
	setTimer ( function()
		outputChatBox ( "5 second delay text!" )
	end, 5000, 1 )
end

mainFunction() --call function
```

Click to collapse [-]
Example 3

This example outputs some random text to the chat every 300000 milliseconds (5 minutes).

```
setTimer(function()
    outputChatBox("Text " .. math.random(1,4))
end, 300000, 0)
```

Click to collapse [-]
Example 4

This example should send a global message about the death of a player on a random time. I used [math.round](https://wiki.multitheftauto.com/wiki/Math.round) in this example to give a nicer output.

```
function math.round(number, decimals, method) -- math.round, useful function taken from the wiki: https://wiki.multitheftauto.com/wiki/Math.round
    decimals = decimals or 0
    local factor = 10 ^ decimals
    if (method == "ceil" or method == "floor") then return math[method](number * factor) / factor
    else return tonumber(("%."..decimals.."f"):format(number)) end
end

function onWasted()
	local delay = math.random(500, 5000) -- 0.5s to 5s of delay
	setTimer(function(thePlayer) -- Starts the Timer
		local whoDied = "Someone" -- In case the name can't be read, Someone will appear
		if isElement(thePlayer) then -- This checks if thePlayer's element still exists (which means thePlayer hasnt disconnected yet)
			whoDied = getPlayerName(thePlayer) -- Changes Someone to thePlayer's name
		end
		outputChatBox(whoDied.." #FFFFFFhas #FF0000died #FFFFFF"..math.round(delay/1000, 1).." seconds ago.", root, 255, 175, 0, true) -- This will output to everyone on the server that thePlayer (or Someone) died X seconds ago.
	end
	,delay, 1, source) -- The source at the end is an argument for the function we made before, you can't use the source directly because it won't be readed
end
addEventHandler("onPlayerWasted", root, onWasted) -- Executed every time someone dies
```

## See Also

- [addDebugHook](mta://scripting/shared/functions/adddebughook.md)

- [debugSleep](mta://scripting/shared/functions/debugsleep.md)

- [decodeString](mta://scripting/shared/functions/decodestring.md)

- [encodeString](mta://scripting/shared/functions/encodestring.md)

- [fromJSON](mta://scripting/shared/functions/fromjson.md)

- [generateKeyPair](mta://scripting/shared/functions/generatekeypair.md)

- [getColorFromString](mta://scripting/shared/functions/getcolorfromstring.md)

- [getDevelopmentMode](mta://scripting/shared/functions/getdevelopmentmode.md)

- [getDistanceBetweenPoints2D](mta://scripting/shared/functions/getdistancebetweenpoints2d.md)

- [getDistanceBetweenPoints3D](mta://scripting/shared/functions/getdistancebetweenpoints3d.md)

- [getEasingValue](mta://scripting/shared/functions/geteasingvalue.md)

- [getNetworkStats](mta://scripting/shared/functions/getnetworkstats.md)

- [getNetworkUsageData](mta://scripting/shared/functions/getnetworkusagedata.md)

- [getPerformanceStats](mta://scripting/shared/functions/getperformancestats.md)

- [getRealTime](mta://scripting/shared/functions/getrealtime.md)

- [getTickCount](mta://scripting/shared/functions/gettickcount.md)

- [getTimerDetails](mta://scripting/shared/functions/gettimerdetails.md)

- [getTimers](mta://scripting/shared/functions/gettimers.md)

- [getFPSLimit](mta://scripting/shared/functions/getfpslimit.md)

- [getUserdataType](mta://scripting/shared/functions/getuserdatatype.md)

- [getVersion](mta://scripting/shared/functions/getversion.md)

- [gettok](mta://scripting/shared/functions/gettok.md)

- [isTransferBoxVisible](mta://scripting/shared/functions/istransferboxvisible.md)

- [setTransferBoxVisible](mta://scripting/shared/functions/settransferboxvisible.md)

- [hash](mta://scripting/shared/functions/hash.md)

- [inspect](mta://scripting/shared/functions/inspect.md)

- [interpolateBetween](mta://scripting/shared/functions/interpolatebetween.md)

- [iprint](mta://scripting/shared/functions/iprint.md)

- [isOOPEnabled](mta://scripting/shared/functions/isoopenabled.md)

- [isTimer](mta://scripting/shared/functions/istimer.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22701](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22701):

- [isTimerPaused](mta://scripting/shared/functions/istimerpaused.md)

- [setTimerPaused](mta://scripting/shared/functions/settimerpaused.md)

- [killTimer](mta://scripting/shared/functions/killtimer.md)

- [md5](mta://scripting/shared/functions/md5.md)

- [passwordHash](mta://scripting/shared/functions/passwordhash.md)

- [passwordVerify](mta://scripting/shared/functions/passwordverify.md)

- [pregFind](https://wiki.multitheftauto.com/index.php?search=pregFind)

- [pregMatch](mta://scripting/shared/functions/pregmatch.md)

- [pregReplace](mta://scripting/shared/functions/pregreplace.md)

- [removeDebugHook](mta://scripting/shared/functions/removedebughook.md)

- [resetTimer](mta://scripting/shared/functions/resettimer.md)

- [setDevelopmentMode](mta://scripting/shared/functions/setdevelopmentmode.md)

- [setFPSLimit](mta://scripting/shared/functions/setfpslimit.md)

- setTimer

- [ref](mta://scripting/shared/functions/ref.md)

- [deref](mta://scripting/shared/functions/deref.md)

- [sha256](mta://scripting/shared/functions/sha256.md)

- [split](mta://scripting/shared/functions/split.md)

- [teaDecode](mta://scripting/shared/functions/teadecode.md)

- [teaEncode](mta://scripting/shared/functions/teaencode.md)

- [toJSON](mta://scripting/shared/functions/tojson.md)

- [tocolor](mta://scripting/shared/functions/tocolor.md)

- [getProcessMemoryStats](mta://scripting/shared/functions/getprocessmemorystats.md)

- [utfChar](mta://scripting/shared/functions/utfchar.md)

- [utfCode](mta://scripting/shared/functions/utfcode.md)

- [utfLen](https://wiki.multitheftauto.com/index.php?search=utfLen)

- [utfSeek](mta://scripting/shared/functions/utfseek.md)

- [utfSub](mta://scripting/shared/functions/utfsub.md)

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
