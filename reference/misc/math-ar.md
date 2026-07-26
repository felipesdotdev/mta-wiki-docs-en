---
doc_id: "mta-wiki:6711"
title: "AR/Math"
source_title: "Math ar"
source_url: "https://wiki.multitheftauto.com/wiki/Math_ar"
revision_id: 73365
language: "en"
categories: []
generated_at: "2026-07-26T16:16:10.899744+00:00"
---

# AR/Math

math.abs

تستخدم لتحويل العدد من السالب الي الموجب

## تركيب الكود

```
float/int math.abs(number)
```

### المفردات

- **number** = الرقم الذي تريد ان تحوله الى موجب

## مثال

Click to collapse [-]
مثال

هذا المثال يقوم بتحويل العدد الى رقم موجب في الردار

```
myElegy = createVehicle(562, 1591.596680, -2495.323242, 18.098244) 

local x,y,z = getElementPosition(myElegy)

grX = math.abs(math.random(-30,1)
grY = math.abs(math.random(-30,1)

areaID = createRadarArea(x,y, grX, grY, 0, 0, 0, 0)
```

## math.ceil

يستخدم لتقريب العدد العشري الى اكبر عدد صحيح

## تركيب الكود

```
float/int math.ceil(number)
```

## المفردات

- **number** = الرقم الذي تريد تقريبه الى العدد الصحيح الاكبر

## مثال

Click to collapse [-]
مثال

```
myElegy = createVehicle(562, 1591.596680, -2495.323242, 18.098244) 

local x,y,z = getElementPosition(myElegy)

grX = math.ceil(math.random(1.235,100.4575))
grY = math.ceil(math.random(1.235,100.4575))

areaID = createRadarArea(x,y, grX, grY, 0, 0, 0, 0)
```

 

## math.floor

يستخدم لتقريب العدد العشري وحذف العدد العشري الذي بعد الفاصله

## تركيب الكود

```
float/int math.floor(number)
```

## المفردات

- **number** = العدد الذي تريد ان تقربه وتحذف الفاصله

## مثال

Click to collapse [-]
مثال

```
addCommandHandler('Health', -- امر من اف8
function(player,_,who) -- وظيفه
	if who then -- تحقق
		local ThePlayer = getPlayerFromName(who) -- نحظر اسم اللاعب
			local Health = math.floor(getElementHealth(ThePlayer)) -- نحظر صحه اللاعب (الدم) مع حذف الارقام بعد الفاصله
				outputChatBox('* His Health : '..Health,player,255,255,255,true) -- نخرج نص الى الشات
		end -- اغلاق
	end -- اغلاق
) -- اغلاق

-- By : The Best
```

 

## math.round

يستخدم للتقريب إما عدد اكبر او اصغر بحيث اذا كان العدد الذي بعد الفاصله 5 او اكبر يقربه الى الاكبر منه,أما اذا كان العدد اصغر من 5 فسوف يحذف الرقم الي بعد الفاصله فقط

## تركيب الكود

```
float/int math.round(number)
```

## المفردات

- **number** = العدد الذي تريد تقريبه الى الاكبر او الاصغر

## مثال

Click to collapse [-]
مثال

```
-- .ملاحظة : الكود ما راح يشتغل بدون هذه الوظيفه

function math.round(number, decimals, method)
    decimals = decimals or 0
    local factor = 10 ^ decimals
    if (method == "ceil" or method == "floor") then return math[method](number * factor) / factor
    else return tonumber(("%."..decimals.."f"):format(number)) end
end

-- : المثال

local Number = 10.5 -- متغير مع قيمه

addCommandHandler('Round', -- امر من اف8
function(player) -- وظيفه 
	outputChatBox('* The Number : '..math.round(tonumber(Number)),player,255,255,255,true) -- نص في الشات
	end -- اغلاق
) -- اغلاق

-- 11 الناتج راح يكون

-- لأن العدد الذي بعد الفاصله 5 او اكبر

-- لو كان العدد 10.4 راح يكون الناتج 10

-- By : The Best
```

 

