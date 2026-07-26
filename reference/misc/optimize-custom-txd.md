---
doc_id: "mta-wiki:7214"
title: "Optimize Custom TXD"
source_title: "Optimize Custom TXD"
source_url: "https://wiki.multitheftauto.com/wiki/Optimize_Custom_TXD"
revision_id: 63006
language: "en"
categories: []
generated_at: "2026-07-26T16:16:27.057211+00:00"
---

# Optimize Custom TXD

Introduction

A TXD file contains image files for GTA to use. Model mods downloaded from the 'internet' often contain bloated TXD files. These can usually be reduced by several MB's which saves memory and download time.

## Example of how to reduce the size of a TXD file

### Magic.TXD

- Find, install and run "Magic.TXD" (for example on GTAForums)

- Double click on your TXD to open it

For best results in the next steps, select **Tools > Mass Convert** and export them all to an output folder, with all convert options checkboxes selected (and mipmaps to 25).
This step will initially increase the texture size, but give a better final reduction size/quality preservation result if you further optimize its specific textures.

- Select a texture from the list for optimization

- If the texture is not compressed (raw raster format) click on "Edit -> Manipulate" and select compression format DXTn to save much space

- If the texture is too big in width x height click "Edit -> Resize" and type in dimensions to scale down texture. It is usually safe (without significant quality loss) to half the resolution, or depending on model complexity (is it a highly realistic mod or not) up to reducing resolution by the power of 4 (for example resize from 512 x 512 to 128 x 128) or even 8 if the internal textures are unnecesarily high resolution (like initially 2048 x 2048)

- If the texture is lacking mipmaps click "Edit -> Generate mipmaps" to add new ones (for all internal materials)

- Once finished editing click "File -> Save"

### TXD Workshop

- Find, install and run the TXD editing program "TXD Workshop" (by Jernej L.)

- Press the 'Open TXD' button at the top and load a TXD file.

- Look down the list of images and find any that are too big. Examples of too big:

- Almost anything over 512 x 512

- Images of small details, such as vehicle dashboards and license platers which are over 128 x 128

- Images with one color, such as 'remapsub' which are over 32 x 32

- In TXD Workshop, select an image and press the 'Export' button at the top, select PNG and save the file.

- Open the file in a image editing program and reduce the file to one of these sizes:

- 32x32, 64x64, 128x128, 256x256, 512x512

- Save the file.

- Back in TXD Workshop, press the 'Import' button and load the reduced file.

- Then press the 'Save TXD' button.

## Optimization using TxdGen

To further improve the quality of TXD files, it is advised to **clean them**. You can do that by passing the textures through the [TxdGen tool](http://www.gtamodding.com/wiki/TxdGen). It can detect a wide variety of structural problems inside of TXD files and fix them automatically for you.

Tutorials for its usage are included on the GTA Modding page.
