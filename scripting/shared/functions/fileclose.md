---
doc_id: "mta-wiki:3402"
title: "FileClose"
source_title: "FileClose"
source_url: "https://wiki.multitheftauto.com/wiki/FileClose"
revision_id: 78692
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:00.766651+00:00"
---

# FileClose

Closes a file handle obtained by [fileCreate](mta://scripting/shared/functions/filecreate.md) or [fileOpen](mta://scripting/shared/functions/fileopen.md).

## Syntax

```
bool fileClose ( file theFile )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[file](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1):close(...)*

### Required Arguments

- **theFile:** The file handle to close.

### Returns

Returns *true* if successful, *false* otherwise.

## Example

This example creates a text file and writes a string to it.

```
local newFile = fileCreate("test.txt")                -- attempt to create a new file
if newFile then                                       -- check if the creation succeeded
    fileWrite(newFile, "This is a test file!")        -- write a text line
    fileClose(newFile)                                -- close the file once you're done with it
end
```

It is important to remember to close a file after you've finished all your operations on it, especially if you've been writing to the file. If you don't close a file and your resource crashes, all changes to the file may be lost.

## See Also

- fileClose

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

- [fileSetPos](mta://scripting/shared/functions/filesetpos.md)

- [fileWrite](mta://scripting/shared/functions/filewrite.md)
