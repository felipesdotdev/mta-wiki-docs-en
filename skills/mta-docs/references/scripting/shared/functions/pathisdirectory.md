---
doc_id: "mta-wiki:14310"
title: "PathIsDirectory"
source_title: "PathIsDirectory"
source_url: "https://wiki.multitheftauto.com/wiki/PathIsDirectory"
revision_id: 79576
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# PathIsDirectory

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470))

Checks if a specified path points to a directory.

## Syntax

```
bool pathIsDirectory ( string path )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[path](https://wiki.multitheftauto.com/index.php?title=Path&action=edit&redlink=1):isDirectory(...)*

### Required Arguments

- **path:** A [string](mta://reference/misc/string.md) containing a path you want to check against

### Returns

Returns **[true](mta://reference/misc/boolean.md)** if the path points to a directory, **[false](mta://reference/misc/boolean.md)** otherwise.

## Example

Click to collapse [-]
Shared

This example lists entire structure of a folder

```
function string.startsWith(str, start)
    return string.sub(str, 1, #start) == start
end

function string.repetition(what, n)
    local out = ''
    for i=1, n do
        out = out..what
    end
    return out
end

local function getStructure(thePath)
    if thePath:startsWith('/') then
        thePath = thePath:sub(2)
    end

    local structure = {}
    for _, entry in ipairs(pathListDir(thePath)) do
        local entryPath = thePath..'/'..entry
        if pathIsDirectory(entryPath) then
            structure[entry] = getStructure(entryPath)
        elseif pathIsFile(entryPath) then
            structure[entry] = false
        end
    end
    return structure
end

local function printStructure(struct, tab)
    tab = tab or 0
    for entry, isDir in pairs(struct) do
        iprint(string.repetition(' ',tab)..'- '..entry)
        if isDir then
            printStructure(isDir, tab + 2)
        end
    end
end

printStructure(getStructure('.'))
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [pathListDir](mta://scripting/shared/functions/pathlistdir.md)

- [pathIsFile](mta://scripting/shared/functions/pathisfile.md)

- pathIsDirectory
