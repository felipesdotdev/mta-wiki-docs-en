---
doc_id: "mta-wiki:3399"
title: "FileRead"
source_title: "FileRead"
source_url: "https://wiki.multitheftauto.com/wiki/FileRead"
revision_id: 80013
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# FileRead

Reads the specified number of bytes from the given file starting at its current read/write position, and returns them as a string.

## Syntax

```
string fileRead ( file theFile, int count )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[file](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1):read(...)*

### Required Arguments

- **theFile:** A handle to the file you wish to read from. Use [fileOpen](mta://scripting/shared/functions/fileopen.md) to obtain this handle.

- **count:** The number of bytes you wish to read.

### Returns

Returns the bytes that were read in a string. Note that this string might not contain as many bytes as you specified if an error occured, i.e. end of file.

## Example

This example opens the file test.txt and outputs its contents to the console.

```
function readFile(path)
    local file = fileOpen(path) -- attempt to open the file
    if not file then
        return false -- stop function on failure
    end
    local count = fileGetSize(file) -- get file's total size
    local data = fileRead(file, count) -- read whole file
    fileClose(file) -- close the file once we're done with it
    outputConsole(data) -- output code in console
end

addCommandHandler("readfile",function(cmd,fileName) -- add command to test this function
    readFile(fileName) -- execute the function
end)
```

[fileOpen](mta://scripting/shared/functions/fileopen.md) sets the read/write position to the beginning of the file.
[fileGetSize](mta://scripting/shared/functions/filegetsize.md) gets the total size in bytes of given file.

## See Also

- [fileClose](mta://scripting/shared/functions/fileclose.md)

- [fileCopy](mta://scripting/shared/functions/filecopy.md)

- [fileCreate](mta://scripting/shared/functions/filecreate.md)

- [fileDelete](mta://scripting/shared/functions/filedelete.md)

- [fileExists](mta://scripting/shared/functions/fileexists.md)

- [fileFlush](mta://scripting/shared/functions/fileflush.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21938](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21938):

- [fileGetContents](mta://scripting/shared/functions/filegetcontents.md)

ADDED/UPDATED IN VERSION 1.6.0 [r23289](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23289):

- [fileGetHash](mta://scripting/shared/functions/filegethash.md)

- [fileGetPath](mta://scripting/shared/functions/filegetpath.md)

- [fileGetPos](mta://scripting/shared/functions/filegetpos.md)

- [fileGetSize](mta://scripting/shared/functions/filegetsize.md)

- [fileIsEOF](mta://scripting/shared/functions/fileiseof.md)

- [fileOpen](mta://scripting/shared/functions/fileopen.md)

- fileRead

- [fileRename](mta://scripting/shared/functions/filerename.md)

- [fileSetPos](mta://scripting/shared/functions/filesetpos.md)

- [fileWrite](mta://scripting/shared/functions/filewrite.md)
