---
doc_id: "mta-wiki:3527"
title: "Resource : Admin"
source_title: "Admin"
source_url: "https://wiki.multitheftauto.com/wiki/Admin"
revision_id: 79102
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:10:43.023474+00:00"
---

# Resource : Admin

A quick tutorial on how to get admin rights and install admin resource.

To add an account in **MTA 1.6** use the following command in the server

```
addaccount <username> <password>
```

| [[{{{image}}}\|link=\|]] | Note: Server should not be running when you are editing the acl file below |
| --- | --- |
|  |  |

Then you open the **acl.xml** file located in the same folder and add yourself as an object to the Admin group by using the 'user.*' syntax, where * would be your account name.

```
<!-- The Admin group can do anything --> 
    <group name="Admin">
        <acl name="Moderator" />
        <acl name="SuperModerator" />
        <acl name="Admin" />
        <acl name="RPC" />
        <object name="user.lil_Toady" />
        <object name="resource.admin" />
    </group>
```

Now open your **mtaserver.conf** file and scroll to the bottom, make sure the admin resource is added to the ones that start with the server (note: protected="1" means that it can not be stopped).

```
<resource src="admin" startup="1" protected="0">  <!-- This is -->
    <resource src="helpmanager" startup="1" protected="0">
    <resource src="mapcycler" startup="1" protected="0">
    <resource src="mapmanager" startup="1" protected="0">
```

Now that you're done with server files, you can finally start it. Connect to the server itself and login with your account details: use 'login [username] <password>'. If it tells you to press 'p' you have done everything right, congratulations! If not, do this from the very beginning.

## Resource commands

Here are the commands from this resource. You need specific privileges to use most of them.

#### admin

Opens/Closes admin panel GUI.

- **Permission needed:** general.adminpanel

- **Syntax:** admin

#### ban

Bans the specified player and disconnects him from the server.

- **Permission needed:** command.ban

- **Syntax:** ban <playerName> <[reason]> <[period]> <[serial]>

- playerName: The name of the player you wish to ban.

- reason: Optional. The reason to ban the player. This will be shown to everyone on chatbox and also to the banned player.

- period: Optional. The seconds to keep the player banned. After this period, the player will be automatically unbanned. If not specified, this is 0 by default and the player will be banned permanently.

- serial: Optional. This can be any value. If specified, the player will be banned by serial. Otherwise the player will be banned by IP.

#### blendweather

Changes gradually the weather to the specified.

- **Permission needed:** command.blendweather

- **Syntax:** blendweather <weatherID>

- weatherID: The weather ID to gradually change to.

#### blowvehicle

Blows up the specified player's vehicle, killing its occupants and causing damage to nearest players and vehicles.

- **Permission needed:** command.blowvehicle

- **Syntax:** blowvehicle <playerName>

- playerName: The name of the player you wish to blow up the vehicle of.

#### createteam

Creates a new team that shows on TAB Score Table.

- **Permission needed:** command.createteam

- **Syntax:** createteam <teamName> <[red]> <[green]> <[blue]>

- teamName: The name of the team you wish to create.

- red: Optional. An integer representing the red color value. If not specified, it is 255 by default.

- green: Optional. An integer representing the green color value. If not specified, it is 255 by default.

- blue: Optional. An integer representing the blue color value. If not specified, it is 255 by default.

#### destroyteam

Deletes the specified team.

- **Permission needed:** command.destroyteam

- **Syntax:** destroyteam <teamName>

- teamName: The name of the team you wish to delete.

#### destroyvehicle

Deletes the vehicle from the specified player. The player must be inside a vehicle.

- **Permission needed:** command.destroyvehicle

- **Syntax:** destroyvehicle <playerName>

- playerName: The name of the player you wish to delete the vehicle of.

#### freeze

Freezes/unfreezes the specified player. If the player is inside a vehicle, the vehicle is frozen instead of the player. Also, if the player or the player's vehicle is already frozen, this command will unfrozen it.

- **Permission needed:** command.freeze

- **Syntax:** freeze <playerName>

- playerName: The name of the player you wish to freeze/unfreeze.

#### givevehicle

Creates a vehicle with the specified ID at the player position and teleports the player into the driver' seat. If the player is already in a vehicle, this command will change the vehicle model instead.

