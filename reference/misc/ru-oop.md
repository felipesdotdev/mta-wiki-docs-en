---
doc_id: "mta-wiki:14295"
title: "Ru/OOP"
source_title: "Ru/OOP"
source_url: "https://wiki.multitheftauto.com/wiki/Ru/OOP"
revision_id: 79361
language: "en"
categories: ["OOP"]
generated_at: "2026-07-26T16:16:35.448989+00:00"
---

# Ru/OOP

Объектно-ориентированное программирование было введено в MTA:SA 1.4 и поставляется со специальными служебными классами, такими как [Vector](mta://reference/misc/vector.md) и [Matrix](mta://reference/misc/matrix.md). Эта страница содержит общую информацию о функциях OOP и содержит полезные ссылки.

## Включение

По умолчанию ООП отключено (однако векторы и матрицы доступны всегда) - это происходит главным образом потому, что подавляющее большинство серверов предпочитают придерживаться того, что они знают, - процедурного программирования. На самом деле, функции по-прежнему доступны, даже если ООП включено. Включить ООП так же просто, как добавить следующую строку в мета-файл ресурса:

```
<oop>true</oop>
```

## Векторы и матрицы

[Vectors](mta://reference/misc/vector.md) и [Matrices](mta://reference/misc/matrix.md) так будет проще отказаться от сложной математики и сразу перейти к увлекательной ее части. Как упоминалось выше, для этого необязательно включать OOP в конфигурации сервера.

## ДОПОЛНИТЕЛЬНО: Метастабильная структура OOP

Вы поймете это, если хорошо владеете Lua и хорошо разбираетесь в метатаблях. Понимание этого раздела не обязательно для использования OOP.

```
-- Подвержен воздействию глобальной окружающей среды
Element = {
    Element = createElement,
    setPosition = setElementPosition,
    ...
}

Vehicle = {
    Vehicle = createVehicle,
    setColor = setVehicleColor,
    ...
}

-- Скрыто в реестре lua, применяется к пользовательским данным
ElementMT = {
    __index = CLuaClassDefs::Index,
    __newindex = CLuaClassDefs::NewIndex,
    __class = Element,
    __call = __class.create,
    __set = {
        type = CLuaClassDefs::ReadOnly,
        health = setElementHealth,
        ...
    },
    __get = {
        type = getElementType,
        health = getElementHealth,
        ...
    },
}

VehicleMT = {
    __index = CLuaClassDefs::Index,
    __newindex = CLuaClassDefs::NewIndex,
    __class = Vehicle,
    __parent = ElementMT,
    __call = __class.create,
    __set = {
        damageProof = setVehicleDamageProof
        ...
    },
    __get = {
        damageProof = isVehicleDamageProof
        ...
    },
}
```

## Полезные ссылки

- **[OOP Introduction](mta://tutorials/oop-introduction.md)** - познакомит вас с основами OOP

- **[Function list (client)](mta://reference/misc/oop-client.md)** и **[Function list (server)](mta://reference/misc/oop-server.md)** - список реализованных функций

## Выше предоставлены страницы с полезными ссылками на английском языке.
