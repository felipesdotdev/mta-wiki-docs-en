---
doc_id: "mta-wiki:7954"
title: "Строка"
source_title: "Строка"
source_url: "https://wiki.multitheftauto.com/wiki/%D0%A1%D1%82%D1%80%D0%BE%D0%BA%D0%B0"
revision_id: 70744
language: "en"
categories: ["Понятия_скриптинга"]
generated_at: "2026-07-26T16:16:57.838954+00:00"
---

# Строка

String *(строка)* - это тип данных, значение которого является последовательность символов.

Использование функции lua [tostring()](https://uopilot.uokit.com/wiki/index.php?title=Tostring_(Lua)) может преобразовать другие типы данных в string:

```
local theReturn = tostring(isPedDead(getRandomPlayer())) -- преобразует тип данных boolean в string
outputChatBox("Возврат функции: "..theReturn) -- сообщит игроку: "true" или "false"
outputChatBox("Тип данных возврата функции: "..type(theReturn)) -- сообщит игроку "string"
```

Использование функции lua [type()](https://user.su/lua/index.php?id=3) может помочь вам узнать, что это за тип данных:

```
local thePlayer = getRandomPlayer()
setPlayerName(thePlayer, "Bob")
local namePlayer = getPlayerName(thePlayer)
outputChatBox("Возврат функции: "..namePlayer) -- сообщит игроку: "Bob"
outputChatBox("Тип данных возврата функции: "..type(namePlayer)) -- сообщит игроку "string"
```

## Пример присвоения значений

```
str = "Hello, World!" -- двойные кавычки
str = 'Hello, World!' -- одинарные кавычки
str = [[Hello, 
      World!]] -- сохраняет табуляцию и переносы
str = nil -- если вы хотите стереть переменную
```

## Список всех стандартных функций для манипуляций над строками в Lua

- [string.byte](http://www.lua.org/manual/5.1/manual.html#pdf-string.byte)

- [string.char](http://www.lua.org/manual/5.1/manual.html#pdf-string.char)

- [string.dump](http://www.lua.org/manual/5.1/manual.html#pdf-string.dump)

- [string.find](http://www.lua.org/manual/5.1/manual.html#pdf-string.find)

- [string.format](http://www.lua.org/manual/5.1/manual.html#pdf-string.format)

- [string.gmatch](http://www.lua.org/manual/5.1/manual.html#pdf-string.gmatch)

- [string.gsub](http://www.lua.org/manual/5.1/manual.html#pdf-string.gsub)

- [string.len](http://www.lua.org/manual/5.1/manual.html#pdf-string.len)

- [string.lower](http://www.lua.org/manual/5.1/manual.html#pdf-string.lower)

- [string.match](http://www.lua.org/manual/5.1/manual.html#pdf-string.match)

- [string.rep](http://www.lua.org/manual/5.1/manual.html#pdf-string.rep)

- [string.reverse](http://www.lua.org/manual/5.1/manual.html#pdf-string.reverse)

- [string.sub](http://www.lua.org/manual/5.1/manual.html#pdf-string.sub)

- [string.upper](http://www.lua.org/manual/5.1/manual.html#pdf-string.upper)

## Смотрите также

- ["String" в программировании на Lua](http://www.lua.org/pil/2.4.html)
