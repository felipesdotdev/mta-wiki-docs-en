---
doc_id: "mta-wiki:14306"
title: "PathListDir"
source_title: "PathListDir"
source_url: "https://wiki.multitheftauto.com/wiki/PathListDir"
revision_id: 81965
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:28.014565+00:00"
---

# PathListDir

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

Reads a specified directory and returns all entries inside of it. These entries can be file or folder names.

| [[{{{image}}}\|link=\|]] | Note: Listing other resource directory can be done by passing ":resourceName/." For listing current resource (the one where code is executed), you can pass either "" or ":currentResourceName/." (preferably use first approach, because the latter will require removing this part, once result is ready) |
| --- | --- |
|  |  |

## Syntax

```
table pathListDir ( string path )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[path](https://wiki.multitheftauto.com/index.php?title=Path&action=edit&redlink=1):listDir(...)*

### Required Arguments

- **path:** A [string](mta://reference/misc/string.md) containing a path you want to get entries from

### Returns

Returns [table](mta://reference/misc/table.md) with all entries in a specified directory.

## Example

Click to collapse [-]
Client

This example loads all models from a certain directory

```
-- from https://gist.github.com/kgriffs/124aae3ac80eefe57199451b823c24ec
local function stringEndsWith(str, ending)
    return ending == "" or str:sub(-#ending) == ending
end

-- get all files from a models directory that exists in the resource root folder (resources/ResourceName)
-- and load them into the game
addEventHandler('onClientResourceStart', resourceRoot, function()
    local entries = pathListDir('models') or {}
    for _, fileOrFolder in ipairs(entries) do
        if pathIsFile(fileOrFolder) then
            local file = fileOrFolder
            local modelName = tonumber(file:sub(1, -5))
            if modelName then
                -- the full path to the file
                local filePath = 'models/'..file

                if stringEndsWith(file, '.col') then
                    local colData = engineLoadCOL(filePath)
                    if colData then
                        engineReplaceCOL(colData, modelName)
                    end
                end
                if stringEndsWith(file, '.txd') then
                    local txdData = engineLoadTXD(filePath)
                    if txdData then
                        engineImportTXD(txdData, modelName)
                    end
                end
                if stringEndsWith(file, '.dff') then
                    local dffData = engineLoadDFF(filePath)
                    if dffData then
                        engineReplaceModel(dffData, modelName)
                    end
                end
            end
        end
    end
end, false)
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- pathListDir

- [pathIsFile](mta://scripting/shared/functions/pathisfile.md)

- [pathIsDirectory](mta://scripting/shared/functions/pathisdirectory.md)
