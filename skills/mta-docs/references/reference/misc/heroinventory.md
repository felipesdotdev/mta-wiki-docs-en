---
doc_id: "mta-wiki:6961"
title: "HeroInventory"
source_title: "HeroInventory"
source_url: "https://wiki.multitheftauto.com/wiki/HeroInventory"
revision_id: 35308
language: "en"
categories: []
---

# HeroInventory

Description

HeroInventory is a new way to expand a roleplay server's features. This resource allows a server to not only archive items; but organize them appropriately! Adding items, and groups are very simple.

community page link[[1]](http://community.mtasa.com/index.php?p=resources&s=details&id=6310)

## Notes

You're able to add items by editing g_items.lua.
An example use of the resource:HeroBook[[2]](https://wiki.multitheftauto.com/wiki/HeroBook#Integrate_Into_HeroInventory)(from Malicious Hero)

## Callbacks

### onPlayerUseItem

```
bool onPlayerUseItem( int itemID, int itemAmount )
```

- source = player using the item

The callback is found in e_item_use.lua in the folder "events". Examples are shown.

### onPlayerPickupItem

```
bool onPlayerPickupItem( element playerElement, int itemID, string itemDroppedBy )
```

The callback is found in e_item_pickup.lua in the folder "events". Examples are shown.

## Player Functions

### addPlayerItem

```
bool addPlayerItem ( element playerElement, int itemID, int amount )
```

```
@title
        addPlayerItem
@author
	Malicious Hero.
@parameters
	playerElement - The element you wish to add an item to.
	itemID - The item ID; This can be found in g_items.lua.
	amount - The amount of the item you want.
@description
	This will add an item to a client.
```

### refreshClientGroups

```
bool refreshClientGroups( )
```

```
@title
	refreshClientGroups
@author
	Malicious Hero.
@parameters
		
@description
	This is not really a function used when exporting; but it's important this command remains
	in this resource because without this, groups would not be sync properly.
```

### removeItemFromPlayer

```
bool removeItemFromPlayer( element playerElement, int itemID, [ int amount ] )
```

```
@title
	removeItemFromPlayer
@author
	Malicious Hero.
@parameters
	playerElement - The player.
	itemID - The item ID
	amount - The amount you wish to remove. You can leave this blank to remove everything.
@description
	Use this function to remove an item from a player.
```

### transferPlayerItem

```
bool transferPlayerItem( element playerElement, element targetElement, int itemID, int amount )
```

```
@title
	transferPlayerItem
@author
	Malicious Hero.
@parameters
	playerElement - The player.
	targetElement - The target.
	itemID - The item ID
	amount - The amount you wish to remove. You can leave this blank to remove everything.
@description
	Use this function to move one item to another player.
```

### doesPlayerHaveItem

```
bool doesPlayerHaveItem( element playerElement, int itemID)
```

```
@title
	doesPlayerHaveItem
@author
	Malicious Hero.
@parameters
	playerElement - The player.
	itemID - The item ID
@description
	Use this function to move one item to another player.
@returns
	if returning true, it will return the amount as well.
```

### getPlayerItemAmount

```
bool getPlayerItemAmount( element playerElement, int itemID )
```

```
@title
	getPlayerItemAmount
@author
	Malicious Hero.
@parameters
	playerElement - The player.
	itemID - The item ID
@description
	Use this function to get a player's item amount
@returns
	The amount item. If false, they don't have the item
```

## Group Functions

### addInventoryGroup

```
bool addInventoryGroup( string group_name, path imagesrc )
```

```
@title
	addInventoryGroup
@author
	Malicious Hero.
@parameters
	group_name - Indicates the group name that you wish to add.
	imagesrc - The picture you want to associate with the group.
@description
	This will add a inventory group, which will allow the server to create new items.
	Please keep in mind that in s_inventory_config.lua, you are able to set the maximum amount
	of groups you allow.
```

### removeInventoryGroup

```
bool removeInventoryGroup( string group_name )
```

```
@title
	removeInventoryGroup
@author
	Malicious Hero.
@parameters
	group_name - Indicates the group name that you wish to add.
@description
	This will remove an inventory group.
```
