---
doc_id: "mta-wiki:3401"
title: "FileFlush"
source_title: "FileFlush"
source_url: "https://wiki.multitheftauto.com/wiki/FileFlush"
revision_id: 78702
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# FileFlush

Forces pending disk writes to be executed. [fileWrite](mta://scripting/shared/functions/filewrite.md) doesn't directly write to the hard disk but places the data in a temporary buffer; only when there is enough data in the buffer it is actually written to disk. Call this function if you need the data written right now without closing the file. This is useful for log files that might want to be read while the resource is still executing. fileFlush can be called after each log entry is written. Without this, the file may appear empty or outdated to the user.

## Syntax

```
bool fileFlush ( file theFile )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[file](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1):flush(...)*

### Required Arguments

- **theFile:** The file handle of the file you wish to flush.

### Returns

Returns *true* if succeeded, *false* in case of failure (e.g. the file handle is invalid).

## Example

```
local fileHandle = fileCreate("test.txt")
if fileHandle then
    fileWrite(fileHandle, "Line 1")
    fileFlush(fileHandle)
    -- ... further writing operations
    fileClose(fileHandle)
end
```

Note that [fileClose](mta://scripting/shared/functions/fileclose.md) automatically flushes the file.

## See Also

- [fileClose](mta://scripting/shared/functions/fileclose.md)

- [fileCopy](mta://scripting/shared/functions/filecopy.md)

- [fileCreate](mta://scripting/shared/functions/filecreate.md)

- [fileDelete](mta://scripting/shared/functions/filedelete.md)

- [fileExists](mta://scripting/shared/functions/fileexists.md)

- fileFlush

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
