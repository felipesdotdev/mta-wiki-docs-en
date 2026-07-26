---
doc_id: "mta-wiki:5232"
title: "Building MTASA Server on GNU Linux"
source_title: "Building MTASA Server on GNU Linux"
source_url: "https://wiki.multitheftauto.com/wiki/Building_MTASA_Server_on_GNU_Linux"
revision_id: 82020
language: "en"
categories: ["Needs_Checking", "Development"]
---

# Building MTASA Server on GNU Linux

|  | This article needs checking. |
| --- | --- |
| Reason(s): Confirm steps work. |  |

## Installing and Running MTASA server on Linux

| [[{{{image}}}\|link=\|]] | Note: This article is only for developers who changed the server code. If you are looking for the precompiled server (for normal server owners). Go to: linux.mtasa.com and see Installing and Running MTASA Server on GNU_Linux |
| --- | --- |
|  |  |

## Preparing your system

In order to build the Multi Theft Auto dedicated server, you will have to set up your system with the correct libraries and tools. How these are installed depends on your distribution.

Our network module (net.dll or net.so) is distributed as a precompiled binary library. The file for GNU/Linux can be found inside the lastest Linux nightly from [here](http://nightly.mtasa.com/). Use the net.so from 1.6 if you are compiling from the trunk, or the net.so from 1.6.0 if you are compiling the 1.6.0 branch. Be sure the read the top of *Server/version.h* as it contains directions on how to compile the different build types.

### Ubuntu 20.04

The following instructions are specifically for Ubuntu 20.04.

You will need to install the required build tools, headers, and libraries. These can be installed using the following packages:

- **g++-10:** package provides the GNU C++ compiler version 10. It is used to compile C++ source code into executable programs or libraries

- **build-essential:** provides tools, headers, and libraries required to build applications

- **automake:** provides tools for automatically generating Makefiles

- **libtool:** required for building shared libraries

- **libreadline-gplv2-dev:** provides the GNU readline library (version 5)

- **libncurses5-dev:** provides tools for writing to the console screen

- **libncursesw5-dev:** provides wide character support for ncurses

- **default-libmysqlclient-dev:** provides the MySQL client development files

- **git:** version control tool used to clone the code repository

- **unzip:** archive unpacking utility

To install all required packages, run the following commands in the terminal (execute as root):

```
apt-get update
apt-get install g++-10
apt-get install build-essential automake libtool
apt-get install libreadline-gplv2-dev libncurses5-dev libncursesw5-dev
apt-get install default-libmysqlclient-dev git unzip
```

### Gentoo Linux

You will need the necessary build tools, headers and libraries. Because Gentoo’s portage system is designed to compile any packages on your own system, the necessary build tools will have already been installed. This only leaves you to install the necessary libraries:

- **git:** contains the git client used to check out our code repository

To compile and install these packages through *emerge*, use the **emerge -v <package list>** command. The -v option shows additional * * information and can be omitted. (If you want to use any USE flags, prepend emerge with USE="use flags here". You can also use the -pv option to verify that you’re using the correct flags.) Refer to the [Gentoo Handbook](http://www.gentoo.org/doc/en/handbook/handbook-x86.xml?part=2&chap=1) or manual for more information on emerge.

Example:

```
emerge -v git sqlite
USE=“net-misc/curl ssl” emerge -v curl
```

### Fedora

You will need these packages to be able to successfully compile a MTA server on Fedora:

- **glibc-devel:**

- **readline-devel:** contains the readline library

- **git:** contains the git client to check out the source code

To install these packages through yum, use the yum install <package list> command as in the following example (execute as root):

```
yum install glibc-devel readline-devel git
```

## General instructions for 1.6

**Downloading the source.**

First, you need to download the source. Either clone as shown below or [download a zip snapshot](https://github.com/multitheftauto/mtasa-blue/archive/master.zip)

```
git clone https://github.com/multitheftauto/mtasa-blue.git mtasa-blue
cd mtasa-blue
sudo chmod -R 777 .
```

Then compile it thus:

```
./linux-build.sh
```

Then copy the configuration files, network module and resources into **Bin/server** by running this command:

```
./linux-install-data.sh
```

And the resources and stuff should be downloaded and stuff. As well as the net_d.dll file.

### **Troubleshooting**

If you’re getting any unexpected errors while compiling, please check our [GitHub issues](https://github.com/multitheftauto/mtasa-blue/issues) or our [development-focused Discord server](https://discord.com/invite/GNN6PRtTnu).

- If you get a message saying "Killed" when running premake5 gmake (linux-build.sh), that usually means you ran out of memory.  

You can confirm this by searching for kill logs by running `sudo dmesg | grep -i kill`  

A possible solution for this might be to [turn on swap](https://opensource.com/article/18/9/swap-space-linux-systems) or upgrade your system memory temporarily.  

1 GB is likely **not** enough of memory to complete the build.
