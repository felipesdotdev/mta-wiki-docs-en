---
doc_id: "mta-wiki:14293"
title: "MTA:SA Developers: Mobile"
source_title: "MTA:SA Developers: Mobile"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3ASA_Developers%3A_Mobile"
revision_id: 82706
language: "en"
categories: []
---

# MTA:SA Developers: Mobile

|  |
| --- |

## Introduction

MTA:SA Developers: Mobile — this is an improved version of the application [MTA Compiler & Script editor](https://forum.multitheftauto.com/topic/128180-mta-compiler-script-editor/), which contains a mobile version of the forum, wiki and MTA:SA community, an improved file manager with the ability to view Renderware models and the code editor.

## Features of the current version of the mobile application

 
MTA:SA developers: Mobile

- Viewing MTA:SA forum news feed, participating in discussions, viewing forum content in details

- Viewing MTA:SA Wiki

- Viewing MTA:SA Community, including browsing MTA:SA servers and downloading MTA:SA resources

- Viewing and editing files. Unpacking, viewing and editing zip-archives

- Compiling Lua scripts directly in the archive

- Viewing Renderware models, including a visual view of the model as well as a view of the model dump

- Viewing and editing script code

- Compressing opened files into a zip-archive

- Choosing of dark or light theme

- Opening MTA:SA links directly in the application

## Mobile application installation

You can install the mobile application on an Android device version 7 and higher:

- Install on Google play: [https://play.google.com/store/apps/details?id=ru.limedev.mtacse](https://play.google.com/store/apps/details?id=ru.limedev.mtacse)

- Install on Huawei App Gallery: [https://appgallery.huawei.com/#/app/C103285117](https://appgallery.huawei.com/#/app/C103285117)

## Changelog

### Version 3.1.2

- Improved stability on new versions of Android

- Added support for Portuguese and Indonesian languages

### Version 3.1.1

- Updated rwparser library, tested on a broken and empty file

- Added hints for the Lua language in the code editor

- Additional Wiki pages have been implemented

- Adding / removing files to / from archive has been implemented

- New design of the main page of the file manager has been implemented (added feature of creating resources from ready-made templates)

- Implemented a folder selection dialog when adding a file to the archive

- An analysis of the implementation of notifications in the application was carried out. Implemented notifications in the application

- Implemented setting the XML file type in the code editor when importing the corresponding code from Wiki

- Fixed a bug when opening a file and endless loading

- Added clearing cache data when opening new files in the file manager

### Version 3.1

In version 3.1 of the application, the additional "More" tab in the navigation panel was mainly improved. The application version includes:

- Dark theme

- Ability to view Renderware models, including a visual representation of the model, as well as viewing a dump of the model

- Reading mode in the code editor

- Highlighting code blocks on the forum

- More Screen

- Settings screen where you can configure:

- Application theme

- Enable / Disable code wrapping on the forum

- Enable / Disable automatic video start on the forum

- Load localized Wiki pages

- Enable MTA:SA Wiki deeplinks for Android 12+ (it is disabled by default)

- Community MTA:SA screen containing:

- Recently uploaded resources that you can download

- MTA:SA Server List screen with the ability to:

- View a sorted list of MTA:SA servers

- Edit list of favorite servers

- Screen with partners

- MTA:SA Wiki deeplinks

- Embedded browser

### Version 3.0.2

- Fixed application crash when opening empty archives

- Fixed bugs in opening dialogs about saving files and archives

- Application architecture optimization

### Version 3.0.1

- Added syntax highlighting in Wiki code blocks

- Added copying and importing code from Wiki to the code editor

- Fixed FPS drop when scrolling HTML and XML code in the code editor

- Added a standard name when creating a file from the code editor

- Added saving of opened file in the file manager

- Added synchronization with the physical keyboard in the code editor, hotkeys:

- CTRL + <- (move the caret to the beginning of the line)

- CTRL + -> (move the caret to the end of the line)

- ALT + <- (caret shift to previous word)

- ALT + -> (caret shift to next word)

- CTRL + Z (undo)

- CTRL + Y (redo)

- CTRL + S (save file)

- CTRL + D (clear code editor)

- ALT + M (open code editor menu)

- ALT + ↓ (hide tabs)

- ALT + ↑ (show tabs)

### Version 3.0

Application version 3.0 implements a Minimum Viable Product (MVP), which includes:

- Mobile version of MTA:SA forum

- Mobile version of MTA:SA Wiki

- Improved file manager

- Mobile code editor

Now, unlike MTA Compiler & Script editor, the file manager has the ability to work separately with archives and individual files, as well as the ability to save and encrypt both a separate script and the entire archive with a resource. The code editor has acquired a new engine, it has become more convenient to work with. Also, in addition to XML, Lua, HLSL syntaxes, I introduced into it support for HTML syntax with support for Lua functions.

## Contact

You can contact the application developer:

- In [created topic](https://forum.multitheftauto.com/topic/141940-mtasa-developers-mobile/) on the forum

- Going to the [developer's website](https://limedev.ru/)

- Via Discord @limedev.ru
