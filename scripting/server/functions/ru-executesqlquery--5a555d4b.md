---
doc_id: "mta-wiki:12043"
title: "RU/ExecuteSQLQuery"
source_title: "Ru/executeSQLQuery"
source_url: "https://wiki.multitheftauto.com/wiki/Ru/executeSQLQuery"
revision_id: 69421
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:35.460651+00:00"
---

# RU/ExecuteSQLQuery

Эта функция выполняет произвольный запрос SQL и возвращает строки результата, если они существуют. Это обеспечивает привязку параметров для безопасности (предотвращает SQL-инъекции).

| [[{{{image}}}\|link=\|]] | Примечание: Эта функция действует только для registry.db. Используйте dbQuery для запроса пользовательской базы данных SQL. |
| --- | --- |
|  |  |

## Синтаксис

```
table executeSQLQuery ( string query [, var param1 [, var param2 ... ] ] )
```

### Обязательные аргументы

- **query:** SQL-запрос. Позиции, в которые будут вставлены значения параметров, отмечены знаком "?".

### Необязательные аргументы

- **paramX:** переменное количество параметров. Это должны быть строки или числа - важно убедиться, что они имеют правильный тип. Кроме того, количество передаваемых параметров должно быть равно количеству "?" символы в строке запроса.

Строковые параметры автоматически экранируются добавлением обратной косой черты \ перед символами ' и \

### Возвращает

Возвращает таблицу с результатом запроса, если это был запрос SELECT, или *false*, если это не так. В случае запроса SELECT таблица результатов может быть пустой (если строк результатов нет). Таблица имеет вид:

```
{
    { colname1=value1, colname2=value2, ... },
    { colname1=value3, colname2=value4, ... },
    ...
}
```

Следующая таблица представляет следующую строку.

## Пример

Ниже приведены примеры эквивалентов для устаревших функций executeSQL. Обратите внимание, что ` (символ) может использоваться для окружения имен таблиц и строк. Обычно это хорошая идея, чтобы избежать конфликтов имен с зарезервированными словами SQL.

Эквивалент executeSQLCreateTable:

```
executeSQLQuery("CREATE TABLE IF NOT EXISTS players (clothes_head_texture TEXT, clothes_head_model TEXT, name TEXT)")
executeSQLQuery("CREATE TABLE IF NOT EXISTS `players` (`clothes_head_texture` TEXT, `clothes_head_model` TEXT, `name` TEXT)")
```

Эквивалент executeSQLDelete:

```
playerName = getPlayerName(thePlayer)
executeSQLQuery("DELETE FROM players WHERE name=?", playerName)
executeSQLQuery("DELETE FROM `players` WHERE `name`=?", playerName)
```

Эквивалент executeSQLDropTable:

```
executeSQLQuery("DROP TABLE players" )
executeSQLQuery("DROP TABLE `players`" )
```

Эквивалент executeSQLSelect:

```
playerName = getPlayerName(thePlayer)
executeSQLQuery("SELECT score,health FROM players WHERE name=?", playerName )
executeSQLQuery("SELECT `score`,`health` FROM `players` WHERE `name`=?", playerName )
```

Эквивалент executeSQLInsert:

```
playerName = getPlayerName(thePlayer)
colorName = "Blue"
soundName = "sound.mp3"
executeSQLQuery("INSERT INTO players(name,color,sound) VALUES(?,?,?)", playerName, colorName, soundName )
executeSQLQuery("INSERT INTO `players`(`name`,`color`,`sound`) VALUES(?,?,?)", playerName, colorName, soundName )
```

Эквивалент executeSQLUpdate:

```
playerName = getPlayerName(thePlayer)
colorName = "Blue"
soundName = "sound.mp3"
executeSQLQuery("UPDATE players SET color='green',sound='somehead' WHERE name=?", playerName )
executeSQLQuery("UPDATE players SET color=?,sound=? WHERE name=?", colorName, soundName, playerName )
executeSQLQuery("UPDATE `players` SET `color`=?,`sound`=? WHERE `name`=?", colorName, soundName, playerName )
```

В этом примере определяется консольная команда, которая показывает идентификаторы и имена всех зарегистрированных (сохраненных в базе данных) игроков, у которых сумма денег превышает указанную.

```
function listPlayersWithMoreMoneyThan(thePlayer, command, amount)
    local players = executeSQLQuery("SELECT id, name FROM players WHERE money > ?", tonumber(amount))
    outputConsole("Players with more money than " .. amount .. ":", thePlayer)
    for i, playerdata in ipairs(players) do
        outputConsole(playerdata.id .. ": " .. playerdata.name, thePlayer)
    end
end

addCommandHandler("richplayers", listPlayersWithMoreMoneyThan)
```

В этом примере показано количество денег, которое имеет определенный зарегистрированный игрок.

```
function showPlayerMoney(thePlayer, command, playerName)
    local result = executeSQLQuery("SELECT money FROM players WHERE name=?", playerName)
    if(#result == 0) then
        outputConsole("No player named " .. playerName .. " is registered.", thePlayer)
    else
        outputConsole("Money amount of player " .. playerName .. " is " .. result[1].money, thePlayer)
    end
end
addCommandHandler("playermoney", showPlayerMoney)
```

Обратите внимание на отсутствие одинарных кавычек вокруг "?" в этом примере, хотя он представляет строку. executeSQLQuery увидит, что переменная playerName является строкой, и позаботится о правильном выполнении запроса самостоятельно.

Преимущество использования executeSQLQuery заключается в том, что он невосприимчив к пользователям, пытающимся использовать запрос с помощью атаки SQL-инъекцией. playerName может содержать специальные символы, такие как ', "или -, которые не будут влиять на запрос, в отличие от более старого подхода, где playerName будет объединяться в строку запроса.
