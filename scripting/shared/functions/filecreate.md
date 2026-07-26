---
doc_id: "mta-wiki:3394"
title: "FileCreate"
source_title: "FileCreate"
source_url: "https://wiki.multitheftauto.com/wiki/FileCreate"
revision_id: 81448
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.6"]
generated_at: "2026-07-26T16:15:00.811433+00:00"
---

# FileCreate

Creates a new file in a directory of a resource. If there already exists a file with the specified name, it is overwritten with an empty file.

| [[{{{image}}}\|link=\|]] | Note: To prevent memory leaks, ensure each successful call to fileCreate has a matching call to fileClose |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: If you do not want to share the content of the created file with other servers, prepend the file path with @ (See filepath for more information) |
| --- | --- |
|  |  |

## Syntax

```
file fileCreate ( string filePath )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the File class.*

**Method**: *[File](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1).new(...)*

ADDED/UPDATED IN VERSION 1.5.6 [r11865](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=11865):

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This is a static function underneath the File class. Using **File(...)** to open a file will attempt to create the file, if it doesn't exist*

**Method**: *[File](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1).new(...)*

### Required Arguments

- **filePath:** The [filepath](mta://reference/misc/filepath.md) of the file to be created in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is in, and 'path' is the path from the root directory of the resource to the file.

For example, if you want to create a file named 'myfile.txt' in the resource 'mapcreator', it can be created from another resource this way: *fileCreate(":mapcreator/myfile.txt")*.

If the file is in the current resource, only the file path is necessary, e.g. *fileCreate("myfile.txt")*.

### Returns

If successful, returns a file handle which can be used with other file functions ([fileWrite](mta://scripting/shared/functions/filewrite.md), [fileClose](mta://scripting/shared/functions/fileclose.md)...). Returns *false* if an error occured.

## Example

This example creates a text file in the current resource and writes a string to it.

```
local newFile = fileCreate("test.txt")                -- attempt to create a new file
if (newFile) then                                       -- check if the creation succeeded
    fileWrite(newFile, "This is a test file!")        -- write a text line
    fileClose(newFile)                                -- close the file once you're done with it
end
```

Notice that you can't simply do *fileWrite("test.txt", "File content")*. Instead, file functions operate on a **file handle**, which is a special object representing an open file. *fileCreate* creates a file, opens it, and returns the resulting handle.

It is also important to remember to close a file after you've finished all your operations on it, especially if you've been writing to the file. If you don't close a file and your resource crashes, all changes to the file may be lost.
If the file already exists, a new file will be created on local.

## See Also

- [fileClose](mta://scripting/shared/functions/fileclose.md)

- [fileCopy](mta://scripting/shared/functions/filecopy.md)

- fileCreate

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
