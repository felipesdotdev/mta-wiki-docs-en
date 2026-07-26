---
doc_id: "mta-wiki:3400"
title: "FileWrite"
source_title: "FileWrite"
source_url: "https://wiki.multitheftauto.com/wiki/FileWrite"
revision_id: 78725
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:01.066172+00:00"
---

# FileWrite

Writes one or more strings to a given file, starting at the current read/write position. Advances the position over the number of bytes that were written.

## Syntax

```
int fileWrite ( file theFile, string string1 [, string string2, string string3 ...])
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[file](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1):write(...)*

### Required Arguments

- **theFile:** A handle to the file you wish to write to. The file must have been opened with write access, i.e. the file handle must be a result of [fileCreate](mta://scripting/shared/functions/filecreate.md) or [fileOpen](mta://scripting/shared/functions/fileopen.md) with the readonly parameter set to *false*.

- **string1:** The string to write.

### Optional Arguments

- You can provide any number of additional strings to write after **string1**. These will be written in the order in which they are specified.

### Returns

Returns the number of bytes successfully written to the file, returns *false* if invalid arguments were specified.

## Example

This example creates a text file and writes a string to it.

```
local fileHandle = fileCreate("test.txt")             -- attempt to create a new file
if fileHandle then                                    -- check if the creation succeeded
    fileWrite(fileHandle, "This is a test file!")     -- write a text line
    fileClose(fileHandle)                             -- close the file once you're done with it
end
```

Notice that you can't simply do fileWrite("test.txt", "File content"). Instead, file functions operate on a **file handle**, which is a special object representing an open file.

It is also important to remember to close a file after you've finished all your operations on it, especially if you've been writing to the file. If you don't close a file and your resource crashes, all changes to the file may be lost.

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

- [fileSetPos](mta://scripting/shared/functions/filesetpos.md)

- fileWrite
