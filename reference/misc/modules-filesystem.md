---
doc_id: "mta-wiki:7549"
title: "Modules/FileSystem"
source_title: "Modules/FileSystem"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem"
revision_id: 76320
language: "en"
categories: ["Modules"]
generated_at: "2026-07-26T16:16:11.560516+00:00"
---

# Modules/FileSystem

| Module info |  |
| --- | --- |
| Name | FileSystem |
| Version | 2.0 |
| Author | Martin Turski (The_GTA) |
| Module website | Here |
| Download link | Win32 AMD64 (Win) Linux (AMD64) |
| License | here |
| Written in | C++ |
| Operating system | Cross-platform |
| Compatible with | 1.X |

FileSystem is the [MTA:Eir](mta://reference/misc/mta-eir.md) file management implementation exported as MTA:BLUE module. It is made for those people who are not satisfied with the standard MTA file functions. Its feature-set covers **binary stream writing**, **directory scanning** and **path resolution logic**. It should satisfy all needs regarding file functionality. The modules' source code is released [within the MTA:Eir SVN](https://osdn.net/projects/green-candy/scm/svn/tree/head/blueMods/fileSystem/).

It's documentation can be found [here](mta://reference/misc/mta-eir-filesystem.md). To find coding examples, *browse the individual class methods*.

## Installing FileSystem into your Server

- Place the fileSystem*.dll module into your MTA server modules directory

- Add the module into the mtaserver.conf module loading list (at the bottom of the file)

- **Edit the acl.xml in a way that resources require admin rights to call** [createFilesystemInterface](mta://reference/misc/modules-filesystem-createfilesysteminterface.md)**

## System Access Possibilities

- Accessing whole system

- Listing and editing all server resources

- Modifying MTA Server configuration

**Be careful how you expose the FileSystem module to your server resources!**

## OOP-style API

Since version 2.0 of this library the API has been changed to match the MTA OOP-style API. This means that object methods are now accessed solely using the **colon operator** instead of the **dot operator**. If you have old FileSystem code (pre 2.0) then you may have to adjust it.

## Support

If you are looking for direct support about this module then contact [The_GTA on the MTA forums](https://forum.mtasa.com/profile/9756-the_gta/). The official MTA forums support topic can be found [here](https://forum.mtasa.com/topic/133936-filesystem-module-for-mtablue/).

- [Porting Clientside and Serverside code](mta://reference/misc/modules-filesystem-porting-between-clientside-and-serverside.md)

## FileSystem Library Functions

- [createFilesystemInterface](mta://reference/misc/modules-filesystem-createfilesysteminterface.md)

## FileSystem Namespace Functions

- [createTranslator](mta://reference/misc/modules-filesystem-createtranslator.md)

- [createRAMDisk](mta://reference/misc/modules-filesystem-createramdisk.md)

- [createMemoryFile](mta://reference/misc/modules-filesystem-creatememoryfile.md)

- [createFileIterative](mta://reference/misc/modules-filesystem-createfileiterative.md)

- [copyFile](mta://reference/misc/modules-filesystem-copyfile.md)

- [copyStream](mta://reference/misc/modules-filesystem-copystream.md)

- [copyStreamCount](mta://reference/misc/modules-filesystem-copystreamcount.md)

- [pathToFilename](mta://reference/misc/modules-filesystem-pathtofilename.md)

- [streamCompare](mta://reference/misc/modules-filesystem-streamcompare.md)

- [topointer](mta://reference/misc/modules-filesystem-topointer.md)

- [type](mta://reference/misc/modules-filesystem-type.md)

- [setDoBufferAllRaw](mta://reference/misc/modules-filesystem-setdobufferallraw.md)

- [getDoBufferAllRaw](mta://reference/misc/modules-filesystem-getdobufferallraw.md)

## FileSystem Object Functions

- [destroy](mta://reference/misc/modules-filesystem-object-destroy.md)

## FileSystem Translator Functions

- [open](mta://reference/misc/modules-filesystem-translator-open.md)

- [exists](mta://reference/misc/modules-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/modules-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/modules-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/modules-filesystem-translator-delete.md)

- [copy](mta://reference/misc/modules-filesystem-translator-copy.md)

- [rename](mta://reference/misc/modules-filesystem-translator-rename.md)

- [size](mta://reference/misc/modules-filesystem-translator-size.md)

- [stat](mta://reference/misc/modules-filesystem-translator-stat.md)

- [relPath](mta://reference/misc/modules-filesystem-translator-relpath.md)

- [relPathRoot](mta://reference/misc/modules-filesystem-translator-relpathroot.md)

- [absPath](mta://reference/misc/modules-filesystem-translator-abspath.md)

- [absPathRoot](mta://reference/misc/modules-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/modules-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/modules-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/modules-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/modules-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/modules-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)

## FileSystem File Functions

- [read](mta://reference/misc/modules-filesystem-file-read.md)

- [readByte](mta://reference/misc/modules-filesystem-file-readbyte.md)

- [readUByte](mta://reference/misc/modules-filesystem-file-readubyte.md)

- [readShort](mta://reference/misc/modules-filesystem-file-readshort.md)

- [readUShort](mta://reference/misc/modules-filesystem-file-readushort.md)

- [readInt](mta://reference/misc/modules-filesystem-file-readint.md)

- [readUInt](mta://reference/misc/modules-filesystem-file-readuint.md)

- [readFloat](mta://reference/misc/modules-filesystem-file-readfloat.md)

- [readDouble](mta://reference/misc/modules-filesystem-file-readdouble.md)

- [readBoolean](mta://reference/misc/modules-filesystem-file-readboolean.md)

- [write](mta://reference/misc/modules-filesystem-file-write.md)

- [writeByte](mta://reference/misc/modules-filesystem-file-writebyte.md)

- [writeUByte](mta://reference/misc/modules-filesystem-file-writeubyte.md)

- [writeShort](mta://reference/misc/modules-filesystem-file-writeshort.md)

- [writeUShort](mta://reference/misc/modules-filesystem-file-writeushort.md)

- [writeInt](mta://reference/misc/modules-filesystem-file-writeint.md)

- [writeUInt](mta://reference/misc/modules-filesystem-file-writeuint.md)

- [writeFloat](mta://reference/misc/modules-filesystem-file-writefloat.md)

- [writeDouble](mta://reference/misc/modules-filesystem-file-writedouble.md)

- [writeBoolean](mta://reference/misc/modules-filesystem-file-writeboolean.md)

- [size](mta://reference/misc/modules-filesystem-file-size.md)

- [stat](mta://reference/misc/modules-filesystem-file-stat.md)

- [tell](mta://reference/misc/modules-filesystem-file-tell.md)

- [seek](mta://reference/misc/modules-filesystem-file-seek.md)

- [eof](mta://reference/misc/modules-filesystem-file-eof.md)

- [flush](mta://reference/misc/modules-filesystem-file-flush.md)

- [isWritable](mta://reference/misc/modules-filesystem-file-iswritable.md)

- [isReadable](mta://reference/misc/modules-filesystem-file-isreadable.md)
