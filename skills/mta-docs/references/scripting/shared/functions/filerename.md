---
doc_id: "mta-wiki:5633"
title: "FileRename"
source_title: "FileRename"
source_url: "https://wiki.multitheftauto.com/wiki/FileRename"
revision_id: 78721
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# FileRename

Renames the specified file.

| [[{{{image}}}\|link=\|]] | Note: Also with this function you can move specified file to a new location, new folder or even to another resource's folder. But for this action executing resource must have 'ModifyOtherObjects' ACL right set to true . |
| --- | --- |
|  |  |

## Syntax

```
bool fileRename ( string filePath, string newFilePath )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the File class.*

**Method**: *[File](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1).rename(...)*

### Required Arguments

- **filePath:** The [filepath](mta://reference/misc/filepath.md) of the source file in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is in, and 'path' is the path from the root directory of the resource to the file. If the file is in the current resource, only the file path is necessary.

- **newFilePath:** Destination [filepath](mta://reference/misc/filepath.md) for the specified source file in the same format.

### Returns

If successful, returns *true*. Otherwise returns *false*.

## Example

This example renames the file *test1.txt* that is in the root of the current resource to *test2.txt*.

```
if fileRename( "test1.txt", "test2.txt" ) then
    outputConsole("File `test1.txt` successfully renamed to `test2.txt`")
else
    outputConsole("Unable to rename `test1.txt`")
end
```

This example moves the file *test1.txt* that is in the root of the current resource to *myFolder* folder. If this folder is not exists, it will be created before moving the file *test1.txt*.

```
if fileRename( "test1.txt", "myFolder/test1.txt" ) then
    outputConsole("File `test1.txt` successfuly moved to `myFolder` folder")
else
    outputConsole("Unable to move `test1.txt`")
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

- fileRename

- [fileSetPos](mta://scripting/shared/functions/filesetpos.md)

- [fileWrite](mta://scripting/shared/functions/filewrite.md)
