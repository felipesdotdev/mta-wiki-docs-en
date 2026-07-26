---
doc_id: "mta-wiki:7627"
title: "MTA:Eir/functions/getElementRenderMode"
source_title: "MTA:Eir/functions/getElementRenderMode"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/getElementRenderMode"
revision_id: 39309
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.585163+00:00"
---

# MTA:Eir/functions/getElementRenderMode

This function returns the current value of an internal GTA:SA rendering property. Use this function for management or debugging purposes in combination with [setElementRenderMode](mta://reference/misc/mta-eir-functions-setelementrendermode.md).

## Syntax

```
value/bool string getElementRenderMode ( element theElement, string propertyName, [ string preferedValueType ] )
```

### Arguments

- **theElement**: the element to change a render property of

- **propertyName**: name of the property to adjust

- **preferedValueType** (optional): *int*, *bool* or *float*

### Valid Properties

| Name | Internal Type | Description | Default Value |
| --- | --- | --- | --- |
| lighting | Boolean | This is a switch to the entire lighting status of an entity. If true, lighting calculations are allowed on the entity. Otherwise all lighting computations are dropped. Setting this flag to false for entities that never expected no lighting can cause undefined behavior. | true |
| lighting_ambient | Boolean | This is a switch that controls ambient lighting calculations for entities. If true, ambient lighting colors are added to the final color. | true |
| lighting_directional | Boolean | This is a switch that controls directional lighting calculations for entities. If true, directional lighting is added to the final color. | true |
| lighting_point | Boolean | This is a switch that controls point lighting calculations for entities. If true, point lighting colors are added to the final color. | true |
| lighting_spot | Boolean | This is a switch that controls spot lighting calculations for entities. If true, spot lighting colors are added to the entity's final color. | true |
| lighting_material | Boolean | This is a switch that controls special material lighting calculations for entities. If true, materials are allowed to create special light sources that affect only them. Only vehicles are using material lighting. | true |
| reflection | Boolean | This is a switch that controls GTA:SA reflection technology for entities. If true, the entity is allowed to display reflection effects on reflective materials. Several game objects use reflections. | true |
| alphaClamp | Float | This is a number that specifies the alpha value that is used for alpha testing. In the original world render mode, any pixel whose alpha value is below the alphaClamp value is cut away. Other world render modes behave smarter. | 100.0f / 255.0f |

### Returns

Returns the **property value** if a valid property was selected, **false** and a debug message otherwise.
