---
doc_id: "mta-wiki:9320"
title: "Importer"
source_title: "Importer"
source_url: "https://wiki.multitheftauto.com/wiki/Importer"
revision_id: 82619
language: "en"
categories: ["Useful_Classes"]
generated_at: "2026-07-26T16:15:52.856716+00:00"
---

# Importer

This function allow to import functions from other scripts.
Author: CrosRoad95
Contact discord: mtasa.com/discord

## Requirements

OOP turn on

## Code

```
importer={}
importer.__index = importer
function importer:import(functionsToImport)
	assert(functionsToImport:len()>0,"specify what you want to import")
	local impr = {}
	setmetatable(impr,importer)
	impr.scripts=functionsToImport
	return impr
end
function importer:from(script)
	local res=getResourceFromName(script)
	assert(res,"script doesnt exists")
	local functions=getResourceExportedFunctions(res)
	assert(#functions>0,"script must contain exports")
	local importThis={}
	if(self.scripts=="*")then
		importThis=functions
	else
		local tbsplit=split(self.scripts,",")
		for i,v in ipairs(functions)do
			for ii,vv in ipairs(tbsplit)do
				if(string.find(v,vv))then
					table.insert(importThis,v)
				end
			end
		end
	end
	for i,v in ipairs(importThis)do
		_G[v]=function(...)
			return call(res,v,...)
		end
	end
end
function import(...)
	return importer:import(...)
end
```

## Example 1

Import specified functions

```
import("function1,function2"):from("myScript") -- import functions "function1" and "function2" from script "myScript"
-- now "function1()" is same as "exports.myScript:function()"
function1("test")
```

## Example 2

Import functions which contain string

```
import("function,otherFunctions"):from("myScript") -- import functions contain "function" in name, in this example import "function1" and "function2" from script "myScript"
function1("test")
```

## Example 3

Import all functions

```
import("*"):from("myScript") -- import all functions, in this example import "function1" and "function2" from script "myScript"
function1("test")
```

## See Also

- [Singleton](mta://scripting/shared/classes/singleton.md) » This class allows to restrict the instantiation of a specific class to one object.

- [CThread](mta://scripting/shared/classes/cthread.md) » This class represents a simple coroutine manager which can be used to limit method calls / loop.

- Importer » This class make easy to use exported functions.

- [Observable](mta://scripting/shared/classes/observable.md) » Observable variables. Call function on variable value change.

- [MatrixPOP](mta://scripting/shared/classes/matrixpop.md) » This class allows to use simple matrix without using MTA's OOP functions
