---
doc_id: "mta-wiki:5724"
title: "Shader examples"
source_title: "Shader examples"
source_url: "https://wiki.multitheftauto.com/wiki/Shader_examples"
revision_id: 69694
language: "en"
categories: []
---

# Shader examples

This page contains some example shader resources to try. If you are looking to make your own, please be sure to read about the [shader element](https://wiki.multitheftauto.com/index.php?search=shader%20element) as well.

## Road shine

 

Road shine

| Download shader_roadshine.zip Requires Shader Model 2 graphics card This resource creates a light reflection effect on the ground (looks best when moving). It uses a custom flag in the effect file to generate surface normals for the ground model: int CUSTOMFLAGS < string createNormals = "yes"; >; Surface normals are not usually present in the ground and building models, but are useful for creating lighting effects such as these. |
| --- |

## Road shine 2

 

Road shine 2

| Download shader_roadshine2.zip Requires Shader Model 2 graphics card Bit more complicated than the first Road shine, as it tracks the sun or moon to calculate the position of the highlight. The effect can be hard to see depending on the time of day. Best used with the play resource as the model it modifies is near the initial spawn point. |
| --- |

## Road shine 3 (Deluxe edition)

 

Road shine 3

| Download shader_roadshine3.zip Requires Shader Model 2 graphics card This resource shows how to: Stop a wild card match shader from being applied to certain world textures. Use isLineOfSightClear to stop an effect when something is not visible (The sun in this case). Use a shader maxDrawDistance setting to avoid GPU overload. The final effect is a faster shader with less rendering issues than the previous two road shine examples. |
| --- |

## UV scroll

 

UV scroll

| Download shader_uv_scroll.zip This resource scrolls a texture from left to right. It doesn't use vertex or pixels shaders, so it should work on all hardware. |
| --- |

## UV scripted

 

UV scripted

| Download shader_uv_scripted.zip This resource controls a texture's UVs using Lua. It shows that anything is possible if you can imagine it. |
| --- |

## Car paint

 

Car paint

| Download shader_car_paint.zip Requires Shader Model 2 graphics card This resource shows you how to apply a shader to the vehicle models. The shader itself is not that great, so don't get your hopes up. |
| --- |

## Water

 

Water

| Download shader_water.zip Requires Shader Model 2 graphics card This resource applies a shader to the GTA world water. The Lua script shows how to use a timer to transfer the conventional water color setting to the shader. |
| --- |

## Bloom

 

Bloom

| Download shader_bloom.zip Requires Shader Model 2 graphics card This resource shows you how 'bounce' full screen effects using a render target pool. It uses the onClientHUDRender event to exclude the HUD from the effect. |
| --- |

## Block world

 

Block world

| Download shader_block_world.zip Requires Shader Model 2 graphics card This resource makes the textures look all blocky. It also changes colors when the 'k' key is pressed. |
| --- |

## Texture names

 

Texture names

| Download shader_tex_names.zip This resource is only a tool, and doesn't do anything pretty. It shows a list of the current visible texture names, and highlights the selected texture. Ideal for finding a texture name to use with engineApplyShaderToWorldTexture . num_8 shows/hides the texture list, num_7 and num_9 step through the list, and 'k' copies the current texture name to the clipboard. |
| --- |

## Skid marks

 

Skid marks

| Download shader_skidmarks.zip Requires Shader Model 2 graphics card This resource shows you how to do multiple passes in a shader, and input different variables to the vertex shader for each pass. Use the command /skidmarks 1-4 to see the different effects. (You have skid a car to see it!) |
| --- |

## HDR contrast

 

HDR contrast

| Download shader_contrast.zip Requires Shader Model 2 graphics card This resource applies a 'High Dynamic Range' contrast effect. It uses a 1 pixel render target to sample the whole scene, and then uses that to brighten or darken the next frame. So going into somewhere dark will automatically brighten the scene, and visa versa |
| --- |

## Tessellation

 

Tessellation action

| Download shader_flag.zip Requires Shader Model 2 graphics card This resource shows how to use shader tessellation to animate the shape of a dxDrawImage and use shader transform to give it a 3rd dimension. The example has a GUI (press numpad-8) so you can fiddle with the settings. |
| --- |

## Radial blur

 

Radial blur

| Download shader_radial_blur.zip Requires Shader Model 2 graphics card This resource sort of looks a little bit like the GTAIV motion blur you get when you move the mouse quickly, or drive a fast car. The fast car effect is a bit more subtle than the screen shot would suggest, as it leaves the center of the screen nice and clear so you can see where you are going. It also has the option of suspending the effect during times of low FPS. Check the two settings at the top of c_radial_blur.lua . The file c_switch.lua contains information on how to toggle the effect from another resource using events. |
| --- |

## Detail

 

Detail

| Download shader_detail.zip Requires Shader Model 2 graphics card Applies a few monochrome detail textures, at various scales, to (parts of) the world. (Not finished and probably never will be.) |
| --- |

## Ped morph

 

Ped morph

| Download shader_ped_morph.zip Requires Shader Model 2 graphics card This resource uses a vertex shader to modify the geometry of a ped model as it is rendered. When the resource has started, use the 'k' and 'l' keys to change morph size. |
| --- |

## Ped shell

 

Ped shell

| Download shader_ped_shell.zip Requires Shader Model 2 graphics card This resource draws a translucent effect as a shader layer. The first pass is done by GTA, and the vertex shader is only applied in the second to add the effect 'on top' of the standard output. When the resource has started, use the 'm' key to see the shell effect. |
| --- |

## Hud mask

 

Hud mask

| Download shader_hud_mask.zip This resource shows how to draw a hud texture with a shape mask. |
| --- |

## dxDrawCircle

 

dxDrawCircle

| Download shader_circle.zip This resource exports a 'dxDrawCircle' function for use in your own scripts. Example resource calling dxDrawCircle function from shader_circle: circle_example.zip |
| --- |