## math.mod

هذا الحدث يستخدم لتحديد باقي القسمة بحيث عند كتابة عددين يقوم الحدث بايجاد باقي القسم بين العدد المقسوم والعدد المقسوم عليه

## تركيب الكود

```
float/int math.mod(number)
```

## المفردات

- **number** = العدد الذي تريد تحديد باقي القسمه له

## مثال

Click to collapse [-]
مثال

```
-- TODO
```

 

## math.sqrt

تستخدم لحساب الجذر التربيعي للعدد

## تركيب الكود

```
float/int math.sqrt(number)
```

## المفردات

- **number** = العدد الذي تريد حساب الجذر التربيعي له

## مثال

Click to collapse [-]
مثال

```
-- ملاحظة : الحساب يكون بالجذر التربيعي للعدد

-- مثال --

math.sqrt(100) -- نحدد قيمه الجذر
10 -- الناتج

-- مثال آخر -- 

math.sqrt(10000) -- نحدد قيمة الجذر
100 -- الناتج

-- مثال على كود --

-- كلينت 

Health = guiCreateButton(131,163,113,46,"Give me health",false) -- نسوي زر
addEventHandler("onClientGUIClick",Health, -- اذا ضغط على الزر
function() -- وظيفة
triggerServerEvent("Health",localPlayer) -- نرسل الوظيفة للسيرفر
end,false) -- اغلاق

-- سيرفر

addEvent("Health",true) -- نحظر الوظيفة من الكلينت
addEventHandler("Health",root, -- نحظر الوظيفة من الكلينت
function() -- وظيفة
if (getElementHealth(source) <= 30 ) then -- نتحقق ان دم اللاعب يساوي 30 او اقل
setElementHealth(source,math.sqrt(10000)) -- اعطاء دم للجذر التربيعي 10000
      end -- اغلاق
end) -- اغلاق

-- هنا راح يعطي اللاعب دم على حسب الجذر التربيعي للـ10000

-- الجذر التربيعي لـ10000 = 100

-- By : The Best
```

 

## math.pow

تستخدم لحساب الأسس بحيث اذا تم كتابه رقمين يتم ضرب الرقم الاول في الثاني حسب العدد

## تركيب الكود

```
float/int math.pow(number,number2)
```

## المفردات

- **number** = العدد الاول الذي تريد ان تضربه في العدد الثاني

- **number2** = العدد الثاني الذي سيضرب العدد الاول فيه

## مثال

Click to collapse [-]
مثال

```
-- عملية الحساب تكون بالضرب

math.pow(9,9) -- نضرب الاسس
3.8742048 -- الناتج

-- مثال آخر -- 

math.pow(6,7) -- نضرب الاسس
279936 -- الناتج

-- عملية الضرب كالتالي :

-- اول مثال الناتج 90

-- نضرب 9 في نفسها 9 مرات :

-- 9×9×9×9×9×9×9×9×9 = 3.8742048

-- المثال الثاني :

-- نضرب 6 في نفسها 7 مرات :

-- 6×6×6×6×6×6×6 = 279936

-- مثال على كود --

addEventHandler("onResourceStart",resourceRoot, -- اذا تم تشغيل السكربت
function() -- وظيفة
for _,Player in pairs ( getElementsByType ( "player" ) ) do -- تحديد النوع وهم جميع اللاعبين
if (getPlayerMoney(Player) >= 50 ) then -- نتحقق ان فلوس اللاعب تساوي 50 او اكثر
givePlayerMoney(Player,math.pow(9,4)) -- نعطي اللاعب فلوس على حسب ضرب الاسس
            end -- اغلاق
      end -- اغلاق
end) -- اغلاق

-- الفلوس الي راح يعطيها اللاعب هي 6561

-- نتيجه للضرب 9×9×9×9 = 6561

-- By : The Best
```

 

## math.random

