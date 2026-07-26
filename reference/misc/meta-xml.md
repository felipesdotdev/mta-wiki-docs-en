---
doc_id: "mta-wiki:6422"
title: "Meta.xml"
source_title: "Meta.xml"
source_url: "https://wiki.multitheftauto.com/wiki/Meta.xml"
revision_id: 81735
language: "en"
categories: ["Changes_in_1.5.0", "Scripting_Concepts"]
generated_at: "2026-07-26T16:16:11.372490+00:00"
---

# Meta.xml

The *meta.xml* file presents MTA with a set of metadata, such as the resource's name, the scripts to include, and which files to precache for sending to clients among other things. It is also the scope of "elements". It is written in XML, which is based on HTML and is the parent of XHTML.

# Tags

XML is a textual data format which is widely used for the representation of data. MTA uses an XML-based language to describe the metadata for resources by using the tags below:

- **<info />** Information about this resource, possible parameters include (any arbitrary parameters can be used and read using [getResourceInfo](mta://scripting/server/functions/getresourceinfo.md)):

- **author:** The author of this resource

- **version:** The version of this resource

- **name:** The name of this resource

- **description:** A brief description of this resource

- **type:** The type of this resource, that can be "gamemode", "script", "map" or "misc".

- **gamemodes:** The gamemodes to be compatible with the resource. It must be the name of the gamemode resource, not the gamemode name. If you want it to be compatible with multiple gamemodes, it must be in a comma-separated list without spaces. (e.g. gamemodes="test1,test2").

- **<script />** Source code for this resource, possible parameters are:

- **src:** The file name of the source code

- [BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430))

**src:** Added support for glob patterns, see [example](https://wiki.multitheftauto.com/wiki/Meta.xml#Loading_files_via_pattern).

- **type:** The type of source code: "client", "server" or "shared".

- A **shared** script will be ran for both client and server, but separately as usual (basically adds the script twice: once for server and once for client)

- **cache:** When the script file type is "client", this setting controls whether the file is saved on the clients' hard drive. If you are concerned about your scripts security, make sure to read [Script security guide](https://wiki.multitheftauto.com/wiki/Script_security). Default is "true". Using "false" will mean the file is not saved. *(Note: cache=false files are started at the client first, so lua file load order might differ when mixing cache settings)*

- **validate:** If set to "false", compatibility checks are skipped.

- **<map />** The map for a gamemode, possible parameters are:

- **src:** .map file name (can be path too eg. "maps/filename.map")

- **dimension:** Dimension in which the map will be loaded (optional)

- **<file />** A client-side file. Generally these are images, .txd, .col, .dff or .xml files. They'll be downloaded by clients when the resources is started (or on join)

- **src:** client-side file name (can be path too eg. "images/image.png")

- [BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430))

**src:** Added support for glob patterns, see [example](https://wiki.multitheftauto.com/wiki/Meta.xml#Loading_files_via_pattern).

- **download:** Whether or not to be sent to the client automatically (optional). Default is "true". Using "false" will mean they are not sent on resource start but could later be used by [downloadFile](mta://scripting/client/functions/downloadfile.md).

- **<include />** Include resources that this resource will use

- **resource:** Resource name that you want to start with this resource

- **minversion:** Minimum version that **resource** needs to be (optional)

- **maxversion:** Maximum version that **resource** needs to be (optional)

- **<config />** Config file (.xml) can be accessed by resource, possible parameters are:

- **src:** The file name of the config file

- **type:** The type of the config file: "client" or "server"

- **<export />** This exports functions from this resource, so other resources can use them with [call](mta://scripting/shared/functions/call.md)

- **function:** The function name

- **type** Whether function is exported server-side or client-side (valid values are: "client", "server" and "shared")

- A **shared** export will make the function callable from both client and server scripts (basically adds the export twice: once for server and once for client)

- **http:** Can the function be called via HTTP (true/false)

- **<html />**

- **src:** The filename for the HTTP file (can be a path)

- **default:** The html file is one that is shown by default when visiting /resourceName/ on the server. Only one html can be default, the rest are ignored. (true/false)

- **raw:** The html file is not parsed by the Lua interpreter and is treated as binary data. Must be used for binary files (images mainly) (true/false)

- **<settings />** Most gamemodes use [settings system](mta://reference/misc/settings-system.md) to let server admins to configure it how they like. For instance you could set round time and then use [get](mta://scripting/server/functions/get.md) and [set](mta://scripting/server/functions/set.md) to get the value or change it, respectively.

- **<setting />** Resource settings can be accessed by resource and Admin panel, possible parameters are:

- **name:** The setting name used by the scripts to get or set the setting value

- **value:** The setting default value used by the scripts

- **friendlyname:** A friendly name to the setting (optional)

- **accept:** The values the setting could accept (optional)

- **examples:** An Example of a value (optional)

- **desc:** A description of the setting (optional)

- **<min_mta_version />** Minimum version requirements for this resource to run correctly. When authoring resources, the minimum version should usually be set to the current released version of MTA:SA, in the sortable format (e.g. **1.6.0-9.22279.0**). See [getVersion](mta://scripting/shared/functions/getversion.md) for details.

- **client:** The minimum client version

- **server:** The minimum server version

- **both:** The minimum client and server version (instead of the previous two attributes)

- **<aclrequest />** A list of [ACL](mta://tutorials/access-control-list.md) rights this resource will need. Any user with admin permission can accept or reject a resource ACL request by using the command: /aclrequest [list/allow/deny] <resourceName> [<right>/all]

- **<right />** an individual right

- **name:** The right name.

- **access:** Set to *true* to allow the resource to access this right. Set to *false* to deny the access to this right.

- **<sync_map_element_data />** Controls whether map [element data](mta://reference/misc/element-data--975d1ea3.md) such as "PosX" and "DoubleSided" are transferred to the client. This data is usually not required by most gamemodes or resources. (Map Editor and Interiors require this to be not set to false to work). When set in a gamemode meta.xml, the setting will apply to all maps loaded by that resource.

- **false:** Disable transfer of map element data for all resources. This can reduce map download times considerably.

- **true:** Enable transfer of map element data for all resources. (If **false** and **true** are set in different resources, true will have priority and all resources will transfer map element data)

- **<oop />** OOP - Please refer to [OOP](mta://tutorials/oop.md) for documentation.

- **false:** Disable OOP.

- **true:** Enable OOP.

- **<download_priority_group />** If not set, the download priority group for a resource defaults to 0. If this is set higher than 0, then the resource will be downloaded and started on the client earlier than other resources. This option is useful for resources with critical client functionality that other things in your gamemode (or fair play) rely on. If set to less than 0 (a negative number, like -1), the resource will be downloaded and started on the client later than other resources. As this can be confusing, here is an example:

- **Resource A: <download_priority_group>20</download_priority_group>** will start earlier than..

- **Resource B: <download_priority_group>10</download_priority_group>**  
In this case, Resource A will start earlier than Resource B because its value (20) is higher than (10). In turn, Resource B will still start earlier than a resource with a negative value or a value below 10 (like 5).

## Example

Quick start template:

```
<meta>
    <script src="server.lua" type="server" />
    <script src="client.lua" type="client" />
</meta>
```

Here's an example of a meta file using some of the tags mentioned:

```
<meta>
    <info author="Slothman" version="1.0.2" name="Stealth" description="Allow scripts to insert a ped that simulates combat with a real player" type="gamemode" />

    <script src="stealthmain_server.lua" />
    <script src="noiseblip.lua" />
    <script src="mission_timer.lua" />
    <script src="gadgets_server.lua" />
    <script src="gadgets_client.lua" type="client"/>
    <script src="stealthmain_client.lua" type="client" validate="true"/>
    <script src="noisebar.lua" type="client"/>
    <script src="spycam.lua" type="client"/>
    <script src="riemann_z_demonstration.lua" type="client" cache="false"/>

    <map src="base.map" dimension="1"/>

    <file src="riot_shield.txd" download="false" />
    <file src="riot_shield.dff" download="false" />
    <file src="riot_shield.col" download="false" />
    <file src="armor.png" />
    <file src="camera.png" />
    <file src="cloak.png" />
    <file src="goggles.png" />
    <file src="mine.png" />
    <file src="radar.png" />
    <file src="shield.png" />

    <include resource="scoreboard" />
    <include resource="killmessages" />
    <include resource="maplimits" />
    
    <config src="help.xml" type="client"/>

    <export function="exampleExport1" type="server" />
    <export function="exampleExport2" type="client" />
    <export function="exampleExport3" type="shared" />

    <settings>
        <setting name="roundlimit" value="[6]" /> 
	<setting name="teamdamage" value="[1]" /> 
	<setting name="teambalance" value="[1]" /> 
	<setting name="isAllowedToShoot" value="true" />
	<setting name="admingroup" value="Admin,AdminPlus"
		friendlyname="Admin group list"
		group="_Advanced"
		accept="*"
		examples="Admin,Moderator,SuperModerator"
		desc="To use this resource, the player must belong to one of the groups listed."
		/> 
	<setting name="spazammo" value="[25]" /> 
	<setting name="m4ammo" value="[100]" />
	<setting name="shotgunammo" value="[25]" />
	<setting name="sniperammo" value="[20]" />
	<setting name="ak47ammo" value="[120]" />
	<setting name="rifleammo" value="[40]" />
	<setting name="deserteagleammo" value="[45]" />
	<setting name="pistolammo" value="[132]" />
	<setting name="uziammo" value="[150]" />
	<setting name="tec9ammo" value="[150]" />
	<setting name="silencedammo" value="[65]" />
	<setting name="grenadeammo" value="[4]" />
	<setting name="satchelammo" value="[4]" />
	<setting name="teargasammo" value="[4]" />
	<setting name="molatovammo" value="[4]" />
    </settings>

    <min_mta_version server="1.5.2-9.07903" client="1.5.2-9.07903" />

    <aclrequest>
        <right name="function.startResource" access="true" />
        <right name="function.stopResource" access="true" />
        <right name="function.setPlayerMuted" access="true" />
    </aclrequest>

    <sync_map_element_data>false</sync_map_element_data>

    <oop>false</oop>

    <download_priority_group>0</download_priority_group>
</meta>
```

## Loading files via pattern

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430))

Since version [[r22430](https://buildinfo.mtasa.com/?Revision=22430&Branch)] and above, you can conveniently load files into your resources using [glob library](https://en.wikipedia.org/wiki/Glob%20(programming)) - see [more details](https://github.com/p-ranav/glob).

```
<meta>
    <script src="shared/**/*.lua" type="shared" cache="false" />
    <script src="client/**/*.lua" type="client" cache="false" />
    <script src="server/**/*.lua" type="server" />

    <file src="assets/fonts/**/*.ttf" />
    <file src="assets/sounds/**/*.mp3" />
    <file src="assets/images/**/*.png" />
</meta>
```