- **Permission needed:** command.givevehicle

- **Syntax:** givevehicle <playerName> <vehicleID>

- playerName: The name of the player you wish to give a vehicle.

- vehicleID: The model ID of the vehicle you wish to give to the player.

#### giveweapon

Gives a weapon with the specified ID to the specified player. If the player already has the specified weapon, the ammo is increased by the amount specified.

- **Permission needed:** command.giveweapon

- **Syntax:** giveweapon <playerName> <weaponID> <[ammo]>

- playerName: The name of the player you wish to give a weapon.

- vehicleID: The weapon ID of the weapon you wish to give to the player.

- ammo: Optional. The ammo you wish to give with the weapon. If not specified, it is 30 by default.

#### jetpack

Gives/removes a jetpack to the specified player.

- **Permission needed:** command.jetpack

- **Syntax:** jetpack <playerName>

- playerName: The name of the player you wish to give/remove a jetpack.

#### kick

Kicks the specified player from the server.

- **Permission needed:** command.kick

- **Syntax:** kick <playerName> <[reason]>

- playerName: The name of the player you wish to kick from the server.

- reason: Optional. The reason to kick the player. This will be shown to the kicked player after the kick.

#### mute

Mutes the specified player by the specified period or until the player disconnects with the specified reason. If the player is already muted, this command will unmute the player.

- **Permission needed:** command.mute

- **Syntax:** mute <playerName> <[reason]> <[period]>

- playerName: The name of the player you wish to mute.

- reason: Optional. The reason to mute the player. This will be shown to everyone on chatbox.

- period: Optional. The seconds the player will stay muted. After this period, the player will be automatically unmuted. If not specified, the player will be muted until disconnects or manually unmuted by someone.

#### register

Adds a new account with the username and password.

- **No permission needed.**

- **Syntax:** register <[username]> <password>

- username: Optional. The name of the account you wish to add, if not specified, it is the player's name.

- password: This is the password used to access the account. Minimum length is 4 characters and maximum length is 30 characters.

#### setarmour

Sets the specified player's armour health.

- **Permission needed:** command.setarmour

- **Syntax:** setarmour <playerName> <value>

- playerName: The name of the player you wish to set armour.

- value: The new armour's health. Accepts values from 0 to 100.

#### setcolor

Sets the specified player's vehicle colors.

- **Permission needed:** command.setcolor

- **Syntax:** setcolor <playerName> <[color1]> <[color2]> <[color3]> <[color4]>

- playerName: The name of the player you wish to set vehicle's colors. The player must be in a vehicle.

- color1: Optional. An hexadecimal code of the vehicle's color 1. If not specified, it is #000000 by default.

- color2: Optional. An hexadecimal code of the vehicle's color 2. If not specified, it is #000000 by default.

- color3: Optional. An hexadecimal code of the vehicle's color 3. If not specified, it is #000000 by default. *Note: Only three GTA SA vehicles are using this color: Camper, Cement Truck, Squalo.*

- color4: Optional. An hexadecimal code of the vehicle's color 4. If not specified, it is #000000 by default. *Note: Actually there's no vehicles on GTA SA using this color.*

| [[\|link=\|]] | Warning: This command needs corrections. Nowadays, all colors are mandatory. |
| --- | --- |
|  |  |

#### setdimension

Sets the specified player's dimension.

- **Permission needed:** command.setdimension

- **Syntax:** setdimension <playerName> <value>

- playerName: The name of the player you wish to set dimension.

- value: The new dimension. Accepts values from 0 to 65535.

#### setgame

Sets the server's game type. This will be visible in the server browser.

- **Permission needed:** command.setgame

- **Syntax:** setgame <gameType>

- gameType: The name of the game type.

#### setgamespeed

Sets the server's game speed.

- **Permission needed:** command.setgamespeed

- **Syntax:** setgamespeed <gameSpeed>

- gameSpeed: The speed of the game. Normal speed is 1. Accepts values from 0 to 10. *Note: Actually only values from 0.001 to 4 make difference.*

#### setgravity

Sets the server's game gravity.

- **Permission needed:** command.setgravity

- **Syntax:** setgravity <gravity>

