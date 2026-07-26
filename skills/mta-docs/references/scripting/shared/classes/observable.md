---
doc_id: "mta-wiki:12505"
title: "Observable"
source_title: "Observable"
source_url: "https://wiki.multitheftauto.com/wiki/Observable"
revision_id: 78819
language: "en"
categories: ["Useful_Classes"]
---

# Observable

This class allows you to watch for variables changes.

Call observable variable to push new state.

Author: CrosRoad95
Contact discord: mtasa.com/discord

## Requirements

OOP turn on

## Code

```
observable = {}

function observable:onChange(callback)
	self.callback = callback
end

function observable:__tostring()
	return self.value
end

function observable:__call(newState)
	if(self.value == newState)then
		return false
	end
	local oldValue = self.value;
	self.value = newState;
	if(self.callback)then
		self.callback(oldValue, self.value)
	end
	return true;
end

function observable:create(defaultValue)
	local t = { value = defaultValue, observators = {} }
	setmetatable(t, self)
	self.__index = self
	return t
end

function watch(callback, ...)
	for i,v in ipairs({...})do
		v:onChange(function(old, new) 
			if(callback)then
				callback(i, old, new)
			end
		end)
	end
end
```

## Example 1

How it works

```
a = observable:create("asdf") -- "asdf" is a default value.
b = observable:create(10)

watch(function(index, prvValue, newValue) -- called every time observable value has change.
	print("index",index, "change", prvValue, "=> ",newValue)
end, a, b) -- pass variables you want to watch

a(20) -- index 1 change asdf => 20
b(30) -- index 2 change 10 => 30
a("aaa") -- index 1 change 20 => aaa

print("value:", a) -- in this case it will print "aaa"
```

## See Also

- [Singleton](mta://scripting/shared/classes/singleton.md) » This class allows to restrict the instantiation of a specific class to one object.

- [CThread](mta://scripting/shared/classes/cthread.md) » This class represents a simple coroutine manager which can be used to limit method calls / loop.

- [Importer](mta://scripting/shared/classes/importer.md) » This class make easy to use exported functions.

- Observable » Observable variables. Call function on variable value change.

- [MatrixPOP](mta://scripting/shared/classes/matrixpop.md) » This class allows to use simple matrix without using MTA's OOP functions
