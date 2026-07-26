---
doc_id: "mta-wiki:14585"
title: "FileGetHash"
source_title: "FileGetHash"
source_url: "https://wiki.multitheftauto.com/wiki/FileGetHash"
revision_id: 82257
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# FileGetHash

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r23289](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23289))

This function returns a hash of the entire file in the specified algorithm. This function *does not* move the file pointer/position. Beware though, there will always be a minuscule period of time between checking the hash and loading the contents of the file, which can be abused by a potential attacker to modify the contents.

## Syntax

```
nil|string fileGetHash ( file theFile, string algorithm [, table options ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[file](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1):getHash(...)*

### Required Arguments

- **theFile:** A handle to the file you wish to get the hash from. Use [fileOpen](mta://scripting/shared/functions/fileopen.md) to obtain this handle.

- **algorithm**: A string which must be one of these: "md5", "sha1", "sha224", "sha256", "sha384", "sha512", "hmac"

### Optional arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **options**: A table with options and other necessary data for the algorithm, as detailed below.

### Options for each algorithm

- *hmac* ([HMAC](https://en.wikipedia.org/wiki/HMAC))

- **key**: a key to encode the input with.

- **algorithm**: a string which must be one of these: "md5", "sha1", "sha224", "sha256", "sha384", "sha512".

### Returns

Returns the hash of the entire file on success, and *nil* on failure.

## Example

This example opens the code.lua file, computes the hash with every algorithm, and then displays them.

```
local handle = fileOpen("code.lua", true)
local hashMD5 = fileGetHash(handle, "md5")
local hashSHA1 = fileGetHash(handle, "sha1")
local hashSHA224 = fileGetHash(handle, "sha224")
local hashSHA256 = fileGetHash(handle, "sha256")
local hashSHA384 = fileGetHash(handle, "sha384")
local hashSHA512 = fileGetHash(handle, "sha512")
local hashHMAC = fileGetHash(handle, "hmac", { algorithm = "sha256", key = "blue apple tree" })
fileClose(handle)

iprint("MD5", hashMD5)
iprint("SHA1", hashSHA1)
iprint("SHA224", hashSHA224)
iprint("SHA256", hashSHA256)
iprint("SHA384", hashSHA384)
iprint("SHA512", hashSHA512)
iprint("HMAC-SHA256", hashHMAC )
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

- fileGetHash

- [fileGetPath](mta://scripting/shared/functions/filegetpath.md)

- [fileGetPos](mta://scripting/shared/functions/filegetpos.md)

- [fileGetSize](mta://scripting/shared/functions/filegetsize.md)

- [fileIsEOF](mta://scripting/shared/functions/fileiseof.md)

- [fileOpen](mta://scripting/shared/functions/fileopen.md)

- [fileRead](mta://scripting/shared/functions/fileread.md)

- [fileRename](mta://scripting/shared/functions/filerename.md)

- [fileSetPos](mta://scripting/shared/functions/filesetpos.md)

- [fileWrite](mta://scripting/shared/functions/filewrite.md)
