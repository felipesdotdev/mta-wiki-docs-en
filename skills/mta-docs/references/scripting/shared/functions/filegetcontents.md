---
doc_id: "mta-wiki:14099"
title: "FileGetContents"
source_title: "FileGetContents"
source_url: "https://wiki.multitheftauto.com/wiki/FileGetContents"
revision_id: 80819
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# FileGetContents

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21938](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21938))

Reads the entire contents of the file, optionally verifies the read contents by computing and comparing the checksum with the expected one, and returns the content as string. The file cursor position is not modified by calls to this function. File must be added in the [meta.xml](mta://reference/misc/meta-xml.md).

Please note that even if you enable SD #22 and #23 on your server, you are not protected from user attacks, which can happen after verification of the file, but before you read the contents of such verified file. This function enables you to safely read the contents of a meta.xml-listed file on both client and server.

## Syntax

```
nil|string fileGetContents ( file theFile [ , bool verifyContents = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[file](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1):getContents(...)*

### Required Arguments

- **theFile:** A handle to the file you wish to get the contents from. Use [fileOpen](mta://scripting/shared/functions/fileopen.md) to obtain this handle.

- **verifyContents:** Set to true, to compare the computed and the expected checksum of the file content.

### Returns

Returns the bytes that were read from the file, but only if verification was disabled or if the checksum comparison succeeded. On failure, this function returns *nil*.

## Example

This example opens the code.lua file, checks its contents, and then runs it.

```
local handle = fileOpen("code.lua", true)
local buffer = fileGetContents(handle) -- code.lua must be listed in meta.xml (for example as <file> for this example)
fileClose(handle)

if buffer then
    loadstring(buffer)() -- This is just an example. You should avoid using loadstring. If you are dealing with configuration use json functions instead for security reasons.
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

- fileGetContents

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
