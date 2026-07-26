---
doc_id: "mta-wiki:7547"
title: "MTA:Eir/FileSystem"
source_title: "MTA:Eir/FileSystem"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem"
revision_id: 73708
language: "en"
categories: []
---

# MTA:Eir/FileSystem

The **MTA:Eir FileSystem** is the framework used for accessing persistent data in [MTA:Eir](mta://reference/misc/mta-eir.md) on places like the harddisk and .zip archives. It is a cross-platform library that currently supports Windows and Unix operating systems. It is based on browsing file system directories after named file entries. A directory can be accessed using a **translator**. Each file entry has a path which can be accessed from **translators**. To open a file, a **binary stream handle** is created and returned to the runtime (CFile native class). Each translator has a **root directory** and **current directory** that it bases all operations on. It is only allowed to access file system objects from **its directory tree**.

## Definition of Paths

A **path** is a string that is used to **browse a file system** with. It can consist of multiple namespaces that resolve into folders on the underlying file system. Every path has a *target location* that it points to on a translator file system.

### Distinction between paths

A **directory path** is a path that ends with either **/** or **\**. Functions that expect directory paths are allowed to **trim away the filename at the end of the path**.

A **file path** is a path that does **not** end with either **/** or **\**. These paths are accepted by functions that **open binary streams** or **handle binary data directly**. There has to be a **filename** at the end of the **file path**. It is a string whose size is greater than 0 and contains the name of a **file object**.

The **null path** is the path whose **size is zero**. This path has to be accepted by all functions. It should cause **no additional browsing** other than the **translators current status**. If passed to **translator path resolution functions**, these functions should return the path that they base operations on (i.e. the current directory of the translator).

A **relative path** is a directory or file path that is resolved based on the **translators current directory** (unless otherwise specified). Two relative paths are only equal if their translators current directory at the time of resolution was the same.

An **absolute path** is a directory or file path that is resolved based on the **translators current directory** (unless otherwise specified). Two absolute paths can be equal independent from the **translator status**.

An **unique path** is a path that is returned by **translator path resolution functions**. It must not contain **path scripting symbols**. If two unique paths are compared for equality, then they **point to the same file system object** if the *context of the comparison* stays the same (i.e. the translator current directory).

### Windows

On Windows, a file path is **case-**in**sensitive**. This means that paths can be checked for equality by comparing the lower-case version of their **unique absolute path**. Paths do not allow the symbols **<**, **>**, **"**, **|**, **?** and *****. File paths cannot allow the symbols **/** and **\**.

### Linux

On Linux, a file path is **case-sensitive**. Paths can be checked for equality by **comparing their characters directly**. In Lua, this is a simple string reference comparison.

## Browsing a File System using Paths

A **file system** is a structure that consists of named and partitioned **file system objects**. It is a **tree structure** that has a *root directory*. From the root directory each file system object should be addressable using **paths**. There are infinite variations of paths to address file system objects using **path scripting**, unless the path is an **unique path**.

Translators behave in a similar way in that they have a root directory where every file system object is addressable from. Hence a translator is a *special derivation* of a file system. Like in file systems the runtime **cannot address file system objects that are outside of the root directory** (a process called up-rooting). Using scanning functions translators can request the contents of directories. The returned list of names is OS specific. In general, if the OS sets a *hidden-flag* onto a file object, its name should not be returned.

### Translator Access on Windows

| Path Syntax | Description |
| --- | --- |
| *drive_letter* :/ *path* | Format of an absolute path that is based from the drive root (OS specific). |
| / *path* | Format of a relative path that is based from the translator root . |
| // *path* | Format of a relative path that is based from the translator root . |
| *path* | Format of a relative path that is based from the translator current directory . |
| \\ *unc-name* \ *path* | Format of a UNC-path (OS specific) |

**Hint:** to specify UNC-paths in Lua programs it is a good idea to make use of the **multi-line-string** literal, for example.

```
fs.root:setOutbreakEnabled(true)
local logFile = fs.root:open([[\\wsl$\Ubuntu-20.04\var\log\dpkg.log]], "rb")
```

### Translator Access on Unix

| Path Syntax | Description |
| --- | --- |
| / *path* | Format of an absolute path that is based from the Unix file system root (OS specific). |
| // *path* | Format of a relative path that is based from the translator root . |
| *path* | Format of a relative path that is based from the translator current directory . |

## Path Scripting and Path Resolution

Paths can contain the following scripting and formating symbols.

| Symbol | Description |
| --- | --- |
| / or \ | Namespace separator . If a string of valid file system characters is put before it or the string is a special namespace , then that string is recognized as a namespace. |
| . | Current-directory pointer . If this character is recognized as a namespace, then it stands for the current directory at parsing level . Effectively, this symbol does nothing. |
| .. | Previous-directory pointer . If this character is recognized as a namespace, then the parser changes context to the upper directory on the translator file system tree. |

## References

- [FileSystem module Lua functions](mta://reference/misc/modules-filesystem-functions.md)

- [MTA:BLUE FileSystem Module Port](mta://reference/misc/modules-filesystem.md)
