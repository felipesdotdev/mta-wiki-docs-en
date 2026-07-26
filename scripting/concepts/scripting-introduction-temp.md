---
doc_id: "mta-wiki:14678"
title: "Scripting Introduction temp"
source_title: "Scripting Introduction temp"
source_url: "https://wiki.multitheftauto.com/wiki/Scripting_Introduction_temp"
revision_id: 82832
language: "en"
categories: []
generated_at: "2026-07-26T16:16:36.303357+00:00"
---

# Scripting Introduction temp

MTA Scripting: From Zero to Your First Script

Many beginners think scripting requires pages of complex code before anything happens. In Multi Theft Auto (MTA), a fully working script can be as short as a single line.

This tutorial will show you the bare basics of how scripts work, how to navigate the MTA Wiki to find functions, and how to expand your script progressively into interactive commands and events.

### What is a "Resource"?

In MTA, everything you run on a server (gamemodes, maps, custom scripts) is called a **resource**. 
A resource is simply a folder inside your server directory that contains:

- One configuration file named **meta.xml** (which tells the server what files to load).

- One or more script files written in the **Lua** programming language.

#### Server-side vs. Client-side

MTA splits scripts into two distinct environments:

- **Server-side (Server):** Scripts that run on the host server. They manage things that affect everyone, like the game world, weather, global variables, and player accounts.

- **Client-side (Client):** Scripts that run on the individual player's computer. They handle things the player sees directly on their screen, like custom user interfaces (GUIs) and visual effects.

In this tutorial, we will start with **Server-side** scripting, and then show you how to transition to the client.

---

## Step 1: The One-Line Script

Let us create the absolute simplest working script possible: a script that sets the game world's weather.

Navigate to your server's resources directory:

```
server/mods/deathmatch/resources/
```

Create a new folder here and name it: `my_first_script`

#### 1. Create your meta.xml

Inside your `my_first_script` folder, create a plain text file, name it `meta.xml`, and type or paste the following code:

```
<meta>
     <info author="YourName" type="script" name="My First Script" description="Simple weather script" />
     <script src="script.lua" type="server" />
</meta>
```

*Reminder: The `<script />` tag tells the server engine to locate a file named `script.lua` and run it in the server environment (`type="server"`).*

#### 2. Write your script.lua

In the same folder, create a text file named `script.lua`. Open it in your code editor and **type** this exact line of code yourself:

```
setWeather(8)
```

