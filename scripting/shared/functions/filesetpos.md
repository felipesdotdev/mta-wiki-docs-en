---
doc_id: "mta-wiki:3398"
title: "FileSetPos"
source_title: "FileSetPos"
source_url: "https://wiki.multitheftauto.com/wiki/FileSetPos"
revision_id: 78723
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:01.048530+00:00"
---

# FileSetPos

Sets the current read/write position in the file.

## Syntax

```
int fileSetPos ( file theFile, int offset )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[file](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1):setPos(...)*

**Variable**: *.pos*

**Counterpart**: *[fileGetPos](mta://scripting/shared/functions/filegetpos.md)*

### Required Arguments

- **theFile:** The file handle of which you want to change the read/write position.

- **offset:** The new position. This is the number of bytes from the beginning of the file. If this value is larger than the file size, it is limited to 52,428,800 bytes (50 MB).

### Returns

Returns where the offset was actually set at. I.e. if **offset** was past the end of the file, it will be set at the end of the file, and this position will be returned. Returns *false* in case of failure (e.g. the specified file handle is invalid).

## Example

This example opens a binary file and prints the value of the byte at position 8 to the console.

```
local hFile = fileOpen("test.dat")          -- attempt to open the file
if hFile then                               -- check if it succeeded
    fileSetPos(hFile, 8)                    -- set the read/write position
    local readByte = fileRead(hFile, 1)     -- read one byte from this position
    outputConsole("Byte at position 8 = " .. string.byte(readByte))     -- output it
    fileClose(hFile)                        -- close the file
else
    outputConsole("Unable to open test.dat")
end
```

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

- [fileRead](mta://scripting/shared/functions/fileread.md)

- [fileRename](mta://scripting/shared/functions/filerename.md)

- fileSetPos

- [fileWrite](mta://scripting/shared/functions/filewrite.md)
