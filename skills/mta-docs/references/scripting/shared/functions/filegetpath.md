---
doc_id: "mta-wiki:8421"
title: "FileGetPath"
source_title: "FileGetPath"
source_url: "https://wiki.multitheftauto.com/wiki/FileGetPath"
revision_id: 78707
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.3"]
---

# FileGetPath

This function retrieves the path of the given file.

## Syntax

```
string fileGetPath ( file theFile )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[file](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1):getPath(...)*

**Variable**: *.path*

### Required Arguments

- **theFile:** The file you want to get the path.

### Returns

Returns a *string* representing the file path, *false* if invalid file was provided.

## Example

Click to collapse [-]
Server Example 1

```
local newFile = fileCreate("test.txt")                -- attempt to create a new file
if (newFile) then                                       -- check if the creation succeeded
    local path = fileGetPath(newFile)
    outputChatBox("New file created at: "..path, root, 0, 255, 0)
    fileClose(newFile)                                -- close the file once you're done with it
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

- fileGetPath

- [fileGetPos](mta://scripting/shared/functions/filegetpos.md)

- [fileGetSize](mta://scripting/shared/functions/filegetsize.md)

- [fileIsEOF](mta://scripting/shared/functions/fileiseof.md)

- [fileOpen](mta://scripting/shared/functions/fileopen.md)

- [fileRead](mta://scripting/shared/functions/fileread.md)

- [fileRename](mta://scripting/shared/functions/filerename.md)

- [fileSetPos](mta://scripting/shared/functions/filesetpos.md)

- [fileWrite](mta://scripting/shared/functions/filewrite.md)
