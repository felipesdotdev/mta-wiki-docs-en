---
doc_id: "mta-wiki:5132"
title: "FileExists"
source_title: "FileExists"
source_url: "https://wiki.multitheftauto.com/wiki/FileExists"
revision_id: 78700
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# FileExists

This functions checks whether a specified file exists inside a resource.

## Syntax

```
bool fileExists ( string filePath )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the File class.*

**Method**: *[File](https://wiki.multitheftauto.com/index.php?title=File&action=edit&redlink=1).exists(...)*

### Required Arguments

- **filePath:** The [filepath](mta://reference/misc/filepath.md) of the file, whose existence is going to be checked, in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is checked to be in, and 'path' is the path from the root directory of the resource to the file.

For example, if you want to check whether a file named 'myfile.txt' exists in the resource 'mapcreator', it can be done from another resource this way: *fileExists(":mapcreator/myfile.txt")*.

If the file, whose existence is going to be checked, is in the current resource, only the file path is necessary, e.g. *fileExists("myfile.txt")*. Note that you must use forward slashes '/' for the folders, backslashes '\' will return false.

### Returns

Returns *true* if the file exists, *false* otherwise.

## Example

This example checks if a file exists in a resource directory

```
function checkExistingFile(player,cmd,filename,resourcename)
	if not filename then -- if the player didn't include a filename
		outputChatBox("ERROR: Syntax '/checkfile filename resourcename(optional)'.",player) -- display error
		return false  -- stop function
	end
	if not resourcename then -- if the player didn't specify the resource he wants to check, use current resource
		resourcename = getResourceName(resource) --every resource has a predefined global variable called resource that contains the resource pointer for that resource, in other words, the value that getThisResource() function returns.
	else
		if not getResourceFromName(resourcename) then -- if a resource with that name doesn't exist, output error and stop function
			outputChatBox("ERROR: Resource "..resourcename.." doesn't exist.",player) -- output error message
			return false -- stop the function here
		end
	end
	-- as it hasn't stopped anywhere, we have both correct resourcename and filename
	local exists = fileExists((":%s/%s"):format(resourcename,filename)) -- using shorter format of string.format, see StringLibraryTutorial in lua wiki for that
	if exists then
		outputChatBox(("The file %q in resource %q exists"):format(filename,resourcename))
	else
		outputChatBox(("The file %q in resource %q doesn't exist"):format(filename,resourcename))
	end
end
addCommandHandler("exists",checkExistingFile)
```

## See Also

- [fileClose](mta://scripting/shared/functions/fileclose.md)

- [fileCopy](mta://scripting/shared/functions/filecopy.md)

- [fileCreate](mta://scripting/shared/functions/filecreate.md)

- [fileDelete](mta://scripting/shared/functions/filedelete.md)

- fileExists

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
