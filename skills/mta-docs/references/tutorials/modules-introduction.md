---
doc_id: "mta-wiki:13730"
title: "Modules Introduction"
source_title: "Modules Introduction"
source_url: "https://wiki.multitheftauto.com/wiki/Modules_Introduction"
revision_id: 82748
language: "en"
categories: []
---

# Modules Introduction

| [[\|link=\|]] | Warning: This is an unofficial article and the github link may not work |
| --- | --- |
|  |  |

Modules are extensions for Multi Theft Auto's Lua core, allowing the integration and use of custom Lua functions that have been written in C++, and compiled as a DLL or SO file. Modules are commonly used to create functions for such purposes that Multi Theft Auto lacks, such as [sockets](mta://reference/misc/modules-sockets.md).

## Getting started

To start writing new modules, you need to have at least basic knowledge of programming in C/C++.  

This tutorial **does not teach** you how to get started with C++.   

Let's start by downloading a template to create our own module.
We can do it in 2 ways:

### From terminal

Make sure you have the [GIT](https://git-scm.com/downloads) source control package installed.
Open the command prompt (Win + R -> CMD) and enter this command:

```
git clone https://github.com/multitheftauto/mtasa-modules.git
```

### From website

Go to the website [of the sample module](https://github.com/multitheftauto/mtasa-modules) and download it (Green button "Code" -> "Download ZIP") then unpack the archive

## Template's content

### The structure of the template module

- **hpp**

- config.hpp

- functions.hpp

- main.hpp

- **include**

- **lua**

- lauxlib.h

- lua.h

- lua.hpp

- luaconf.h

- lualib.h

- **mta**

- CLuaArgument.hpp

- CLuaArguments.hpp

- ILuaModuleManager.hpp

- init.hpp

- mta_main.hpp

- **lib**

- **lua5.1.lib**

- **lua5.1_64.lib**

- **src**

- **mta**

- CLuaArgument.cpp

- CLuaArguments.cpp

- mta_main.cpp

- functions.cpp

- main.cpp

- ml_basic.sln

- ml_basic.vcxproj

- ml_basic.vcxproj.filters

- ml_basic.vcxproj.user

Files are marked in green font  

Folders are marked in **bolded blue font**  

Files and **folders**
that **should not** be modified are marked in red
