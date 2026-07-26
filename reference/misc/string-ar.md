---
doc_id: "mta-wiki:6671"
title: "AR/String"
source_title: "String ar"
source_url: "https://wiki.multitheftauto.com/wiki/String_ar"
revision_id: 74410
language: "en"
categories: []
generated_at: "2026-07-26T16:16:54.046662+00:00"
---

# AR/String

المكتبه ناقصة الدوال

string.dump()

ساعدنا بااضافة الدوال للمكتبه

**string.upper** وهي دالة

```
تستخدم للتحويل حالةالاحرف من الاحرف الصغيره الى الاحرف الكبيره
.
```

Click to collapse [-]
Example

```
test1 = string.upper("Hello, Lua user!")

HELLO, LUA USER!
```

___________________________________________________________________

**string.sub**

```
تستخدم لتحديد بداية ونهاية السلسله ، حيث ان الرقم الاول يحدد بداية السلسه
والرقم الثاني يحدد نهاية السلسه 
وعند وضع الرقم بالسالب سوف تقوم بتحديد السلسه بالعكس
```

Click to collapse [-]
Example

```
test1 = string.sub("Hello Lua user", 7)
Lua user

test2 = string.sub("Hello Lua user", 7, 9)
Lua

test3 = string.sub("Hello Lua user", -8)
Lua user

test4 = string.sub("Hello Lua user", -8,9)
Lua

test5 = string.sub("Hello Lua user", -8,-6)
Lua
```

___________________________________________________________________

**string.reverse**

```
تستخدم لعكس السلسه
.
```

Click to collapse [-]
Example

```
test1 = string.reverse("krsofa")

afosrk
```

___________________________________________________________________

**string.rep**

```
تستخدم لنسخ السلسه على حسب الرقم
.
```

Click to collapse [-]
Example

```
test1 = string.rep("Lua ",5)
Lua Lua Lua Lua Lua

test2 = string.rep("KrSoFa\n",3)
KrSoFa                                                                 
KrSoFa
KrSoFa
```

___________________________________________________________________

**string.lower**

```
تستخدم للتحويل حالةالاحرف من الاحرف الكبيره الى الاحرف الصغيره
.
```

Click to collapse [-]
Example

```
test1 = string.lower("Hello, KrSoFa user!")
hello, krsofa user!
```

___________________________________________________________________

**string.len**

```
تستخدم لمعرفة طول السلسله 
.
```

Click to collapse [-]
Example

```
test1 = string.lower("Hello, KrSoFa user!")
hello, krsofa user!

test1  = string.len("Lua")
3
test2  = string.len("")
0
test3  = string.len("Lua\000user")   -- Lua strings are 8 bit pure so \000 does not terminate
8
```

___________________________________________________________________

**string.gsub**

```
هذه هي وظيفة قوية جدا، ويمكن استخدامها بطرق متعددة
 يمكن أن تستخدم للتبديل والاستبدال
.
```

Click to collapse [-]
Example

```
-- المثال الاول يقوم بتنقيح لـ كلمة
-- banana 
 
test1 = string.gsub("Hello banana", "banana", "Lua user")
Hello Lua user  1

-- المثال الثاني يقوم بااستبدال الاحرف الاولى الصغيره 
-- a
-- الى احرف كبيره A
-- ويقوم بالاستبدال مرتين فقط
 

test2 = string.gsub("banana", "a", "A", 2)  -- limit substitutions made to 2
bAnAna  2
```

```
ويمكن أيضا إستخدامها مع الوظايف function
```

Click to collapse [-]
Example

```
--  المثال الاول يقوم بطباعة السلسله

test1 = string.gsub("Hello Lua user", "(%w+)", print)  -- print any words found
Hello
Lua
user
        3

--  المثال الثاني يقوم بتحديد طول السلسله

test2 = string.gsub("Hello Lua user", "(%w+)", function(w) return string.len(w) end) -- replace with lengths
5 3 4   3

--  المثال الثالث بااستبدال الحرف الى حروف كبيره

test3 = string.gsub("banana", "(a)", string.upper)     -- make all "a"s found uppercase
bAnAnA  3

--  المثال الثالث الوظيفه تقوم بتبديل بين الحرفين

test4 = string.gsub("banana", "(a)(n)", function(a,b) return b..a end) -- reverse any "an"s
bnanaa  2
```

___________________________________________________________________

**string.format**

```
هذه لتنسيق 
 يمكن أن تستخدم لتنسيق السلسله والمتغيرات
.
```

