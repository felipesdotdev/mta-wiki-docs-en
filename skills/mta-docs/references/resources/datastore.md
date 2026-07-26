---
doc_id: "mta-wiki:11942"
title: "Resource : Datastore"
source_title: "Resource:Datastore"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ADatastore"
revision_id: 68091
language: "en"
categories: ["Resource"]
---

# Resource : Datastore

DataStore allows you to store data (string/table) to a specific key in the database table. All you have to do is enter your database information in settings.lua('sqlite' or 'mysql') and once connected you can use the datastore exported functions to store and/or get data from the db table.
Very useful for beginner developers who lack experience with MySQL/SQLite.

## Overview

Fairly easy to use.

## Exported functions

#### getDatabase

Click to collapse [-]
Server

This function returns the database, if there is one at least.

```
exports['datastore']:getDatabase()
```

### Returns

Returns the database connection if one was connected.

#### storeData

Click to collapse [-]
Server

This function stores data into a specific key in the connected database table.

```
exports['datastore']:storeData(string key, string/table value, string theTable)
```

### Required Arguments

- **key**: Key that the data is gonna be stored in

- **value**: Data to be stored in the key **(tables are automatically stored as a string)**

### Optional Arguments

- **theTable**: the table that you're wanting to store the data in **(the data is stored in the default table if you didn't enter the specific table)** - only works from version 1.1

### Returns

Returns true if the data was stored successfully.

#### getData

Click to collapse [-]
Server

This function gets the data stored in a specific key.

```
exports['datastore']:getData(string key, string theTable)
```

### Required Arguments

- **key**: Key that you would like to receive the data of.

### Optional Arguments

- **theTable**: the table that you're wanting to get the data from **(if no table was entered here then it automatically looks in the default table)** - only works from version 1.1

### Returns

Returns the data that was stored in the key if found. *(converted tables to strings are automatically returned as tables)*

#### getAllData

Click to collapse [-]
Server

This function gets all the keys and data stored in the connected database table.

```
exports['datastore']:getAllData(string theTable)
```

### Optional Arguments

- **theTable**: the table that you're wanting to get the data from **(if no table was entered here then it automatically looks in the default table)** - only works from version 1.1

### Returns

- **Version 1.0**: Returns table of all the data received from the connected database table. Key names being the index value, value being the data of the key.

- **From Version 1.1 and forward**: Returns table of all the data received from the selected database table (default table if none was entered). Indexed numerically, value being a table of the key and value

#### removeData

Click to collapse [-]
Server

This function removes the data stored in a specific key. - Only works from version 1.1

```
exports['datastore']:removeData(string key, string theTable)
```

### Required Arguments

- **key**: Key that you would like to remove the data of.

### Optional Arguments

- **theTable**: the table that you're wanting to remove the data from **(if no table was entered here then it automatically removes from the default table)**

### Returns

Returns true if successful

## See Also

**Resource:** [https://community.multitheftauto.com/?p=resources&s=details&id=17541](https://community.multitheftauto.com/?p=resources&s=details&id=17541)
