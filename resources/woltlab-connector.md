---
doc_id: "mta-wiki:6823"
title: "Resource : Woltlab-Connector"
source_title: "Resource:Woltlab-Connector"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AWoltlab-Connector"
revision_id: 33733
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:17:14.758418+00:00"
---

# Resource : Woltlab-Connector

**Current Version: 1.1.2**

This is a library, created by xthepr0mise, which allows you to connect to your forum software easily.
It uses the MySQL-Plugin to connect to the database and includes a full log which documents nearly every (woltlab_)function called by the user.

## Functions

### Connection

#### woltlab_connect

Click to collapse [-]
Server

## Syntax

```
bool woltlab_connect ( dbHost, dbUsername, dbPasswort, dbName )
```

## Required Arguments

- **dbHost**: The IP-Address of the database

- **dbUsername**: The username of the database

- **dbPasswort**: The password of the database

- **dbName**: The name of the database

## Returns

Returns **true** if it connected successfully else **false**

```
-- TODO
```

#### woltlab_disconnect

Click to collapse [-]
Server

## Syntax

```
bool woltlab_disconnect ( )
```

## Required Arguments

- **None**

## Returns

Returns **true** if it disconnected successfully else **false**

```
-- TODO
```

### User-Functions

#### woltlab_checkPassword

Click to collapse [-]
Server

## Syntax

```
bool woltlab_checkPassword ( username, password )
```

## Required Arguments

- **username**: The username of the player you want to check

- **password**: The password he entered (encrypted)

## Returns

Returns **true** if the password is right else **false**

```
-- TODO
```

#### woltlab_getUserID

Click to collapse [-]
Server

## Syntax

```
int woltlab_getUserID ( username )
```

## Required Arguments

- **username**: The username of the player whose ID you want to get

## Returns

Returns **int ID** or **false** if the user does not exist

```
-- TODO
```

#### woltlab_addUser

Click to collapse [-]
Server

## Syntax

```
bool woltlab_addUser ( username, email, password )
```

## Required Arguments

- **username**: The username of the player you want to add

- **email**: His e-mail address

- **password**: His password (encrypted)

## Returns

Returns **true** if the user got created or **false**

```
-- TODO
```

#### woltlab_userExists

Click to collapse [-]
Server

## Syntax

```
bool woltlab_userExists ( username )
```

## Required Arguments

- **username**: The username of the player you want to check

## Returns

Returns **true** or **false**

```
-- TODO
```

### Board-Functions

#### woltlab_getBoardID

Click to collapse [-]
Server

## Syntax

```
int woltlab_getBoardID ( title )
```

## Required Arguments

- **title**: The title of the board whose ID you want to get

## Returns

Returns **int ID** or **false** if the board does not exist

```
-- TODO
```

#### woltlab_getBoardTitle

Click to collapse [-]
Server

## Syntax

```
string woltlab_getBoardTitle ( id )
```

## Required Arguments

- **id**: The ID of the board whose title you want to get

## Returns

Returns **string title** or **false** if the board does not exist

```
-- TODO
```

#### woltlab_addThread

Click to collapse [-]
Server

## Syntax

```
bool woltlab_addThread ( username, boardID, prefix, head, description, [registered] )
```

## Required Arguments

- **username**: The username of the player which creates the thread

- **boardID**: The ID of the board in which the thread should be created

- **prefix**: The prefix of the thread

- **head**: The title of the thread

- **description**: The content of the thread

## Optional Arguments

- **registered**: A bool whether the user is registered in the forum or not

## Returns

Returns **true** if the thread got created or **false**

```
-- TODO
```

### Group-Functions

#### woltlab_groupExists

Click to collapse [-]
Server

## Syntax

```
bool woltlab_groupExists ( ID )
```

## Required Arguments

- **ID**: The ID of the group

## Returns

Returns **true** if the group exists or **false**

```
-- TODO
```

#### woltlab_isUserInGroup

Click to collapse [-]
Server

## Syntax

```
bool woltlab_isUserInGroup ( username, ID )
```

## Required Arguments

- **username**: The username of the player you want to check

- **ID**: The ID of the group

## Returns

Returns **true** if he is in the group or **false**

```
-- TODO
```

#### woltlab_getGroupID

Click to collapse [-]
Server

## Syntax

```
bool woltlab_getGroupID ( title )
```

## Required Arguments

- **title**: The title of the group

## Returns

Returns **int ID** of the group or **false**

```
-- TODO
```

#### woltlab_getGroupTitle

Click to collapse [-]
Server

## Syntax

```
bool woltlab_getGroupTitle ( ID )
```

## Required Arguments

- **ID**: The ID of the group

## Returns

Returns **string title** of the group or **false**

```
-- TODO
```

#### woltlab_addUserToGroup

Click to collapse [-]
Server

## Syntax

```
bool woltlab_addUserToGroup ( username, groupID )
```

## Required Arguments

- **username**: The username of the player

- **groupID**: The ID of the group

## Returns

Returns **true** if he got added or **false**

```
-- TODO
```

#### woltlab_removeUserFromGroup

Click to collapse [-]
Server

## Syntax

```
bool woltlab_removeUserFromGroup ( username, groupID )
```

## Required Arguments

- **username**: The username of the player

- **groupID**: The ID of the group

## Returns

Returns **true** if he got removed or **false**

```
-- TODO
```

## Usage

### Option 1

```
exports.woltlab:FUNCTION ( PARAMETERS )
```

### Option 2

```
exports:['woltlab']:FUNCTION ( PARAMETERS )
```

## Examples

### Simple password-checking

Click to collapse [-]
Server

```
exports.woltlab:woltlab_connect ( "127.0.0.1", "root", "", "wcf" )
local login = exports.woltlab:woltlab_checkPassword ( "xthepr0mise", "test" )
if login == true then
    outputChatBox("Your password is right!")
else
    outputChatBox("Your password is wrong!")
end
exports.woltlab:woltlab_disconnect()
```

## Known Bugs

- **none**