Click to collapse [-]
Example

```
function getPlayerStats(thePlayer)
    local account = getPlayerAccount(thePlayer)
    if account then
        local kills = getAccountData(account,"kills") or 0
        local deaths = getAccountData(account,"deaths") or 0
        local ratio = string.format("%.2f", kills / deaths)
        outputChatBox("s Stats: Kills: ".. tostring(kills) .." ), ".. tostring(deaths) .." Deaths, Ratio: ".. tostring(ratio).."", getRootElement(), 50, 255, 0)
    end
end
addCommandHandler("stats",getPlayerStats)

-- مثال لتحويل اللوان الى هيكس

function chatbox(text, msgtype)

    local account = getAccountName(getPlayerAccount(source))

    local name = getPlayerName(source)

    local tag = getElementData(source, "ID") or 0

    local r, g, b = getPlayerNametagColor(source)

    local hex = RGBToHex(r, g, b)

    if (msgtype == 0) then

        if isObjectInACLGroup("user." .. account, aclGetGroup("HeadAdmin")) then

            cancelEvent(true)

            outputChatBox(" #cccccc[".. tag .."]  #8B1A1A[HEADADMIN] ".. hex .."".. name ..": #FFFFFF".. text, root, 255, 255, 255, true)

            outputServerLog("CHAT: [HEADADMIN] " .. name .. ": " .. text)

        elseif isObjectInACLGroup("user." .. account, aclGetGroup("Admin")) then

            cancelEvent(true)

            outputChatBox("#cccccc[".. tag .."]   #FF0000[ADMIN] ".. hex .."" .. name ..": #FFFFFF" .. text, root, 255, 255, 255, true)

            outputServerLog("CHAT: [ADMIN] " .. name .. ": " .. text)

        elseif isObjectInACLGroup("user." .. account, aclGetGroup("Moderator")) then

            cancelEvent(true)

            outputChatBox("#cccccc[".. tag .."]   #00FF00[MODERATOR] ".. hex .."" .. name .. ": #FFFFFF" .. text, root, 255, 255, 255, true)

            outputServerLog("CHAT: [MODERATOR] " .. name .. ": " .. text)

        elseif isObjectInACLGroup("user." .. account, aclGetGroup("Everyone")) then

            cancelEvent(true)

            outputChatBox("#cccccc[".. tag .."] #FFFFFF".. hex .."" .. name .. ": #FFFFFF" .. text, root, 255, 255, 255, true)

            outputServerLog("CHAT: " .. name .. ": " .. text)

        end

    end

end

addEventHandler("onPlayerChat", root, chatbox)

 

function RGBToHex(red, green, blue, alpha)

    if((red < 0 or red > 255 or green < 0 or green > 255 or blue < 0 or blue > 255) or (alpha and (alpha < 0 or alpha > 255))) then

        return nil

    end

    if(alpha) then

        return string.format("#%.2X%.2X%.2X%.2X", red,green,blue,alpha)

    else

        return string.format("#%.2X%.2X%.2X", red,green,blue)

    end

end

-- لتحويل السلسله النصيه الى سلسله نصيه مقتبسه بعلامتي التنصيص

test9 = string.format("%s %q", "Hello", "Lua user!")   -- string and quoted string
Hello "Lua user!"

test10 = string.format("%c%c%c", 76,117,97)             -- char
Lua

-- مثال لاستخدام الأس

test11 = string.format("%e, %E", math.pi,math.pi)       -- exponent
3.141593e+000, 3.141593E+000

-- مثال لاستخدام float
test12 = string.format("%f, %g", math.pi,math.pi)       -- float and compact float
3.141593, 3.14159

test13 = string.format("%d, %i, %u", -100,-100,-100)    -- signed, signed, unsigned integer
-100, -100, 4294967196

test14 = string.format("%d, %i, %u", -100,-100,-100)    -- signed, signed, unsigned integer
-100, -100, 4294967196

test15 = string.format("%o, %x, %X", -100,-100,-100)    -- octal, hex, hex
37777777634, ffffff9c, FFFFFF9C
```

___________________________________________________________________

**string.find**

```
للبحث  بالسلسله 
.يجب ان تكون السلسله بعد التحميل later loadstring
```

Click to collapse [-]
Example

