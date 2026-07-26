---
doc_id: "mta-wiki:7046"
title: "Error Codes"
source_title: "Error Codes"
source_url: "https://wiki.multitheftauto.com/wiki/Error_Codes"
revision_id: 81428
language: "en"
categories: []
---

# Error Codes

| Error Code | Associated strings | File:LineNumber |
| --- | --- | --- |
| CC20 | Error Invalid nick provided | Client\core\CConnectManager.cpp:77 |
| CC21 | Error Invalid host provided | Client\core\CConnectManager.cpp:104 |
| CC22 | Error Failed to connect | Client\core\CConnectManager.cpp:120 |
| CC23 | Error Connection timed out connect-timed-out | Client\core\CConnectManager.cpp:258 |
| CC24 | Disconnected: unknown protocol error encryption key mismatch | Client\core\CConnectManager.cpp:272 |
| CC25 | Disconnected: disconnected remotely | Client\core\CConnectManager.cpp:278 |
| CC26 | Disconnected: connection lost remotely | Client\core\CConnectManager.cpp:281 |
| CC27 | Disconnected: you are banned from this server | Client\core\CConnectManager.cpp:284 |
| CC28 | Disconnected: disconnected from the server | Client\core\CConnectManager.cpp:290 |
| CC29 | Disconnected: connection to the server was lost | Client\core\CConnectManager.cpp:293 |
| CC30 | Disconnected: connection was refused | Client\core\CConnectManager.cpp:299 |
| CC31 | Error Mod loading failed | Client\core\CConnectManager.cpp:393 |
| CC32 | Error Bad server response (2) | Client\core\CConnectManager.cpp:400 |
| CC33 | Error Bad server response (1) [%d] | Client\core\CConnectManager.cpp:410 |
| CC34 | Disconnected: unknown protocol error old raknet version | Client\core\CConnectManager.cpp:275 |
| CC40 | %s module is incorrect! Error | Client\core\CCore.cpp:829 |
| CC41 | Error Error executing URL | Client\core\CCore.cpp:1162 |
| CC42 | Error Command line Mod load failed | Client\core\CCore.cpp:1175 |
| CC43 | Fatal error | Client\core\CCore.cpp:660 |
| CC50 | Error Could not initialize Direct3D9. Please ensure the DirectX End-User Runtime and latest Windows Service Packs are installed correctly. | Client\core\DXHook\CDirect3DHook9.cpp:120 |
| CC51 | The skin you selected could not be loaded, and the default skin also could not be loaded, please reinstall MTA. Error | Client\core\CGUI.cpp:83 |
| CC70 | Error No address specified! | Client\core\Serverbrowser\CServerBrowser.cpp:1222 |
| CC71 | Unknown protocol Please use the mtasa:// protocol! | Client\core\Serverbrowser\CServerBrowser.cpp:1235 |
| CC72 | Error Invalid nickname! Please go to Settings and set a new one! | Client\core\Serverbrowser\CServerBrowser.cpp:1244 |
| CC73 | Error Invalid nickname! Please go to Settings and set a new one! | Client\core\Serverbrowser\CServerBrowser.cpp:1301 |
| CC74 | Information You have to select a server to connect to. | Client\core\Serverbrowser\CServerBrowser.cpp:1323 |
| CC75 | Error No address specified! | Client\core\Serverbrowser\CServerBrowser.cpp:1351 |
| CC80 | Error Please disconnect before changing skin | Client\core\Settings\CInterfaceSettingsTab.cpp:531 |
| CC81 | Error Your nickname contains invalid characters! | Client\core\Settings\CMultiplayerSettingsTab.cpp:237 |
| CC82 | Error Please disconnect before changing language | Client\core\Settings\CInterfaceSettingsTab.cpp:503 |
| CC99 | PLEASE WAIT.................... | Client\core\CGUI.cpp:243 |
| CD01 | Error Invalid nickname! Please go to Settings and set a new one! | Client\mods\deathmatch\logic\CClientGame.cpp:556 |
| CD02 | Error Not connected; please use Quick Connect or the 'connect' command to connect to a server. | Client\mods\deathmatch\logic\CClientGame.cpp:619 |
| CD03 | Error Invalid nickname! Please go to Settings and set a new one! | Client\mods\deathmatch\logic\CClientGame.cpp:655 |
| CD04 | Error The server is not installed | Client\mods\deathmatch\logic\CClientGame.cpp:677 |
| CD05 | Error You were kicked from the game ( %s ) | Client\mods\deathmatch\logic\CClientGame.cpp:1004 |
| CD06 | Error Error connecting to server. | Client\mods\deathmatch\logic\CClientGame.cpp:1084 |
| CD07 | Error Connecting to local server timed out. See console for details. | Client\mods\deathmatch\logic\CClientGame.cpp:1094 |
| CD08 | Error Connection timed out connect-timed-out | Client\mods\deathmatch\logic\CClientGame.cpp:1163 |
| CD09 | Error Connection with the server was lost | Client\mods\deathmatch\logic\CClientGame.cpp:1197 |
| CD10 | Disconnected: unknown protocol error encryption key mismatch | Client\mods\deathmatch\logic\CClientGame.cpp:1208 |
| CD11 | Disconnected: disconnected remotely | Client\mods\deathmatch\logic\CClientGame.cpp:1211 |
| CD12 | Disconnected: connection lost remotely | Client\mods\deathmatch\logic\CClientGame.cpp:1214 |
| CD13 | Disconnected: you are banned from this server | Client\mods\deathmatch\logic\CClientGame.cpp:1217 |
| CD14 | Disconnected: the server is currently full | Client\mods\deathmatch\logic\CClientGame.cpp:1220 |
| CD15 | Disconnected: disconnected from the server | Client\mods\deathmatch\logic\CClientGame.cpp:1223 |
| CD16 | Disconnected: connection to the server was lost | Client\mods\deathmatch\logic\CClientGame.cpp:1226 |
| CD17 | Disconnected: invalid password specified | Client\mods\deathmatch\logic\CClientGame.cpp:1229 |
| CD18 | Disconnected: connection was refused | Client\mods\deathmatch\logic\CClientGame.cpp:1232 |
| CD19 | Error MTA Client verification failed! | Client\mods\deathmatch\logic\CClientGame.cpp:1249 |
| CD20 | Error HTTP Error | Client\mods\deathmatch\logic\CResourceFileDownloadManager.cpp:138 |
| CD30 | Disconnected: Invalid nickname | Client\mods\deathmatch\logic\CPacketHandler.cpp:470 |
| CD31 | Disconnect from server | Client\mods\deathmatch\logic\CPacketHandler.cpp:473 |
| CD32 | Disconnected: Serial is banned.\nReason: %s | Client\mods\deathmatch\logic\CPacketHandler.cpp:476 |
| CD33 | Disconnected: You are banned.\nReason: %s | Client\mods\deathmatch\logic\CPacketHandler.cpp:481 |
| CD34 | Disconnected: Account is banned.\nReason: %s | Client\mods\deathmatch\logic\CPacketHandler.cpp:486 |
| CD35 | Disconnected: Version mismatch | Client\mods\deathmatch\logic\CPacketHandler.cpp:490 |
| CD36 | Disconnected: Join flood. Please wait a minute, then reconnect. | Client\mods\deathmatch\logic\CPacketHandler.cpp:493 |
| CD37 | Disconnected: Server from different branch.\nInformation: %s | Client\mods\deathmatch\logic\CPacketHandler.cpp:496 |
| CD38 | Disconnected: Bad version.\nInformation: %s | Client\mods\deathmatch\logic\CPacketHandler.cpp:500 |
| CD39 | Disconnected: Server is running a newer build.\nInformation: %s | Client\mods\deathmatch\logic\CPacketHandler.cpp:504 |
| CD40 | Disconnected: Server is running an older build.\nInformation: %s | Client\mods\deathmatch\logic\CPacketHandler.cpp:508 |
| CD41 | Disconnected: Nick already in use | Client\mods\deathmatch\logic\CPacketHandler.cpp:512 |
| CD42 | Disconnected: Player Element Could not be created. | Client\mods\deathmatch\logic\CPacketHandler.cpp:515 |
| CD43 | Disconnected: Server refused the connection: %s | Client\mods\deathmatch\logic\CPacketHandler.cpp:518 |
| CD44 | Disconnected: Serial verification failed | Client\mods\deathmatch\logic\CPacketHandler.cpp:522 |
| CD45 | Disconnected: Connection desync %s | Client\mods\deathmatch\logic\CPacketHandler.cpp:525 |
| CD46 | Disconnected: You were kicked by %s | Client\mods\deathmatch\logic\CPacketHandler.cpp:533 |
| CD47 | Disconnected: You were banned by %s | Client\mods\deathmatch\logic\CPacketHandler.cpp:537 |
| CD48 | %s Custom disconnect reason | Client\mods\deathmatch\logic\CPacketHandler.cpp:542 |
| CD49 | Disconnected: Server shutdown or restarting | Client\mods\deathmatch\logic\CPacketHandler.cpp:546 |
| CD50 | Disconnected: Serial already in use | Client\mods\deathmatch\logic\CPacketHandler.cpp:575 |
| CD60 | Error Could not start the local server. See console for details. | Client\mods\deathmatch\logic\CServer.cpp:193 |
| CD61 | Error DoDisconnectRemote | Shared\mods\deathmatch\logic\CLatentTransferManager.cpp:374 |
| CD62 | Fatal error | Client\mods\deathmatch\logic\Utils.cpp:149 |
| CD63 | Connection error Protocol error | Client\mods\deathmatch\logic\Utils.cpp:166 |
| CD64 | This version has expired. MTA: San Andreas | Client\mods\deathmatch\CClient.cpp:41 |
| CL01 | MTA:SA could not complete the following task:\n\n '%s'\n Multi Theft Auto: San Andreas | Client\loader\CInstallManager.cpp:350 |
| CL02 | Could not update due to file conflicts. Please close other applications and retry Error | Client\loader\CInstallManager.cpp:533 |
| CL03 | Multi Theft Auto has not been installed properly, please reinstall. %s Error | Client\loader\CInstallManager.cpp:542 |
| CL04 | Error Trouble restarting MTA:SA | Client\loader\MainFunctions.cpp:227 |
| CL05 | Another instance of MTA is already running.\n\nIf this problem persists, please restart your computer Error | Client\loader\MainFunctions.cpp:240 |
| CL06 | Another instance of MTA is already running.\n\nDo you want to terminate it? Error | Client\loader\MainFunctions.cpp:243 |
| CL07 | Are you having problems running MTA:SA?.\n\nDo you want to revert to an earlier version? MTA: San Andreas | Client\loader\MainFunctions.cpp:267 |
| CL08 | There seems to be a problem launching MTA:SA.\nResetting GTA settings can sometimes fix this problem.\n\nDo you want to reset GTA settings now? MTA: San Andreas | Client\loader\MainFunctions.cpp:295 |
| CL09 | File could not be deleted: '%s' Error | Client\loader\MainFunctions.cpp:309 |
| CL10 | An instance of GTA: San Andreas is already running. It needs to be terminated before MTA:SA can be started. Do you want to do that now? Information | Client\loader\MainFunctions.cpp:552 |
| CL11 | Unable to terminate GTA: San Andreas. If the problem persists, please restart your computer. Information | Client\loader\MainFunctions.cpp:557 |
| CL12 | Registry entries are missing. Please reinstall Multi Theft Auto: San Andreas. reg-entries-missing | Client\loader\MainFunctions.cpp:579 |
| CL13 | The path to your installation of GTA: San Andreas contains unsupported (unicode) characters. Please move your Grand Theft Auto: San Andreas installation to a compatible path that contains only standard ASCII characters and reinstall Multi Theft Auto: San Andreas. | Client\loader\MainFunctions.cpp:583 |
| CL14 | It appears you have a Steam version of GTA:SA, which is currently incompatible with MTASA. You are now being redirected to a page where you can find information to resolve this issue. | Client\loader\MainFunctions.cpp:587 |
| CL15 | move your installation(s) to a path that does not contain a semicolon. path-semicolon | Client\loader\MainFunctions.cpp:603 |
| CL16 | Load failed. Please ensure that the latest data files have been installed correctly. mta-datafiles-missing | Client\loader\MainFunctions.cpp:741 |
| CL17 | Load failed. Please ensure that the latest data files have been installed correctly. mta-datafiles-missing | Client\loader\MainFunctions.cpp:748 |
| CL18 | Load failed. Please ensure that %s is installed correctly. client-missing | Client\loader\MainFunctions.cpp:755 |
| CL20 | Load failed. Could not find gta_sa.exe in %s. gta_sa-missing | Client\loader\MainFunctions.cpp:762 |
| CL21 | Load failed. %s exists in the GTA directory. Please delete before continuing. file-clash | Client\loader\MainFunctions.cpp:772 |
| CL22 | contact MTA at www.multitheftauto.com. \n\n[%s] createprocess-fail&err= Could not start GTA:SA | Client\loader\MainFunctions.cpp:1128 |
| CL23 | directory within the MTA root directory. core-missing Core.dll missing | Client\loader\MainFunctions.cpp:60 |
| CL24 | and the latest DirectX is correctly installed. vc-redist-missing Core.dll load failed. Ensure VC++ Redists and DX are installed | Client\loader\MainFunctions.cpp:93 |
| CL25 | GTA: San Andreas may not have launched correctly. Do you want to terminate it? Information | Client\loader\MainFunctions.cpp:1187 |
| CL26 | and the latest DirectX is correctly installed. vc-redist-missing Core.dll load failed. Ensure VC++ Redists and DX are installed | Client\loader\MainFunctions.cpp:116 |
| CL28 | Remove these .asi files if you experience problems with MTA:SA. asi-files | Client\loader\MainFunctions.cpp:831 |
| CL29 | maybe-virus1 | Client\loader\MainFunctions.cpp:793 |
| CL30 | Data files modified. Possible virus activity.\n\nSee online help if MTA does not work correctly. maybe-virus2 | Client\loader\MainFunctions.cpp:819 |
| CL31 | gta-fopen-fail&name=%s | Client\loader\Utils.cpp:1775 |
| CL33 | Error | Client\loader\MainFunctions.cpp:781 |
| CL34 | gta-model-fail&id=%d&reason=%s | Client\loader\Utils.cpp:1826 |
| CL35 | gta-upgrade-fail&id=%d&upgid=%d&frame=%d | Client\loader\Utils.cpp:1853 |
| CL36 | gta-file-missing&name=%s | Client\loader\Utils.cpp:1798 |
| CL37 |  | Client\loader\MainFunctions.cpp:421 |
| CL38 | module-not-loadable&name= | Client\loader\Utils.cpp:1300 |
| CL39 | forboden-programs | Client\loader\Utils.cpp:2021 |
| CL40 | bad-file-version | Client\loader\MainFunctions.cpp:897 |
| CL41 | missing-file | Client\loader\MainFunctions.cpp:906 |
| CL42 | safe-mode | Client\loader\MainFunctions.cpp:917 |
| CL43 | not-used-menu-evolve | Client\loader\MainFunctions.cpp:387 |
| CL44 | img-file-corrupt&name=%s | Client\loader\Utils.cpp:1872 |
| U01 | Multi Theft Auto has not been installed properly, please reinstall. Error | Shared\sdk\SharedUtil.Misc.hpp:84 |
