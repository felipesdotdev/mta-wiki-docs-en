---
doc_id: "mta-wiki:3396"
title: "FileIsEOF"
source_title: "FileIsEOF"
source_url: "https://wiki.multitheftauto.com/wiki/FileIsEOF"
revision_id: 78713
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:00.972629+00:00"
---

# FileIsEOF

Checks if the file position is at the end of the file.

| [[{{{image}}}\|link=\|]] | Note: Due to underlying C API restrictions this function may return false until an attempt to read further than the end of the file is made. |
| --- | --- |
|  |  |

## Syntax

```
bool fileIsEOF ( file theFile )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[file](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1):isEOF(...)*

**Variable**: *.eof*

### Required Arguments

- **theFile:** A handle to the file you wish to check.

### Returns

Returns *true* if the file position of the specified file is at the end of the file, *false* otherwise.

## Example

This example opens the file test.txt and outputs its contents to the console.

```
local hFile = fileOpen("test.txt", true)       -- attempt to open the file (read only)
if hFile then                                  -- check if it was successfully opened
    local buffer
    while not fileIsEOF(hFile) do              -- as long as we're not at the end of the file...
        buffer = fileRead(hFile, 500)          -- ... read the next 500 bytes...
        outputConsole(buffer)                  -- ... and output them to the console
    end
    fileClose(hFile)                           -- close the file once we're done with it
else
    outputConsole("Unable to open test.txt")
end
```

When you open a file, its file position is set to the beginning of the file. Each call to [fileRead](mta://scripting/shared/functions/fileread.md) or [fileWrite](mta://scripting/shared/functions/filewrite.md) moves the position ahead by the amount of bytes that were read/written. This way, by using *fileIsEOF* you can check if you've passed through the whole file.

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

- fileIsEOF

- [fileOpen](mta://scripting/shared/functions/fileopen.md)

- [fileRead](mta://scripting/shared/functions/fileread.md)

- [fileRename](mta://scripting/shared/functions/filerename.md)

- [fileSetPos](mta://scripting/shared/functions/filesetpos.md)

- [fileWrite](mta://scripting/shared/functions/filewrite.md)