```
-- مثال للبحث عن كلمة  في سلسله
--

test1 = string.find("Hello Lua user", "Lua")
7       9
test2 = string.find("Hello Lua user", "banana")
nil

-- للبحث عن كلمه بااستخدام تحديد مكان البحث
-- بالرقم 

test3 = string.find("Hello Lua user", "Lua", 1)  -- start at first character
7       9
test4 = string.find("Hello Lua user", "Lua", 8)  -- "Lua" not found again after character 8
nil
test5 = string.find("Hello Lua user", "e", -5)   -- first "e" 5 characters from the end
13      13

-- مثال للبحث بااستخدام PatternsTutorial 
test6 = string.find("Hello Lua user", "%su")          -- find a space character followed by "u"
10      11

test7 = string.find("Hello Lua user", "%su", 1, true) -- turn on plain searches, now not found
nil
```

___________________________________________________________________

**string.char**

```
character codes  تستخدم لتكوين سلسلة نصيه من 
.
```

Click to collapse [-]
Example

```
test1 = string.char(65,66,67)
ABC
test2 = string.char()  -- empty string
```

___________________________________________________________________

**string.byte**

```
character codes  تستخدم  لتحويل من سلسلة نصيه الى 
.
```

Click to collapse [-]
Example

```
test1 = string.byte("ABCDE")      -- عند عدم التحديد يتم استخدام الحرف الاول للتحويل
65

test2 = string.byte("ABCDE",1)    -- تحويل الحرف الاول
65

test3 = string.byte("ABCDE",0)    -- لا يعمل عند عدم التحديد

test4 = string.byte("ABCDE",100)  -- القيمه اعلى من السلسله 

test5 = string.byte("ABCDE",3,4) -- تحويل الحرف الثالث والرابع
67      68

s = "ABCDE"
test6 = s:byte(3,4)               -- يمكن استخدام المتغير مع الداله بااستخدامها هكذا
67      68
```

___________________________________________________________________

**string.match**

تستخدم للبحث عن الكلمات المتطابقة فـ اذا لم تكن متطابقة النتيجة

**nil**

**nil** = لا قيمة أو لا شيء

Click to collapse [-]
Example

```
Exmaple1 = string.match("Tete", "Tet") -- شبه متطابقة
tet -- النتيجة

Example2 = string.match("Tete", "Tete") -- متطابقة تماماً
Tete -- النتيجة

Example3 = string.match("Tete", "mta") -- لا يوجد تطابق هنا
nil -- النتيجة
```

___________________________________________________________________

**string.rep**

تستخدم لـ مضاعفة الكلمة او الحرف إلى القيمة المعطاه

Click to collapse [-]
Example

```
Exmaple1 = string.rep("Tete", 5) -- المضاعفة 5 مرات
TeteTeteTeteTeteTete -- النتيجة

Example2 = string.rep("T .", 20) -- المضاعفة 20 مرة
T .T .T .T .T .T .T .T .T .T .T .T .T .T .T .T .T .T .T .T . -- النتيجة
```

___________________________________________________________________

**string.gmatch**

(لا شيء) nil تقوم بارجاع دالة التكرار في كل مرة يتم استدعاء هذه الوظيفة، تقوم بارجاع السلسلة الفرعية التالية الموجودة في السلسلة التي تطابق وصف النموذج. إذا لم يتم العثور على السلسلة الموضحة بنمط المعلمة، فتُرجع أداة التكرار

Click to collapse [-]
Example

```
text = "my nickname is RONIEDER"
for w in string.gmatch(text,("%u")) do -- text <- على الاحرف الكبيرة الموجودة داخل السلسلة النصية compiler سوف يبحث المترجم او  %u بما انني استخدمت 
print(w)
end
--[[
-----------
:النتيجة
R
O
N
I
E
D
E
R
-----------
سأشرح لكم شكل السلسلة / أنماطها
%a: يمثل كل الحروف
%w: يمثل جميع الأحرف الأبجدية الرقمية
%c: يمثل كل حروف التحكم
%d: decimal number = نظام العد العشري
%x: hexadecimal = يمثل جميع الأرقام السداسية عشرية
%o: octal = نظام عد ثماني
%f: floating point number = رقم النقطة العائمة
%s: strings = يمثل كل السلاسل النصية 
%p: punctuation = يمثل كل حروف الترقيم
%l: lower case = يمثل كل الحروف الصغيرة 
%u: upper case = ( يمثل كل الحروف الكبيرة ( استخدمناها لجلب الحروف الكبيرة من السلسلة النصية في المثال أعلاه
-----------
--]]
```

___________________________________________________________________

دوال لم يتم ترجمتها ووضع امثله عليها

string.dump(function)
