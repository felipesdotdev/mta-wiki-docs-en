---
doc_id: "mta-wiki:8256"
title: "Singleton"
source_title: "Singleton"
source_url: "https://wiki.multitheftauto.com/wiki/Singleton"
revision_id: 78817
language: "en"
categories: ["Useful_Classes"]
---

# Singleton

This class allows you to restrict the instantiation of a specific class to one object.

## Requirements

sbx320's classLib, can be found Here[[1]](https://github.com/sbx320/lua_utils/blob/master/classlib.lua)

OOP on

## Code

```
Singleton = {}

function Singleton:getSingleton(...)
	if not self.ms_Instance then
		self.ms_Instance = self:new(...)
	end
	return self.ms_Instance
end

function Singleton:new(...)
	self.new = function() end
	local inst = new(self, ...)
	self.ms_Instance = inst
	return inst
end

function Singleton:isInstantiated()
	return self.ms_Instance ~= nil
end

function Singleton:virtual_destructor()
	for k, v in pairs(super(self)) do
		v.ms_Instance = nil
		v.new = Singleton.new
	end
end
```

**Call class methods by newest instance**

## Example

```
-- DEFINE CLASS
TestClass = inherit(Singleton)

function TestClass:run()
   -- DO SOMETHING
end

TestClass:getSingleton():run()
```

## See Also

- Singleton » This class allows to restrict the instantiation of a specific class to one object.

- [CThread](mta://scripting/shared/classes/cthread.md) » This class represents a simple coroutine manager which can be used to limit method calls / loop.

- [Importer](mta://scripting/shared/classes/importer.md) » This class make easy to use exported functions.

- [Observable](mta://scripting/shared/classes/observable.md) » Observable variables. Call function on variable value change.

- [MatrixPOP](mta://scripting/shared/classes/matrixpop.md) » This class allows to use simple matrix without using MTA's OOP functions
