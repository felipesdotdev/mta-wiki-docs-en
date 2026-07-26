---
doc_id: "mta-wiki:12785"
title: "DGS Custom Plugin"
source_title: "DGS Custom Plugin"
source_url: "https://wiki.multitheftauto.com/wiki/DGS_Custom_Plugin"
revision_id: 74262
language: "en"
categories: []
---

# DGS Custom Plugin

What is?

DGS has basic elements and plugins. Plugins in DGS are something that can be used like normal DGS elements, can be applied to a DGS elements, or can interact with DGS elements...

## Why?

In DGS, we have a lot of basic elements and some plugins. But when it comes to more complicated things which can be implemented with dx functions easily, using existing DGS elements and plguins seems to be strenuous.

**To Solve The Problem:**

This document is for creating custom plugins that can implement complicated dx draws, which are also regarded as DGS elements. This means, your plugins will be able to support all of the basic functions of DGS.

## How?

- To get started, you must know how to use DGS. *Or close this page and learn [DGS](https://wiki.multitheftauto.com/index.php?search=DGS).*

- The following tutorial shows how to create a custom DGS plugin example by hand.

- DGS environment is required.

### Create A File

- 1. Get into the folder "**DGS/plugin/**", and create a file named "**myPlugin.lua**". This file is our protagonist.

- 2. Open the "**meta.xml**" of DGS, and find this string "**<!--You can also add your custom plugins here -- >**".

- 3. Under this line, insert a new line "**<script src="plugin/myPlugin.lua" type="client" >**"

### Write Function

Now open the file "**myPlugin.lua**" with your editor. We need a "creation" function for our plugin.

- We are going to create a label that have adjustable background color.

- 1. This function can be named as **dgsCreateMyPlugin**.

- 2. For position and size, we need:

- **x**

- **y**

- **width**

- **height**

- **relative**

- **parent**

- 3. For text, we need:

- **text**

- 4.For the background color, we need:

- **backgroundColor**

- According to the requirement, we can make such function template:

```
function dgsCreateMyPlugin(x,y,w,h,text,backgroundColor,relative,parent)

	--Here we use a dgs-dximage as the base of our plugin.
	--Image has only 1 renderer which is enough for us.
	local myPlugin = dgsCreateImage(x,y,w,h,_,relative,parent,backgroundColor)

	--Hook the renderer of the image, so that we can write our own renderer
	--[[
	Custom Renderer has these predefined variables
		posX,posY,width,height,self,rotation,rotationCenterOffsetX,rotationCenterOffsetY,color,postGUI
	]]
	
	--[[
		We have some methods to get the text.
		1.slowest (access the text from dgsGetText function)
		local text = dgsGetText(dgsElement)

		2.slower (access the text from dgsGetProperty function)
		local text = dgsGetProperty(dgsElement,"text")

		3.faster (access the text from internal dgsGetData function)
		local text = dgsGetData(dgsElement,"text")

		4.fastest (access the text directly from the data table)
		local text = dgsElementData[dgsElement].text
	]]	
	local customRenderer = dgsCreateCustomRenderer([[

		--Draw the background
		dxDrawRectangle(posX,posY,width,height,color,postGUI)

		--For the performance, here we use the method 4
		
		--Variable "self" means this custom renderer. To get the dgsElement:
		local dgsElement = dgsElementData[self].dgsElement
		
		--To get the text:
		local text = dgsElementData[dgsElement].text
		
		--Draw the text
		dxDrawText(text,posX,posY,posX+width,posY+height,tocolor(255,255,255,255),1,1,"default","left","top",false,false,postGUI)
	]])

	-- Name our plugin type (required)
	dgsSetProperty(myPlugin,"asPlugin","dgs-dxmyplugin")
	
	-- Give the custom renderer information about its related dgs element
	dgsSetProperty(customRenderer,"dgsElement",myPlugin)
	
	-- Set the text property
	dgsSetProperty(myPlugin,"text",text)
	
	-- Apply the custom renderer to dgs-dximage's renderer
	dgsSetProperty(myPlugin,"image",customRenderer)
	
	-- Don't forget to make the custom renderer destroy with myPlugin
	dgsAttachToAutoDestroy(customRenderer,myPlugin,-1)	-- Use index "-1" as the meaning of "built-in"
	
	-- Trigger on create event (required)
	triggerEvent("onDgsPluginCreate",myPlugin,sourceResource)

	return myPlugin --Please return this element, otherwise you will get nothing after calling this function
end
```

### Use Custom Plugin

After defined our custom plugin, it is easy to use. Here is the syntax of our custom plugin:

```
dgs-dxmyplugin dgsCreateMyPlugin( float x, float y, float width, float height, string text, integer backgroundColor, bool relative )
```

Here is the code of creating the plugin (In DGS):

```
myplugin = dgsCreateMyPlugin(500,500,200,200,"The Text Of My Plugin",tocolor(0,0,0,128),false)
```

### Export Functions

In DGS, we can create our custom plugin by calling function "dgsCreateMyPlugin". If we want to create in external resource, we have to export the function.

- 1. Go to "**meta.xml**", and find the line where we just added "**<script src="plugin/myPlugin.lua" type="client" />**"

- 2. Under this line, insert a new line "**<export function="dgsCreateMyPlugin"  type="client" />**". Save and done.

From external resource, we can call this function like using DGS built-in functions such as "dgsCreateLabel":

- Normal usage

```
myplugin = exports.dgs:dgsCreateMyPlugin(500,500,200,200,"The Text Of My Plugin",tocolor(0,0,0,128),false)
```

- Shortened usage:

```
DGS = exports.dgs --shorten the export function prefix
myplugin = DGS:dgsCreateMyPlugin(500,500,200,200,"The Text Of My Plugin",tocolor(0,0,0,128),false)
```

- Usage with "**[dgsImportFunction](mta://scripting/client/functions/dgsimportfunction.md)**":

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions
myplugin = dgsCreateMyPlugin(500,500,200,200,"The Text Of My Plugin",tocolor(0,0,0,128),false)
```
