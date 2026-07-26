---
doc_id: "mta-wiki:6120"
title: "Resource : Exp system"
source_title: "Resource:Exp system"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AExp_system"
revision_id: 37322
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:17:12.375902+00:00"
---

# Resource : Exp system

A level/experience system made from scratch by [Castillo](https://wiki.multitheftauto.com/index.php?title=User:Castillo&action=edit&redlink=1).  

It uses SQLite to save level and experience.

# Exported Functions

Click to collapse [-]
Server

This function is used to get a player level.

## Syntax

```
bool getPlayerLevel ( player thePlayer )
```

## Required Arguments

- **thePlayer**: The player element you wish you get the level.

## Returns

Returns a number with the level of the player.
<syntaxhighlight lang="lua">
addCommandHandler ( "mylevel",
	function ( thePlayer )

```
local myLevel = exports.exp_system:getPlayerLevel ( thePlayer )
```

outputChatBox ( "Your level is: ".. myLevel, thePlayer )
	end
)

Click to collapse [-]
Server

This function is used to set a player level.

## Syntax

```
bool setPlayerLevel ( player thePlayer, int theLevel )
```

## Required Arguments

- **thePlayer**: The player element you wish you set the level.

- **theLevel**: The level you want to set.

## Returns

Returns a bool, whether the level was set successfully or not.
<syntaxhighlight lang="lua">
addCommandHandler ( "setmylevel",
	function ( thePlayer, commandName, theLevel )

```
local theLevel = tonumber ( theLevel ) or 1
```

exports.exp_system:setPlayerLevel ( thePlayer, theLevel )
	end
)

Click to collapse [-]
Server

This function is used to get a player experience.

## Syntax

```
bool getPlayerEXP ( player thePlayer )
```

## Required Arguments

- **thePlayer**: The player element you wish you get the experience.

## Returns

Returns a number with with the experience of the player.

## Example

<syntaxhighlight lang="lua">
addCommandHandler ( "myexp",
	function ( thePlayer )

```
local myExp = exports.exp_system:getPlayerEXP ( thePlayer )
```

outputChatBox ( "Your experience is: ".. myExp, thePlayer )
	end
)

Click to collapse [-]
Server

This function is used to set a player experience.

## Syntax

```
bool setPlayerEXP ( player thePlayer, int theExperience )
```

## Required Arguments

- **thePlayer**: The player element you wish you set the experience.

- **theExperience**: The exprience you want to set.

## Returns

Returns a bool, whether the experience was set successfully or not.

## Example

<syntaxhighlight lang="lua">
addCommandHandler ( "setmyexp",
	function ( thePlayer, commandName, theExp )

```
local theExp = tonumber ( theExp ) or 0
```

exports.exp_system:setPlayerEXP ( thePlayer, theExp )
	end
)

Click to collapse [-]
Server

This function is used to give a player experience.

## Syntax

```
bool addPlayerEXP ( player thePlayer, int theExperience )
```

## Required Arguments

- **thePlayer**: The player element you wish you to give the experience.

- **theExperience**: The exprience you want to give.

## Returns

Returns a bool, whether the experience was given successfully or not.

## Example

<syntaxhighlight lang="lua">
addEvent ( "onZombieWasted", true )
addEventHandler ( "onZombieWasted", root,
	function ( theKiller )
		exports.exp_system:addPlayerEXP ( theKiller, 5 )
	end
)

Click to collapse [-]
Server

This function is used to get an account level.

## Syntax

```
bool getAccountLevel ( account theAccount )
```

## Required Arguments

- **theAccount**: The player element you wish you get the level.

## Returns

Returns a number with with the level of the account.
<syntaxhighlight lang="lua">
addCommandHandler ( "mylevel",
	function ( thePlayer )
		local account = getPlayerAccount ( thePlayer )

```
local myExp = exports.exp_system:getAccountLevel ( account )
```

outputChatBox ( "Your account level is: ".. myLevel, thePlayer )
	end
)

Click to collapse [-]
Server

This function is used to set an account level.

## Syntax

```
bool setAccountLevel ( account theAccount, int theLevel )
```

## Required Arguments

- **theAccount**: The player element you wish you set the level.

- **theLevel**: The level you want to set.

## Returns

Returns a bool, whether the level was set successfully or not.
<syntaxhighlight lang="lua">
addCommandHandler ( "setmylevel",
	function ( thePlayer, commandName, theLevel )
		local account = getPlayerAccount ( thePlayer )

```
local theLevel = tonumber ( theLevel ) or 1
```

exports.exp_system:setAccountLevel ( account, theLevel )
	end
)

Click to collapse [-]
Server

This function is used to get an account experience.

## Syntax

```
bool getAccountEXP ( account theAccount )
```

## Required Arguments

- **theAccount**: The player element you wish you get the experience.

## Returns

Returns a number with with the experience of the player.

## Example

<syntaxhighlight lang="lua">
addCommandHandler ( "myexp",
	function ( thePlayer )
		local account = getPlayerAccount ( thePlayer )

```
local myExp = exports.exp_system:getAccountEXP ( account )
```

outputChatBox ( "Your account experience is: ".. myExp, thePlayer )
	end
)

Click to collapse [-]
Server

This function is used to set an account experience.

## Syntax

```
bool setAccountEXP ( account theAccount, int theExperience )
```

## Required Arguments

- **theAccount**: The player element you wish you set the experience.

- **theExperience**: The exprience you want to set.

## Returns

Returns a bool, whether the experience was set successfully or not.

## Example

<syntaxhighlight lang="lua">
addCommandHandler ( "setmyexp",
	function ( thePlayer, commandName, theExp )
		local account = getPlayerAccount ( thePlayer )

```
local theExp = tonumber ( theExp ) or 0
```

exports.exp_system:setAccountEXP ( account, theExp )
	end
)

Click to collapse [-]
Server

This function is used to refresh the levels.

## Syntax

```
bool loadLevelsFromXML( )
```

## Required Arguments

- **None**

## Example

<syntaxhighlight lang="lua">
addCommandHandler ( "refreshlevels",
	function ( )
		exports.exp_system:loadLevelsFromXML ( )
	end
)

Click to collapse [-]
Server

This function is used to obtain the name and experience required of a level.

## Syntax

```
getLevelData ( int theLevel )
```

## Required Arguments

- **theLevel**

## Returns

Returns the name of the level and the experience required.

## Example

<syntaxhighlight lang="lua">
addCommandHandler ( "getleveldata",
	function ( thePlayer )
		local level = exports.exp_system:getPlayerLevel ( thePlayer )
		local name, expreq = exports.exp_system:getLevelData ( level )
		outputChatBox ( name ..": ".. expreq, thePlayer )
	end
)

# Custom Events

Click to collapse [-]
Server

This event is called when a player level changes.

## Syntax

```
event onPlayerChangeLevel
```

## Parameters

- **oldLevel**: The player old level.

- **newLevel**: The player new level.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) whose level changed.

Click to collapse [-]
Server

This event is called when a player level UP.

## Syntax

```
event onPlayerLevelUP
```

## Parameters

- **oldLevel**: The player old level.

- **newLevel**: The player new level.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) who leveled UP.

# See also

[Download page](http://community.mtasa.com/index.php?p=resources&s=details&id=1253)
