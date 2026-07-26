---
doc_id: "mta-wiki:7093"
title: "BitNot"
source_title: "BitNot"
source_url: "https://wiki.multitheftauto.com/wiki/BitNot"
revision_id: 45173
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.3.2"]
---

# BitNot

This function performs a bitwise NOT on an (unsigned) 32-bit [integer](mta://reference/misc/int.md). See [Bitwise operation](http://en.wikipedia.org/wiki/Bitwise_operation#NOT) for more details.

## Syntax

```
uint bitNot ( uint var )
```

### Required arguments

- **var:** The value you want to perform a bitwise NOT on

### Returns

Returns the value on which the operation has been performed.

## Example

Click to collapse [-]
server

--In this example we make a command which you can do a bitNot operator

```
function bitnot(thePlayer,cmd,value)

    outputChatBox(bitNot(value),thePlayer)

end

addCommandHandler("bitnot",bitnotFunc)
```

## See Also

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- bitNot

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
