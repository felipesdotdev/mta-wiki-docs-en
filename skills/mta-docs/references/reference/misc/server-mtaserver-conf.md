---
doc_id: "mta-wiki:5974"
title: "Server mtaserver.conf"
source_title: "Server mtaserver.conf"
source_url: "https://wiki.multitheftauto.com/wiki/Server_mtaserver.conf"
revision_id: 82471
language: "en"
categories: ["Support"]
---

# Server mtaserver.conf

This page lists the settings that can be set in the settings file. *Setting from the default **mtaserver.conf** settings file is in italics*.

## Settings

#### servername

*<servername>Default MTA Server</servername>*

This parameter specifies the name the server will be visible as in the ingame server browser and on Game-Monitor. It is a required parameter.

#### rule

*<rule name="NAME_HERE" value="VALUE_HERE"/>*

The rule parameters are optional. There can be as many as you want in the config file. They contain information for the Server Browser/List. [Read this article for more information](mta://reference/misc/server-browser-rules.md).

#### owner_email_address

*<owner_email_address></owner_email_address>*

This parameter specifies the contact email addresses for the owner(s) of this server.

The email addresses will not be publicly available, and only used by MTA administrators to contact the server owner.

Note: Missing or incorrect owner_email_address can affect visibility in the master server list.

Values: Comma separated list of email addresses

#### serverip

*<serverip>auto</serverip>*

**ONLY USE THIS PARAMETER IF YOU ARE SURE OF WHAT YOU ARE DOING** - it is generally only needed for complex network topologies and should be left at the default value otherwise.

This parameter specifies the public IP address that the server will announce to the MTA servers, for the purposes of registering itself in the master server list and receiving some internal status updates. Usually, setting this parameter is only useful for some specialized scenarios, like servers that can be reached by multiple public addresses, or when a firewall is used for controlling incoming connections. If set to auto, the public IP address the requests originate from will be used as the server IP for communicating with MTA servers, which works fine in most cases.

Values: auto or x.x.x.x ; default value: auto

SERVERIP SHOULD BE LEFT SET TO auto UNLESS YOU ARE SURE OF WHAT YOU ARE DOING

WARNING: SETTING serverip AND THEN ASKING FOR SUPPORT CAN CAUSE DEATH OR INJURY

#### serverport

*<serverport>22003</serverport>*

This parameter specifies the UDP port on which the server will be accepting incoming player connections;

default value: 22003. It is a required parameter.

#### maxplayers

*<maxplayers>32</maxplayers>*

This parameter specifies the number of maximum player slots available on the server;

default value: 32. It is a required parameter.

#### httpserver

*<httpserver>1</httpserver>*

This parameter specifies whether the built-in http server will be used.

Values: 0 - disabled , 1 - enabled ; default value: 1. Optional parameter.

More information: [Using the web interface](mta://getting-started/server-manual.md)

#### httpport

*<httpport>22005</httpport>*

This parameter specifies the TCP port on which the server will be accepting incoming http connections. It can be set to the same value as <serverport>. It is a required parameter if <httpserver> is set to 1.

More information: [Using the web interface](mta://getting-started/server-manual.md)

#### httpdownloadurl

*<httpdownloadurl></httpdownloadurl>*

If set, this parameter specifies the external URL from which clients will be able to download needed resources ingame. Otherwise they will download them directly from the server.

More information: [Configuring an external web server](mta://getting-started/server-manual.md)

#### httpmaxconnectionsperclient

*<httpmaxconnectionsperclient>5</httpmaxconnectionsperclient>*

This parameter limits the number of http connections each client can make. Depending on the type of http server that is used, a lower figure may reduce download timeouts. Only relevant when using an external http server.

Available range: 1 to 8.

#### httpthreadcount

*<httpthreadcount>8</httpthreadcount>*

Number of HTTP server threads.

Available range: 1 to 20. default value: 8

#### httpdosthreshold

*<httpdosthreshold>20</httpdosthreshold>*

This parameter limits the number http connections that an IP can initiate over a short period of time.

Available range: 1 to 100. default value: 20

#### http_dos_exclude

*<http_dos_exclude></http_dos_exclude>*

This parameter lists the IP addresses that are to be excluded from http dos threshold limits.

e.g. 88.11.22.33,101.2.3.4

#### allow_gta3_img_mods

*<allow_gta3_img_mods>none</allow_gta3_img_mods>*

By default, the server will block the use of locally customized gta3.img player skins

This setting can be used to allow such mods. Not recommended for competitive servers.

Values: none, peds ; default value: none

#### client_file

*<!-- <client_file name="data/carmods.dat" verify="0" /> -->*

By default, the server will block the use of customized GTA:SA data files.

To allow specific client files, add one or more of the above lines.

More information: [Anti-cheat guide](mta://scripting/concepts/anti-cheat-guide.md)

#### disableac

*<disableac></disableac>*

Comma separated list of disabled anti-cheats.

e.g. To disable anti-cheat #2 and #3, use: 2,3

More information: [Anti-cheat guide](mta://scripting/concepts/anti-cheat-guide.md)

#### enablesd

*<enablesd>31,32</enablesd>*

Comma separated list of enabled special detections. A special detection is a type of anti-cheat for (usually) harmless game modifications.

Competitive servers may wish to enable certain special detections, but most servers should leave this setting on its default.

Values: special detection (SD) codes ; default value: 31,32 (e.g. enables special detections #31 and #32)

More information: [Anti-cheat guide](mta://scripting/concepts/anti-cheat-guide.md)

#### hideac

*<hideac>0</hideac>*

When this parameter is enabled client won't get any info about Anticheat settings when connecting to server.

Values: 0 - disabled , 1 - enabled ; default value: 0. Optional parameter.

#### minclientversion

*<minclientversion></minclientversion>*

Minimum client version. Clients with a lower version will not be allowed to connect. After disconnection, clients will be given an opportunity to download an update. If left blank, this setting is disabled and there are no restrictions on who can connect. Version numbers are described in [getPlayerVersion](mta://scripting/server/functions/getplayerversion.md) and look like this: 1.6.0-9.22953.0

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

**Note that this setting only determines if the client should be prompted to update. The actual build number they receive will be the [[highest available](https://nightly.mtasa.com/ver)].**

#### minclientversion_auto_update

*<minclientversion_auto_update>1</minclientversion_auto_update>*

This parameter specifies if/when the <minclientversion> setting is automatically updated.

Keeping <minclientversion> updated can help reduce cheating.

Note: The instant setting (2) is only recommended for competitive servers.

Values: 0 - disabled, 1 - enabled (delayed by a few days), 2 - enabled (instant) ; default value: 1.

#### recommendedclientversion

*<recommendedclientversion></recommendedclientversion>*

Recommended client version. When connecting, if clients have a lower version, they will be given the option to download an update. If left blank, this setting is disabled.

This parameter can changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

**Note that this setting only determines if the client should be prompted to update. The actual build number they receive will be the [[highest available](https://nightly.mtasa.com/ver)].**

#### ase

*<ase>1</ase>*

This parameter can be used to make the server report to Game-Monitor master servers, allowing it to be visible in the in-game server browser. An additional UDP port needs to be available for this to work (value from <serverport> + 123 , so on a default <serverport> value 22003 the right port will be 22126 ).

Available values: 0 - disabled , 1 - enabled. Optional parameter, defaults to 0.

#### donotbroadcastlan

*<donotbroadcastlan>0</donotbroadcastlan>*

This parameter allows you to disable LAN broadcasting.

#### password

*<password></password>*

If set, players will have to provide a password specified below, before they can connect to the server. If left blank, server doesn't require a password from them.

This parameter can changed and saved while the server is running with [setServerPassword](mta://scripting/server/functions/setserverpassword.md) or [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

#### net_auto_filter

*<net_auto_filter>1</net_auto_filter>*

**ONLY USE THIS PARAMETER IF YOU ARE SURE OF WHAT YOU ARE DOING**

Net auto filter.

Values: 0 - disabled, 1 - enabled. default value: 1

#### update_cycle_datagrams_limit

*<update_cycle_datagrams_limit>4</update_cycle_datagrams_limit>*

**ONLY USE THIS PARAMETER IF YOU ARE SURE OF WHAT YOU ARE DOING**

Send datagrams limit.

Available range: 1 to 100. default value: 4

#### update_cycle_messages_limit

*<update_cycle_messages_limit>50</update_cycle_messages_limit>*

**ONLY USE THIS PARAMETER IF YOU ARE SURE OF WHAT YOU ARE DOING**

Send messages limit.

Available range: 10 to 1000. default value: 50

#### bandwidth_reduction

*<bandwidth_reduction>medium</bandwidth_reduction>*

This parameter reduces the server's bandwidth usage by using various optimizations.

Values: none, medium or maximum ; default value: medium

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

Bandwidth reduction causes de-sync when players are on mapped objects [See GitHub issue](https://github.com/multitheftauto/mtasa-blue/issues/4460)

#### unoccupied_vehicle_syncer_distance

*<unoccupied_vehicle_syncer_distance>130</unoccupied_vehicle_syncer_distance>*

This parameter determines the distance limit for remote synced unoccupied vehicles

Available range: 50 - 400; default value: 130

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

#### ped_syncer_distance

*<ped_syncer_distance>100</ped_syncer_distance>*

This parameter determines the distance limit for remote synced peds

Available range: 50 - 400; default value: 100

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

#### player_sync_interval

*<player_sync_interval>100</player_sync_interval>*

This parameter determines the time in milliseconds between player sync packets.

Available range: 50 - 4000; default value: 100

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

Suggested values for this and the other sync_interval settings can be found here: [Sync interval settings](mta://reference/misc/sync-interval-settings.md)

#### lightweight_sync_interval

*<lightweight_sync_interval>1500</lightweight_sync_interval>*

This parameter determines the time in milliseconds between lightweight (player) sync packets.

Available range: 200 - 4000; default value: 1500

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

Suggested values for this and the other sync_interval settings can be found here: [Sync interval settings](mta://reference/misc/sync-interval-settings.md)

#### camera_sync_interval

*<camera_sync_interval>500</camera_sync_interval>*

This parameter determines the time in milliseconds between camera sync packets.

Available range: 50 - 4000; default value: 500

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

Suggested values for this and the other sync_interval settings can be found here: [Sync interval settings](mta://reference/misc/sync-interval-settings.md)

#### ped_sync_interval

*<ped_sync_interval>500</ped_sync_interval>*

This parameter determines the time in milliseconds between ped sync packets when the ped is near the player.

Available range: 50 - 4000; default value: 500

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

Suggested values for this and the other sync_interval settings can be found here: [Sync interval settings](mta://reference/misc/sync-interval-settings.md)

#### ped_far_sync_interval

*<ped_far_sync_interval>2000</ped_far_sync_interval>*

This parameter determines the time in milliseconds between ped sync packets when the ped is far away from the player.

Available range: 50 - 4000; default value: 2000

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

Suggested values for this and the other sync_interval settings can be found here: [Sync interval settings](mta://reference/misc/sync-interval-settings.md)

#### unoccupied_vehicle_sync_interval

*<unoccupied_vehicle_sync_interval>400</unoccupied_vehicle_sync_interval>*

This parameter determines the time in milliseconds between unoccupied vehicle sync packets.

Available range: 50 - 4000; default value: 400

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

Suggested values for this and the other sync_interval settings can be found here: [Sync interval settings](mta://reference/misc/sync-interval-settings.md)

#### keysync_mouse_sync_interval

*<keysync_mouse_sync_interval>100</keysync_mouse_sync_interval>*

This parameter determines the minimum time in milliseconds between key sync packets due to mouse movement.

Available range: 50 - 4000; default value: 100

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

Suggested values for this and the other sync_interval settings can be found here: [Sync interval settings](mta://reference/misc/sync-interval-settings.md)

#### keysync_analog_sync_interval

*<keysync_analog_sync_interval>100</keysync_analog_sync_interval>*

This parameter determines the minimum time in milliseconds between key sync packets due to joystick movement.

Available range: 50 - 4000; default value: 100

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

Suggested values for this and the other sync_interval settings can be found here: [Sync interval settings](mta://reference/misc/sync-interval-settings.md)

#### donkey_work_interval

*<donkey_work_interval>100</donkey_work_interval>*

Update near list interval in milliseconds.

Available range: 50 to 4000. default value: 100

#### bullet_sync

*<bullet_sync>1</bullet_sync>*

This parameter can improve the reliability of shots when using certain weapons. However, it uses more bandwidth.

Note that bullet sync will be active regardless of this setting when certain [glitches](mta://scripting/server/functions/setglitchenabled.md) are enabled.

Values: 0 - disabled , 1 - enabled ; default value: 1.

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430))

#### vehicle_contact_sync_radius

*<vehicle_contact_sync_radius>30</vehicle_contact_sync_radius>*

This parameter specifies the radius in which any contact with a vehicle will turn the player into its syncer.

Changing this setting to 0 will cause vehicles to not pick a new syncer based on which player is touching the vehicle.

Available range: 0 to 130.  Default - 30

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

#### vehext_percent

*<vehext_percent>0</vehext_percent>*

This parameter sets the amount of extrapolation that clients will apply to remote vehicles.

This can reduce some of the latency induced location disparency by predicting where the remote vehicles will probably be.

Depending on the gamemode, an incorrect prediction may have a negative effect.

Therefore this setting should be considered experimental.

Available range: 0 to 100.  Default - 0

#### vehext_ping_limit

*<vehext_ping_limit>150</vehext_ping_limit>*

This parameter places a limit on how much time (in milliseconds) the vehicle extrapolation will attempt to compensate for.

Only relevant if <vehext_percent> is greater than zero.

Available range: 50 to 500.  Default - 150

#### latency_reduction

*<latency_reduction>0</latency_reduction>*

This parameter can reduce the delay of player actions appearing on remote clients by 2 frames (approx 50ms).

Due to the impact this may have on shot lag compensation, it should be considered experimental.

Values: 0 - disabled , 1 - enabled ; default value: 0.

Bugs caused by enabling latency_reduction: [https://bugs.mtasa.com/view.php?id=8191](https://bugs.mtasa.com/view.php?id=8191) + [https://bugs.mtasa.com/view.php?id=8226](https://bugs.mtasa.com/view.php?id=8226)

#### threadnet

*<threadnet>1</threadnet>*

This parameter specifies whether or not to run the network synchronization on another thread.

Enabling will make the sync smoother, but may increase CPU usage slightly.

Values: 0 - disabled , 1 - enabled ; default value: 1.

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

#### idfile

*<idfile>server-id.keys</idfile>*

Specifies the location and file name of this servers unique private key. This is used to prevent private files saved on the client from being read by other servers.

Keep a backup of this file in a safe place. Default value: server-id.keys

More information about client private files: [Filepath](mta://reference/misc/filepath.md)

#### logfile

*<logfile>logs/server.log</logfile>*

Specifies the location and name of the main server log file. If left blank, server won't be saving this file.

#### authfile

*<authfile>logs/server_auth.log</authfile>*

As well as the main log file, login successes and failures are logged here for easy reviewing of security issues. If left blank, this file is not used

#### dbfile

*<dbfile>logs/db.log</dbfile>*

Specifies the location and name of the file used to log database queries. The server command [debugdb](mta://reference/misc/server-commands.md) sets the amount of logging.

#### loadstringfile

*<!-- <loadstringfile>logs/loadstring.log</loadstringfile> -->*

Specifies the location and name of the file used to log loadstring function calls. If left blank or not set, no logging is done.

#### acl

*<acl>acl.xml</acl>*

This parameter specifies the location and name of the Access Control List settings file. If left

blank, server will use acl.xml file, located in the same folder as this configuration file.

#### scriptdebuglogfile

*<scriptdebuglogfile>logs/scripts.log</scriptdebuglogfile>*

Specifies the location and name of the debugscript log file. If left blank, server won't be saving this file.

#### scriptdebugloglevel

*<scriptdebugloglevel>0</scriptdebugloglevel>*

Specifies the level of the debugscript log file. Available values: 0, 1, 2, 3. When not set, defaults to 0.

#### htmldebuglevel

*<htmldebuglevel>0</htmldebuglevel>*

Specifies the level of the html debug. Available values: 0, 1, 2, 3. When not set, defaults to 0.

#### filter_duplicate_log_lines

*<filter_duplicate_log_lines>1</filter_duplicate_log_lines>*

Specifies whether or not duplicate log lines should be filtered. Available values: 0 or 1, defaults to 1.

#### fpslimit

*<fpslimit>74</fpslimit>*

Specifies the frame rate limit that will be applied to connecting clients.

Available range: 25 to 32767. Default: 74. You can also use 0 for uncapped fps.

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

#### voice

*<voice>0</voice>*

This parameter specifies whether or not to enable player voice chat in-game

Values: 0 - disabled , 1 - enabled

#### voice_samplerate

*<voice_samplerate>1</voice_samplerate>*

This parameter specifies the sample rate for voice chat.  'voice' parameter must be set to 1 for this to be effective. Higher settings use more bandwidth and increase the sampling quality of voice chat

Values: 0 - Narrowband (8kHz), 1 - Wideband (16kHz), 2 - Ultrawideband (32kHz).  Default - 1

#### voice_quality

*<voice_quality>4</voice_quality>*

This parameter specifies the voice quality for voice chat.  'voice' parameter must be set to 1 for this to be effective. Higher settings use more bandwidth and increase the the overall quality of voice chat

Available range: 0 to 10.  Default - 4

#### voice_bitrate

*<!-- <voice_bitrate>24600</voice_bitrate> -->*

Specifies the voice bitrate, in bps. This optional parameter overrides the previous two settings. If not set, MTA handles this automatically.  Use with care.

#### backup_path

*<backup_path>backups</backup_path>*

This parameter specifies the path to use for a basic backup of some server files. Note that basic backups are only made during server startup. Default value: backups

#### backup_interval

*<backup_interval>3</backup_interval>*

This parameter specifies the number of days between each basic backup. Backups are only made during server startup, so the actual interval maybe much longer. Setting backup_interval to 0 will disable backups

Available range: 0 to 30.  Default - 3

#### backup_copies

*<backup_copies>10</backup_copies>*

This parameter specifies the maximum number of backup copies to keep. Setting backup_copies to 0 will disable backups

Available range: 0 to 100.  Default - 10

#### compact_internal_databases

*<compact_internal_databases>1</compact_internal_databases>*

This parameter specifies when the internal sqlite databases should be defragmented.

For more info see: [https://www.sqlite.org/lang_vacuum.html](https://www.sqlite.org/lang_vacuum.html)

Values: 0 - Never, 1 - On server start only after basic backup, 2 - On server start always.  Default - 1

#### server_logic_fps_limit

*<server_logic_fps_limit>0</server_logic_fps_limit>*

**ONLY USE THIS PARAMETER IF YOU ARE SURE OF WHAT YOU ARE DOING**

Server logic FPS limit.

Available range: 0 to 100. default value: 0

#### crash_dump_upload

*<crash_dump_upload>1</crash_dump_upload>*

This parameter specifies whether server crash dump files should be sent to MTA HQ.

Values: 0 - Off, 1 - On. Default - 1

#### fakelag

*<fakelag>0</fakelag>*

This parameter specifies whether the [fakelag and sfakelag](mta://reference/misc/command-fakelag.md) commands are enabled

Values: 0 - Off, 1 - On. Default - 0

#### auth_serial_groups

*<auth_serial_groups>Admin</auth_serial_groups>*

This parameter lists the ACL groups that are protected by serial authorization.

Login attempts to a protected account from a second serial are blocked until the serial is manually authorized via the authserial command.

For more info see: [https://mtasa.com/authserial](https://mtasa.com/authserial)

Note: This is security critical feature and disabling auth_serial_groups can affect visibility in the master server list.

Values: Comma separated list of ACL groups.  Default - Admin

See [Authorized Serial Account Protection](mta://reference/misc/authorized-serial-account-protection.md) for more information.

#### auth_serial_http

*<auth_serial_http>1</auth_serial_http>*

This parameter specifies if the authorized serial login checks should also apply to the http interface.

Protected account login attempts to the http interface will only succeed if the IP address matches one recently used by the account holder in-game.

For more info see: [https://mtasa.com/authserialhttp](https://mtasa.com/authserialhttp)

Note: This is security critical feature and disabling auth_serial_http can affect visibility in the master server list.

Values: 0 - Off, 1 - Enabled.  Default - 1

#### auth_serial_http_ip_exceptions

*<auth_serial_http_ip_exceptions>127.0.0.1</auth_serial_http_ip_exceptions>*

This parameter specifies which IP addresses should always pass auth_serial_http checks.

Values: Comma separated list of IP addresses

#### database_credentials_protection

*<database_credentials_protection>1</database_credentials_protection>*

This parameter specifies if extra security measures are applied to resources which use [dbConnect](mta://scripting/server/functions/dbconnect.md) with MySQL.

The extra measures are:

- script files cannot be accessed with [fileOpen](mta://scripting/shared/functions/fileopen.md)

- [meta.xml](mta://reference/misc/meta-xml.md) is read-only

**NOTE:** This only protects resources which use [dbConnect](mta://scripting/server/functions/dbconnect.md) with MySQL.

Values: 0 - disabled, 1 - enabled; default - 1

ADDED/UPDATED IN VERSION 1.6.0-22790 :

#### elementdata_whitelisted

*<elementdata_whitelisted>0</elementdata_whitelisted>*

Enables extra protection for [element data](mta://scripting/shared/functions/setelementdata.md).

When this option is enabled, the server ignores element data sync packets from the client, except for allowed keys. To allow a client to change a key, use setElementData(element, name, nil, true, "allow") first.

Values: 0 - disabled, 1 - enabled; default - 0

ADDED/UPDATED IN VERSION 1.6.0-22815 :

#### check_duplicate_serials

*<check_duplicate_serials>1</check_duplicate_serials>*

This parameter determines whether server will compare player serial on connection to any other serial present on server.

When this option is enabled, the server will deny entry for player whose serial is already in use by other player on server. You might want to disable this when using VMs.

Values: 0 - disabled, 1 - enabled; default - 1

#### player_triggered_event_interval

*<player_triggered_event_interval>1000</player_triggered_event_interval>*

Time interval for counting max (see below: max_player_triggered_events_per_interval) triggered events (via triggerServerEvent), exceeding this will call [onPlayerTriggerEventThreshold](mta://scripting/server/events/onplayertriggereventthreshold.md)

Values: 50-5000; default: 1000 (in ms)

#### max_player_triggered_events_per_interval

*<max_player_triggered_events_per_interval>100</max_player_triggered_events_per_interval>*

Max triggered amount of events (via triggerServerEvent) within interval above (player_triggered_event_interval), exceeding this will call [onPlayerTriggerEventThreshold](mta://scripting/server/events/onplayertriggereventthreshold.md)

Values: 1-1000; default: 100

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22930](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22930))

#### player_teleport_alert

*<player_teleport_alert>100</player_teleport_alert>*

Defines the maximum allowed unexpected position change (in units). If a player's position changes by more than this value without using [setElementPosition](mta://scripting/shared/functions/setelementposition.md), the event [onPlayerTeleport](mta://scripting/server/events/onplayerteleport.md) will be triggered.

Values: 5-500; default: 100

#### module

*<!-- <module src="sample_win32.dll" /> -->*

*<!-- <module src="sample_linux.so" /> -->*

Specifies the module(s) which are loaded with the server. To load several modules, add more <module> parameter(s). Optional parameter.

#### resource_client_file_checks

*<resource_client_file_checks>1</resource_client_file_checks>*

If enabled, the server will perform checks on files in resources (listed in [meta.xml](mta://reference/misc/meta-xml.md)) with PNG, TXD and DFF extensions, checking if they are corrupted. When the system finds a non-valid file of these types, it outputs a warning to the server console.

You may want to disable thse checks when storing different/non-conforming data in files with these extensions (e.g. encrypted data).

Values: 0 - Off, 1 - Enabled.  Default - 1

#### resource

*<resource src="admin" startup="1" protected="0" />*

*<resource src="defaultstats" startup="1" protected="0" />*

*<resource src="helpmanager" startup="1" protected="0" />*

*<resource src="joinquit" startup="1" protected="0" />*

*<resource src="mapcycler" startup="1" protected="0" />*

*<resource src="mapmanager" startup="1" protected="0" />*

*<resource src="parachute" startup="1" protected="0" />*

*<resource src="resourcebrowser" startup="1" protected="1" default="true" />*

*<resource src="resourcemanager" startup="1" protected="1" />*

*<resource src="scoreboard" startup="1" protected="0" />*

*<resource src="spawnmanager" startup="1" protected="0" />*

*<resource src="voice" startup="1" protected="0" />*

*<resource src="votemanager" startup="1" protected="0" />*

*<resource src="webadmin" startup="1" protected="0" />*

*<resource src="play" startup="1" protected="0" />*

*<resource src-"resources" startup"1" protected="0"*

Specifies persistent resources which are loaded when the server starts. Persistent resources are not stopped even if all the other resources that depend on them stop; that is, the only way to stop them is by explicitly using the *stop* server command or [stopResource](mta://scripting/server/functions/stopresource.md) scripting function. To load several resources, add more <resource> parameters.

In addition, there are several flags which control how the server deals with each resource:

- **src**: the resource name. This is the only mandatory flag.

- **startup**: controls whether the resource will be started with the server or not. If "1", "true" or "yes", the resource will be started. If not specified, defaults to not starting the resource.

- **protected**: if "1", "true" or "yes", the resource will not be able to be stopped when started. Otherwise, even if not specified, it will default to the normal behaviour.

- **default**: if given a "1", "true" or "yes" value, this resource will be the one who populates the built-in HTTP server main page, which is seen when no resource is given in the web address. It is not possible to have more than one default resource.

#### busy_sleep_time

*<busy_sleep_time>-1</busy_sleep_time>*

**ONLY USE THIS PARAMETER IF YOU ARE SURE OF WHAT YOU ARE DOING** - This parameter configures the server's sleep duration in milliseconds during busy processing, affecting CPU usage and responsiveness.

Available range: -1 to 50; default value: -1

-1 sets the server to automatically determine the optimal value based on workload.

Setting it to 0 is recommended for achieving the best performance but may result in higher CPU usage.

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md).

#### idle_sleep_time

*<idle_sleep_time>-1</idle_sleep_time>*

**ONLY USE THIS PARAMETER IF YOU ARE SURE OF WHAT YOU ARE DOING** - This parameter configures the server's sleep duration in milliseconds during idle periods, affecting CPU usage and responsiveness.

Available range: -1 to 50; default value: -1

-1 sets the server to automatically determine the optimal value based on workload.

Setting it to 10 is recommended for achieving the best performance while balancing CPU usage.

This parameter can be changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md).

## Deprecated settings

The following settings have been deprecated in the production version of MTA:SA and no longer work.

#### networkencryption

*<networkencryption>1</networkencryption>*

This parameter specifies whether communications between the server and client is encrypted. Encryption can help prevent network data being viewed and modified.

Values: 0 - disabled , 1 - enabled ; default value: 1. Optional parameter.

This parameter can changed and saved while the server is running with [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

#### autologin

*<autologin>0</autologin>*

Specifies whether or not players should automatically be logged in based on their IP adresses.

Values: 0 - disabled , 1 - enabled ; default value: 0.

#### httpautoclientfiles

*<httpautoclientfiles>1</httpautoclientfiles>*
