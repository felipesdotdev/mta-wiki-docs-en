---
doc_id: "mta-wiki:8536"
title: "BitRRotate"
source_title: "BitRRotate"
source_url: "https://wiki.multitheftauto.com/wiki/BitRRotate"
revision_id: 46734
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:12:11.181919+00:00"
---

# BitRRotate

This functions performs a bitwise circular right-rotation on the integer **value** by integer **n** positions.
See [Bitwise operation](https://en.wikipedia.org/wiki/Bitwise_operation#Rotate_no_carry) for more details.

## Syntax

```
int bitRRotate ( int value, int n )
```

### Required arguments

- **value:** The value you want to perform the rotation on.

- **n:** The amount of positions to rotate the value by.

### Returns

Returns the circular right-rotated value as *integer*.

## Example

Click to collapse [-]
Client

This example adds the clientside command **/rightrotate [value] [positions = 1]**, which will print the result from the function bitRRotate.

```
function getNumberAsBitString(value)
    if type(value) ~= 'number' then
        return false
    else
        local binary = ''

        for field = 31, 0, -1 do
            binary = binary .. bitExtract(value, field)

            if field % 4 == 0 then
                binary = binary ..' '
            end
        end

        return binary
    end
end

addCommandHandler('rightrotate',
    function (command, value, positions)
        if type(value) ~= 'string' or value:len() == 0 then
            return outputChatBox('* Syntax: /rightrotate [value] [positions = 1]')
        end

        if type(positions) ~= 'string' or positions:len() == 0 then
            positions = 1
        end

        local result = bitRRotate(tonumber(value), tonumber(positions))
        local binary = getNumberAsBitString(result)

        outputChatBox('* Decimal: '.. result ..', Binary: '.. binary)
    end
)
```

If you trigger the command with **/rightrotate 0xFF0000 16** you will receive as response:

```
* Decimal: 255, Binary: 0000 0000 0000 0000 0000 0000 1111 1111
```

## See Also

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- bitRRotate

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