هذه الداله تستخدم لكي تظهر رقم عشوائي بحيث عند كتابة العدد الاول والعدد الثاني يقوم الحدث  باظهار رقم عشوائي بين الرقمين التي ادخلتها

```
float/int math.random(number)
```

Click to collapse [-]
مثال

```
addEventHandler("onResourceStart",resourceRoot, -- اذا تم تشغيل السكربت
function() -- وظيفه
Height = math.random(50,100) -- رقم عشوائي لإرتفاع الماء
setWaveHeight(Height) -- نربط ارتفاع الماء بالرقم العشوائي
end) -- اغلاق

-- مثال آخر --

addEventHandler("onResourceStart",resurceRoot, -- اذا تم تشغيل السكربت
function() -- وظيفه
for _,Player in ipairs ( getElementType ( "player" ) ) do -- نحدد النوع وهو اللاعب
if getPlayerMoney ( Player ) >= 100 then --  اذا اللاعب عنده 100 او اكثر 
givePlayerMoney(Player, math.random(50,100)) -- يعطيه رقم عشوائي مابين 50 و 100
           end -- اغلاق
     end -- اغلاق
end) -- اغلاق

-- By : The Best
```

 

___________________________________________________________________

## math.randomseed

هذا الحدث يستخدم لكي يظهر رقم عشوائي ثابت بحيث عند كتابة عدد يقوم الحدث  باظهار رقم عشوائي ثابت بين رقمين مثل (100-9999) ولن يتغير هذا 
الرقم العشوائي ابداً ولتغيره يجب تغير العدد المدخل في البداية

```
float/int math.randomseed(number)
```

Click to collapse [-]
مثال

```
--
```

 

___________________________________________________________________

## math.HexToNumber

هذا الحدث يستخدم لتحويل الارقام من النظام السادس عشر (Hex) الى النظام العشري (Dec)بحيث عند كتابة عدد Hex يقوم الحدث  بتحويله الى عدد Dec 

معلومة :
ارقام Hex هي (0 ، 1 ، 2، 3 ،4 ،5 ، 6، 7 ،8 ، 9 ، F ،E ،D ،C ،B ، A )

ارقام Dec هي (0 ، 1 ، 2، 3 ،4 ،5 ، 6، 7 ،8 ، 9 )

```
float/int math.HexToNumber(number)
```

Click to collapse [-]
مثال

```
--
```

 

___________________________________________________________________

## math.rad

هذا الحدث يستخدم لتحويل قياس الزاوية من راديان الى درجة بحيث عند كتابة الزاوية بالراديان يعمل الحدث  بتحويله الى درجة

```
float/int math.rad(number)
```

Click to collapse [-]
مثال

```
--
```

 

## math.HexColorToNumber

هذا الحدث يستخدم لتحويل رقم اللون من هيكس الى ديكس بحيث عند كتابة رقم هيكس يعمل الحدث بتحويله الى ديكس

```
float/int math.HexColorToNumber(number)
```

Click to collapse [-]
مثال

```
--
```

 

## math.deg

هذا الحدث يستخدم لتحويل قياس الزاوية من درجة الى راديان بحيث عند كتابة درجة الزاوية يقوم الحدث Math.Rad بتحويله الى راديان

معلومة:

راديان :هي وحدة قياس الزوايا الرسمية المعتمدة ضمن مجموعة الوحدات القياسية المستخدمة في الرياضيات و الفيزياء و تعرف بأنها الزاوية المركزية المتوضعة على مركز الدائرة و التي تحدد قوسا طولها مساوي لنصف قطر الدائرة.
كيف نحسب الراديان
للتحويل من راديان إلى درجات نضرب الراديان في 180 ونقسم الحاصل على ( باي ) وللتحويل من الدرجات إلى راديان نضرب الدرجات في ( باي ) ونقسم الحاصل على 180

```
float/int math.deg(number)
```

Click to collapse [-]
مثال

```
--
```

 

## math.RGBToNumber

