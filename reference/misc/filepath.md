---
doc_id: "mta-wiki:4637"
title: "Filepath"
source_title: "Filepath"
source_url: "https://wiki.multitheftauto.com/wiki/Filepath"
revision_id: 79632
language: "en"
categories: ["Scripting_Concepts"]
generated_at: "2026-07-26T16:15:01.072554+00:00"
---

# Filepath

A filepath is a path that leads up to a file.  These are relative to the root directory of the resource it is being called from.

It is also possible to use special filepaths in order to reference files from other resources.  This can be done with the following syntax

```
:<resourceName>/file.ext
```

So, for example

```
xmlLoadFile ( ":helpmanager/help.xml" )
```

| [[{{{image}}}\|link=\|]] | Note: Server side filepaths which refer to resources will work correctly even if the other resource is not running. However client side filepaths require the target resource to be running. |
| --- | --- |
|  |  |

### Client file security

To protect a client file from being read by another server, prepend the filepath with @ when the file is created:

```
xmlCreateFile ( "@:myresource/someinfo.xml" )
fileCreate ( "@listofthings.txt" )
```

To read a private file, @ must also be prepended when the file is reopened:

```
xmlLoadFile ( "@:myresource/someinfo.xml" )
fileOpen ( "@listofthings.txt" )
```

Notes:

- The filepath without @ is read/writeable by all servers.

- The public and all the private versions of a particular filepath can exist at the same time. Which one is accessed depends upon the usage of @ and the server that is currently connected.

- The server file "mods/deathmatch/server-id.keys" is used for private file security. Keep a copy of it in a safe place!
