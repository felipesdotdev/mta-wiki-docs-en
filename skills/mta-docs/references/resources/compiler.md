---
doc_id: "mta-wiki:13403"
title: "Resource : Compiler"
source_title: "Resource:Compiler"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ACompiler"
revision_id: 72989
language: "en"
categories: ["Resource"]
---

# Resource : Compiler

**Name**: Compiler

**Developer**: [User:GalAnonim](https://wiki.multitheftauto.com/index.php?title=User:GalAnonim&action=edit&redlink=1) (Rick)

**State**: OpenSource

**GitHub Source**: [https://github.com/httpRick/Compiler/tree/master](https://github.com/httpRick/Compiler/tree/master)

**Server Discord**: [https://discord.gg/gJszaFjDQA](https://discord.gg/gJszaFjDQA)

**Current Version**: 1.0.0

## Overview

A simple-to-use resource that can be exported both on the client side and on the server side. consisting in the encryption/decryption of files

## Exported functions

### fileCompile

Click to collapse [-]
Shared

This function encrypts the data of the file

```
string exports.Compiler:fileCompile(string filePath, var key, [int maxBytes = 1024])
```

### Required Arguments

- **string filePath:** The [filepath](mta://reference/misc/filepath.md) of the file in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is in, and 'path' is the path from the root directory of the resource to the file.

For example, if there is a file named 'coolObjects.txt' in the resource 'objectSearch', it can be opened from another resource this way: *fileOpen(":objectSearch/coolObjects.txt")*.

If the file is in the current resource, only the file path is necessary, e.g. *fileOpen("coolObjects.txt")*.

- **var key:** The key you want to use as the file encoding key (the first 16 characters of the result are used)

### Optional Arguments

- **int maxBytes:** Maximum interger of bytes to be encoded, default is 1024 bytes. (using less than 1024 bytes is not recommended)

### Returns

Returns the encrypted bytes that have been read in the file, if something is unsuccessful, returns false.

### fileDecompile

Click to collapse [-]
Shared

This function decrypted the data of the file

```
string exports.Compiler:fileDecompile(string filePath, var key)
```

### Required Arguments

- **string filePath:** The [filepath](mta://reference/misc/filepath.md) of the file in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is in, and 'path' is the path from the root directory of the resource to the file.

For example, if there is a file named 'coolObjects.txt' in the resource 'objectSearch', it can be opened from another resource this way: *fileOpen(":objectSearch/coolObjects.txt")*.

If the file is in the current resource, only the file path is necessary, e.g. *fileOpen("coolObjects.txt")*.

- **var key:** The key you want to use as the file decrypted key (the first 16 characters of the result are used)

### Returns

Returns the decrypted bytes that have been read in the file, if something is unsuccessful, returns false.

### replaceCompileFile

Click to collapse [-]
Shared

The function encrypts and overwrites the file or creates a new one at the specified path

```
boolean exports.Compiler:replaceCompileFile(string filePath, var key, [string newFilePath, int maxBytes])
```

### Required Arguments

- **string filePath:** The [filepath](mta://reference/misc/filepath.md) of the file in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is in, and 'path' is the path from the root directory of the resource to the file.

For example, if there is a file named 'coolObjects.txt' in the resource 'objectSearch', it can be opened from another resource this way: *fileOpen(":objectSearch/coolObjects.txt")*.

If the file is in the current resource, only the file path is necessary, e.g. *fileOpen("coolObjects.txt")*.

- **var key:** The key you want to use as the file decrypted key (the first 16 characters of the result are used)

### Optional Arguments

- **string newFilePath:** Destination filepath for the specified source file in the same format.

- **int maxBytes:** Maximum interger of bytes to be encoded, default is 1024 bytes. (using less than 1024 bytes is not recommended)

### Returns

Returns true on valid encryption, and returns false if unsuccessful

### replaceDecompileFile

Click to collapse [-]
Shared

The function decrypted and overwrites the file or creates a new one at the specified path

```
boolean exports.Compiler:replaceDecompileFile(string filePath, var key, [string newFilePath])
```

### Required Arguments

- **string filePath:** The [filepath](mta://reference/misc/filepath.md) of the file in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is in, and 'path' is the path from the root directory of the resource to the file.

For example, if there is a file named 'coolObjects.txt' in the resource 'objectSearch', it can be opened from another resource this way: *fileOpen(":objectSearch/coolObjects.txt")*.

If the file is in the current resource, only the file path is necessary, e.g. *fileOpen("coolObjects.txt")*.

- **var key:** The key you want to use as the file decrypted key (the first 16 characters of the result are used)

### Optional Arguments

- **string newFilePath:** Destination filepath for the specified source file in the same format.

### Returns

Returns true on valid decryption, and returns false if unsuccessful

## Examples

### fileCompile

Click to collapse [-]
Server

```
function onResourceStart()
	local encryptedData = exports.Compiler:fileCompile("yourFile.txt", "YourPassword")
	if encryptedData then
		local fileHandler = fileCreate("yourFile.txtc")
		fileWrite(fileHandler, encryptedData)
		fileClose(fileHandler)
        outputChatBox(encryptedData)
		outputChatBox("Successfully encrypted yourFile.txt")
	else
		outputChatBox("Failed to encrypted yourFile.txt")
	end
end
addEventHandler( "onResourceStart", resourceRoot, onResourceStart)
```

Click to collapse [-]
Client

```
function onClientResourceStart()
	local txd = exports.Compiler:fileCompile("banshee.txd", "YourPassword")
	local dff = exports.Compiler:fileCompile("banshee.dff", "YourPassword")
	if txd and dff then
		local fileHandlerTxd = fileCreate("banshee.txdc")
		fileWrite(fileHandlerTxd, txd)
		fileClose(fileHandlerTxd)

		local fileHandlerDff = fileCreate("banshee.dffc")
		fileWrite(fileHandlerDff, dff)
		fileClose(fileHandlerDff)
		outputChatBox("Successfully encrypted model banshee")
	else
		outputChatBox("Failed to encrypted model banshee")
	end
end
addEventHandler( "onClientResourceStart", resourceRoot, onClientResourceStart)
```

### fileDecompile

Click to collapse [-]
Server

```
function onResourceStart()
	local decryptedData = exports.Compiler:fileDecompile("yourFile.txtc", "YourPassword")
    if decryptedData then
    	outputChatBox(decryptedData)
    	outputChatBox("Successfully decrypted yourFile.txtc")
    else
    	outputChatBox("Failed to decrypted yourFile.txtc")
    end
end
addEventHandler( "onResourceStart", resourceRoot, onResourceStart)
```

Click to collapse [-]
Client

```
function onClientResourceStart()
	local txd = exports.Compiler:fileDecompile("banshee.txdc", "YourPassword")
	local dff = exports.Compiler:fileDecompile("banshee.dffc", "YourPassword")
	if txd and dff then
		local loadTXD = engineLoadTXD(txd)
		engineImportTXD(loadTXD, 429)
		local loadDFF = engineLoadDFF(dff)
		engineReplaceModel(loadDFF, 429)
		outputChatBox("Successfully decrypted model banshee and loaded")
	else
		outputChatBox("Failed to decrypted model banshee")
	end
end
addEventHandler( "onClientResourceStart", resourceRoot, onClientResourceStart)
```

### replaceCompileFile

Click to collapse [-]
Server

```
function onResourceStart()
	local isEncrypted = exports.Compiler:replaceCompileFile("yourFile.txt", "YourPassword", "yourFile.txtc")
	if isEncrypted then
		outputChatBox("Successfully encrypted and created yourFile.txtc")
	else
		outputChatBox("Failed to encrypted yourFile.txt")
	end
end
addEventHandler( "onResourceStart", resourceRoot, onResourceStart)
```

Click to collapse [-]
Client

```
function onClientResourceStart()
	local isEncryptedTxd = exports.Compiler:replaceCompileFile("banshee.txd", "YourPassword")
	local isEncryptedDff = exports.Compiler:replaceCompileFile("banshee.dff", "YourPassword")
	if isEncryptedTxd and isEncryptedDff then
		outputChatBox("Successfully encrypted and overwritten banshee model files")
	else
		outputChatBox("Failed to encrypted model banshee")
	end
end
addEventHandler( "onClientResourceStart", resourceRoot, onClientResourceStart)
```

### replaceDecompileFile

Click to collapse [-]
Server

```
function onResourceStart()
	local isDecrypted = exports.Compiler:replaceDecompileFile("yourFile.txtc", "YourPassword", "yourFile.decrypted")
	if isEncrypted then
		outputChatBox("Successfully decrypted and created yourFile.decrypted")
	else
		outputChatBox("Failed to decrypted yourFile.txtc")
	end
end
addEventHandler( "onResourceStart", resourceRoot, onResourceStart)
```

Click to collapse [-]
Client

```
function onClientResourceStart()
	local isDecryptedTxd = exports.Compiler:replaceDecompileFile("banshee.txd", "YourPassword")
	local isDecryptedDff = exports.Compiler:replaceDecompileFile("banshee.dff", "YourPassword")
	if isDecryptedTxd and isDecryptedDff then
		outputChatBox("Successfully decrypted and overwritten banshee model files")
	else
		outputChatBox("Failed to decrypted model banshee")
	end
end
addEventHandler( "onClientResourceStart", resourceRoot, onClientResourceStart)
```
