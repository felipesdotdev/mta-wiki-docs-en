---
doc_id: "mta-wiki:4012"
title: "FileDelete"
source_title: "FileDelete"
source_url: "https://wiki.multitheftauto.com/wiki/FileDelete"
revision_id: 78698
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:00.832709+00:00"
---

# FileDelete

Deletes the specified file.

## Syntax

```
bool fileDelete ( string filePath )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the File class.*

**Method**: *[File](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1).delete(...)*

### Required Arguments

- **filePath:** The [filepath](mta://reference/misc/filepath.md) of the file to delete in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is in, and 'path' is the path from the root directory of the resource to the file.

For example, if you want to delete a file name "myFile.txt" in the resource 'fileres', it can be deleted from another resource this way: *fileDelete(":fileres/myFile.txt")*.

If the file is in the current resource, only the file path is necessary, e.g. *fileDelete("myFile.txt")*.

### Returns

Returns *true* if successful, *false* otherwise (for example if there exists no file with the given name, or it does exist but is in use).

## Example

This example will show us how to create a file "text.txt" spell it "This is a test file!", Close the file and delete it:

```
local newFile = fileCreate("test.txt")                -- attempt to create a new file
if (newFile) then                                     -- check if the creation succeeded
    fileWrite(newFile, "This is a test file!")        -- write a text line
    fileClose(newFile)                                -- close the file once you're done with it
    fileDelete("test.txt")                            -- delete file
end
```

## See Also

- [fileClose](mta://scripting/shared/functions/fileclose.md)

- [fileCopy](mta://scripting/shared/functions/filecopy.md)

- [fileCreate](mta://scripting/shared/functions/filecreate.md)

- fileDelete

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