هذا الحدث يستخدم لتحويل رقم الالوان الاساسية الاحمر والاخضر والازرق من Hex الى Dec بحيث عند كتابة ارقام ثلاثة الالوان يعمل الحدث Math.RGBToNumber بتحويله الى Dex

```
float/int math.RGBToNumber(number)
```

Click to collapse [-]
مثال

```
--
```

 

## math.sin

هذا الحدث يستخدم لحساب جيب الزاوية (جا) بحيث عند كتابة قياس الزاوية يعمل الحدث Math.Sin بحساب جيب الزاوية

ملاحظة : يجب قبل حساب جا تحويل قياس الزاوية الى راديان بالحدث Math.Rad

```
float/int math.sin(number)
```

Click to collapse [-]
مثال

```
--
```

 

## math.cos

هذا الحدث يستخدم لحساب جيب تمام الزاوية (جتا) بحيث عند كتابة قياس الزاوية يعمل الحدث  بحساب جيب الزاوية

```
float/int math.cos(number)
```

Click to collapse [-]
مثال

```
--
```

 

## math.tan

هذا الحدث يستخدم لحساب ظل الزاوية (ظا) بحيث عند كتابة قياس الزاوية يعمل الحدث  بحساب ظل الزاوية

```
float/int math.tan(number)
```

Click to collapse [-]
مثال

```
--
```

 

## math.asin

هذا الحدث يستخدم لحساب معكوس جا بحيث عند كتابة العدد يعمل الحدث  بحساب معكوس جا الزاوية

```
float/int math.asin (number)
```

Click to collapse [-]
مثال

```
--
```

 

## math.acos

هذا الحدث يستخدم لحساب معكوس جتا بحيث عند كتابة العدد يعمل الحدث  بحساب معكوس جتا الزاوية

```
float/int math.acos (number)
```

Click to collapse [-]
مثال

```
--
```

 

___________________________________________________________________

## math.atan

هذا الحدث يستخدم لحساب معكوس ظا بحيث عند كتابة العدد يعمل الحدث  على حساب معكوس ظا الزاوية

```
float/int math.atan(number)
```

Click to collapse [-]
مثال

```
--
```

 

___________________________________________________________________

## math.atan2

هذا الحدث يستخدم لحساب مقسوم معكوس ظا بحيث عند كتابة العدد الاول والثاني يعمل الحدث Math.Atan2 على حساب معكوس ظا (العدد الاول / العدد الثاني)

```
float/int math.atan2(number)
```

Click to collapse [-]
مثال

```
--
```

 

## math.max

```
هذا الحدث يستخدم لتحديد العدد الاكبر من الاخر بحيث عند كتابة عددين يقوم الحدث 
بمقارنة العددين وتحديد العدد الاكبر
```

```
float/int math.max(number1,number2,number...)
```

Click to collapse [-]
مثال

```
math.max(15, -100, 30) -- نحدد القيم المراد الاختيار منها
30 -- الناتج
math.max(2.5, -2.5)
2.5 -- النتاج

ملاحظة : السالب تكون قيمته صغيرة

-- By The Best
```

 

## math.min

```
هذا الحدث يستخدم لتحديد العددالاصغر من الاخر بحيث عند كتابة عددين يقوم الحدث 
بمقارنة العددين وتحديد العدد الاصغر
```

```
float/int math.min(number1,number2,number...)
```

Click to collapse [-]
مثال

```
addEventHandler("onResourceStart",resourceRoot, -- اذا تم تشغيل السكربت
function() -- وظيفة
outputChatBox("The number is "..math.min(10,-20).." is good") -- نظهر نص في الشات
end) -- اغلاق

-- الرقم الي بيظهر في الشات هو -20

-- ملاحظة السالب اصغر من الموجب

-- By The Best
```

 

تعريب السالمي 
[http://ams4arab.arabstar.biz/t107-topic](http://ams4arab.arabstar.biz/t107-topic)  المصدر     

## See Also

- [Math](mta://reference/misc/math.md)

- [Math examples on the LUA Wiki](http://lua-users.org/wiki/MathLibraryTutorial)
