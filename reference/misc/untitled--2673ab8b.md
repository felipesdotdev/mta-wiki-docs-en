---
doc_id: "mta-wiki:5576"
title: "AR/مقدمه في البرمجه"
source_title: "مقدمه في البرمجه"
source_url: "https://wiki.multitheftauto.com/wiki/%D9%85%D9%82%D8%AF%D9%85%D9%87_%D9%81%D9%8A_%D8%A7%D9%84%D8%A8%D8%B1%D9%85%D8%AC%D9%87"
revision_id: 74417
language: "en"
categories: []
generated_at: "2026-07-26T16:16:58.249388+00:00"
---

# AR/مقدمه في البرمجه

مقدمه

```
تختلف أنواع السكربتات فمنها خريطة أو وضع للعب
```

MTA السكربتات جزء اساسي في تشغيل

...وغيرها " freeroam , race , deathmatch " فتستطيع بإستخدامهم إنشاء تطبيقات لتحسين اللعب

(Lua) [www.lua.org] برمجة السكربتات تعتمد على لغة البرمجة

لغة البرمجة تعتمد إعتماداً كلياً على اللغة الإنجليزية , فيجب أن تكون لديك خلفية في اللغة الإنجليزية قبل المتابعة.

لبرمجة سكربت ما تحتاج لمحرر .. ويفضل إستخدام محرر إحترافي لكي يسهل عليك البرمجة مثل :

