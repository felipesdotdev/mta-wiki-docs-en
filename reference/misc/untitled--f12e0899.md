---
doc_id: "mta-wiki:12929"
title: "RU/Number"
source_title: "Целое число"
source_url: "https://wiki.multitheftauto.com/wiki/%D0%A6%D0%B5%D0%BB%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE"
revision_id: 70882
language: "en"
categories: ["Понятия_скриптинга"]
generated_at: "2026-07-26T16:16:57.860623+00:00"
---

# RU/Number

Number - это тип данных, значение которого является любое число. Оно может быть отрицательным, нулевым или положительным, а также целым или действительным (число с десятичной запятой).

Обычно числа делятся на два типа данных - **integer** и **float**. Но Lua автоматически преобразует эти числа друг в друга при необходимости, поэтому можно сказать, что Lua не имеет целочисленного типа (integer), но рассказать о нём стоит.

## Integer

**Int** или **integer** - это тип данных, значение которого является любое целое число (число без десятичной запятой). Оно может быть положительным, нулевым или отрицательным.

### Пример присвоения значений

```
int = 10 -- стандартная запись типа данных integer
int = -10 -- отрицательное значение типа данных integer
int = 0 -- нулевое значение типа данных integer
int = tonumber("10") -- преобразует строку "10" в числовое значение
int = "10" + 10 -- автоматически преобразует строку "10" в числовое значение при математических операциях
int = nil -- если вы хотите стереть переменную
```

## Float

**Float** - это тип данных, значение которого является любое число с плавающей запятой (число с десятичной запятой). Оно может быть положительным или отрицательным.

### Пример присвоения значений

```
float = 10,5 -- стандартная запись типа данных float
float = -10,5 -- отрицательное значение типа данных float
float = 314.16e-2 -- тип данных float с десятичным порядком
float = 0xff -- тип данных float в шестнадцатеричной системе, используя префикс 0x
float = nil -- если вы хотите стереть переменную
```

## Преобразование [String](https://wiki.multitheftauto.com/wiki/RU/String) в Number

**Пример 1:** Использование функции Lua [tonumber()](https://uopilot.uokit.com/wiki/index.php?title=Tostring_(Lua)) может преобразовать string в number:

```
local thePlayer = getRandomPlayer()
local money = tonumber(getAccountData(getPlayerAccount(thePlayer), "money.key")) -- преобразует полученный тип данных string в number
setPlayerMoney(thePlayer, money)
```

**Пример 2:** Автоматическое преобразование string в number при математических операциях:

```
local str = "1234,56"
local x = str * 1
local y = str + 5
local z = 2000 - str
setElementPosition(theElement, x, y, z)
```

**Пример 3:** Использование функции Lua [type()](https://user.su/lua/index.php?id=3) может помочь вам узнать, что это за тип данных:

```
local thePlayer = getRandomPlayer()
local money = getAccountData(getPlayerAccount(thePlayer), "money.key")
outputChatBox("Возврат функции: "..type(money)) -- сообщит игроку: "string"
outputChatBox("Возврат функции: "..type(tonumber(money))) -- сообщит игроку: "number"
```

## Смотрите также

- ["Number" в программировании на Lua](http://www.lua.org/pil/2.3.html)