Let us look at what you just wrote. You called a function named [setWeather](mta://scripting/shared/functions/setweather.md) and passed it an argument of `8`. The number `8` is an identifier that tells the MTA engine to change the sky to a raining thunderstorm.

#### 3. Run the script

- Start your server executable (`MTA Server.exe`).

- In the server console window, type: `start my_first_script` and press Enter.

- Connect to your server in-game. When you spawn, the weather will instantly become rainy.

---

## Understanding the MTA Wiki

Now, you might be wondering: how did we know that [setWeather](mta://scripting/shared/functions/setweather.md) exists, or that putting an `8` inside the parentheses makes it rain?

There is an easy solution for that: The MTA Wiki. You do not need to memorize code; you just need to know how to read the documentation.

If you search for [setWeather](mta://scripting/shared/functions/setweather.md) on the wiki, you will see a syntax block that looks like this:

```
bool setWeather ( int weatherID )
```

To be able to understand how functions work in MTA, we need to learn how to read this syntax on the wiki.

#### How to read this syntax:

- **bool** (Boolean): The first word tells you what the function *returns* after it finishes. A boolean means it gives back either `true` (success) or `false` (failure).

- **setWeather**: The exact name of the function you must type.

- **int weatherID** (Integer): The information you must provide inside the parentheses. An `int` expects a whole number (like `0`, `1`, or `8`). The documentation page lists what each number means (e.g., `8` is a rainstorm).

Now let us look at another essential function, [outputChatBox](mta://scripting/shared/functions/outputchatbox.md):

```
bool outputChatBox ( string text [, element visibleTo=root, int r=255, int g=255, int b=255, bool colorCoded=false ] )
```

#### How to read optional parameters:

- **string text**: The first argument must be a string (regular text wrapped in quotation marks, like `"Hello world"`).

- **Square Brackets `[ , ... ]`**: Anything inside square brackets is **optional**. You do not have to type it.

- **Default Values (`=`)**: If you skip an optional argument, the engine uses the default value shown. For example, `visibleTo=root` means if you don't specify a target player, the message defaults to `root` (meaning it sends to everyone). `r=255, g=255, b=255` defaults the text color to white.

---

## Step 2: Making Things Interactive (Events)

Our one-line script runs immediately when the resource starts, but games are interactive. You usually want code to trigger only when a specific action happens in the world—like a player entering a vehicle or taking damage. We handle this using [Events](mta://reference/misc/event.md).

Let us replace our script with something more interesting: greeting players personally the moment they join the server.

Open your `script.lua`, delete the old code, and write this complete updated code:

```
-- Define a function containing the actions we want to happen
function welcomeNewPlayer()
    -- 'source' is a built-in variable representing the player who just joined
    outputChatBox("Welcome to the server!", source)
end

-- Connect our function to the built-in player join event
addEventHandler("onPlayerJoin", root, welcomeNewPlayer)
```

#### How this flows:

- **function welcomeNewPlayer()**: We group our code inside a named block called a function. This code sits silently and does nothing until it is called.

- **[addEventHandler](mta://scripting/shared/functions/addeventhandler.md)**: We tell the server to listen for a specific trigger.

- **[onPlayerJoin](mta://scripting/server/events/onplayerjoin.md)**: The built-in MTA event that triggers whenever any player connects.

- **root**: This tells the event listener where to listen. Using the predefined global variable `root` means "listen for anyone connecting to the entire server."

- **welcomeNewPlayer**: The name of the function we want to fire when the event happens.

- **[source](https://wiki.multitheftauto.com/index.php?title=Source&action=edit&redlink=1)**: Inside an event function, `source` is a hidden variable created by MTA. You can refer to the wiki page for [source](https://wiki.multitheftauto.com/index.php?title=Source&action=edit&redlink=1) to learn more. For `onPlayerJoin`, `source` always refers to the specific player element who just connected.

---

## Step 3: Giving Control to Players (Commands)

Next, let us allow players to trigger code whenever they type a command in the chat box, such as `/rain`.

To make a command, we follow a flow very similar to events: we write a function, and then we link that function to a command word using [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md).

Replace the code in your `script.lua` with this basic command setup:

```
-- 1. Write the function we want the command to trigger
function makeSkyRain()
    setWeather(8)
    outputChatBox("The sky is now dark and raining!")
end

-- 2. Hook the command word "/rain" to our function
addCommandHandler("rain", makeSkyRain)
```

If you restart your resource and type `/rain` in the game chat, the weather will instantly start storming.

### Adding Arguments to Commands

What if we want the player to choose the weather ID themselves? Like typing `/setweather 8`.

When a player uses a server-side command handler, MTA automatically passes three variables into your function:

- The **player** who typed the command.

- The **name** of the command itself.

- Whatever **text** the player typed after the space.

Let us update `script.lua` to accept a weather ID argument.

```
-- The function receives: the player element, the command name, and the extra text
function customWeatherCommand(thePlayer, commandName, weatherIDText)

    -- Convert the typed text into a real number
    local weatherNumber = tonumber(weatherIDText)

    -- Validation check: If the player didn't type a number, stop right here
    if not weatherNumber then
        outputChatBox("Syntax: /setweather [ID number]", thePlayer)
        return -- 'return' instantly stops the function from continuing
    end

    -- If the check passed, change the weather to the typed number
    setWeather(weatherNumber)
end

addCommandHandler("setweather", customWeatherCommand)
```

### Server-Side vs. Client-Side Commands

Note that we have configured `script.lua` to be on the server side in our `meta.xml`. This means the command will run on the server side and change the weather for **everyone** on the server!

Depending on your server, you might not want players changing the weather for everybody. We could fix this in two ways:

- Make it so only administrators are able to use the command.

- OR, write the command on the **client side** instead.

Let us look at how to implement the second option. A client-side script will only change the weather for the player who typed the command, leaving everyone else's weather untouched.

#### Modifying the Meta

To add a client-side script, create a new text file inside your `my_first_script` folder and name it `client.lua`. Then, update your `meta.xml` to tell the server about this new client file:

```
<meta>
     <info author="YourName" type="script" name="My First Script" description="Simple weather script" />
     <script src="script.lua" type="server" />
     <script src="client.lua" type="client" />
</meta>
```

#### Writing the Client-Side Command

Open `client.lua` and add the following code:

```
function localWeatherCommand(commandName, weatherIDText)
    local weatherNumber = tonumber(weatherIDText)

    if not weatherNumber then
        outputChatBox("Syntax: /myweather [ID number]")
        return
    end

    setWeather(weatherNumber)
    outputChatBox("You changed your local weather!")
end

addCommandHandler("myweather", localWeatherCommand)
```

Notice a big difference? In client-side commands, we don't need `thePlayer` as the first function argument. This is because on the client side, the script is only running for one person, so the player element is always automatically the [localPlayer](mta://scripting/client/functions/localplayer.md).

Now, typing `/setweather 8` (Server) changes the sky for everyone, but typing `/myweather 8` (Client) changes it only for you!

---

## Step 4: Your Best Friend (Debugging)

As you write your own scripts, you will inevitably make mistakes. If you misspell a function name or forget a closing parenthesis, your script simply will not work.

However, debugging is not just for typos or syntax errors—it can show other errors too, like logic errors, passing the wrong type of data (e.g., passing text instead of a number), or trying to modify a vehicle or player element that has already disconnected or been destroyed.

Instead of guessing what went wrong, you should use MTA's built-in script monitor.

### Enabling Debugscript

In the game client, open your console (usually by pressing the `F8` key or the `~` key) and type:

```
debugscript 3
```

A small transparent box will appear at the bottom of your screen. The `3` tells MTA to show all Errors, Warnings, and Information messages in real-time.

#### Seeing it in action

Let us intentionally make a typo to see how `/debugscript 3` helps us. Open your `script.lua` and change [setWeather](mta://scripting/shared/functions/setweather.md) to a misspelled word:

```
function brokenCommand()
    setWeatherrrr(8) -- Intentionally misspelled function
end
addCommandHandler("brokeweather", brokenCommand)
```

Save the file, restart your resource, and type `/brokeweather` in-game.

Look at the bottom of your screen. You will see a red error message pop up:

```
ERROR: my_first_script/script.lua:2: attempt to call global 'setWeatherrrr' (a nil value)
```

This debug line tells you exactly where the problem is: inside the `my_first_script` folder, in `script.lua`, on **line 2**. It even tells you that `setWeatherrrr` is a "nil value" (meaning the engine doesn't recognize the word).

Keeping `/debugscript 3` open while you code is the single most important habit you can build as an MTA developer.