- Notepad++ [[1]](http://notepad-plus-plus.org/download)

- Lua Edit [LuaEdit](http://luaedit.sourceforge.net/)

```
فهو يسهل برمجتها MTASE لكن يفضل استخدام برنامج :
```

- [MTA Script Editor](mta://reference/misc/mtase.md).****

## إنشاء سكربت

سوف نتعلم كيف نقوم بإنشاء سكربت يدخل اللاعب إلى اللعبة .. خطوة بحطوة

اولا لا بد من معرفة انواع ملفات السكربت

1-Meta.xml -- يقوم هذا الملف بتعرف الملفات الموجود في السكربت للسيرفر

2-Client -- يقوم هذا الملف بتشغيل جميع أوامر المتعلقة بالاعب فقط

3-Server -- يقوم هذا الملف بتشغيل جميع الاوامر سواء كانت للسيرفر او الاعب

### أين مسار كل البرامج النصية (السكريبتات أو المودات)؟

الان نتعرف على مجلد المودات أو السكربتات.
اذهب إلى مجلد Multi Theft Auto واتبع المسار التالي:

/Your MTA Server/mods/deathmatch/resources/

. أو مجلد عادي zip سترى الكثير من الملفات. ربما ترى مجلدات صيغتها , MTA .. وجميعها يقبله الـ

وهو الذي سنستخدمه بالبرنامج التعليمي "myserver" ولإنشاء المودات الخاصة بك: قم بعمل مجلد جديد واجعل اسمه كما تريد فمثلاً قم بتسميته

والان يجب أن يكون مسار المجلد الذي قمت بعمله هذا:

/Your MTA Server/mods/deathmatch/resources/myserver/

- myserver: اسم المجلد الذي قمت بتسميته

### meta.xml تعريف السكربت اضافة ملف

حتى يستطيع السيرفر من معرفة المودات, يجب علينا إنشاء ملف meta.xml

" ويكون بداخل مجلد السكربت الذي قمنا بإنشائه وهو "myserver"

ولإنشاء ملف meta.xml :

وافتحه باستخدام المفكرة =) meta.xml أفتح ملف نصي جديد وقم بتسميته

ولا تنسى ان يكون بداخل مجلد السكربت .

أدخل الكود التالي في ملف *meta.xml*:

```
<meta>
     <info author="إسمك" type="gamemode" name="إسم السكربت" description="وصف بسيط للسكربت" />
     <script src="script.lua" />
</meta>
```

هنا يتم تعريف أجزاء السكربت فمثلاً :

- <info ..>

تضع فيه بيانات السكربت .. مثل الإسم والنوع والوصف

- type="gamemode"

تعني أن نوع السكربت هو مود لعب وتوجد أنواع عديدة مثل :

- - gamemode

- map

- script

### إنشاء ملف السكربت Lua

قمنا بوضع هذا السطر في :

- meta.xml

```
<script src="script.lua" />
```

الآن نقوم بإنشاء ملف نصي بنفس الإسم

- - script.lua

بإستخدام برنامج التحرير لديك .. نقوم بإنشاء الكود

```
function joinHandler() -- الوظيفة .. وبعدها نقوم بكتابة الإسم
	local x = 1959.55 -- تعريف x
	local y = -1714.46 -- تعريف y
	local z = 10 -- تعريف z
	spawnPlayer(source, x, y, z) -- نقوم بإستخدام هذه الوظيفة لإنتاج اللاعب ونقوم بتحديد اللاعب وهو المصدر : source
	fadeCamera(source, true) -- نقوم بعمل fade للكاميرا
	setCameraTarget(source, source) -- نجعل هدف الكاميرا هو اللاعب 
	outputChatBox("مرحباً بك في السيرفر", source) -- نقوم بإخراج نص في الدردشة
end
addEventHandler("onPlayerJoin", getRootElement(), joinHandler) -- نقوم بإضافة المعالج حيث سيتم تشغيله بعد الحدث المحدد وهو عند دخول اللا
```

وصف وشرح الكود اعلاه : 
	سيقوم السكربت بوضع اللاعب في الاحداثيات (x,y,z) المحدده اعلاه, عند دخوله الى السيرفر
	لاحظ انه يجب استخدام  وظيفة [ *fadeCamera* ] ستكون الشاشة سوداء وأيضاً يجب تعيين الكاميرا ( setTargetCamera ) ..

نرى أن **source** هو المصدر وهو اللاعب الذي يقوم بالدخول

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md) - الاحداث وهي ما يجب فعله من قبل المستخدم او السيرفر

- [function](https://wiki.multitheftauto.com/index.php?title=Function&action=edit&redlink=1) - وظيفة تعمل عند حدث من الاحداث وتحتوي على امر او أوامر

أيضاً لو رأينا في المعالج

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md) - إضافة معالج للحدث

نرى 3 أشياء

- onPlayerJoin - عند دخول اللاعب

وهو الحدث .. حيث يحدد متى يتم تشغيل المعالج - في هذه الحالة عند دخول اللاعب

- getRootElement() - جلب العنصر الحالي

هذا يقوم بتعيين العنصر الذي يقوم بتشغيل الحدث

- joinHandler

وهو إسم الوظيفة التي قمنا بصناعتها

يمكنك التوسع أكثر في : [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

### تشغيل السكربت

بعد أن تقوم بحفظ أجزاء السكربت في ملف واحد ويمكن حفظه في الملفات التالية :

- مجلد

- أرشيف .zip

ونقوم بنسخه إلى مجلد السكربتات داخل سيرفرك ونقوم بتشغيله بالطريقة العادية.

الآن إنتهينا من صنع السكربت .. بعد هذا سنقوم بصنع سكربت مع أمر

- command

يمكنك المتابعة أو الذهاب إلى دورة صناعة النوافذ

- [Introduction to Scripting GUI](mta://scripting/concepts/introduction-to-scripting-gui.md)

### إنشاء سكربت بطريقة مفصلة

## صناعة أمر بسيط

لنعد الآن إلى ملف

- script.lua

ونقوم بتعديله قليلاً لإنشاء أمر بسيط يقوم بإنشاء سيارة بجانب اللاعب

```
-- في البداية نقوم بكتب وظيفة إنشاء السيارة
function createVehicleForPlayer(thePlayer, command, vehicleModel)
   -- هنا نقوم بكتابة وظيفة إنشاء السيارة كـ
   -- createVehicle
end

-- نقوم بإضافة الأمر
addCommandHandler("createvehicle", createVehicleForPlayer)
```

*ملاحظة: يمكنك الضغط على الوظائف والتعمق فيها بداخل الويكي.*

## الوظيفة

الوظيفة هي شيء يسمى

function

الوظيفة هي الشيء التي يتكون عليها الحدث

يمكنك ان تسمي الوظيفة كما شئت ويمكنك أيضاً عدم وضع اسم للوظيفة

**مثال لـ وظيفة لها إسم**

```
function arabs( ) -- الوظيفة
    outputChatBox("مرحباً بك") --s  ستلاحظ بـ أن كلمة " مرحباً بك " ظهرت في الشات عند دخول الاعب 
end
addEventHandler("onPlayerJoin", root, arabs) -- .الحدث مع اسم الوظيفة
-- root = getRootElement()
```

**مثال لـ وظيفة ليس لها إسم**

```
addEventHandler("onPlayerWasted", root,
function(_,killer)
    outputChatBox( killer .. " من قبل" .. getPlayerName(source) .. " لقد قُتل الاعب" )
end)
```

كما تلاحظ ووضع قوس قريباً من

end)

هذا القوس يكمل القوس الآخر كما نلاحظ في الحدث

addEventHandler(

## الحدث

الحدث هو شيء يسمى

event

الحدث هو الذي يتكون على بناء الوظيفة
فـ اذا رجعنا الى الامثلة التي في الاعلى سوف نرى عدة احداث ومنها

[onPlayerWasted](mta://scripting/server/events/onplayerwasted.md)

الحدث ببساطة يحدد متى سوف تحدث او كيف سوف تحدث الوظائف التي ادخلتها

onPlayerWasted

عند موت الاعب

**مثال للحدث**

```
function onJoin()
    x, y, z = getElementPosition(source) -- s يآتي بمكان الاعب x, y, z
	    local theVehicle = createVehicle(445, x, y, z) -- s السيارة التي سـ تصنع بمكان الاعب الذي تم تحديده مسبقاً
		    warpPedIntoVehicle(source, theVehicle) -- s يجعل الاعب داخل السيارة
end
addEventHandler("onPlayerJoin", root, onJoin) -- s الحدث
-- root = getRootElement()
```

هذه الوظيفة مع هذا الحدث سوف يعطون الاعب سيارة عند دخوله السيرفر

ملاحظة الحدث ليس دائم على الوظيفة فـ أيصاً يمكنك تكوين هذه الوظيفة على حدث آخر

**مثال**

```
function onJoin()
    x, y, z = getElementPosition(source)
	    local theVehicle = createVehicle(445, x, y, z)
		    warpPedIntoVehicle(source, theVehicle)
end
addEventHandler("onPlayerLogin", root, onJoin)
```

هذا سوف يعطي الاعب سيارة لاكن ليس عند دخوله السيرفر , إنما عند دخوله حسابه

مثال آخر

```
addEventHandler("onVehicleExplode",root, -- نضيف حدث عند إنفجار اي سيارة
    function() -- الوظيفة
        setTimer(destroyElement,5000,1,source) -- يخفي السيارة بعد 5 ثواني من انفاجرها 
    end
)
```

يمكنك ان تجد
الاحداث
والوظائف 
كلنت وسيرفر
هنا

كلنت:

**وظائف كلنت**

[http://wiki.multitheftauto.com/wiki/Client_Scripting_Functions](http://wiki.multitheftauto.com/wiki/Client_Scripting_Functions)

**احداث كلنت**

[http://wiki.multitheftauto.com/wiki/Client_Scripting_Events](http://wiki.multitheftauto.com/wiki/Client_Scripting_Events)

سيرفر:

**وظائف سيرفر**

[http://wiki.multitheftauto.com/wiki/Server_Scripting_Functions](http://wiki.multitheftauto.com/wiki/Server_Scripting_Functions)

**احداث سيرفر**

[http://wiki.multitheftauto.com/wiki/Server_Scripting_Events](http://wiki.multitheftauto.com/wiki/Server_Scripting_Events)

## String الـ

السترنج هو شيء يوجد في بعض الوظايف التي توجد داخل الام تي اي

مثلاً

```
addEventHandler("onResourceStart",resourceRoot, -- الايفنت هنا يجب ان تكون بين سترنق كما الموضح هنا
    function()
        outputChatBox("تم بدء السكربت") -- s هنا سوف يظهر رسالة بالشات " تم بدء السكربت " عند بدء السكربت ويجب ان تكون سترنق
    end
) -- نهاية قوس الحدث
```

السترنق له عدة أشكال , فيمكن ان يكون كالآتي

""

أو

' '

أو

[[]]

فمثلاً اذا نريد ان نخرج رسالة بعلبة الشات

يمكن ان تكون كذلك

```
outputChatBox([[مرحباً]])

-- أو كذلك
outputChatBox('مرحباً')

-- أو كذلك

outputChatBox("مرحباً")
```

#### Command handlerعن الـ

.(`) أو زر F8 التي يمكن للاعب ان يعرضها باستخدام زر Consoleهو اسم الامر الذي يمكن للاعب ان يدخله في الـ [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md) في argument أول

."createVehicleForPlayer"هي وظيفة تُنفذ عند كتابة اللاعب الامر في هذه الحالة لـ [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md) في argument ثاني

اذا كنت متمرس في البرمجة, ستعرف انك ستحتاج ان تنفذ وظيفة مثل

```
functionName(argument1, argument2, argument3, ..)
```

```
functionName(thePlayer, commandName, argument3, ..)
```

إذا ألقينا نظرة فاحصة على المثال السفلي أعلاه ، فيمكننا أن نرى الوسيطة 1 هي اللاعب و الوسيطة 2 هي commandName. thePlayer هو ببساطة الشخص الذي كتب الأمر ، لذا أياً كان ما تسميه ، فإن المتغير سيحتوي على اللاعب الذي قام بتنشيط الأمر. commandName هو ببساطة الأمر الذي كتبوه. لذلك إذا كتبوا "/ تحية" ، فستحتوي هذه الوسيطة على "تحية". الحجة 3 هي شيء إضافي كتبه اللاعب ، وستتعلمه قليلاً في البرنامج التعليمي. لا تنس أبدًا أن الوسيطتين الأوليين عبارة عن وسيطات قياسية ، ولكن يمكنك تسميتها بأي شيء تريده.

لقد أطلقنا على وظيفة addCommandHandler بهذه الطريقة بالفعل ، وبما أن createVehicleForPlayer هي وظيفة أيضًا ، يمكن تسميتها بهذه الطريقة أيضًا. لكننا نستخدم معالج أوامر لذلك ، والذي يطلق عليه بطريقة مماثلة ، داخليًا.

على سبيل المثال: يقوم شخص ما بكتابة "createvehicle 468" في لوحة التحكم لإنتاج Sanchez ، يستدعي معالج الأوامر وظيفة createVehicleForPlayer ، كما لو كان لدينا سطر التعليمات البرمجية هذا في البرنامج النصي:

```
createVehicleForPlayer(thePlayer,"createvehicle","468") -- thePlayer هو الشيء الي كتب الكومند
```

As we can see, it provides several parameters: the player who called the command, the command he entered and whatever text he had after that, in this case "468" as vehicle id for the Sanchez. The first two parameters are the same with all command handlers, which you can read on the [addEventHandler](mta://scripting/shared/functions/addeventhandler.md) page. For this fact, you always have to define at least those two parameters to use any after that (for example to process text that was entered after the command, like in our example the vehicle model id).

*Note: You have to add the command handler AFTER you defined the handler function, else it can't find it. The order of execution matters.*

#### Writing the function

In order to fill the function we created, we need to think about what we have to do:

- Get the players position, so we know where to spawn the vehicle (we want it to appear right beside the player)

- Calculate the position we want to spawn the vehicle at (we don't want it to appear in the player)

- Spawn the vehicle

- Check if it has been spawned successfully, or output a message

In order to achieve our goals, we have to use several functions. To find function we need to use, we should visit the [Server Functions List](mta://scripting/concepts/scripting-functions.md). First we need a function to get the players position. Since players are Elements, we first jump to the **Element functions** where we find the [getElementPosition](mta://scripting/shared/functions/getelementposition.md) function. By clicking on the function name in the list, you get to the function description. There we can see the syntax, what it returns and usually an example. The syntax shows us what arguments we can or have to submit.

For [getElementPosition](mta://scripting/shared/functions/getelementposition.md), the syntax is:

```
float, float, float getElementPosition ( element theElement )
```

The three *float* in front of the function name are the return type. In this case it means the function returns three floating point numbers. (x, y and z) Within the parentheses, you can see what arguments you have to submit. In this case only the element whose position you want to get, which is the player in our example.

```
function createVehicleForPlayer(thePlayer, command, vehicleModel)
	-- نأتي باحداثيات المكان الي نبغي نضع فيه السيارة بشكل x, y, z
	-- (local  تعني ان هاد الاختصار ما رح يشغل غير في هاد الفنكشن)
	local x,y,z = getElementPosition(thePlayer)
end
```

Next we want to ensure that the vehicle won't spawn directly in the player, so we add a few units to the *x* variable, which will make it spawn east from the player.

```
function createVehicleForPlayer(thePlayer, command, vehicleModel)
	local x,y,z = getElementPosition(thePlayer) -- نأتي بمكان الاعب
	x = x + 5 -- add 5 units to the x position
end
```

Now we need another function, one to spawn a vehicle. We once again search for it on the [Server Functions List](mta://scripting/concepts/scripting-functions.md), this time - since we are talking about vehicles - in the **Vehicle functions** section, where we will choose [createVehicle](mta://scripting/shared/functions/createvehicle.md). In this function's syntax, we only have one return type (which is more common), a vehicle element that points to the vehicle we just created. Also, we see that some arguments are enclosed within [ ] which means that those are optional.

We already have all arguments we need for [createVehicle](mta://scripting/shared/functions/createvehicle.md) in our function: The position we just calculated in the *x,y,z* variables and the model id that we provided through the command ("createvehicle 468") and can access in the function as *vehicleModel* variable.

```
function createVehicleForPlayer(thePlayer, command, vehicleModel)
	local x,y,z = getElementPosition(thePlayer) --  نأتي بمكان الاعب
	x = x + 5 -- add 5 units to the x position
	-- create the vehicle and store the returned vehicle element in the ''createdVehicle'' variable
	local createdVehicle = createVehicle(tonumber(vehicleModel),x,y,z)
end
```

Of course this code can be improved in many ways, but at least we want to add a check whether the vehicle was created successfully or not. As we can read on the [createVehicle](mta://scripting/shared/functions/createvehicle.md) page under **Returns**, the function returns *false* when it was unable to create the vehicle. Thus, we check the value of the *createVehicle* variable.

Now we have our complete script:

```
function createVehicleForPlayer(thePlayer, command, vehicleModel)
	local x,y,z = getElementPosition(thePlayer) --  نأتي بمكان الاعب
	x = x + 5 -- نضيف 5 وحد ل الاحداثيات X
	local createdVehicle = createVehicle(tonumber(vehicleModel),x,y,z)
	-- نشوف لو السيارة اتعملت ام لا
	if (createdVehicle == false) then
		-- لو السياره اتعملت يبقي نعمل رسالة,لكن للاعب فقط
		outputChatBox("Failed to create vehicle.",thePlayer)
	end
end
addCommandHandler("createvehicle", createVehicleForPlayer)
```

As you can see, we introduced another function with [outputChatBox](mta://scripting/shared/functions/outputchatbox.md). By now, you should be able to explore the function's documentation page yourself. For more advanced scripting, please check out the [Map Manager](mta://mapping/map-manager.md).

## ما تحتاج إلى معرفته

You already read some things about resources, command handlers and finding functions in the documentation in the first paragraph, but there is much more to learn. This section will give you a rather short overview over some of these things, while linking to related pages if possible.

### سكربتات الخادم والعميل

You may have already noticed these or similiar terms (Server/Client) somewhere on this wiki, mostly in conjunction with functions. MTA not only supports scripts that run on the server and provide commands (like the one we wrote above) or other features, but also scripts that run on the MTA client the players use to connect to the server. The reason for this is, that some features MTA provides have to be clientside (like a GUI - Graphical User Interface), others should be because they work better and still others are better off to be serverside or just don't work clientside.

Most scripts you will make (gamemodes, maps) will probably be serverside, like the one we wrote in the first section. If you run into something that can't be solved serverside, you will probably have to make it clientside. For a clientside script for example, you would create a ordinary script file (for example called *client.lua*) and specify it in the meta.xml, like this:

```
<script src="client.lua" type="client" />
```

The *type* attribute defaults to 'server', so you only need to specify it for clientside scripts. When you do this, the clientside script will be downloaded to the player's computer once he connects to the server. Read more about [Client side scripts](mta://reference/misc/client-side-scripts.md).

### مصادر اكثر تعقيدا

The previous section showed briefly how to add clientside scripts to the resource, but there is also much more possible. As mentioned at the very top of this page, resources can be pretty much everything. Their purpose is defined by what they do. Let's have some theoretical resources, by looking at the files it contains, the *meta.xml* and what they might do:

#### First example - A utility script

```
/admin_commands
	/meta.xml
	/commands.lua
	/client.lua
```

```
<meta>
	<info author="Someguy" description="admin commands" />
	<script src="commands.lua" />
	<script src="client.lua" type="client" />
</meta>
```

- The *commands.lua* provides some admin commands, like banning a player, muting or something else that can be used to admin the server

- The *client.lua* provides a GUI to be able to perform the mentioned actions easily

This example might be running all the time (maybe even auto-started when the server starts) as it's useful during the whole gaming experience and also wont interfere with the gameplay, unless an admin decides to take some action of course.

#### Second example - A gamemode

```
/counterstrike
	/meta.xml
	/counterstrike.lua
	/buymenu.lua
```

```
<meta>
	<info author="Someguy" description="Counterstrike remake" type="gamemode" />
	<script src="counterstrike.lua" />
	<script src="buymenu.lua" type="client" />
</meta>
```

- The *counterstrike.lua* contains similiar to the following features:

- Let players choose their team and spawn them

- Provide them with weapons, targets and instructions (maybe read from a Map, see below)

- Define the game's rules, e.g. when does the round end, what happens when a player dies

- .. and maybe some more

- The *buymenu.lua* is a clientside script and creates a menu to buy weapons

This example can be called a gamemode, since it not only intereferes with the gameplay, but actually defines the rules of it. The *type* attribute indicates that this example works with the [Map manager](mta://mapping/map-manager.md), yet another resource that was written by the QA Team to manage gamemodes and map loading. It is highly recommended that you base your gamemodes on the techniques it provides.

This also means that the gamemode probably won't run without a map. Gamemodes should always be as generic as possible. An example for a map is stated in the next example.

#### Third example - A Map

```
/cs-airport
	/meta.xml
	/airport.map
	/airport.lua
```

```
<meta>
	<info author="Someguy" description="Counterstrike airport map" type="map" gamemodes="counterstrike" />
	<map src="airport.map" />
	<script src="airport.lua" />
</meta>
```

- The *airport.map* in a XML file that provides information about the map to the gamemode, these may include:

- Where the players should spawn, with what weapons, what teams there are

- What the targets are

- Weather, World Time, Timelimit

- Provide vehicles

- The *airport.lua* might contain map-specific features, that may include:

- Opening some door/make something explode when something specific happens

- Create or move some custom objects, or manipulate objects that are created through the .map file

- .. anything else map-specific you can think of

As you can see, the *type* attribute changed to 'map', telling the [Map manager](mta://mapping/map-manager.md) that this resource is a map, while the *gamemodes* attribute tells it for which gamemodes this map is valid, in this case the gamemode from the above example.
What may come as a surprise is that there is also a script in the Map resource. Of course this is not necessarily needed in a map, but opens a wide range of possibilities for map makers to create their own world within the rules of the gamemode they create it for.

The *airport.map* file might look similiar to this:

```
<map mode="deathmatch" version="1.0">
	<terrorists>
		<spawnpoint posX="2332.23" posY="-12232.33" posZ="4.42223" skins="23-40" />
	</terrorists>
	<counterterrorists>
		<spawnpoint posX="2334.23443" posY="-12300.233" posZ="10.2344" skins="40-50" />
	</counterterrorists>

	<bomb posX="23342.23" posY="" posZ="" />
	
	<vehicle posX="" posY="" posZ="" model="602" />	
	<vehicle posX="" posY="" posZ="" model="603" />	
</map>
```

When a gamemode is started with a map, the map resources is automatically started by the mapmanager and the information it contains can be read by the gamemode resource. When the map changes, the current map resource is stopped and the next map resource is started. For a more in-depth explanation and examples of how map resources are utilized in the main script, please visit the [Writing Gamemodes](mta://mapping/writing-gamemodes.md) page.

## Where to go from here

You should now be familiar with the most basic aspects of MTA scripting and also a bit with the documentation. The [Main Page](mta://reference/misc/main-page.md) provides you with links to more information, Tutorials and References that allow a deeper look into the topics you desire to learn about.

From here we recommend reading the [debugging](mta://scripting/concepts/debugging.md) tutorial. Good debugging skills are an absolute necessity when you are making scripts.
