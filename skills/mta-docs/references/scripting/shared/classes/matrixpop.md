---
doc_id: "mta-wiki:13601"
title: "MatrixPOP"
source_title: "MatrixPOP"
source_url: "https://wiki.multitheftauto.com/wiki/MatrixPOP"
revision_id: 78820
language: "en"
categories: ["Useful_Classes"]
---

# MatrixPOP

This class allows you to handle matrixes without using MTA's OOP functions  

This class is called POP because it doesn't use any OOP functions while keeping Lua's class structure.

## Syntax

```
MatrixPOP MatrixPOP( element eheElement )
```

### Required Arguments

- **theElement:** The [element](mta://reference/misc/element.md) which you wish to retrieve the [matrix](mta://reference/misc/matrix.md) for.

### Returns

Returns a matrix class  

Returns *false* if the element is not streamed in, and not a [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle), [ped](https://wiki.multitheftauto.com/index.php?search=ped) or [object](https://wiki.multitheftauto.com/index.php?search=object).

## Code

```
MatrixPOP = setmetatable({},{
    __metatable = 'MatrixPOP',
    __call = function(self,ply)
        local matrixObj = {}
        setmetatable(matrixObj, self)
        self.__index = self
        
        if not isElement(ply) or (
            getElementType(ply) ~= 'player' and
            getElementType(ply) ~= 'vehicle' and
            getElementType(ply) ~= 'object'
        ) then return false end

        matrixObj.matrix = getElementMatrix(ply)
        matrixObj.rotation = { getElementRotation(ply) }

        return matrixObj
    end
})
function MatrixPOP:getRotation()
    if not self then return false end
    return Vector3(self.rotation[1],self.rotation[2],self.rotation[3])
end
function MatrixPOP:getLeft()
    if not self then return false end
    local matrix = self.matrix[1]
    return Vector4(matrix[1], matrix[2], matrix[3], 1)
end
function MatrixPOP:getForward()
    if not self then return false end
    local matrix = self.matrix[2]
    return Vector4(matrix[1], matrix[2], matrix[3], 1)
end
function MatrixPOP:getUp()
    if not self then return false end
    local matrix = self.matrix[3]
    return Vector4(matrix[1], matrix[2], matrix[3], 1)
end
function MatrixPOP:getPosition()
    if not self then return false end
    local matrix = self.matrix[4]
    return Vector4(matrix[1], matrix[2], matrix[3], 1)
end
function MatrixPOP:__tostring()
    local matrix = self.matrix
    local m1 = matrix[1]
    local m2 = matrix[2]
    local m3 = matrix[3]
    local m4 = matrix[4]
    m1 = ('{ %s, %s, %s }'):format(m1[1],m1[2],m1[3])
    m2 = ('{ %s, %s, %s }'):format(m2[1],m2[2],m2[3])
    m3 = ('{ %s, %s, %s }'):format(m3[1],m3[2],m3[3])
    m4 = ('{ %s, %s, %s }'):format(m4[1],m4[2],m4[3])

    return ('MatrixPOP: {\n%s,\n%s,\n%s,\n%s\n}'):format(m1,m2,m3,m4)
end
collectgarbage('setpause',100)
```

## Example

Transform player's matrix into MatrixPOP

Click to collapse [-]
Example

```
addEventHandler('onPlayerJoin',root,function()
    local matrix = MatrixPOP(source)
    local position = matrix:getPosition()
    outputChatBox(('Your coordinates are: %s, %s, %s'):format(position.x, position.y, position.z)
end)
```

## See Also

- [Singleton](mta://scripting/shared/classes/singleton.md) » This class allows to restrict the instantiation of a specific class to one object.

- [CThread](mta://scripting/shared/classes/cthread.md) » This class represents a simple coroutine manager which can be used to limit method calls / loop.

- [Importer](mta://scripting/shared/classes/importer.md) » This class make easy to use exported functions.

- [Observable](mta://scripting/shared/classes/observable.md) » Observable variables. Call function on variable value change.

- MatrixPOP » This class allows to use simple matrix without using MTA's OOP functions
