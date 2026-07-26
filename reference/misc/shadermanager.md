---
doc_id: "mta-wiki:6225"
title: "Resource : Shadermanager"
source_title: "Shadermanager"
source_url: "https://wiki.multitheftauto.com/wiki/Shadermanager"
revision_id: 30183
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:16:50.379505+00:00"
---

# Resource : Shadermanager

|  | Warning: This is a planned resource (it's not ready yet!) |
| --- | --- |
|  |  |

Shadermanager is a *planned* resource to facilitate the managment of shaders in MTA, analogous to mapmanager for maps. This page is simply here to serve as a place to share the proposed system. To discuss, contact [John](https://wiki.multitheftauto.com/wiki/User:John) on #mta.

## Proposed Features

- Adoption of a "type='shader'" standard to allow shadermanager to find all the shaders on a server.

- Adoption of the #shadername.defaultState setting to determine whether or not to enable the shader by default (0 for no, 1 for yes, 0 by default).

- Minimalistic GUI to allow for the enabling/disabling of shaders.

- Small log to allow for viewing of shader-specific errors.

- Exported functions to allow shadermanager to function as a backend for other scripts (allowing someone else to implement their own GUI, for example).

- getShaderFromName, getAllShaders, setShaderEnabled, isShaderEnabled, isShaderCompatibleWithClient

- Adoption of certain exported functions for shaders to allow shadermanager to control all the shaders on a server.

- setShaderEnabled, isShaderEnabled

## Making your shader resource compatible with *shadermanager*

To make your shader resource compatible with shadermanager (which you should do), be sure to:

- Setup your resource's [meta.xml](mta://reference/misc/meta-xml.md) file properly:

- Set the resource's type to "shader"

```
<info name="myawesomeshader" author="John_Michael" version="1.0.0" type="shader" description="My awesome shader!" />
```

- Setup the resource's settings. You should provide a default state setting, that will determine whether or not the shader is enabled by default (use "0" for disabled, "1" for enabled). If you do not provide this, it will default to "0".

```
<settings>    <setting name="#shader_water.defaultState" value="1" />    </settings>
```

- Ensure the following exported functions are available:

- (TODO)
