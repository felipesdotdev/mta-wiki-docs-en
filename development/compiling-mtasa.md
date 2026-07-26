---
doc_id: "mta-wiki:5231"
title: "Compiling MTASA"
source_title: "Compiling MTASA"
source_url: "https://wiki.multitheftauto.com/wiki/Compiling_MTASA"
revision_id: 82689
language: "en"
categories: ["Development"]
generated_at: "2026-07-26T16:11:20.240605+00:00"
---

# Compiling MTASA

In order to successfully build Multi Theft Auto from source, it is necessary to perform a number of steps, which we will explain below.

Please read the instructions carefully and do not skip parts of it, if you have no experience.

# Prerequisites

Compiling the Multi Theft Auto client & server is supported on Windows 10 and 11. On Linux, you can also compile the Multi Theft Auto server ([check this article](mta://development/building-mtasa-server-on-gnu-linux.md)).

**Skipping any prerequisite steps will lead to unexpected build failures. Read the sections below carefully to understand the entire developer workflow.**

**There are solutions to common problems you may encounter in the [#Error Troubleshooting](#Error_Troubleshooting) section below.**

Make sure you have the following software and SDKs installed:

## Visual Studio 2026

- Download  and install **[Microsoft Visual Studio 2026](https://visualstudio.microsoft.com/vs/)** - make sure you get the Community Edition, that one is free.

- On the installation checklist, [make sure you tick these 2 items](https://wiki.multitheftauto.com/wiki/File:VsFoundationClasses.png):

- *Desktop development with C++*

- Optional component *C++ MFC for latest v145 build tools (x86 & x64)*

If you've made a mistake, you can run the *Visual Studio Installer* app to modify your current installation. There is no need to uninstall and reinstall.

## Microsoft DirectX SDK

**Download and install Microsoft DirectX SDK (August 2009) (DXSDK_Aug09.exe):**

- [Mirror 1 (archive.org)](https://archive.org/download/dxsdk_aug09/DXSDK_Aug09.exe)

- [Mirror 2 (mega.nz)](https://mega.nz/file/pQJCiAJY#jBcYT6ZP4DMBpnm12BLRto9EQ-RjjpP3BWkSPanpvLI)

Restart your computer after installing *Microsoft DirectX SDK*, because otherwise the environment variable **DXSDK_DIR** won't be available yet. After restarting it re-run **create-projects.bat**

See [DXSDK Aug09 Hashes](mta://development/compiling-mtasa-dxsdk-aug09-hashes.md) for file hashes of the installer.

## Git Client

If you would like to contribute to MTA, you should use Git. This will allow you to collaborate with us by creating branches and pushing changes to [GitHub](https://github.com/multitheftauto/).

[**Visual Studio** comes with a Git client](https://learn.microsoft.com/en-us/visualstudio/version-control/git-with-visual-studio) that you can use to manage your local repository. You should fork the [mtasa-blue repository](https://github.com/multitheftauto/mtasa-blue) and clone on your machine.

If you only want to compile the source code and are not interested in contributing to MTA, you can download the source directly (see below).

# Getting the latest source code

To get the latest code, you will have to download the latest copy of our Git repository.  

We recommend cloning the repository in your Git client because you can pull any updates from there easily.

- **Repository:** [multitheftauto/mtasa-blue](https://github.com/multitheftauto/mtasa-blue)

- **.zip:** [master.zip](https://github.com/multitheftauto/mtasa-blue/archive/master.zip)

- **.tar.gz:** [master.tar.gz](https://github.com/multitheftauto/mtasa-blue/archive/master.tar.gz)

# Compiling the code

Follow these steps to successfully build the **mtasa-blue** project.

- Execute the script **win-create-projects.bat**. This installs dependencies and generates the Visual Studio project files that are mandatory to compile the code.

- Open the solution file **MTASA.sln** in the **Build** directory. If you are asked to upgrade the project, click **Cancel**.

- Select **Debug** - **Win32** configuration in Visual Studio, then press Build > Build Solution (may take some minutes).

- Alternatively, you may execute the script **win-build.bat**, which runs the previous mentioned steps, without the need to open Visual Studio.

- Finally, execute the script **win-install-data.bat**. This copies important files to the Bin directory that are required for MTA to function. It gives you the option to **Install the official resources**, which you can read about in the [#Running the dedicated server](#Running_the_dedicated_server) section below.

# Running the software

This section contains information on how to run the Multi Theft Auto client and server separately.

## Running the client

You can start your client in the **Bin** directory. You might find there a *Multi Theft Auto.exe* and/or *Multi Theft Auto_d.exe* executable. The *_d* suffix indicates a debug build of the software.  

Furthermore, you can also run your client inside the debugger from Visual Studio if you want to investigate a stack trace or set breakpoints in interesting code regions (read more in the section Debugging below).

## Running the dedicated server

If you already have run **win-install-data.bat** and selected "*Install resources*" then you can go to [#Starting the server](#Starting_the_server).

### Installing the latest resources

If you want to run the Multi Theft Auto dedicated server, you will have to install the official resources. This default package includes resources that implmenent the most basic functionality (e.g. spawning players) in order to play.

Our official resources repository is [hosted on GitHub](https://github.com/multitheftauto/mtasa-resources). You can download the latest resources from there or [download a zipped version](http://mirror.multitheftauto.com/mtasa/resources/). Make sure that you have the latest resources package.

### Starting the server

To run the server, open the *MTA Server.exe* executable in the **Bin/server** directory. The *_d* suffix indicates a debug build of the software.  

You can also run the debug build *MTA Server_d.exe* with the Visual Studio Debugger (as of writing, you can do that by right-clicking on the Server's Launcher project and selecting *Start a local instance* in the *Debugger* menu), but you can also attach to a running debug build MTA server (see more in the section Debugging below).

# Debugging

If you already compiled the code in the **Debug** configuration then continue reading, if not, then go up to *Compiling the code* and follow the steps for a *Debug* build.  

To compile in **Release**, click on the **Debug** list and switch to **Release**.  

You can either launch MTA yourself and attach any debugger you want to use (also applies to the Visual Studio debugger) or you start a local debugging session in Visual Studio.

## How to enable breakpoints

If you choose to run MTA with Visual Studio then you should also attach the debugger to the executable **gta_sa.exe** (press *CTRL + ALT + P* in Visual Studio) - otherwise, your
breakpoints will not work for anything besides the MTA Launcher project.

## Extending timeout duration

When you use breakpoints during debugging, you may get kicked by the server due to timeout, because the client is frozen. To prevent this, create the **timeout.longtime** file in your *Bin/server/* directory.  
The content of the file is the new timeout duration in seconds, so make sure you type a huge number in there. If you keep the file empty, the timeout will be set to 120 seconds.

## ReAttach for Visual Studio

You can use [ReAttach](https://marketplace.visualstudio.com/items?itemName=ErlandR.ReAttach) to re-attach the debugger to the **gta_sa.exe** executable whenever you start your local debugger in Visual Studio.

# Getting involved

Please see our [Coding guidelines](mta://scripting/concepts/coding-guidelines.md) for information on the coding practice.

# Additional information

If you need more information, try our [bug tracker](https://github.com/multitheftauto/mtasa-blue/issues) or [Discord](https://discord.com/invite/mtasa).

# Error Troubleshooting

## Cannot open include file 'afxres.h'

This error is caused by your incomplete Visual Studio configuration. Use the Visual Studio Installer to enable Optional component *C++ MFC for latest v143 build tools (x86 & x64)*.

## Cant find d3dx9.h

Add the **$(DXSDK_DIR)Include;** to the VC++ Directories in DirectX9GuiRenderer, GUI and Client Core projects.
You can find the VC++ Directories list by selecting a project, then pressing the shortcut ALT + ENTER (without the +), then under the 'Configuration properties' you can find 'VC++ Directories', and in there you can find the 'Include Directories' field, click on it and add **;$(DXSDK_DIR)Include;** at the end of it. 
**Note: You need to do the same thing in Release mode as well**

## Cant find d3dx9.lib

Do do same as in the error above, but instead of **;$(DXSDK_DIR)Include;** you must add **;$(DXSDK_DIR)Lib/x86;** to the **Library directories** field
**Note: You need to do the same thing in Release mode as well**

## S1023 Error

["S1023" error when you install the DirectX SDK (June 2010)](https://support.microsoft.com/en-us/kb/2728613)

## Cannot open source file "xxx.h" after upgrading to Visual Studio 2022

If you've just upgraded to Visual Studio 2022 and were working on MTA using a previous version, you may receive errors about header files not being found (stdio.h, stddef.h, etc) when building the project.

Make sure you have the latest Windows 10 SDK installed (via the Visual Studio Installer) and restart your PC.

If that doesn't work - close Visual Studio, go into the `Build` folder (where your mtasa-blue is located) and delete the `.vs` folder. Start Visual Studio and everything should be fixed.

## CL38 error. [netc_d.dll not found]

Solution: Delete **Multi Theft Auto_d.exe** and hit compile again.

## After cloning the repository, it doesn't compile the project

Solution: Execute **win-create-projects.bat** in main directory.

## CL17 Load field. Please ensure that the latest data files have been installed correctly

Solution: Execute **win-install-data.bat** in main directory.

## ERROR: Loading network library (net_d.dll) failed!

Solution: Execute **win-install-data.bat** in main directory.
