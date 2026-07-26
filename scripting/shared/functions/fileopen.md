---
doc_id: "mta-wiki:3395"
title: "FileOpen"
source_title: "FileOpen"
source_url: "https://wiki.multitheftauto.com/wiki/FileOpen"
revision_id: 81446
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.6"]
generated_at: "2026-07-26T16:15:00.995417+00:00"
---

# FileOpen

Opens an existing file for reading and writing.

| [[{{{image}}}\|link=\|]] | Note: To prevent memory leaks, ensure each successful call to fileOpen has a matching call to fileClose . |
| --- | --- |
|  |  |

|  | Warning: As of 1.5.4 r10413 , this function will fail when trying to access a script file of another resource, even with general.ModifyOtherObjects rights granted, which uses a mysql connection through dbConnect when database_credentials_protection is enabled in the server configuration. Additionally, meta.xml will be un-writable and will always open in read-only mode. |
| --- | --- |
|  |  |

## Syntax

```
file fileOpen ( string filePath [, bool readOnly = false ])
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *The function will only attempt to open the file, it won't create it.*

**Method**: *[File](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1)(...)*

ADDED/UPDATED IN VERSION 1.5.6 [r11865](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=11865):

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This is a static function underneath the File class. Using **File(...)** to open a file will attempt to create the file, if it doesn't exist*

**Method**: *[File](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1).open(...)*

### Required Arguments

- **filePath:** The [filepath](mta://reference/misc/filepath.md) of the file in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is in, and 'path' is the path from the root directory of the resource to the file.

For example, if there is a file named 'coolObjects.txt' in the resource 'objectSearch', it can be opened from another resource this way: *fileOpen(":objectSearch/coolObjects.txt")*.

If the file is in the current resource, only the file path is necessary, e.g. *fileOpen("coolObjects.txt")*.

### Optional Arguments

- **readOnly:** By default, the file is opened with reading and writing access. You can specify *true* for this parameter if you only need reading access.

### Returns

If successful, returns a file handle for the file. Otherwise returns *false* (f.e. if the file doesn't exist).

## Example

This example opens the file test.txt that is in the root of the current resource, and outputs its contents to the console.

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

This example show how to append data to an existing file:

```
local hFile = fileOpen("test.txt")             -- attempt to open the file (read and write mode)
if hFile then                                  -- check if it was successfully opened
    fileSetPos( hFile, fileGetSize( hFile ) )  -- move position to the end of the file
    fileWrite(hFile, "hello" )                 -- append data
    fileFlush(hFile)                           -- Flush the appended data into the file.
    fileClose(hFile)                           -- close the file once we're done with it
else
    outputConsole("Unable to open test.txt")
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

- fileOpen

- [fileRead](mta://scripting/shared/functions/fileread.md)

- [fileRename](mta://scripting/shared/functions/filerename.md)

- [fileSetPos](mta://scripting/shared/functions/filesetpos.md)

- [fileWrite](mta://scripting/shared/functions/filewrite.md)
