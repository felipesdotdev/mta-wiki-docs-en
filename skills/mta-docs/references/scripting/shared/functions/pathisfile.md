---
doc_id: "mta-wiki:14308"
title: "PathIsFile"
source_title: "PathIsFile"
source_url: "https://wiki.multitheftauto.com/wiki/PathIsFile"
revision_id: 79575
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# PathIsFile

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470))

Checks if a specified path points to a file.

## Syntax

```
bool pathIsFile ( string path )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[path](https://wiki.multitheftauto.com/index.php?title=Path&action=edit&redlink=1):isFile(...)*

### Required Arguments

- **path:** A [string](mta://reference/misc/string.md) containing a path you want to check against

### Returns

Returns **[true](mta://reference/misc/boolean.md)** if the path points to a file, **[false](mta://reference/misc/boolean.md)** otherwise.

## Example

Click to collapse [-]
Shared

This example lists all files in a directory

```
local files = {}

for _,entry in ipairs(pathListDir('.')) do
    if pathIsFile(entry) then
        table.insert(files, entry)
    end
end

iprint('Files:')
for _,file in ipairs(files) do
    iprint(' - '..file)
end
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [pathListDir](mta://scripting/shared/functions/pathlistdir.md)

- pathIsFile

- [pathIsDirectory](mta://scripting/shared/functions/pathisdirectory.md)
