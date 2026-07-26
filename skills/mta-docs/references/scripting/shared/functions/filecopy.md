---
doc_id: "mta-wiki:6747"
title: "FileCopy"
source_title: "FileCopy"
source_url: "https://wiki.multitheftauto.com/wiki/FileCopy"
revision_id: 81447
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# FileCopy

This function copies a file.

| [[{{{image}}}\|link=\|]] | Tip: If you do not want to share the content of the created file with other servers, prepend the file path with @ (See filepath for more information) |
| --- | --- |
|  |  |

## Syntax

```
bool fileCopy ( string filePath, string copyToFilePath [, bool overwrite = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the File class.*

**Method**: *[File](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1).copy(...)*

### Required Arguments

- **filePath**: The path of the file you want to copy.

- **copyToFilePath**: Where to copy the specified file to.

### Optional Arguments

- **overwrite**: If set to true it will overwrite a file that already exists at copyToFilePath.

## Returns

Return true if the file was copied, else false if the 'filePath' doesn't exist.

## Example

Click to collapse [-]
Server

This example copies a file called 'test.txt' and called it 'test1.txt'.

```
addEventHandler("onResourceStart", resourceRoot, function(res)
    local filePath = ":"..getResourceName(res).."/test.txt"
    fileCreate(filePath) --create the file in this resource and name it 'test.txt'.
    if fileCopy(filePath, ":"..getResourceName(res).."/test1.txt") then
         outputChatBox("File was successfully copied!", root, 0, 100, 0)
    else
         outputChatBox("File was not successfully copied, probably because it doesn't exist.", root, 100, 0, 0)
    end
end)
```

Click to collapse [-]
Client

This example copies a file called 'test.txt' and called it 'test1.txt'.

```
addEventHandler("onClientResourceStart", resourceRoot, function(res)
    local filePath = ":"..getResourceName(res).."/test.txt"
    fileCreate(filePath) --create the file in this resource and name it 'test.txt'.
    if fileCopy(filePath,":"..getResourceName(res).."/test1.txt") then
         outputChatBox("File was successfully copied!", 0, 100, 0)
    else
        outputChatBox("File was not successfully copied, probably because it doesn't exist.", 100, 0, 0)
    end
end)
```

## See Also

- [fileClose](mta://scripting/shared/functions/fileclose.md)

- fileCopy

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