- gravity: The gravity of the game. Normal gravity is 0.008. *Note: Higher gravity also increase fall damage.*

#### sethealth

Sets the specified player's health.

- **Permission needed:** command.sethealth

- **Syntax:** sethealth <playerName> <value>

- playerName: The name of the player you wish to set health.

- value: The new health. Accepts values from 0 to 200. *Note: To use health higher than 100, the player must set health stats. Otherwise maximum health is 100.*

#### setinterior

Sets the specified player's interior. Only interiors from interiors.xml can be used.

- **Permission needed:** command.setinterior

- **Syntax:** setinterior <playerName> <interiorName>

- playerName: The name of the player you wish to change interior.

- interiorName: The interior name. The names are at the "id" attribute. *Note: Interior names are in capital letters.*

#### setmap

Sets the server's map name. This will be visible in the server browser.

- **Permission needed:** command.setmap

- **Syntax:** setmap <mapName>

- mapName: The name of the map.

#### setpaintjob

Sets the specified player's vehicle paintjob.

- **Permission needed:** command.setpaintjob

- **Syntax:** setpaintjob <playerName> <paintjobID>

- playerName: The name of the player you wish to set vehicle's paintjob. The player must be in a vehicle.

- paintjobID: The paintjob ID. Accepts values from 0 to 3. Using 3 will remove the paintjob.

#### setpassword

Sets the server's password. Players will need to provide the server password to join the server.

- **Permission needed:** command.setpassword

- **Syntax:** setpassword <password>

- password: The password of the server. If not specified, it will remove the password.

#### setskin

Sets the specified player' skin.

- **Permission needed:** command.setskin

- **Syntax:** setskin <playerName> <skinID>

- playerName: The name of the player you wish to change skin.

- skinID: The new skin ID. Accepts values from 0 to 312. *Note: The following IDs are not working: 3 4 5 6 8 42 65 74 86 119 149 208 273 289.*

#### setstat

Sets the specified player' stat.

- **Permission needed:** command.setstat

- **Syntax:** setstat <playerName> <statID> <value>

- playerName: The name of the player you wish to change the stat.

- statID: The stat ID. Accepts values from 0 to 230 (with exceptions). *Note: See all stat IDs [here](mta://scripting/shared/functions/setpedstat.md).*

- value: The new value to the stat. Accepts values from 0 to 1000.

#### setteam

Sets the specified player' team.

- **Permission needed:** command.setteam

- **Syntax:** setteam <playerName> <teamName>

- playerName: The name of the player you wish to set the team.

- teamName: The team name.

#### settime

Sets the server time.

- **Permission needed:** command.settime

- **Syntax:** settime <hour> <minute>

- hour: The clock hour. Accepts 0-23.

- minute: The clock minute. Accepts 0-59.

#### setweather

Sets the server weather.

- **Permission needed:** command.setweather

- **Syntax:** setweather <weatherID>

- weatherID: The weatherID. Accepts from 0 to 255. *Note: Standard weathers are from 0 to 19. Other weathers are used for effects only.*

#### setwelcome

Sets the server welcome message.

- **Permission needed:** command.setwelcome

- **Syntax:** setwelcome <message>

- message: The welcome message. *Note: You can't use spaces with this command because there's only one parameter.*

#### shout

Sends a message at the specified player' screen. Useful for warn the player.

- **Permission needed:** command.shout

- **Syntax:** shout <playerName> <message>

- playerName: The name of the player who you wish to shout at.

- message: The shout message. *Note: You can't use spaces with this command because there's only one parameter.*

#### slap

Slaps the specified player with the specified damage. Useful for punish the player. The player is also pulled up.

- **Permission needed:** command.slap

- **Syntax:** slap <playerName> <damage>

- playerName: The name of the player who you wish to slap.

- damage: An integer representing the slap damage. If you use 0, the player will just be pulled up.

#### unregister

Removes an account with the specified username. This will also delete the account data.

- **Permission needed:** function.removeAccount

- **Syntax:** unregister <username>

- username: The name of the account you wish to delete. The account can't be on other ACL Groups than "Everyone".

#### repair

Repairs the specified player's vehicle.

- **Permission needed:** command.repair

- **Syntax:** repair <playerName>

- playerName: The name of the player who you wish to repair the vehicle.
