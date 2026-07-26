---
doc_id: "mta-wiki:13413"
title: "Resource : EntityData"
source_title: "Resource:EntityData"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AEntityData"
revision_id: 73705
language: "en"
categories: ["Resource"]
---

# Resource : EntityData

**Name**: entityData

**Developer**: [User:GalAnonim](https://wiki.multitheftauto.com/index.php?title=User:GalAnonim&action=edit&redlink=1) (Rick)

**State**: OpenSource

**GitHub Source**: [https://github.com/httpRick/entityData/tree/main](https://github.com/httpRick/entityData/tree/main)

**Current Version**: 1.0.0

## Overview

The system of non-standard data operation for Elements on the MTA SA platform replaces ElementData

## Exported functions

### setEntityData

This function passes user information about the element to entity Data, the data can be created by the server but you should avoid passing data from client to server when assigning.

Click to collapse [-]
Shared

This function encrypts the data of the file

```
string exports.entityData:setEntityData(element/table theElement, var/table key, var value, [string type="public", int transaction])
```

### Required Arguments

- **element theElement:** The element/elements you wish to attach the data to.

- **var key:** The key/keys you wish to store the data under.

### Optional Arguments

- **string type:**  type of data synchronization

- *"public"* - Synchronizes between the server and the client, and between the client and the server (required to be enabled in the options)

- *"local"* - It does not synchronize, it remains on the side on which it was given

- *"private"* - Assigns and synchronizes one value for a given key for all items

- **int transaction:** - The transaction number, if this value is provided, the data transfer will not be executed immediately

### Returns

Returns true if the data was set succesfully, false otherwise.

### getEntityData

This function retrieves entity data attached to an element under a certain key.

Click to collapse [-]
Shared

This function encrypts the data of the file

```
string exports.entityData:getEntityData(element/table theElement, var/table key, [string type="public"])
```

### Required Arguments

- **element theElement:** This is the element/elements with data you want to retrieve.

- **var key:** The name/names of the entity data entry you want to retrieve.

### Optional Arguments

- **string type:** type of data synchronization

- *"public"* - Synchronizes between the server and the client, and between the client and the server (required to be enabled in the options)

- *"local"* - It does not synchronize, it remains on the side on which it was given

- *"private"* - Assigns and synchronizes one value for a given key for all items

### Returns

This function returns a variable/tables containing the requested entity data, or false if the element/elements or the entity data does not exist.

### getAllEntityData

Click to collapse [-]
Shared

This function returns a table of all entity data of an element.

```
string exports.entityData:getAllEntityData(element/table theElement, [string type="public"])
```

### Required Arguments

- **element theElement:** This is the element/elements with data you want to retrieve.

### Optional Arguments

- **string type:** type of data synchronization

- *"public"*

- *"local"*

- *"private"*

- *"all"*

### Returns

If successful, returns a table with as keys the names of the entity data and as values the corresponding entity data values. Returns false in case of failure.

### hasEntityData

Click to collapse [-]
Shared

This function checks if an element has entity data available under a certain key.

```
boolean exports.entityData:hasEntityData(element/table theElement, var/table key, [string type="public"])
```

### Required Arguments

- **element theElement:** This is the element/elements with data you want to retrieve.

- **var key:** The name/names of the entity data entry you want to check for.

### Optional Arguments

- **string type:**type of data synchronization

- *"public"* - Synchronizes between the server and the client, and between the client and the server (required to be enabled in the options)

- *"local"* - It does not synchronize, it remains on the side on which it was given

- *"private"* - Assigns and synchronizes one value for a given key for all items

### Returns

This function returns true if the element contains entity data for key, or false if the element doesn't exist or there is no data associated with the key.

### setKeyFlag

Click to collapse [-]
Shared

This function imposes restrictions on the key which, if not satisfied, will not perform the entity data assignment

```
boolean exports.entityData:setKeyFlag(var key, table flag)
```

### Required Arguments

- **var key:** The name of the entity data entry you want to check for.

- **table flag:** A flag containing all the [restrictions key](https://wiki.multitheftauto.com/wiki/Resource:EntityData/restrictions_key)

### Returns

Returns true if the flag is set and false if the flag is not set on the key.

### createTransaction

Click to collapse [-]
Shared

This function creates instructions for the data transfer in the form of a transaction that must be accepted or canceled.

```
int exports.entityData:createTransaction()
```

### Returns

Returns the index of a new transaction created

### triggerTransaction

Click to collapse [-]
Shared

This function acceptance of the transaction for sending must be created beforehand, unless you send the instruction itself in the form of an array, then no transaction is needed.

```
string exports.entityData:triggerTransaction(int transaction/table transaction)
```

### Required Arguments

- **int transaction:** - The transaction number, if this value is provided, the data transfer will not be executed

- **table transaction:** - An table with the instruction to be executed to setEntityData

### Returns

Returns true on valid transaction other than false

### cancelTransaction

Click to collapse [-]
Shared

This feature will cancel the transaction and will not allow it to be submitted correctly.

```
boolean exports.entityData:cancelTransaction(int transaction)
```

### Required Arguments

- **int transaction:** - The transaction number, if this value is provided, the data transfer will not be executed immediately

### Returns

Returns true on valid transaction other than false
